"""API Doc generator for the drone side API."""

import json
from doc_gen import HydraDoc, HydraClass, HydraProp, HydraOp


def drone_doc(API):
    """Generate API Doc for drone."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the drone side API",
                       "API Documentation for the drone side system",
                       "/"+API+"/")

    # Drone Class
    drone = HydraClass("Drone", "Drone", "Class for a drone", API)

    # Properties
    drone.add_supported_prop(HydraProp("http://auto.schema.org/speed", "Speed", "true", "true", "true").get())
    drone.add_supported_prop(HydraProp("http://schema.org/geo", "Position", "true", "true", "true").get())
    drone.add_supported_prop(HydraProp("http://schema.org/fuelCapacity", "Battery", "true", "true", "true").get())
    drone.add_supported_prop(HydraProp("http://schema.org/device", "Sensor", "true", "false", "true").get())
    drone.add_supported_prop(HydraProp("http://schema.org/model", "Model", "true", "false", "true").get())
    drone.add_supported_prop(HydraProp("https://schema.org/status", "Status", "true", "true", "true").get())

    # Operations
    drone.add_supported_op(HydraOp("/"+API+"/change_speed",
                                   "ChangeSpeed",
                                   "PUT",
                                   "http://auto.schema.org/speed",
                                   "null",
                                   [{"code": 200, "description": "Speed Changed"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/change_position",
                                   "ChangePosition",
                                   "PUT",
                                   "http://schema.org/geo",
                                   "null",
                                   [{"code": 200, "description": "Position Changed"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/change_status",
                                   "ChangeStatus",
                                   "PUT",
                                   "http://schema.org/status",
                                   "null",
                                   [{"code": 200, "description": "Status Changed"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_speed",
                                   "GetSpeed",
                                   "GET",
                                   "null",
                                   "http://auto.schema.org/speed",
                                   [{"code": 200, "description": "Speed returned"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_position",
                                   "GetPosition",
                                   "GET",
                                   "null",
                                   "http://schema.org/geo",
                                   [{"code": 200, "description": "Position returned"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_battery_status",
                                   "GetBatteryStatus",
                                   "GET",
                                   "null",
                                   "http://schema.org/fuelCapacity",
                                   [{"code": 200, "description": "Battery status returned"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_model",
                                   "GetModel",
                                   "GET",
                                   "null",
                                   "http://schema.org/model",
                                   [{"code": 200, "description": "Model returned"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_status",
                                   "GetStatus",
                                   "GET",
                                   "null",
                                   "http://schema.org/status",
                                   [{"code": 200, "description": "Status returned"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/get_temperature",
                                   "GetTemperature",
                                   "GET",
                                   "null",
                                   "http://schema.org/Float",
                                   [{"code": 200, "description": "Temperature returned"}]).get())

    drone.add_supported_op(HydraOp("/"+API+"/recharge",
                                   "GetTemperature",
                                   "POST",
                                   "http://schema.org/Action",
                                   "http://schema.org/fuelCapacity",
                                   [{"code": 200, "description": "Successfully charged"}]).get())
    api_doc.add_supported_class(drone.get())

    return api_doc


if __name__ == "__main__":
    print(drone_doc("droneapi").to_json())
