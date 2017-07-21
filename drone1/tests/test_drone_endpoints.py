""" Tests for checking if all the drone endpoints are working properly."""

import unittest
import requests
import json
import os
from mechanics.main import get_drone_default
from mechanics.main import gen_Command, gen_State, gen_Datastream

## FOR OUTSIDE THE CONTAINER
# DRONE_URL = "http://192.168.99.100:8081/" ## Windows
# DRONE_URL = "http://localhost:8081/" ##Linux

## FOR INSIDE THE CONTAINER
DRONE_URL = "http://drone1/"

class TestDroneRequests(unittest.TestCase):

    def test_request_vocab(self):
        """Test the drone vocab."""
        request_get = requests.get(DRONE_URL + 'droneapi/vocab')
        request_put = requests.put(DRONE_URL + 'droneapi/vocab', data=json.dumps(dict(foo = 'bar')))
        request_post = requests.post(DRONE_URL + 'droneapi/vocab', data=json.dumps(dict(foo = 'bar')))
        request_delete = requests.delete(DRONE_URL + 'droneapi/vocab')
        assert request_get.status_code == 200
        assert request_put.status_code == 405
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_entrypoint(self):
        """Test the drone entrypoint."""
        request_get = requests.get(DRONE_URL + 'droneapi/')
        request_put = requests.put(DRONE_URL + 'droneapi/', data=json.dumps(dict(foo = 'bar')))
        request_post = requests.post(DRONE_URL + 'droneapi/', data=json.dumps(dict(foo = 'bar')))
        request_delete = requests.delete(DRONE_URL + 'droneapi/')
        assert request_get.status_code == 200
        assert request_put.status_code == 405
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_drone(self):
        """Test the /Drone endpoint."""
        request_get = requests.get(DRONE_URL + 'droneapi/Drone')
        request_put = requests.put(DRONE_URL + 'droneapi/Drone', data=json.dumps(get_drone_default()))
        request_post = requests.post(DRONE_URL + 'droneapi/Drone', data=json.dumps(get_drone_default()))
        request_delete = requests.delete(DRONE_URL + 'droneapi/Drone')
        ## 404 if drone is not initialized use mechanics.drone_init to initialize
        assert request_get.status_code in [200, 404]
        assert request_put.status_code == 405
        assert request_post.status_code in [200,201]
        assert request_delete.status_code == 405

    def test_request_datastream(self):
        """Test the /Datastream endpoint."""
        datastream = gen_Datastream(100, "0,0", -1000)

        request_get = requests.get(DRONE_URL + 'droneapi/Datastream')
        request_put = requests.put(DRONE_URL + 'droneapi/Datastream', data=json.dumps(datastream))
        request_post = requests.post(DRONE_URL + 'droneapi/Datastream', data=json.dumps(datastream))
        request_delete = requests.delete(DRONE_URL + 'droneapi/Datastream')
        ## 404 if drone is not initialized use mechanics.drone_init to initialize
        assert request_get.status_code in [200,404]
        assert request_put.status_code == 405
        assert request_post.status_code in [200,201]
        assert request_delete.status_code == 405

    def test_request_command_collection(self):
        """Test the /CommandCollection endpoint."""
        state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
        command = gen_Command(123, state)

        request_get = requests.get(DRONE_URL + 'droneapi/CommandCollection')
        request_put = requests.put(DRONE_URL + 'droneapi/CommandCollection', data=json.dumps(command))
        request_post = requests.post(DRONE_URL + 'droneapi/CommandCollection', data=json.dumps(command))
        request_delete = requests.delete(DRONE_URL + 'droneapi/CommandCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405


    def test_request_command_collection_wrong_type_put(self):
        """Test the /CommandCollection endpoint PUT with wrong type object."""
        state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
        command = gen_Command(123, state)
        command["@type"] = "Dummy"

        request_put = requests.put(DRONE_URL + 'droneapi/CommandCollection', data=json.dumps(command))
        assert request_put.status_code == 400


if __name__ == '__main__':
    message = """
    Running tests for the app. Checking if all responses are in proper order.
    NOTE: This doesn't ensure that data is entered or deleted in a proper manner.
    It only checks the format of the reponses.
    """
    print(message)
    unittest.main()
