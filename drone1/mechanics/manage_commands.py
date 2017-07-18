from hydra import Resource, SCHEMA
from mechanics.main import DRONE_URL, DRONE1
from mechanics.main import RES_DRONE
import json

def get_command_collection():
    """Get command collection from the drone server."""
    get_command_collection_ = RES_DRONE.find_suitable_operation(None, None, DRONE1.CommandCollection)
    resp, body = get_command_collection_()
    assert resp.status == 200, "%s %s" % (resp.status, resp.reason)

    body = json.loads(body)
    return body

## NOTE: id_ will be the IRI stored in Drone Collection
def delete_command(id_):
    """Delete a command from the collection given command @id attribute."""
    res = Resource.from_iri(DRONE_URL + id_)
    # name = i.value(SCHEMA.name)
    resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
    if resp.status // 100 != 2:
        print("error deleting <%s>" % i.identifier)
    else:
        print("deleted <%s>" % i.identifier)
