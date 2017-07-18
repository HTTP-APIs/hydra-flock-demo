"""Initialize drone."""
from mechanics.main import RES_CS, RES_DRONE
from mechanics.main import CENTRAL_SERVER, DRONE1
from mechanics.main import get_drone, get_drone_default, update_drone

def add_drone(drone):
    """Add the drone object to the central server and return Id."""
    add_drone = RES_CS.find_suitable_operation(
        SCHEMA.AddAction, CENTRAL_SERVER.Drone)
    resp, body = add_drone(drone)
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    drone_id = resp['location'].split("/")[-1]
    return drone_id

def update_drone_id(id_):
    """Update the drone identifier."""
    # GET current drone object
    drone = get_drone()
    # Update the drone id
    drone["DroneID"] = id_

    # Update drone object
    update_drone(drone)
    print("DroneID updated successfully", id_)
    return None

def init_drone():
    """Initialize drone."""
    # Add drone to the central_server and get identifier
    drone_id = add_drone(get_drone_default())
    # Update the drone on localhost
    update_drone_id(drone_id)
    print("Drone initialized successfully!")
    return None
