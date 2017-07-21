# hydra-flock-demo

This is part of the `hydra-flock-simulation` test-bed. Check the `hydra-flock-simulation` for cloud deployment of the full test-bed.

FOR LOCAL TESTS:

Running tests:
* create and activate a virtualenv
* upgrade pip and setuptools
* check if `python3-dev` is installed
* run `pip install -r requirements.txt`
* run `python run_simulation.py`

Different components are cloned in the repository and run locally on different ports.


## Instructions to Run
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
