"""Handle operations related to new commands for the drone."""

from hydra import Resource, SCHEMA
from mechanics.main import DRONE_URL, DRONE1
from mechanics.main import RES_DRONE
from mechanics.main import gen_State
from mechanics.main import gen_Command
import json


def get_command_collection():
    """Get command collection from the drone server."""
    get_command_collection_ = RES_DRONE.find_suitable_operation(None, None, DRONE1.CommandCollection)
    resp, body = get_command_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body
# print(get_command_collection())


def add_command(command):
    """Add command to drone server."""
    add_command_ = RES_DRONE.find_suitable_operation(SCHEMA.AddAction, DRONE1.Command)
    resp, body = add_command_(command)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_command = Resource.from_iri(resp['location'])
    print("Command posted successfully.")
    return new_command
# print(add_command(command))


# NOTE: id_ will be the IRI stored in Drone Collection
def delete_command(id_):
    """Delete a command from the collection given command @id attribute."""
    try:
        i = Resource.from_iri(DRONE_URL + id_)
        # name = i.value(SCHEMA.name)
        resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
        if resp.status // 100 != 2:
            return "error deleting <%s>" % i.identifier
        else:
            return "deleted <%s>" % i.identifier
    except:
        return {404: "Resource with Id %s not found!" % (id_,)}
# print(delete_command("/api/CommandCollection/175"))


state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
command = gen_Command(123, state)
