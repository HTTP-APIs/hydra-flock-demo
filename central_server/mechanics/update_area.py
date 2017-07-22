"""Operations to update Area."""
from mechanics.main import CENTRAL_SERVER
from mechanics.main import RES_CS
from mechanics.main import gen_Area
from hydra import SCHEMA, Resource


def update_area(area):
    """Update the area of interest on central server."""
    update_area_ = RES_CS.find_suitable_operation(
                   operation_type=SCHEMA.UpdateAction,
                   input_type=CENTRAL_SERVER.Area)
    resp, body = update_area_(area)
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    return Resource.from_iri(resp['location'])


if __name__ == "__main__":
    area = gen_Area("0,0", "5,0")
    print(area)

    print(update_area(area))
