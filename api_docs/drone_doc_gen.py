"""API Doc generator for the drone side API."""
import pprint
from parsed_classes_writer import ParsedClasses, HydraClass, HydraProp, HydraOp


def drone_doc(API, BASE_URL):
    """Generate API Doc for drone."""
    # Main API Doc
    parsed_classes = ParsedClasses()

    # Status Class
    status = HydraClass("Status", "Status", "Class for drone status objects", API, BASE_URL)

    # Properties
    status.add_supported_prop(HydraProp("http://auto.schema.org/speed", "Speed", "Speed of drone", "true", "false", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/geo", "Position", "Postion of drone", "true", "false", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/fuelCapacity", "Battery", "Battery of drone.", "true", "true", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/device", "Sensor", "Sensors in drone", "true", "true", "false").get())
    status.add_supported_prop(HydraProp("http://schema.org/model", "Model", "Model of drone", "true", "true", "false").get())
    status.add_supported_prop(HydraProp("https://schema.org/status", "SensorStatus", "Sensor staus of drone", "true", "false", "false").get())

    # Drone Class
    drone = HydraClass("Drone", "Drone", "Class for a drone", API, BASE_URL)

    # Properties
    drone.add_supported_prop(HydraProp("vocab:Status", "DroneStatus", "Current status of Drone.", "true", "false", "false").get())

    # Operations
    drone.add_supported_op(HydraOp("/"+API+"/issue_order",
                                   "ChangeStatus",
                                   "Change status of the drone.",
                                   "POST",
                                   "vocab: Status",
                                   "null",
                                   [{"code": 200, "description": "Status Changed"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_status",
                                   "GetStatus",
                                   "Get status of drone.",
                                   "GET",
                                   "null",
                                   "vocab: Status",
                                   [{"code": 200, "description": "Status Returned"}]).get())

    parsed_classes.add_supported_class(status.get())
    parsed_classes.add_supported_class(drone.get())

    return parsed_classes.get()


if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(drone_doc("droneapi", "http://hydrus.com/"))
