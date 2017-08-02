# hydra-flock-demo

## Instructions to run for local development and tests

Developing and testing:
* create and activate a virtualenv
* upgrade pip and setuptools
* check if `python3-dev` is installed
* `chmod +x bootstrap-dev.sh`
* `./bootstrap-dev.sh`
* `chmod +x init.sh`
* `./bootstrap-dev.sh`

### Central Controller should be available at http://127.0.0.1:8080/api
### Drone1 should be available at http://127.0.0.1:8081/api
### Simulation GUI should be available at http://127.0.0.1:5000/

## **NOTE**: To stop all simulation processes use `pkill -f .py`
Different components are cloned in the repository and run locally on different ports.



## Instructions to run with Docker
- Clone the repo to your local computer using `git clone`.
- Build using `docker-compose build` ( For a fresh build use `docker-compose build --no-cache`).
- Start the docker containers using `docker-compose up`
- If you're running the simulation for the first time, you need to initialize the Postgres database once.
    - Connect to Central server docker container using `docker exec -i -t hydraflockdemo_central_server_1 /bin/bash`
    - Run `python db_init.py`
- Initialize drone with default properties
    - Connect to drone1 docker container using `docker exec -i -t hydraflockdemo_drone1_1 /bin/bash`
    - Cd into mechanics directory using `cd mechanics`
    - Run `python drone_init.py`


### NOTE: You can run different files in `mechanics` folders of both the `Central_server` and `Drone1` simply by typing `python <filename>` in their respective containers, to understand and test how basic operations in simulation will work using hydra-py client.

## Running tests
- For the Central Server
    - Connect to Central server docker container using `docker exec -i -t hydraflockdemo_central_server_1 /bin/bash`
    - Run tests using `python tests/test_central_server_endpoints.py`
- For Drone
    - Connect to drone1 docker container using `docker exec -i -t hydraflockdemo_drone1_1 /bin/bash`
    - Run `python tests/test_drone_endpoints.py`
