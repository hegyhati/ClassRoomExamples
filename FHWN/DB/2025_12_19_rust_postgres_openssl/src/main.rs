use postgres::Client;
use postgres_openssl::MakeTlsConnector;
use openssl::ssl::{SslConnector, SslMethod};
use std::error::Error;
use std::io::{self,Write};
use chrono::NaiveDate; 

fn string_input(prompt: &str) -> String {
    print!("{}: ", prompt);
    io::stdout().flush().unwrap();
    let mut response : String = String::new();
    io::stdin().read_line(&mut response).unwrap();
    return response.trim().to_string();
}

fn get_group_name(client: &mut postgres::Client) -> String {
    let names: Vec<String> = client
        .query("SELECT group_name FROM groups;", &[]).unwrap()
        .iter()
        .map(|row| row.get::<_, String>("group_name"))
        .collect();
    loop {
        let group = string_input(&format!("Which group had the run? {}", names.join("/")));
        if names.contains(&group) { return group; }
        println!("{} is not a groupname...", group);
    }
}

fn get_date(prompt: &str) -> chrono::NaiveDate {
    loop {
        match NaiveDate::parse_from_str(&string_input(prompt), "%Y-%m-%d") {
            Ok(date) => return date,
            Err(_) => println!("Not a valid date, use YYYY-MM-DD format..."),
        }
    }
}

fn get_integer(prompt: &str, can_be_negative: bool) -> i32 {
    loop {
        match string_input(prompt).parse::<i32>() {
            Err(_) => println!("Not a number..."),
            Ok(num) => {
                if can_be_negative || num >= 0 { return num; }
                println!("Cannot be negative...");
            }
        }
    }
}

fn new_entry(client: &mut postgres::Client) {
    let group = get_group_name(client);
    let date = get_date("When was the run?");
    let count = get_integer("How many runners were there?", false);
    match client.execute("INSERT INTO runs (\"group\", \"date\", \"count\") VALUES ($1, $2, $3)", &[&group,&date,&count]) {
        Ok(_) => println!("Entry successfully added :-)"),
        Err(_) => println!("The stars were not aligned, try again next time..."),
    }
}

fn print_attendence_statistics(client: &mut postgres::Client) { 
    let rows = client.query("SELECT \"group\", COUNT(*) AS run_count, MAX(\"count\") AS max_attendance, ROUND(AVG(\"count\"))::int AS average_attendance FROM runs GROUP BY \"group\"", &[]).unwrap();
    println!("| {:15} | {:15} | {:15} | {:15} |", "Group name", "# of runs", "Max runners", "Average runners");
    println!("| {:15} | {:15} | {:15} | {:15} |", "","","","");
    for row in rows {
        let group: String = row.get("group");
        let run_count: i64 = row.get("run_count");
        let max_attendance: i32 = row.get("max_attendance");
        let average_attendance: i32 = row.get("average_attendance");
        println!("| {:15} | {:15} | {:15} | {:15} |", group, run_count, max_attendance, average_attendance);
    }
}

fn main() -> Result<(), Box<dyn Error>> {
    let builder = SslConnector::builder(SslMethod::tls())?;
    let connector = MakeTlsConnector::new(builder.build());
    let database_url = "postgres://USERNAME:PASSWORD@HOST:PORT/DATABASE";
    let mut client = Client::connect(&database_url, connector)?;

    new_entry(&mut client);
    print_attendence_statistics(&mut client);

    client.close()?;
    Ok(())
}
