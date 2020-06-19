# TCC

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/46b7f549be2d41e6a717e5e885ce466c)](https://app.codacy.com/manual/mpgabriel95/TCC?utm_source=github.com&utm_medium=referral&utm_content=mpgabriel95/TCC&utm_campaign=Badge_Grade_Dashboard)

To run this project:

- [Install compose](https://docs.docker.com/compose/install/)
- `Run docker-compose build`
- `Run docker-compose up` add `-d --build` to run in background
- Go to `localhost:5000/`

To create db tables

- `docker-compose exec web python manage.py create_db`

To access local database:

- `docker-compose exec db psql --username=tcc --dbname=tcc` access docker's postgres
- `\c tcc` connect to database
- `\dt` list tables
- `\d table_name` describe table

To add tokens:
 - To execute the extraction you need github tokens, the quantity depends on the network size.
 - `insert into token (token_value, last_expiration) values ('token_value',  now() - INTERVAL '1 DAY');` or run `tokens.sql`

To extract a github network:

 - `curl -i -k -H "Content-Type:application/json" -X POST http://localhost:5000/extract/{user_name}/{steps} -d '{}'`

To extract semantic metrics:

 - `curl -i -k -H "Content-Type:application/json" -X POST http://localhost:5000/metrics/shared-repos -d '{}'`
 - `curl -i -k -H "Content-Type:application/json" -X POST http://localhost:5000/metrics/shared_pulls/{user_name} -d '{}'`
 - `curl -i -k -H "Content-Type:application/json" -X POST http://localhost:5000/metrics/shared_contributions/{user_name} -d '{}'`

To extract topological metrics:

 - `curl -i -k -H "Content-Type:application/json" -X POST http://localhost:5000/metrics/topological/epiresdasilva -d '{}'`
