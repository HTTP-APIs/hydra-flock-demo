from mechanics.main import CENTRAL_SERVER, DRONE1, CENTRAL_SERVER_URL
from mechanics.main import RES_CS, RES_DRONE1

def update_area(area):
    """Update the area of interest on central server."""
    update_area_ = RES_CS.find_suitable_operation(
    operation_type=SCHEMA.updateAction, input_type=CENTRAL_SERVER.Area)
    resp, body = update_area_(area)
    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])
