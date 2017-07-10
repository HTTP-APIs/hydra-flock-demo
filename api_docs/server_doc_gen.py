"""API Doc generator for the server side API."""

from doc_writer import HydraDoc, HydraClass, HydraProp, HydraOp
from drone_doc_gen import drone_doc


def server_doc(API, BASE_URL):
    """Generate API Doc for server."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the server side API",
                       "API Documentation for the server side system",
                       "/"+API+"/",
                       BASE_URL)

    # Drone operations on server must be linked to same operations on the specific drone
    drone_classes = drone_doc(API, BASE_URL).get()["supportedClass"]

    log = HydraClass("LogEntry", "LogEntry", "Class for a log entry", API, BASE_URL)
    # Subject
    log.add_supported_prop(HydraProp("vocab:Drone", "Drone", "true", "true", "true").get())
    # Predicate
    log.add_supported_prop(HydraProp("http://schema.org/UpdateAction", "Update", "true", "true", "false").get())
    log.add_supported_prop(HydraProp("http://schema.org/ReplyAction", "Get", "true", "true", "false").get())
    # Objects
    log.add_supported_prop(HydraProp("vocab:Status", "Status", "true", "true", "true").get())
    # Only create operation for logs
    log.add_supported_op(HydraOp("/"+API+"/get_latest_log",
                                 "GetLogEntries",
                                 "GET",
                                 "vocab:LogEntry",
                                 "null",
                                 [{"code": 200, "description": "Log returned"}]).get())

    data = HydraClass("Data", "Data", "Class for a data entry", API, BASE_URL)
    data.add_supported_prop(HydraProp("http://schema.org/QuantitativeValue", "Temperature", "true", "true", "false").get())

    area = HydraClass("Area", "Area", "Class for Area of Interest of the server", API, BASE_URL)
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

    for class_ in drone_classes:
        api_doc.add_supported_class(class_)
    api_doc.add_supported_class(log.get())
    api_doc.add_supported_class(area.get())

    return api_doc


if __name__ == "__main__":
    print(server_doc("serverapi", "http://hydrus.com/").to_json())
