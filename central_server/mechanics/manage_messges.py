from hydra import Resource, SCHEMA
from mechanics.main import CENTRAL_SERVER_URL, DRONE1
from mechanics.main import RES_CS
from mechanics.main import gen_Message
import json

def get_message_collection():
    """Get order collection from the central server."""
    get_message_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.MessageCollection)
    resp, body = get_message_collection_()
    assert resp.status == 200, "%s %s" % (resp.status, resp.reason)

    body = json.loads(body)
    return body

def create_message(message):
    """Add a message object entity to the central server."""
    message = gen_Message(message)
    create_message_ = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.MessageCollection)
    resp, body = create_message_(message)

    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_message = Resource.from_iri(resp['location'])
    print("Message created successfully.")
    return new_message


## NOTE: id_ will be the IRI stored in Message Collection
def delete_message(id_):
    """Delete a order from the collection given order @id attribute."""
    res = Resource.from_iri(CENTRAL_SERVER_URL + id_)
    # name = i.value(SCHEMA.name)
    resp, _ = i.find_suitable_operation(SCHEMA.DeleteAction)()
    if resp.status // 100 != 2:
        print("error deleting <%s>" % i.identifier)
    else:
        print("deleted <%s>" % i.identifier)
