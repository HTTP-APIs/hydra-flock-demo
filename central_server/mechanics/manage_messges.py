"""Operations for managing messages."""
from hydra import Resource, SCHEMA
from mechanics.main import CENTRAL_SERVER
from mechanics.main import RES_CS
from mechanics.main import gen_Message
import json


def get_message_collection():
    """Get order collection from the central server."""
    get_message_collection_ = RES_CS.find_suitable_operation(None, None, CENTRAL_SERVER.MessageCollection)
    resp, body = get_message_collection_()
    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)

    body = json.loads(body.decode('utf-8'))
    return body


def create_message(message):
    """Add a message object entity to the central server."""
    create_message_ = RES_CS.find_suitable_operation(SCHEMA.AddAction, CENTRAL_SERVER.Message)
    resp, body = create_message_(message)

    assert resp.status in [200, 201], "%s %s" % (resp.status, resp.reason)
    new_message = Resource.from_iri(resp['location'])
    print("Message created successfully.")
    return new_message


if __name__ == "__main__":
    print(get_message_collection())
    message = gen_Message("Hello world")
    print(create_message(message))
