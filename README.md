## Setup

Application requires docker desktop (https://www.docker.com/products/docker-desktop/) to be running. Once docker is running in the background run the following commands:

1. `make init`
2. `make migrate`

## Tests
While the container is up run test suite with `make tests`. The database is seeded by a migration file that pulls from `https://msimon979.github.io/pokemon.json`

## Routes
Refer to openapi.yaml for more information:

`http://0.0.0.0:8000/pokemon/` -> GET, POST

`http://0.0.0.0:8000/pokemon/?type_1=<str>&type_2=<str>&name=<str>` -> GET, optional filters to search pokemon

`http://0.0.0.0:8000/pokemon/<id>/` -> GET
