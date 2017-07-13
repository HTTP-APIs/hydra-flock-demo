"""API Doc generator for the server side API."""

from doc_writer import HydraDoc, HydraClass, HydraClassProp, HydraClassOp
import json


def server_doc(API, BASE_URL):
    """Generate API Doc for server."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the server side API",
                       "API Documentation for the server side system",
                       API,
                       BASE_URL)

    # Drone operations on server must be linked to same operations on the specific drone
    status = HydraClass("Status", "Status", "Class for drone status objects")
    # Properties
    status.add_supported_prop(HydraClassProp("http://auto.schema.org/speed", "Speed", True, False, False))
    status.add_supported_prop(HydraClassProp("http://schema.org/geo", "Position", True, False, False))
    status.add_supported_prop(HydraClassProp("http://schema.org/fuelCapacity", "Battery", True, True, False))
    status.add_supported_prop(HydraClassProp("http://schema.org/device", "Sensor", True, True, False))
    status.add_supported_prop(HydraClassProp("http://schema.org/model", "Model", True, True, False))
    status.add_supported_prop(HydraClassProp("https://schema.org/status", "SensorStatus", True, False, False))

    # Drone Class
    drone = HydraClass("Drone", "Drone", "Class for a drone", endpoint=True)
    # Properties
    drone.add_supported_prop(HydraClassProp("vocab:Status", "DroneStatus", True, False, False))
    # Operations
    drone.add_supported_op(HydraClassOp("ChangeStatus",
                                        "POST",
                                        "vocab:Status",
                                        None,
                                        [{"code": 200, "description": "Status Changed"}]))
    drone.add_supported_op(HydraClassOp("GetStatus",
                                        "GET",
                                        None,
                                        "vocab:Status",
                                        [{"code": 200, "description": "Status Returned"}]))

    log = HydraClass("LogEntry", "LogEntry", "Class for a log entry")
    # Subject
    log.add_supported_prop(HydraClassProp("vocab:Drone", "Drone", True, True, True))
    # Predicate
    log.add_supported_prop(HydraClassProp("http://schema.org/UpdateAction", "Update", True, True, False))
    log.add_supported_prop(HydraClassProp("http://schema.org/ReplyAction", "Get", True, True, False))
    # Objects
    log.add_supported_prop(HydraClassProp("vocab:Status", "Status", True, True, True))

    data = HydraClass("Data", "Data", "Class for a data entry")
    data.add_supported_prop(HydraClassProp("http://schema.org/QuantitativeValue", "Temperature", True, True, False))

    area = HydraClass("Area", "Area", "Class for Area of Interest of the server", endpoint=True)
    # Using two positions to have a bounding box
    area.add_supported_prop(HydraClassProp("http://schema.org/geo", "TopLeft", True, True, True))
    area.add_supported_prop(HydraClassProp("http://schema.org/geo", "BottomRight", True, True, True))
    # Allowing updation of the area of interest
    area.add_supported_op(HydraClassOp("UpdateArea",
                                       "PUT",
                                       "http://hydrus.com/Area",
                                       "null",
                                       [{"code": 200, "description": "Area of interest changed"}]))
    area.add_supported_op(HydraClassOp("GetArea",
                                       "GET",
                                       "null",
                                       "http://hydrus.com/Area",
                                       [{"code": 404, "description": "Area of not found"}]))

    api_doc.add_supported_class(drone, collection=True)
    api_doc.add_supported_class(status)
    api_doc.add_supported_class(data, collection=True)
    api_doc.add_supported_class(log, collection=True)
    api_doc.add_supported_class(area)

    api_doc.add_baseResource()
    api_doc.add_baseCollection()
    api_doc.gen_EntryPoint()
    return api_doc


if __name__ == "__main__":
    print(json.dumps(server_doc("serverapi", "http://hydrus.com/").generate(), indent=4, sort_keys=True))
