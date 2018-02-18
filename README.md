## Forestry Patrol Simulation Demo using [Hydrus](https://github.com/HTTP-APIs/hydrus/) and [Hydra-py](https://github.com/pchampin/hydra-py)
An application that simulates the movements of a flock of drones that have as objective to detect the presence of fires or abnormal heat spots in a given geographical area using an infrared sensors.


## How to run the Simulation:
* create and activate a new virtualenv
* upgrade pip and setuptools
* check if `python3-dev` is installed
* `chmod +x bootstrap-dev.sh`
* `./bootstrap-dev.sh`
* `chmod +x init.sh`
* `./init.sh`

### Simulation GUI should be available at http://127.0.0.1:5000/

#### Central Controller should be available at http://127.0.0.1:8080/api
#### Drones should be available at 
- **Drone 1 - http://127.0.0.1:8081/api**
- **Drone 2 - http://127.0.0.1:8082/api** 
- **Drone 3 - http://127.0.0.1:8083/api**
- **Drone 4 - http://127.0.0.1:8084/api**  

## **NOTE**: To stop all simulation processes use `killall python`
Different components are cloned from their repositories and run locally on different ports.

## Interacting with the simulation
The user can interact with the simulation from the simulation GUI. He can submit messages in structured format to the central controller, the central controller will then parse the submitted message and issue commands to respective drones. Progress can be seen in controller and drone logs in the GUI.

**Some Examples**
- `Set Drone 2 speed 100` (Change the speed of drone with id 2 to 100 Km/h.)
- `Set Drone 8 direction N` (Change the direction of drone with id 8 to North.)
- `Set Drone 13 status off` (Turn drone with id 13 off.)
- `Set Drone 8 status active` (Turn drone with id 8 on.)

### For design principles and other details please read the [Wiki](https://github.com/HTTP-APIs/hydra-flock-demo/wiki)
