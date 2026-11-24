# Containers

## Postgres

No need for it, if you connect to the DB installed on the FH server.

```yaml
  postgres:
    image: postgres:18-alpine
    container_name: local_postgres
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: atleastonenumberandspecialcharacter
    ports:
      - "5432:5432"
```

Local postgres database, connect to it with:

| | |
| --- | --- |
| Host | `postgres` / `localhost`  |
| Username | `postgres` | 
| Password | `atleastonenumberandspecialcharacter` | 
|  Default DB | `postgres` |

Use `localhost` for locally installed pgAdmin, and `postgres` for the dockerized one.

## pgAdmin

No need for it, if you have pgAdmin installed.

```yaml
  pgadmin:
    image: dpage/pgadmin4:9.19
    container_name: local_pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: adminpassword
    ports:
      - "5050:80"
```

You can open [https://localhos:5050](https://localhos:5050), and login with credentials:

| | |
| --- | --- |
| Email | `admin@example.com` | 
| Password | `adminpassword` |


# Start/stop containers

Start:
```
$ docker compose up
```

Stop with deleting data:
```
$ docker compose down -v
```

Stop while preserving data:
```
$ docker compose stop
```

Resume:
```
$ docker compose start
```


