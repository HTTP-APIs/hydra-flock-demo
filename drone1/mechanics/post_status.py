from mechanics.main import RES_CS, RES_DRONE
from mechanics.main import CENTRAL_SERVER, DRONE1
from mechanics.main import get_status

def send_status(drone_status = get_status()):
    """Post the drone current datastream to the central server."""
    post_status = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.StatusCollection)
    resp, body = post_status(drone_status)

    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_status = Resource.from_iri(resp['location'])
    print("Status posted successfully.")
    return new_status
