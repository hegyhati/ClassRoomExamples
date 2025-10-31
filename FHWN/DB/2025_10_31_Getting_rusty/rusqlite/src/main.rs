use rusqlite::{params, Connection, Result, OpenFlags};
use std::io::{self, Write};

const DB_PATH : &str = "../db/movies.sqlite";
const DB_FLAGS : OpenFlags = OpenFlags::SQLITE_OPEN_READ_WRITE;


fn string_input(prompt : &str) -> String {
    print!("{}: ", prompt);
    io::stdout().flush().unwrap();
    let mut response : String = String::new();
    io::stdin().read_line(&mut response).unwrap();
    return response.trim().to_string();
}

fn get_connection() -> Result<Connection> {
    let conn : Connection = Connection::open_with_flags(DB_PATH, DB_FLAGS)?;
    conn.execute("PRAGMA foreign_keys = ON;", [])?;
    return Ok(conn);
}

fn search_for_movie(conn : &Connection) -> Result<()>  {
    let titlepart = string_input("Part of the title");   

    let mut stmt = conn.prepare("SELECT title, original_title, release_date FROM movies WHERE title LIKE ?1 ORDER BY release_date DESC;")?;
    let rows = stmt.query_map(params![format!("%{}%", titlepart)], |row| {
        Ok((row.get::<_, String>(0)?, row.get::<_, String>(1)?, row.get::<_, String>(2)?))
    })?;

    let movies: Vec<(String, String, String)> = rows.collect::<Result<_, _>>()?;

    println!("Movies that have matching titles:");
    for (title, otitle, date) in movies {
        print!("  {}: {}", date, title);
        if title != otitle {
            print!(" - {}", otitle);
        }
        println!();
    }
    Ok(())
}

fn main() -> Result <()> {
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
