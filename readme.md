# TCC

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

*Project in development*
