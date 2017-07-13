"""API Doc generator for the drone side API."""

from doc_writer import HydraDoc, HydraClass, HydraClassProp, HydraClassOp
import json


def drone_doc(API, BASE_URL):
    """Generate API Doc for drone."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the drone side API",
                       "API Documentation for the drone side system",
                       API,
                       BASE_URL)

    # Status Class
    status = HydraClass("Status", "Status", "Class for drone status objects", endpoint=True)

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

    api_doc.add_supported_class(status, collection=False)
    api_doc.add_supported_class(drone, collection=False)

    api_doc.add_baseCollection()
    api_doc.add_baseResource()
    api_doc.gen_EntryPoint()
    return api_doc


if __name__ == "__main__":
    print(json.dumps(drone_doc("droneapi", "http://hydrus.com/").generate(), indent=4, sort_keys=True))
    # print(drone_doc("droneapi", "http://hydrus.com/").generate())
