"""API Doc generator for the drone side API."""

from hydrus.hydraspec.doc_writer import HydraDoc, HydraClass, HydraClassProp, HydraClassOp
import json


# NOTE: @xadahiya: I'll add notes to different parts so that there is no confusion between Doc and Simulation
def doc_gen(API, BASE_URL):
    """Generate API Doc for drone."""
    # Main API Doc
    api_doc = HydraDoc(API,
                       "API Doc for the drone side API",
                       "API Documentation for the drone side system",
                       API,
                       BASE_URL)

    # State Class
    # NOTE: Each drone will have only one State Class, this can't be deleted. Only read and update.
    state = HydraClass("State", "State", "Class for drone state objects")
    # Properties
    state.add_supported_prop(HydraClassProp("http://auto.schema.org/speed", "Speed", True, False, False))
    state.add_supported_prop(HydraClassProp("http://schema.org/geo", "Position", True, False, False))
    state.add_supported_prop(HydraClassProp("http://schema.org/fuelCapacity", "Battery", True, True, False))
    state.add_supported_prop(HydraClassProp("https://schema.org/status", "SensorStatus", True, False, False))

    # Drone Class
    # NOTE: The actual changes to the drone are to be made at the /api/Drone URI.
    # GET will return current State. POST will update the State.
    drone = HydraClass("Drone", "Drone", "Class for a drone", endpoint=True)
    # Properties
    drone.add_supported_prop(HydraClassProp("vocab:State", "DroneState", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/name", "name", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/model", "model", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://auto.schema.org/speed", "MaxSpeed", True, False, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/device", "Sensor", True, True, False))
    drone.add_supported_prop(HydraClassProp("http://schema.org/identifier", "DroneID", True, True, False))
    # Operations
    # The server may need to get the state of the drone, or mechanics may get new state at certain intervals and send to server
    drone.add_supported_op(HydraClassOp("GetState",
                                        "GET",
                                        None,
                                        "vocab:State",
                                        [{"statusCode": 404, "description": "Data not found"},
                                         {"statusCode": 200, "description": "State Returned"}]))
    # When new commands are issued, mechanics will need to change the state of the drone
    drone.add_supported_op(HydraClassOp("UpdateState",
                                        "POST",
                                        "vocab:State",
                                        None,
                                        [{"statusCode": 200, "description": "State updated"}]))

    # Command Class
    # NOTE: Commands are stored in a collection. You may GET a command or you may DELETE it, there is not UPDATE.
    command = HydraClass("Command", "Command", "Class for drone commands", endpoint=True)
    command.add_supported_prop(HydraClassProp("http://schema.org/UpdateAction", "Update", False, True, False))
    command.add_supported_prop(HydraClassProp("vocab:State", "State", False, False, False))
    # Used by mechanics to get newly added commands
    command.add_supported_op(HydraClassOp("GetCommand",
                                          "GET",
                                          None,
                                          "vocab:Command",
                                          [{"statusCode": 404, "description": "Data not found"},
                                           {"statusCode": 200, "description": "Command Returned"}]))
    # Used by server to add new commands
    command.add_supported_op(HydraClassOp("AddCommand",
                                          "PUT",
                                          "vocab:Command",
                                          None,
                                          [{"statusCode": 200, "description": "Command added"}]))
    # Used by mechanics to delete command after it has been executed
    command.add_supported_op(HydraClassOp("DeleteCommand",
                                          "DELETE",
                                          None,
                                          None,
                                          [{"statusCode": 200, "description": "Command deleted"}]))

    # Data class
    # NOTE: This is for the Data to be captured/generated. The mechanics module will enter random data and POST it.
    # The server will read[GET] the data when it needs it. No need for collections. Only one instance showing current reading of sensor
    # The URI is /api/Data
    data = HydraClass("Data", "Data", "Class for a data entry", endpoint=True)
    data.add_supported_prop(HydraClassProp("http://schema.org/QuantitativeValue", "Temperature", True, False, False))
    data.add_supported_prop(HydraClassProp("http://schema.org/identifier", "DroneID", True, False, False))
    data.add_supported_prop(HydraClassProp("http://schema.org/geo", "Position", True, False, False))
    data.add_supported_op(HydraClassOp("GetData",
                                       "GET",
                                       None,
                                       "vocab:Data",
                                       [{"statusCode": 404, "description": "Data not found"},
                                        {"statusCode": 200, "description": "Data returned"}]))
    data.add_supported_op(HydraClassOp("UpdateData",
                                       "POST",
                                       "vocab:Data",
                                       None,
                                       [{"statusCode": 200, "description": "Data updated"}]))

    api_doc.add_supported_class(state, collection=False)
    api_doc.add_supported_class(drone, collection=False)
    api_doc.add_supported_class(command, collection=True)
    api_doc.add_supported_class(data, collection=False)

    api_doc.add_baseCollection()
    api_doc.add_baseResource()
    api_doc.gen_EntryPoint()
    return api_doc


if __name__ == "__main__":
    dump = json.dumps(doc_gen("droneapi", "http://localhost/").generate(), indent=4, sort_keys=True)
    doc = '''"""Generated API Documentation for Drone API using drone_doc_gen.py."""\n\ndrone_doc = %s''' % dump
    doc = doc.replace('true', '"true"')
    doc = doc.replace('false', '"false"')
    doc = doc.replace('null', '"null"')
    f = open("drone_doc.py", "w")
    f.write(doc)
    f.close()
