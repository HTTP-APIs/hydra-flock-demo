"""Initialize drone."""
from mechanics.main import RES_CS, RES_DRONE
from mechanics.main import CENTRAL_SERVER, DRONE1
from hydra import SCHEMA
from mechanics.main import get_drone, get_drone_default, update_drone
from mechanics.main import gen_Datastream, update_datastream, get_drone_id

def init_drone_locally():
    """Initialize the drone locally with Negative identifier."""
    drone = get_drone_default()
    update_drone(drone)

def add_drone(drone):
    """Add the drone object to the central server and return Id."""
    add_drone_ = RES_CS.find_suitable_operation(
        SCHEMA.AddAction, CENTRAL_SERVER.Drone)
    resp, body = add_drone_(drone)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    drone_id = resp['location'].split("/")[-1]
    print(drone_id)
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
    init_drone_locally()
    print("DRone initialization success")

    drone = get_drone()
    drone.pop("DroneID", None)
    drone_id = int(add_drone(drone))

    # Update the drone on localhost
    update_drone_id(drone_id)

    print("Drone initialized successfully!")
    return None

def init_datastream_locally():
    """Initialize the datasteam locally."""
    datastream = gen_Datastream(100, "0,0", get_drone_id())
    update_datastream(datastream)
    print("Datastream initialized locally")
    return None

if __name__ == "__main__":
    init_drone()
    init_datastream_locally()
