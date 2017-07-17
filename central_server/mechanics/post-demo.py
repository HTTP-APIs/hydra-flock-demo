"""
Example to create post reqests to the server.
"""
from hydra import Resource, SCHEMA
from rdflib import Namespace

DRONE1 = Namespace('http://192.168.99.100:8085/serverapi/vocab#')

def main():
    the_iri_of_the_resource = 'http://192.168.99.100:8085/serverapi'

    res = Resource.from_iri(the_iri_of_the_resource)

    print(res)

    print("\nApi documentation:")
    for supcls in res.api_documentation.supported_classes:
        print("  %s" % supcls.identifier)
        for supop in supcls.supported_operations:
            print("    %s" % supop.identifier)
    print("")

# Create new order for drone
    print(DRONE1.Data)
    create_order = res.find_suitable_operation(input_type = None, output_type= DRONE1.DataCollection)
    print(create_order)
    resp, body = create_order()
    print(body)
    # resp, body = create_order({
    #     "Destination": "This is halloween, this is halloween",
    #     "Speed": "2015-10-31T00:00:00Z",
    #     "Identifier": "2015-10-31T23:59:59Z",
    # })

    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_order = Resource.from_iri(resp['location'])
    # print(new_order)

## Create new message for drone
    create_message = res.find_suitable_operation(
        SCHEMA.AddAction, HYDRUS.message)
    resp, body = create_message({
        "message": "testing message 1"
    })

    assert resp.status == 201, "%s %s" % (resp.status, resp.reason)
    new_message = Resource.from_iri(resp['location'])

    print(new_message)


if __name__ == "__main__":
    main()
