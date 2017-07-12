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
    status.add_supported_prop(HydraProp("http://auto.schema.org/speed", "Speed", True, False, False).get())
    status.add_supported_prop(HydraProp("http://schema.org/geo", "Position", True, False, False).get())
    status.add_supported_prop(HydraProp("http://schema.org/fuelCapacity", "Battery", True, True, False).get())
    status.add_supported_prop(HydraProp("http://schema.org/device", "Sensor", True, True, False).get())
    status.add_supported_prop(HydraProp("http://schema.org/model", "Model", True, True, False).get())
    status.add_supported_prop(HydraProp("https://schema.org/status", "SensorStatus", True, False, False).get())

    # Drone Class
    drone = HydraClass("Drone", "Drone", "Class for a drone", API, BASE_URL)

    # Properties
    drone.add_supported_prop(HydraProp("vocab:Status", "DroneStatus", True, False, False).get())

    # Operations
    drone.add_supported_op(HydraOp("ChangeStatus",
                                   "POST",
                                   "vocab:Status",
                                   None,
                                   [{"code": 200, "description": "Status Changed"}]).get())

    drone.add_supported_op(HydraOp("GetStatus",
                                   "GET",
                                   None,
                                   "vocab:Status",
                                   [{"code": 200, "description": "Status Returned"}]).get())

    api_doc.add_supported_class(status.get(), collection=False)
    api_doc.add_supported_class(drone.get(), collection=False)

    api_doc.add_baseCollection()
    api_doc.add_baseResource()
    api_doc.gen_EntryPoint()
    api_doc.gen_Collections()
    return api_doc


if __name__ == "__main__":
    print(drone_doc("droneapi", "http://hydrus.com/").to_json())
