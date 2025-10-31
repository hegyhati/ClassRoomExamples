use std::io::{self, Write};

const DB_PATH : &str = "../db/movies.sqlite";


fn string_input(prompt : &str) -> String {
    print!("{}: ", prompt);
    io::stdout().flush().unwrap();
    let mut response : String = String::new();
    io::stdin().read_line(&mut response).unwrap();
    return response.trim().to_string();
}

fn get_connection() -> Result<sqlite::Connection, Box<dyn std::error::Error>> {
    let conn = sqlite::open(DB_PATH)?;
    conn.execute("PRAGMA foreign_keys = ON;")?;
    Ok(conn)
}

fn search_for_movie(conn: &sqlite::Connection)  -> Result<(), Box<dyn std::error::Error>> {
    let titlepart = string_input("Part of the title");
    let pattern = format!("%{}%", titlepart); 
    let query = "SELECT title, original_title, release_date FROM movies WHERE title LIKE ? ORDER BY release_date DESC;";
    let mut statement = conn.prepare(query)?;
    statement.bind((1,pattern.as_str()))?;

    println!("Movies that have matching titles:");
    while let Ok(sqlite::State::Row) = statement.next() {
        let title: String = statement.read::<String,_>("title")?;
        let otitle: String = statement.read::<String,_>("original_title")?;
        let date: String = statement.read::<String,_>("release_date")?;

        print!("  {}: {}", date, title);
        if title != otitle {
            print!(" - {}", otitle);
        }
        println!();
    }
    Ok(())
}

fn main()  -> Result<(), Box<dyn std::error::Error>> {
    let conn = match get_connection() {
        Ok(v) => v,
        Err(e) => {
            eprintln!("Could not get connection: {}", e);
            return Ok(());
        }
    };
    search_for_movie(&conn)?;
    Ok(())
}
