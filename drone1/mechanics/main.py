""" Handles main configuration for the drone."""
from hydra import Resource, SCHEMA, Collection
from rdflib import Namespace
import json

CENTRAL_SERVER = Namespace('http://central_server/serverapi/vocab#')
DRONE1 = Namespace('http://drone1/droneapi/vocab#')
DRONE_URL = "http://drone1"

global RES_CS, RES_DRONE
the_iri_of_the_resource_cs = 'http://central_server/serverapi'
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = 'http://drone1/droneapi'
RES_DRONE = Resource.from_iri(the_iri_of_the_resource_drone)

### Drone related methods
def get_drone_default():
    """Returns a default drone object with DroneID -1 for initialization."""
    drone_default = {
        "@type": "Drone",
        "Sensor": "Temprature"
        "MaxSpeed": 50
        "model": "drone111"
        "name": "drone1"
        "DroneID": -1,
        "DroneStatus": {
                "Speed": 0,
                "Position": "0,0",
                "Battery": 100,
                "Destination": "0,0",
                "SensorStatus": "Normal"
        }
    }

    return drone_default


def get_drone():
    """Get the drone object from drone server."""
    get_drone = RES_DRONE.find_suitable_operation(
        operation_type=None, input_type=None, output_type=DRONE1.Drone)
    resp, body = get_drone()
    assert resp.status == 200, "%s %s" % (resp.status, resp.reason)

    drone = json.load(body)
    return drone

def get_drone_id():
    """Return current drone id from drone server."""
    drone = get_drone()
    return drone["DroneID"]

def update_drone(drone):
    """Update the drone object on drone server."""
    update_drone = RES_DRONE.find_suitable_operation(
    operation_type=SCHEMA.updateAction, input_type=DRONE1.Drone)
    resp, body = update_drone(drone)
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])

## Datastream related methods
def gen_datastream(temperature, position, drone_id=get_drone_id()):
    """Generate a datastream objects."""
    datastream = {
        "Temperature":temperature,
        "DroneID":drone_id,
        "Position":position
    }

def update_datastream(datastream):
    """Update the drone datastream on drone server."""
    update_datastream = RES_Drone.find_suitable_operation(
        operation_type=SCHEMA.updateAction, input_type=DRONE1.Data)
    resp, body = update_datastream(datastream)
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])

def get_datastream():
    """Get the drone datastream from drone server."""
    get_datastream = RES_DRONE.find_suitable_operation(
        operation_type=None, input_type=None, output_type=DRONE1.Data)
    resp, body = get_drone()
    assert resp.status == 200, "%s %s" % (resp.status, resp.reason)

    datastream = json.load(body)
    return datastream

## Status related methods
def gen_status(speed, position, battery, sensor_status, drone_id=get_drone_id()):
    """Generate a datastream objects."""
    status = {
        "Speed": speed,
        "Position": position,
        "Battery": battery,
        "SensorStatus": sensor_status,
        "DroneID": drone_id,
    }
    return status

def update_status(status):
    """Update the drone status on drone server."""
    drone = get_drone()
    if drone["DroneID"] == status["DroneID"]:
        ## Remove the DroneID key from status
        status.pop("DroneID", None)

        ## Update the drone status
        drone["DroneStatus"] = status
        update_drone(drone)
        print("Drone status updated successfully.")
    else:
        print("ERROR: DroneID %s not valid." %(status["DroneID"]))

def get_status():
    """Get the current drone status from the drone server."""
    drone = get_drone()
    drone_status = drone["DroneStatus"]
    drone_status["DroneID"] = drone["DroneID"]

    return drone_status

## Orders related methods
def get_order_collection():
    """Get order collection from the drone server."""
    get_orders = RES_DRONE.find_suitable_operation(None, None, DRONE1.OrderCollection)
    resp, body = get_orders()
    assert resp.status == 200, "%s %s" % (resp.status, resp.reason)

    body = json.loads(body)
    return body

def delete_order(id_):
    """Delete a order from the collection given order @id attribute."""
    res = Resource.from_iri(DRONE_URL + id_)
    # name = i.value(SCHEMA.name)
    resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
    if resp.status // 100 != 2:
        print("error deleting <%s>" % i.identifier)
    else:
        print("deleted <%s>" % i.identifier)
