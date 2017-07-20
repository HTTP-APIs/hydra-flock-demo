""" Handles main configuration for the Central server."""
from hydra import Resource, SCHEMA
from rdflib import Namespace
import json

global CENTRAL_SERVER, DRONE1, CENTRAL_SERVER_URL
CENTRAL_SERVER = Namespace('http://192.168.99.100:8081/api/vocab#')
DRONE1 = Namespace('http://drone1/droneapi/vocab#')
CENTRAL_SERVER_URL = "http://192.168.99.100:8081"

global RES_CS, RES_DRONE1
the_iri_of_the_resource_cs = 'http://192.168.99.100:8081/api'
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = 'http://drone1/droneapi'
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
