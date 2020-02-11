# TCC

To run this project:

 - [Install compose](https://docs.docker.com/compose/install/)
 - Run docker-compose build 
 - Run docker-compose up 
 - Go to `localhost:8000/`

To access local database:

 - docker exec -it tcc_db_1 psql -U postgres
 - \c postgres connect to database
 - \dt list tables
 - \d `table_name` describe table

Change database timezone:
 - `ALTER database postgres SET timezone ='Brazil/East';`


*Project in development*
