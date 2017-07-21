""" Handles main configuration for the Central server."""
from hydra import Resource, SCHEMA
from rdflib import Namespace
import json
import os


API_NAME = os.environ.get("API_NAME", "api")

global CENTRAL_SERVER, DRONE1, DRONE_URL
CENTRAL_SERVER = Namespace("http://central_server/serverapi/vocab#")
print(CENTRAL_SERVER)
DRONE1 = Namespace("http://drone1/droneapi/vocab#")
# print(DRONE1)

DRONE1_URL = "http://drone1"
CENTRAL_SERVER_URL = "http://central_server"
global RES_CS, RES_DRONE
the_iri_of_the_resource_cs = "http://central_server/serverapi"
# print(the_iri_of_the_resource_cs)
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = "http://drone1/droneapi"
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

# state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
# print(state)

def gen_Command(state):
    """Generate a Command object."""
    command = {
        "@type":"Command",
        "State": state
    }
    return command
