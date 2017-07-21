""" Tests for checking if all the drone endpoints are working properly."""

import unittest
import requests
import json
import os
from mechanics.main import gen_Area, gen_State, gen_Command

## FOR OUTSIDE THE CONTAINER
# CS_URL = "http://192.168.99.100:8080/" ## Windows
# CS_URL = "http://localhost:8080/" ##Linux

## FOR INSIDE THE CONTAINER
CS_URL = "http://central_server/"

class TestCSRequests(unittest.TestCase):

    def test_request_vocab(self):
        """Test the central server vocab."""
        request_get = requests.get(CS_URL + 'serverapi/vocab')
        request_put = requests.put(CS_URL + 'serverapi/vocab', data=json.dumps(dict(foo = 'bar')))
        request_post = requests.post(CS_URL + 'serverapi/vocab', data=json.dumps(dict(foo = 'bar')))
        request_delete = requests.delete(CS_URL + 'serverapi/vocab')
        assert request_get.status_code == 200
        assert request_put.status_code == 405
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_entrypoint(self):
        """Test the central server entrypoint."""
        request_get = requests.get(CS_URL + 'serverapi/')
        request_put = requests.put(CS_URL + 'serverapi/', data=json.dumps(dict(foo = 'bar')))
        request_post = requests.post(CS_URL + 'serverapi/', data=json.dumps(dict(foo = 'bar')))
        request_delete = requests.delete(CS_URL + 'serverapi/')
        assert request_get.status_code == 200
        assert request_put.status_code == 405
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_area(self):
        """Test the Area endpoint."""
        area = gen_Area("0,0", "5,5")

        request_get = requests.get(CS_URL + 'serverapi/Area')
        request_put = requests.put(CS_URL + 'serverapi/Area', data=json.dumps(area))
        request_post = requests.post(CS_URL + 'serverapi/Area', data=json.dumps(area))
        request_delete = requests.delete(CS_URL + 'serverapi/Area')
        ## 404 if area is not set use mechanics.update_areaa to set area.
        assert request_get.status_code in [200, 404]
        assert request_put.status_code == 405
        assert request_post.status_code == 200
        assert request_delete.status_code == 405


    def test_request_command_collection(self):
        """Test the CommandCollection endpoint."""
        state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
        command = gen_Command(state)

        request_get = requests.get(CS_URL + 'serverapi/CommandCollection')
        request_put = requests.put(CS_URL + 'serverapi/CommandCollection', data=json.dumps(command))
        request_post = requests.post(CS_URL + 'serverapi/CommandCollection', data=json.dumps(command))
        request_delete = requests.delete(CS_URL + 'serverapi/CommandCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_datastream_collection(self):
        """Test the DatastreamCollection endpoint."""

        request_get = requests.get(CS_URL + 'serverapi/DatastreamCollection')
        request_put = requests.put(CS_URL + 'serverapi/DatastreamCollection', data=json.dumps({"hello":"World", "@type":"Datastream"}))
        request_post = requests.post(CS_URL + 'serverapi/DatastreamCollection', data=json.dumps({"hello":"World", "@type":"Datastream"}))
        request_delete = requests.delete(CS_URL + 'serverapi/DatastreamCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_drone_collection(self):
        """Test the DroneCollection endpoint."""

        request_get = requests.get(CS_URL + 'serverapi/DroneCollection')
        request_put = requests.put(CS_URL + 'serverapi/DroneCollection', data=json.dumps({"name":"test_drone", "@type":"Drone"}))
        request_post = requests.post(CS_URL + 'serverapi/DroneCollection', data=json.dumps({"name":"test_drone", "@type":"Drone"}))
        request_delete = requests.delete(CS_URL + 'serverapi/DroneCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_log_entry_collection(self):
        """Test the LogEntryCollection endpoint."""

        request_get = requests.get(CS_URL + 'serverapi/LogEntryCollection')
        request_put = requests.put(CS_URL + 'serverapi/LogEntryCollection', data=json.dumps({"@type":"LogEntry", "Log":"Test Log"}))
        request_post = requests.post(CS_URL + 'serverapi/LogEntryCollection', data=json.dumps({"@type":"LogEntry", "Log":"Test Log"}))
        request_delete = requests.delete(CS_URL + 'serverapi/LogEntryCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_message_collection(self):
        """Test the MessageCollection endpoint."""

        request_get = requests.get(CS_URL + 'serverapi/MessageCollection')
        request_put = requests.put(CS_URL + 'serverapi/MessageCollection', data=json.dumps({"@type":"Message", "message":"Test message"}))
        request_post = requests.post(CS_URL + 'serverapi/MessageCollection', data=json.dumps({"@type":"Message", "message":"Test message"}))
        request_delete = requests.delete(CS_URL + 'serverapi/MessageCollection')
        assert request_get.status_code == 200
        assert request_put.status_code == 201
        assert request_post.status_code == 405
        assert request_delete.status_code == 405

    def test_request_command_collection_wrong_type_put(self):
        """Test the CommandCollection endpoint PUT with wrong type ."""
        state = gen_State(-1000, "50", "North", "1,1", "Active", 100)
        command = gen_Command(state)
        command["@type"] = "Dummy"

        request_put = requests.put(CS_URL + 'serverapi/CommandCollection', data=json.dumps(command))
        assert request_put.status_code == 400

    def test_request_datastream_collection_wrong_type_put(self):
        """Test the DatastreamCollection endpoint PUT with wrong object type."""

        request_put = requests.put(CS_URL + 'serverapi/DatastreamCollection', data=json.dumps({"hello":"World", "@type":"Dummy"}))
        assert request_put.status_code == 400

    def test_request_drone_collection_wrong_type_put(self):
        """Test the DroneCollection endpoint PUT with wrong object type."""

        request_put = requests.put(CS_URL + 'serverapi/DroneCollection', data=json.dumps({"name":"test_drone", "@type":"Dummy"}))
        assert request_put.status_code == 400

    def test_request_log_entry_collection_wrong_type_put(self):
        """Test the LogEntryCollection endpoint PUT with wrong object type."""

        request_put = requests.put(CS_URL + 'serverapi/LogEntryCollection', data=json.dumps({"@type":"Dummy", "Log":"Test Log"}))
        assert request_put.status_code == 400

    def test_request_message_collection_wrong_type_put(self):
        """Test the MessageCollection endpoint PUT with wrong object type."""

        request_put = requests.put(CS_URL + 'serverapi/MessageCollection', data=json.dumps({"@type":"Dummy", "message":"Test message"}))
        assert request_put.status_code == 400


if __name__ == '__main__':
    message = """
    Running tests for the app. Checking if all responses are in proper order.
    NOTE: This doesn't ensure that data is entered or deleted in a proper manner.
    It only checks the format of the reponses.
    """
    print(message)
    unittest.main()
