use postgres::{Client, NoTls, Error};



fn setup_database(client: &mut Client) -> Result<(), Error> {
    client.batch_execute("
        CREATE TABLE IF NOT EXISTS Superhero (
            name TEXT NOT NULL PRIMARY KEY,
            secret_identity TEXT NOT NULL,
            franchise TEXT NOT NULL
        );
    ")
}

fn main() {
    let Ok(mut client) = Client::connect(
        "postgresql://postgres:password@localhost:5432/postgres",
        NoTls,
    ) else {
        println!("Cannot connect to server"); 
        return;
    };

    if setup_database(&mut client).is_err() {
        println!("Problem creating / accessing DB.");
        return;
    } 

    /*let _ = client.execute(
        "INSERT INTO Superhero(name, secret_identity, franchise) VALUES ($1, $2, 'DC');",
        &[&"Batman", &"Bruce Wayne"] 
    );*/

    let Ok(rows) = client.query("SELECT * FROM Superhero", &[]) else {
        println!("Query didn't work.");
        return;
    };

    for row in rows {
        let name:&str = row.try_get("name").unwrap();
        println!("{}", name);
    }




}