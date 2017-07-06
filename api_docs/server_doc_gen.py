"""API Doc generator for the server side API."""

import json
from doc_gen import hydra_doc, hydra_class, hydra_prop, hydra_op
from drone_doc_gen import drone_doc


def server_doc(API):
    """Generate API Doc for server."""
    # Main API Doc
    api_doc = hydra_doc(API,
                        "API Doc for the server side API",
                        "API Documentation for the server side system",
                        "/"+API+"/")

    # Drone operations on server must be linked to same operations on the specific drone
    drone = drone_doc(API)["supportedClass"][0]

    log = hydra_class("LogEntry", "LogEntry", "Class for a log entry", API)
    # Subject
    log["supportedProperty"].append(hydra_prop("http://hydrus.com/serverapi/vocab/Drone", "Drone", "true", "true", "true"))

    # Predicate
    log["supportedProperty"].append(hydra_prop("http://schema.org/UpdateAction", "Update", "true", "true", "false"))
    log["supportedProperty"].append(hydra_prop("http://schema.org/ReplyAction", "Get", "true", "true", "false"))

    # Objects
    log["supportedProperty"].append(hydra_prop("http://auto.schema.org/speed", "Speed", "true", "true", "false"))
    log["supportedProperty"].append(hydra_prop("http://schema.org/geo", "Position", "true", "true", "false"))
    log["supportedProperty"].append(hydra_prop("http://schema.org/fuelCapacity", "Battery", "true", "true", "false"))
    log["supportedProperty"].append(hydra_prop("http://schema.org/device", "Sensor", "true", "false", "false"))
    log["supportedProperty"].append(hydra_prop("http://schema.org/model", "Model", "true", "false", "false"))
    log["supportedProperty"].append(hydra_prop("https://schema.org/status", "Status", "true", "true", "false"))

    # Only create operation for logs
    log["supportedOperation"].append(hydra_op("/"+API+"/log_entry",
                                              "CreateEntry",
                                              "POST",
                                              "http://hydrus.com/LogEntry",
                                              "null",
                                              [{"code": 200, "description": "Log entered"}]))

    area = hydra_class("Area", "Area", "Class for Area of Interest of the server", API)

    # Using two positions to have a bounding box
    area["supportedProperty"].append(hydra_prop("http://schema.org/geo", "TopLeft", "true", "true", "true"))
    area["supportedProperty"].append(hydra_prop("http://schema.org/geo", "BottomRight", "true", "true", "true"))

    # Allowing updation of the area of interest
    area["supportedOperation"].append(hydra_op("/"+API+"/update_area",
                                               "UpdateArea",
                                               "PUT",
                                               "http://hydrus.com/Area",
                                               "null",
                                               [{"code": 200, "description": "Area of interest changed"}]))

    api_doc["supportedClass"].append(drone)
    api_doc["supportedClass"].append(log)
    api_doc["supportedClass"].append(area)
    return api_doc


if __name__ == "__main__":
    print(json.dumps(server_doc("serverapi"), indent=4, sort_keys=True))
