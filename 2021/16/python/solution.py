#!/usr/bin/env python3
"""
ref: https://stackoverflow.com/questions/1425493/convert-hex-to-binary

hexstr = "D2FE28"
f'{int(hexstr, 16):b}'

part2:
- 422941676737579 too high
- 53906407519 too low
"""

import itertools
import logging
from functools import reduce
from pprint import pprint
from sys import argv
from typing import Iterable

example_packets = [
    'D2FE28',
    '38006F45291200',
    'EE00D40C823060',
    '8A004A801A8002F478',
    '620080001611562C8802118E34',
    'C0015000016115A2E0802F182340',
    'A0016C880162017C3686B18A3D4780'
]

example_operator_packets = [
    'C200B40A82',
    '04005AC33890',
    '880086C3E88112',
    'CE00C43D881120',
    'D8005AC2A8F0',
    'F600BC2D8F',
    '9C005AC2F8F0',
    '9C0141080250320F1802104A08'
]

# logging so that I can throw debug strings around without feeling bad
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

everypacket = [[]]
packet_group = []


def hex_to_bits(input_str):
    logger.debug(f'hex value: {input_str}')
    parse_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }

    result_bits = ''
    for letter in input_str.strip():
        result_bits += parse_dict[letter]
    return result_bits


def load_input(filename):
    with open(filename) as input:
        return hex_to_bits(input.read())


def binary_parser(input_str, is_subpacket=False):
    if '1' not in input_str:
        return ''

    logger.debug(f"raw bin: {input_str}")

    # grab the first 3 bits for the packet version
    ver_str = input_str[0:3]
    version = int(ver_str, 2)

    # grab the next 3 bits for the packet type ID
    id_str = input_str[3:6]
    type_id = int(id_str, 2)

    # draw the rest of the fucking owl
    remaining_input = input_str[6:]

    logger.debug(f"Header parsing finished - v: {version} t: {type_id}\nremain: {remaining_input}")

    # packet is a literal value
    if type_id == 4:
        value_str = ""

        # grab 5 bit chunks till you see stop bit
        while remaining_input[0] == '1':
            logger.debug(f'More input to parse: {remaining_input[:5]}')
            value_str += remaining_input[1:5]
            remaining_input = remaining_input[5:]

        # grab final stop bit chunk
        logger.debug(f'Final input to parse: {remaining_input[:5]}')
        value_str += remaining_input[1:5]
        remaining_input = remaining_input[5:]

        logger.debug(f"Final value_str: {value_str}")
        lit_value = int(value_str, 2)
        logger.debug(f"Literal value: {lit_value}")

        parsed = {
            'version': version,
            'type_id': type_id,
            'value': lit_value,
            'raw': {
                'version': ver_str,
                'type_id': id_str,
                'value': value_str
            }
        }
        everypacket[-1].append(parsed)

        logger.info(f"[+] Parsed: {parsed}")

    # packet is an operator packet
    else:
        everypacket.append([])
        operator_bit = remaining_input[0]
        remaining_input = remaining_input[1:]

        # static length subpacket operator
        if operator_bit == '0':
            subpacket_length_str = remaining_input[:15]
            subpacket_length = int(subpacket_length_str, 2)
            remaining_input = remaining_input[15:]

            subpacket_bits = remaining_input[:subpacket_length]
            remaining_input = remaining_input[subpacket_length:]

            parsed = {
                'version': version,
                'type_id': type_id,
                'raw': {
                    'version': ver_str,
                    'type_id': id_str,
                    'subpacket_len': subpacket_length,
                    'subpacket_bits': subpacket_bits,
                }
            }
            everypacket[-1].append(parsed)
            logger.info(f"[+] Parsed: {parsed}")

            while subpacket_bits:
                subpacket_bits = binary_parser(subpacket_bits, is_subpacket=True)

        # packet count subpacket operator
        elif operator_bit == '1':
            everypacket.append([])
            subpacket_count = int(remaining_input[:11])
            remaining_input = remaining_input[11:]

            parsed = {
                'version': version,
                'type_id': type_id,
                'raw': {
                    'version': ver_str,
                    'type_id': id_str,
                    'subpacket_count': subpacket_count,
                }
            }

            everypacket[-1].append(parsed)

            logger.info(f"[+] Parsed: {parsed}")

            # grab the next X packets
            for _ in range(0, subpacket_count):
                remaining_input = binary_parser(remaining_input, is_subpacket=True)

    return remaining_input


def operate_packets():
    operation_list = everypacket

    # logger.debug(f"OP List: {[op['type_id'] for op in operation_list]}")
    outside_val = []
    while everypacket:
        operation_list = everypacket.pop()

        if len(operation_list) == 1:
            values = outside_val
            outside_val = []
        else:
            values = []

        if operation_list:
            while operation_list:
                op = operation_list.pop()
                logger.debug(f"Val List: {values}")
                logger.debug(f"Curr OP: {op['type_id']}")
                # literal value
                if op['type_id'] == 4:
                    logger.debug(f"Curr Val: {op['value']}")
                    values.append(int(op['value']))

                # sum op
                elif op['type_id'] == 0:
                    values = [sum(values)]

                # product op
                elif op['type_id'] == 1:
                    if len(values) == 1:
                        pass
                    else:
                        values = [reduce((lambda x, y: x * y), values)]

                # minimum op
                elif op['type_id'] == 2:
                    values = [min(values)]

                # minimum op
                elif op['type_id'] == 3:
                    values = [max(values)]

                # greater than
                elif op['type_id'] == 5:
                    values = [1 if values[1] > values[0] else 0]

                # less than
                elif op['type_id'] == 6:
                    values = [1 if values[1] < values[0] else 0]

                # equals
                elif op['type_id'] == 7:
                    print("VALUES", values)
                    values = [1 if values[1] == values[0] else 0]
                    print("VALUES AFTER:", values)

                else:
                    logger.error(f'Undefined Op: {op["type_id"]}')
            outside_val += values
    print(outside_val)


def flatten_packets(packets):
    for packet in packets:
        if isinstance(packet, list):
            yield from flatten_packets(packet)
        else:
            yield packet


if __name__ == '__main__':
    part1 = False
    filename = argv[1]

    # ill set up my template to have argparse later ;-;
    if len(argv) > 2:
        flag = argv[2]
        if flag == 'd':
            logger.setLevel(logging.DEBUG)

    if len(filename) > 1:
        inputstr = load_input(filename)
    else:
        # inputstr = hex_to_bits(example_packets[int(argv[1])])
        inputstr = hex_to_bits(example_operator_packets[int(argv[1])])

    # parse the packets
    binary_parser(inputstr)

    # part 1 answer
    if part1:
        total = 0
        for p in everypacket:
            total += p['version']
        logger.info(f'part1: {total}')

    # part2 answer
    else:
        operate_packets()
