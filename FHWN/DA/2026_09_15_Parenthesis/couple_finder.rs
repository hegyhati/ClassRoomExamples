pub fn is_correct_parenthesis(input: &str) -> bool {
    let mut copy = input.to_string();

    while !copy.is_empty() {
        match copy.find("()") {
            Some(pos) => copy.replace_range(pos..pos + 2, ""),           
            None => return false,
        }
    }

    true
}

fn main() {
    let Some(input) = std::env::args().nth(1) else {
        eprintln!("Error: missing input. Please provide a parenthesis string.");
        std::process::exit(1);
    };

    println!("The parenthesis string is {}.", if is_correct_parenthesis(&input) { "valid" } else { "invalid" });
}