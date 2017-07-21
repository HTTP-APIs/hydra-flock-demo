""" Handles main configuration for the drone."""
from hydra import Resource, SCHEMA
from rdflib import Namespace
import json
import os

CENTRAL_SERVER_URL_ = os.environ.get("CENTRAL_SERVER_URL", "localhost:8080")
DRONE1_URL_ =  os.environ.get("DRONE1_URL", "localhost:8081")
API_NAME = os.environ.get("API_NAME", "api")

global CENTRAL_SERVER, DRONE1, DRONE_URL
CENTRAL_SERVER = Namespace( CENTRAL_SERVER_URL_+ '/serverapi/vocab#')
print(CENTRAL_SERVER)
DRONE1 = Namespace(DRONE1_URL_+'/droneapi/vocab#')
# print(DRONE1)
DRONE_URL = http://drone1
CENTRAL_SERVER_URL = http://central_server

global RES_CS, RES_DRONE
the_iri_of_the_resource_cs = 'http://central_server/serverapi'
# print(the_iri_of_the_resource_cs)
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = 'http://drone1/droneapi'
# print(the_iri_of_the_resource_drone)
RES_DRONE = Resource.from_iri(the_iri_of_the_resource_drone)

### Drone related methods
def get_drone_default():
    """Returns a default drone object with DroneID -1 for initialization."""
    drone_default = {
        "@type": "Drone",
        "DroneID": -10001,
        "name": "Drone1",
        "model": "xyz",
        "MaxSpeed": 50,
        "Sensor": "Temperature",
        "DroneState": {
            "@type": "State",
            "Speed": 0,
            "Position": "0,0",
            "Battery": 100,
            "Direction": "North",
            "SensorStatus": "Inactive",
        }
    }

    return drone_default


def get_drone():
    """Get the drone object from drone server."""
    get_drone_ = RES_DRONE.find_suitable_operation(
        operation_type=None, input_type=None, output_type=DRONE1.Drone)
    resp, body = get_drone_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    drone = json.loads(body.decode('utf-8'))
    drone.pop("@id", None)
    drone.pop("@context", None)
    return drone

def get_drone_id():
    """Return current drone id from drone server."""
    drone = get_drone()
    return int(drone["DroneID"])

# print(get_drone_id())

def update_drone(drone):
    """Update the drone object on drone server."""
    update_drone_ = RES_DRONE.find_suitable_operation(
    operation_type=SCHEMA.UpdateAction, input_type=DRONE1.Drone)
    resp, body = update_drone_(drone)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])

# print(update_drone(get_drone_default()))
## Datastream related methods
def gen_Datastream(temperature, position, drone_id):
    """Generate a datastream objects."""
    datastream = {
        "@type": "Datastream",
        "Temperature":temperature,
        "Position":position,
        "DroneID":drone_id,
    }

    return datastream

# datastream = gen_datastream(100, "0,0", get_drone_id())
# print(datastream)

def update_datastream(datastream):
    """Update the drone datastream on drone server."""
    update_datastream_ = RES_DRONE.find_suitable_operation(
        operation_type=SCHEMA.UpdateAction, input_type=DRONE1.Datastream)
    resp, body = update_datastream_(datastream)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])

# print(update_datastream(datastream))

def get_datastream():
    """Get the drone datastream from drone server."""
    get_datastream_ = RES_DRONE.find_suitable_operation(
        operation_type=None, input_type=None, output_type=DRONE1.Datastream)
    resp, body = get_datastream_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    datastream = json.loads(body.decode('utf-8'))
    ## remove extra contexts from datastream
    datastream.pop("@context", None)
    datastream.pop("@id", None)
    return datastream

# print(get_datastream())
## Status related methods

def gen_State(drone_id, battery, direction, position, sensor_status, speed):
    """Generate a State objects."""
    state = {
        "@type":"State",
        "DroneID": drone_id,
        "Battery": battery,
        "Direction":direction,
        "Position": position,
        "SensorStatus": sensor_status,
        "Speed": speed,
    }
    return state

# state = gen_state(-1000, "50", "North", "1,1", "Active", 100)
# print(state)

def update_state(state):
    """Update the drone state on drone server."""
    drone = get_drone()
    if int(drone["DroneID"]) == state["DroneID"]:
        ## Remove the DroneID key from state
        state.pop("DroneID", None)

        ## Update the drone state
        drone["DroneState"] = state
        update_drone(drone)
        print("Drone state updated successfully.")
    else:
        print("ERROR: DroneID %s not valid." %(state["DroneID"]))

# print(update_state(state))

def get_state():
    """Get the current drone state from the drone server."""
    drone = get_drone()
    drone_state = drone["DroneState"]
    drone_state["DroneID"] = drone["DroneID"]

    return drone_state

# print(get_state())
## Orders related methods
