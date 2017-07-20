""" Handles main configuration for the Central server."""
from hydra import Resource, SCHEMA
from rdflib import Namespace
import json
import os

CENTRAL_SERVER_URL = os.environ.get("CENTRAL_SERVER_URL", "localhost:8080")
DRONE1_URL =  os.environ.get("DRONE1_URL", "localhost:8081")
API_NAME = os.environ.get("API_NAME", "api")

global CENTRAL_SERVER, DRONE1, DRONE_URL
CENTRAL_SERVER = Namespace( CENTRAL_SERVER_URL+ '/serverapi/vocab#')
print(CENTRAL_SERVER)
DRONE1 = Namespace(DRONE1_URL+'/droneapi/vocab#')
# print(DRONE1)

global RES_CS, RES_DRONE
the_iri_of_the_resource_cs = CENTRAL_SERVER_URL+ '/serverapi'
# print(the_iri_of_the_resource_cs)
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = DRONE1_URL+ '/droneapi'
# print(the_iri_of_the_resource_drone)
RES_DRONE1 = Resource.from_iri(the_iri_of_the_resource_drone)

## Methods related to Area
def gen_Area(top_left, bottom_right):
    """Generate a Area object."""
    Area = {
        "@type":"Area",
        "TopLeft":top_left,
        "BottomRight":bottom_right
    }
    return Area

# area = gen_Area("0,0", "5,5")
## Methods related to Messages
def gen_Message(message):
    message = {
        "@type":"Message",
        "MessageString":message,
    }
    return message

## Methods related to commands

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

def gen_Command(state):
    """Generate a Command object."""
    command = {
        "@type":"Command",
        "State": state
    }
    return command
