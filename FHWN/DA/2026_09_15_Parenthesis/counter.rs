pub fn is_correct_parenthesis (input: &str) -> bool {
    let mut count = 0;

    for c in input.chars() {
        if c == '(' {
            count += 1;
        } else if c == ')' {
            if count == 0 {
                return false;
            }
            count -= 1;
        }
    }

    count == 0
}

fn main() {
    let Some(input) = std::env::args().nth(1) else {
        eprintln!("Error: missing input. Please provide a parenthesis string.");
        std::process::exit(1);
    };

    println!("The parenthesis string is {}.", if is_correct_parenthesis(&input) { "valid" } else { "invalid" });
}