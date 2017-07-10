"""API Doc generator for the drone side API."""

from doc_writer import HydraDoc, HydraClass, HydraProp, HydraOp


def drone_doc(API, BASE_URL):
    """Generate API Doc for drone."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the drone side API",
                       "API Documentation for the drone side system",
                       "/"+API+"/",
                       BASE_URL)

    # Status Class
    status = HydraClass("Status", "Status", "Class for drone status objects", API, BASE_URL)

    # Properties
    status.add_supported_prop(HydraProp("http://auto.schema.org/speed", "Speed", "true", "false", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/geo", "Position", "true", "false", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/fuelCapacity", "Battery", "true", "true", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/device", "Sensor", "true", "true", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/model", "Model", "true", "true", "false").get())
    status.add_supported_prop(HydraProp("https://schema.org/status", "SensorStatus", "true", "false", "false").get())

    # Drone Class
    drone = HydraClass("Drone", "Drone", "Class for a drone", API, BASE_URL)

    # Properties
    drone.add_supported_prop(HydraProp("vocab:Status", "DroneStatus", "true", "false", "false").get())

    # Operations
    drone.add_supported_op(HydraOp("/"+API+"/issue_order",
                                   "ChangeStatus",
                                   "POST",
                                   "vocab: Status",
                                   "null",
                                   [{"code": 200, "description": "Status Changed"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_status",
                                   "GetStatus",
                                   "GET",
                                   "null",
                                   "vocab: Status",
                                   [{"code": 200, "description": "Status Returned"}]).get())

    api_doc.add_supported_class(status.get())
    api_doc.add_supported_class(drone.get())

    return api_doc


if __name__ == "__main__":
    print(drone_doc("droneapi", "http://hydrus.com/").to_json())
