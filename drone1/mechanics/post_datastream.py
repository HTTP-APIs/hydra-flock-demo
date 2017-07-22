"""Operation related to datastream post operations."""
from mechanics.main import RES_CS, RES_DRONE
from mechanics.main import CENTRAL_SERVER, DRONE1
from mechanics.main import get_datastream
from hydra import SCHEMA, Resource


def send_datastream(datastream):
    """Post the drone current datastream to the central server."""
    post_datastream = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.Datastream)
    resp, body = post_datastream(datastream)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_datastream = Resource.from_iri(resp['location'])
    print("Datastream posted successfully.")
    return new_datastream


datastream = get_datastream()
print(datastream)
print(send_datastream(datastream))
