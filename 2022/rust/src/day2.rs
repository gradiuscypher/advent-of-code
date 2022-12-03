type Game = (char, char);

#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Vec<Game> {
    let mut games: Vec<Game> = Vec::new();

    let lines = input.lines();

    for line in lines {
        let split_line: Vec<char> = line.chars().collect();
        let game: Game = (split_line[0], split_line[2]);
        games.push(game);
    }

    games
}

fn game_points(first: char, second: char) -> u32 {
    match first {
        'A' => match second {
            'X' => 4,
            'Y' => 8,
            'Z' => 3,
            _ => 0,
        },
        'B' => match second {
            'X' => 1,
            'Y' => 5,
            'Z' => 9,
            _ => 0,
        },
        'C' => match second {
            'X' => 7,
            'Y' => 2,
            'Z' => 6,
            _ => 0,
        },
        _ => 0,
    }
}

fn calculate_action(first: char, second: char) -> u32 {
    match first {
        'A' => match second {
            // lose
            'X' => game_points(first, 'Z'),
            // draw
            'Y' => game_points(first, 'X'),
            // win
            'Z' => game_points(first, 'Y'),
            _ => 0,
        },
        'B' => match second {
            // lose
            'X' => game_points(first, 'X'),
            // draw
            'Y' => game_points(first, 'Y'),
            // win
            'Z' => game_points(first, 'Z'),
            _ => 0,
        },
        'C' => match second {
            // lose
            'X' => game_points(first, 'Y'),
            // draw
            'Y' => game_points(first, 'Z'),
            // win
            'Z' => game_points(first, 'X'),
            _ => 0,
        },
        _ => 0,
    }
}

#[aoc(day2, part1)]
pub fn part1(input: &[Game]) -> u32 {
    let mut total = 0;
    for game in input {
        total += game_points(game.0, game.1);
    }
    total
}

#[aoc(day2, part2)]
pub fn part2(input: &[Game]) -> u32 {
    let mut total = 0;
    for game in input {
        total += calculate_action(game.0, game.1);
    }
    total
}
