"""API Doc generator for the drone side API."""

from hydrus.hydraspec.doc_writer import HydraDoc, HydraClass, HydraClassProp, HydraClassOp
import json


def doc_gen(API, BASE_URL):
    """Generate API Doc for drone."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the drone side API",
                       "API Documentation for the drone side system",
                       API,
                       BASE_URL)

    # Status Class
    status = HydraClass("http://hydrus.com/Status", "Status", "Class for drone status objects")
    # Properties
    status.add_supported_prop(HydraClassProp("http://auto.schema.org/speed", "Speed", True, False, False))
    status.add_supported_prop(HydraClassProp("http://schema.org/geo", "Position", True, False, False))
    status.add_supported_prop(HydraClassProp("http://schema.org/fuelCapacity", "Battery", True, True, False))
    status.add_supported_prop(HydraClassProp("https://schema.org/status", "SensorStatus", True, False, False))

    # Drone Class
    drone = HydraClass("http://hydrus.com/Drone", "Drone", "Class for a drone", endpoint=True)
    # Properties
    drone.add_supported_prop(HydraClassProp("vocab:Status", "DroneStatus", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/name", "name", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/model", "model", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://auto.schema.org/speed", "MaxSpeed", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/device", "Sensor", True, True, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/identifier", "DroneID", True, True, False))
    # Operations
    drone.add_supported_op(HydraClassOp("GetStatus",
                                        "GET",
                                        None,
                                        "vocab:Status",
                                        [{"statusCode": 200, "description": "Status Returned"}]))
    drone.add_supported_op(HydraClassOp("IssueCommand",
                                        "POST",
                                        "vocab:Command",
                                        None,
                                        [{"statusCode": 200, "description": "Command issued"}]))

    data = HydraClass("http://hydrus.com/Data", "Data", "Class for a data entry", endpoint=True)
    data.add_supported_prop(HydraClassProp("http://schema.org/QuantitativeValue", "Temperature", True, False, False))
    data.add_supported_prop(HydraClassProp("http://schema.org/identifier", "DroneID", True, False, False))
    data.add_supported_prop(HydraClassProp("http://schema.org/geo", "Position", True, False, False))
    data.add_supported_op(HydraClassOp("GetData",
                                       "GET",
                                       None,
                                       "vocab:Data",
                                       [{"statusCode": 404, "description": "Data not found"},
                                        {"statusCode": 200, "description": "Data returned"}]))

    api_doc.add_supported_class(status, collection=False)
    api_doc.add_supported_class(drone, collection=False)
    api_doc.add_supported_class(data, collection=False)

    api_doc.add_baseCollection()
    api_doc.add_baseResource()
    api_doc.gen_EntryPoint()
    return api_doc


if __name__ == "__main__":
    print(json.dumps(doc_gen("droneapi", "http://hydrus.com/").generate(), indent=4, sort_keys=True))
    # print(drone_doc("droneapi", "http://hydrus.com/").generate())
