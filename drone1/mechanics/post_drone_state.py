from mechanics.main import RES_CS, RES_DRONE
from mechanics.main import CENTRAL_SERVER, CENTRAL_SERVER_URL, DRONE1
from mechanics.main import get_drone
from hydra import SCHEMA, Resource


def get_drone_iri(drone):
    """ Get the DroneID from a drone object and return DroneID, drone."""

    drone_id = drone.pop("DroneID", None)
    drone_id = "/serverapi/DroneCollection/"+ drone_id

    return drone_id, drone

drone = get_drone()

drone_id, drone = get_drone_iri(drone)
print(drone_id, drone)

def post_drone(id_, drone):
    """Updates a drone object in  the collection given command @id attribute."""
    try:
        i = Resource.from_iri(CENTRAL_SERVER_URL + id_)
        # name = i.value(SCHEMA.name)
        resp, _ = i.find_suitable_operation(SCHEMA.UpdateAction, CENTRAL_SERVER.Drone)(drone)
        if resp.status // 100 != 2:
            return "error updating <%s>" % i.identifier
        else:
            return "successfully updated <%s>" % i.identifier
    except:
        return {404: "Resource with Id %s not found!" %(id_,)}
# print(delete_command("/api/CommandCollection/175"))

print(post_drone(drone_id, drone))
