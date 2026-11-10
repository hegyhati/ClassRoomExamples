# Rust + Postgres

## Setup 

In order to avoid TLS, we go with a simple local setup, where the DB and its browser runs in [docker](https://www.docker.com/) containers.

If you don't have docker, [install it first](https://docs.docker.com/desktop/setup/install/). Docker is "Linux native", don't forget to install `docker.io`, `docker-cli` and `docker-compose`. On Windows/Mac, Docker Desktop bundles them. On Windows don't forget to [install WSL](https://learn.microsoft.com/en-us/windows/wsl/install) too. 



## Starting the DB and browser

The [compose.yaml](compose.yaml) file contains the description of the two containers we will use.

The database on port 5432.

```yaml
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
```

The web-based DB browser on port 8080.
```yaml
  adminer:
    image: adminer
    restart: always
    ports:
      - "8080:8080"
```

Start both of them by executing this in thea same directory:

```
docker compose up
```

For the first time, it will take some time to download the images.


Now both of them are running, navigate to [localhost:8080](http://localhost:8080), select PostgreSQL, leave `db`, set username&database to `postgres`, password to  `password`, then login. 

Leave both running, while playing around with the Rust code. You can <kbd>Ctrl</kbd>+<kbd>C</kbd> to close it, or if you started with `-d`, then just `docker compose down`. And you can restart whenever you need it again. 

## Rust project

The [`Cargo.toml`](Cargo.toml) is important:

```bash
[package]
name = "postgres_template"
version = "0.1.0"
edition = "2024"

[dependencies]
postgres = "0.19"
```

`cargo run` will take some time forst to download the `postgres` crate. 

The full references are [here](https://docs.rs/postgres/latest/postgres/)

### Most important functions, types, etc.


Start with: 
```rs
use postgres::{Client, NoTls};
```


Then to creat a client:
```rs
let mut client = Client::connect("postgresql://USERNAME:PASSWORD@localhost:5432/DATABASE", NoTls,);
```

But it returns a `Result` so:

```rs
let Ok(mut client) = Client::connect("postgresql://USERNAME:PASSWORD@localhost:5432/DATABASE", NoTls,) else {
    println!("Cannot connect to database.");
    return;
};
```

All other functions will similarly return a `Result` so always check for success. 

To execute multiple `;` separated commands without the possibility to pass values:

```rs
client.batch_execute("SQL1;SQL2;...");
```

To execute a single DML with passing values:

```rs
client.execute("SQL", &[ &val1, &val2, ... ])
```

where `$1`, `$2`, etc. should be used in the SQL string for values, and the function returns the number of affected lines (in a `Result`).

Finally to run a DQL:
```rs
client.query("SQL", &[ &val1, &val2, ... ])
```
that returns a `Vec<Row>` (in a `Result`).

On each `Row` you can run `try_get(column_idx)` or `try_get("column name")` to get a field (in a `Result`) from the row.

