from hydra import Resource, SCHEMA
from mechanics.main import CENTRAL_SERVER_URL, DRONE1
from mechanics.main import RES_DRONE1
from mechanics.main import gen_Command
import json

def get_command_collection():
    """Get command collection from the central server."""
    get_command_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.CommandCollection)
    resp, body = get_command_collection_()
    assert resp.status == 200, "%s %s" % (resp.status, resp.reason)

    body = json.loads(body)
    return body

def create_command(command):
    """Add a command entity to the central server."""
    create_command_ = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.CommandCollection)
    resp, body = create_command_(command)

    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_command = Resource.from_iri(resp['location'])
    print("Command created successfully.")
    return new_command


## NOTE: id_ will be the IRI stored in Drone Collection
def delete_command(id_):
    """Delete a command from the collection given command @id attribute."""
    res = Resource.from_iri(CENTRAL_SERVER_URL + id_)
    # name = i.value(SCHEMA.name)
    resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
    if resp.status // 100 != 2:
        print("error deleting <%s>" % i.identifier)
    else:
        print("deleted <%s>" % i.identifier)

def issue_command(RES, Namespace_, command):
    """Issue Commands to Drones."""
    issue_command_ = RES.find_suitable_operation(SCHEMA.AddAction, Namespace_.CommandCollection)
    resp, body = issue_command_(command)

    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_command = Resource.from_iri(resp['location'])
    print("Command issued successfully.")
    return new_command

# print(issue_command(RES_DRONE1, DRONE1, {"Status":{}}))
