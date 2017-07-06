"""API Doc generator for the drone side API."""

import json
from doc_gen import hydra_doc, hydra_class, hydra_prop, hydra_op


def drone_doc(API):
    """Generate API Doc for drone."""
    # Main API Doc
    api_doc = hydra_doc(API,
                        "API Doc for the drone side API",
                        "API Documentation for the drone side system",
                        "/"+API+"/")

    # Drone Class
    drone = hydra_class("Drone", "Drone", "Class for a drone", API)

    # Properties
    drone["supportedProperty"].append(hydra_prop("http://auto.schema.org/speed", "Speed", "true", "true", "true"))
    drone["supportedProperty"].append(hydra_prop("http://schema.org/geo", "Position", "true", "true", "true"))
    drone["supportedProperty"].append(hydra_prop("http://schema.org/fuelCapacity", "Battery", "true", "true", "true"))
    drone["supportedProperty"].append(hydra_prop("http://schema.org/device", "Sensor", "true", "false", "true"))
    drone["supportedProperty"].append(hydra_prop("http://schema.org/model", "Model", "true", "false", "true"))
    drone["supportedProperty"].append(hydra_prop("https://schema.org/status", "Status", "true", "true", "true"))

    # Operations
    drone["supportedOperation"].append(hydra_op("/"+API+"/change_speed",
                                                "ChangeSpeed",
                                                "PUT",
                                                "http://auto.schema.org/speed",
                                                "null",
                                                [{"code": 200, "description": "Speed Changed"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/change_position",
                                                "ChangePosition",
                                                "PUT",
                                                "http://schema.org/geo",
                                                "null",
                                                [{"code": 200, "description": "Position Changed"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/change_status",
                                                "ChangeStatus",
                                                "PUT",
                                                "http://schema.org/status",
                                                "null",
                                                [{"code": 200, "description": "Status Changed"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/get_speed",
                                                "GetSpeed",
                                                "GET",
                                                "null",
                                                "http://auto.schema.org/speed",
                                                [{"code": 200, "description": "Speed returned"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/get_position",
                                                "GetPosition",
                                                "GET",
                                                "null",
                                                "http://schema.org/geo",
                                                [{"code": 200, "description": "Position returned"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/get_battery_status",
                                                "GetBatteryStatus",
                                                "GET",
                                                "null",
                                                "http://schema.org/fuelCapacity",
                                                [{"code": 200, "description": "Battery status returned"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/get_model",
                                                "GetModel",
                                                "GET",
                                                "null",
                                                "http://schema.org/model",
                                                [{"code": 200, "description": "Model returned"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/get_status",
                                                "GetStatus",
                                                "GET",
                                                "null",
                                                "http://schema.org/status",
                                                [{"code": 200, "description": "Status returned"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/get_temperature",
                                                "GetTemperature",
                                                "GET",
                                                "null",
                                                "http://schema.org/Float",
                                                [{"code": 200, "description": "Temperature returned"}]))

    drone["supportedOperation"].append(hydra_op("/"+API+"/recharge",
                                                "GetTemperature",
                                                "POST",
                                                "http://schema.org/Action",
                                                "http://schema.org/fuelCapacity",
                                                [{"code": 200, "description": "Successfully charged"}]))
    api_doc["supportedClass"].append(drone)

    return api_doc


if __name__ == "__main__":
    print(json.dumps(drone_doc("droneapi"), indent=4, sort_keys=True))
