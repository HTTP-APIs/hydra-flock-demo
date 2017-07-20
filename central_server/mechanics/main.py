""" Handles main configuration for the Central server."""
from hydra import Resource, SCHEMA
from rdflib import Namespace
import json

global CENTRAL_SERVER, DRONE1, CENTRAL_SERVER_URL
CENTRAL_SERVER = Namespace('http://central_server/serverapi/vocab#')
DRONE1 = Namespace('http://drone1/droneapi/vocab#')

CENTRAL_SERVER_URL = "http://central_server"

global RES_CS, RES_DRONE1
the_iri_of_the_resource_cs = 'http://central_server/serverapi'
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = 'http://drone1/droneapi'
RES_DRONE1 = Resource.from_iri(the_iri_of_the_resource_drone)

## Methods related to Area
def gen_Area(top_left, bottom_right):
    """Generate a Area object."""
    Area = {
        "TopLeft":top_left,
        "BottomRight":bottom_right
    }
    return Area

## Methods related to Messages
def gen_Message(message):
    message = {
        "MessageString":message,
    }
    return message

## Methods related to commands
def gen_status(speed, position, battery, sensor_status, drone_id):
    """Generate a Status objects."""
    status = {
        "Speed": speed,
        "Position": position,
        "Battery": battery,
        "SensorStatus": sensor_status,
        "DroneID": drone_id,
    }
    return status

def gen_Command(status):
    """Generate a Command object."""
    command = {
        "Status": status
    }
    return command
