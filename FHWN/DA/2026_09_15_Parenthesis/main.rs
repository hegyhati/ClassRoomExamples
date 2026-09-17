mod couple_finder;
mod counter;

type Tester = fn(&str) -> bool;

fn nested_parentheses(n: usize) -> String {
    "(".repeat(n) + &")".repeat(n)
}

fn list_of_coupled_parentheses(n: usize) -> String {
    "()".repeat(n)
}


fn main() {
    let Some(arg) = std::env::args().nth(1) else {
        eprintln!("Error: missing input. Please provide the number of parentheses pairs");
        std::process::exit(1);
    };

    let Ok(count) = arg.parse::<usize>() else {
        eprintln!("Error: input must be a positive integer");
        std::process::exit(1);
    };

    let inputs = [
        ("coupled", list_of_coupled_parentheses(count)),
        ("nested", nested_parentheses(count)),
    ];

    let testers : [(&str,Tester);2]= [
        ("counter", counter::is_correct_parenthesis),
        ("couple", couple_finder::is_correct_parenthesis),
    ];

    for (input_name, input) in &inputs {
        println!("Input: {}", input_name);
        for (tester_name, tester) in &testers {
            let start = std::time::Instant::now();
            let result = tester(input);
            let duration = start.elapsed();
            println!(
                "  {}: {} --- {:?}",
                tester_name,
                if result { "[OK]" } else { "[NOK]" },
                duration
            );
        }
    }
}
