use postgres::{Client,NoTls,Error};

mod peak;
mod ui;

fn get_connection() -> Result<Client, Error> {
    Client::connect(
        // This url should be in a dotenv
        "postgresql://postgres:password@localhost:5432/postgres",
        NoTls,
    )
}

fn main() {
    let Ok(mut client) = get_connection() else {
        println!("Could not make the connection to the DB.");
        return
    };
    let _ = peak::Peak::initialize_table(&mut client);
    ui::main_menu(&mut client);
}