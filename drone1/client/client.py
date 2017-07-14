"""
Example to create post reqests to the server.
"""
from hydrapy import Resource, SCHEMA, HYDRUS
from hydrus.data import crud

global RES
the_iri_of_the_resource = 'http://central_server/api'
RES = Resource.from_iri(the_iri_of_the_resource)

def update_drone_identifier(identifier):
    drone = crud.get(1, "drone")
    drone["object"]["Identifier"] = identifier
    return crud.update(1,"drone", drone)

def get_drone_identifier():
    drone = crud.get(1, "drone")
    return drone["object"]["Identifier"]


def get_drone():
    return crud.get(1, "drone")

def init_drone():

# Create new order for drone
    create_drone = RES.find_suitable_operation(SCHEMA.AddAction, HYDRUS.drone)
    resp, body = create_drone({
        "name": "drone1",
        "@type": "drone",
        "object": {
                "Identifier": -1,
                "Speed": 0,
                "Position": "0,0",
                "Battery": 100,
                "Destination":"0,0",
                "Sensor": "temprature",
                "Status": "Started"
        }
    })
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_drone = Resource.from_iri(resp['location'])
    identifier = resp['location'].split("/")[-1]
    update_drone_identifier(identifier)
    print("Identifier updated successfully", identifier)
    return None

def send_datastream(temperature):
    drone = get_drone()
    position = drone["object"]["Position"]
    identifier = drone["object"]["Identifier"]

    create_datastream = RES.find_suitable_operation(SCHEMA.AddAction, HYDRUS.datastream)
    resp, body = create_datastream({
        "Position": position,
        "Temperature": temperature,
        "Identifier": identifier,

    })
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_datastream = Resource.from_iri(resp['location'])
    return new_datastream

def send_status(progress):

    drone = get_drone()
    identifier = drone["object"]["Identifier"]
    position = drone["object"]["Position"]
    speed = drone["object"]["Speed"]
    destination = drone["object"]["Destination"]
    battery = drone["object"]["Battery"]
    progress = progress


    create_status = RES.find_suitable_operation(SCHEMA.AddAction, HYDRUS.status)
    resp, body = create_status({
        "Identifier": identifier,
        "Position": position,
        "Speed": speed,
        "Destination": destination,
        "Battery": battery,
        "Progress": progress,
    })
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_status = Resource.from_iri(resp['location'])
    return new_status

#     create_order = RES.find_suitable_operation(SCHEMA.AddAction, SCHEMA.order)
#     resp, body = create_order({
#         "Destination": "This is halloween, this is halloween",
#         "Speed": "2015-10-31T00:00:00Z",
#         "Identifier": "2015-10-31T23:59:59Z",
#     })
#     assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
#     new_order = Resource.from_iri(resp['location'])
#     print(new_order)
#
# ## Create new message for drone
#     create_message = RES.find_suitable_operation(
#         SCHEMA.AddAction, HYDRUS.message)
#     resp, body = create_message({
#         "message": "testing message 1"
#     })
#
#     assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
#     new_message = Resource.from_iri(resp['location'])
#
#     print(new_message)


if __name__ == "__main__":
    init_drone()

    print(send_datastream(300))

    print(send_status("Analysing"))
    # main()
