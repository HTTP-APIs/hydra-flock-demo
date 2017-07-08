"""API Doc generator for the server side API."""

import json
from doc_gen import HydraDoc, HydraClass, HydraProp, HydraOp
from drone_doc_gen import drone_doc


def server_doc(API):
    """Generate API Doc for server."""
    # Main API Doc
    api_doc = HydraDoc(API,
                        "API Doc for the server side API",
                        "API Documentation for the server side system",
                        "/"+API+"/")

    # Drone operations on server must be linked to same operations on the specific drone
    drone = drone_doc(API).get()["supportedClass"][0]

    log = HydraClass("LogEntry", "LogEntry", "Class for a log entry", API)
    # Subject
    log.add_supported_prop(HydraProp("http://hydrus.com/serverapi/vocab/Drone", "Drone", "true", "true", "true").get())

    # Predicate
    log.add_supported_prop(HydraProp("http://schema.org/UpdateAction", "Update", "true", "true", "false").get())
    log.add_supported_prop(HydraProp("http://schema.org/ReplyAction", "Get", "true", "true", "false").get())

    # Objects
    log.add_supported_prop(HydraProp("http://auto.schema.org/speed", "Speed", "true", "true", "false").get())
    log.add_supported_prop(HydraProp("http://schema.org/geo", "Position", "true", "true", "false").get())
    log.add_supported_prop(HydraProp("http://schema.org/fuelCapacity", "Battery", "true", "true", "false").get())
    log.add_supported_prop(HydraProp("http://schema.org/device", "Sensor", "true", "false", "false").get())
    log.add_supported_prop(HydraProp("http://schema.org/model", "Model", "true", "false", "false").get())
    log.add_supported_prop(HydraProp("https://schema.org/status", "Status", "true", "true", "false").get())

    # Only create operation for logs
    log.add_supported_op(HydraOp("/"+API+"/log_entry",
                                 "CreateEntry",
                                 "POST",
                                 "http://hydrus.com/LogEntry",
                                 "null",
                                 [{"code": 200, "description": "Log entered"}]).get())

    area = HydraClass("Area", "Area", "Class for Area of Interest of the server", API)

    # Using two positions to have a bounding box
    area.add_supported_prop(HydraProp("http://schema.org/geo", "TopLeft", "true", "true", "true").get())
    area.add_supported_prop(HydraProp("http://schema.org/geo", "BottomRight", "true", "true", "true").get())

    # Allowing updation of the area of interest
    area.add_supported_op(HydraOp("/"+API+"/update_area",
                                  "UpdateArea",
                                  "PUT",
                                  "http://hydrus.com/Area",
                                  "null",
                                  [{"code": 200, "description": "Area of interest changed"}]).get())

    api_doc.add_supported_class(drone)
    api_doc.add_supported_class(log.get())
    api_doc.add_supported_class(area.get())
    return api_doc


if __name__ == "__main__":
    print(server_doc("serverapi").to_json())
