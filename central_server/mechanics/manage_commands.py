"""Operations for managing commands."""
from hydra import Resource, SCHEMA
from mechanics.main import DRONE1, CENTRAL_SERVER
from mechanics.main import RES_DRONE1, RES_CS
from mechanics.main import gen_Command, gen_State
import json


def get_command_collection():
    """Get command collection from the central server."""
    get_command_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.CommandCollection)
    resp, body = get_command_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body


def create_command(command):
    """Add a command entity to the central server."""
    create_command_ = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.Command)
    resp, body = create_command_(command)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_command = Resource.from_iri(resp['location'])
    print("Command created successfully.")
    return new_command


# NOTE: id_ will be the IRI stored in Drone Collection
def issue_command(RES, Namespace_, command):
    """Issue Commands to Drones."""
    issue_command_ = RES.find_suitable_operation(SCHEMA.AddAction, Namespace_.Command)
    resp, body = issue_command_(command)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_command = Resource.from_iri(resp['location'])
    print("Command issued successfully.")
    return new_command


if __name__ == "__main__":
    print(get_command_collection())

    state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
    command = gen_Command(state)
    print(create_command(command))

    print(issue_command(RES_DRONE1, DRONE1, command))
