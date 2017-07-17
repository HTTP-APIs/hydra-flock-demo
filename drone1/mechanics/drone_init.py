"""Initialize drone."""
from hydra import Resource, SCHEMA
from rdflib import Namespace
import json

CENTRAL_SERVER = Namespace('http://central_server/serverapi/vocab#')
DRONE1 = Namespace('http://drone1/droneapi/vocab#')

global RES_CS, RES_DRONE
the_iri_of_the_resource_cs = 'http://central_server/serverapi'
RES_CS = Resource.from_iri(the_iri_of_the_resource_cs)

the_iri_of_the_resource_drone = 'http://drone1/droneapi'
RES_DRONE = Resource.from_iri(the_iri_of_the_resource_drone)


def update_drone_identifier(id_):
    """Update the drone identifier."""
    ### GET current drone object
    get_drone = RES_DRONE.find_suitable_operation(operation_type=None, input_type = None, output_type= DRONE1.Drone)
    resp, body = get_drone()
    drone = json.load(body)

    ### Update the drone id
    drone["Identifier"] = id_

    ### Update drone object
    update_drone = RES_DRONE.find_suitable_operation(operation_type=SCHEMA.updateAction, input_type=DRONE1.Drone)
    resp, body = update_drone(drone)
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)

    print("Drone initialized successfully!")
    return Resource.from_iri(resp['location'])

def init_drone():

# Create new order for drone
    create_drone = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.Drone)
    resp, body = create_drone({
        "@type": "Drone",
        "Sensor": "Temprature"
        "MaxSpeed": 50
        "model": "drone111"
        "name": "drone1"
        "Identifier": -1,
        "DroneStatus": {
                "Speed": 0,
                "Position": "0,0",
                "Battery": 100,
                "Destination":"0,0",
                "SensorStatus": "Normal"
        }
    })
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_drone = Resource.from_iri(resp['location'])
    identifier = resp['location'].split("/")[-1]
    update_drone_identifier(identifier)
    print("Identifier updated successfully", identifier)
    return None
