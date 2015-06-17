## Moonrock

Moonrock is an example of Python backend implementation of the Moonshot project (a generic admin UI).

- Requires PostgreSQL 9.4+

### PostgreSQL Setup

Against PG 9.4:

  $ createuser -P moonbase
    (Enter 'moonbast' for password.  Repeat.  Answer 'n' to next three 
    questions.)
  $ createdb -O moonbase moonbase


### Tables and Sample Data

Run `env\bin/initialize_moonbase_db development.ini` to get some sample
data along with the tables.

### Running 

`env/bin/pserve development.ini`
 