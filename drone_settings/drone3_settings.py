import os

## Using sqlite as database
global DB_URL
db_path = os.path.join(os.path.dirname(__file__), 'database.db')
DB_URL = 'sqlite:///{}'.format(db_path)


global HYDRUS_SERVER_URL, PORT, API_NAME
HYDRUS_SERVER_URL = "http://localhost:8083/"
PORT = 8083
API_NAME = "api"


## Drone configuration
global CENTRAL_SERVER_NAMESPACE, DRONE_NAMESPACE
CENTRAL_SERVER_NAMESPACE = "http://localhost:8080/api/vocab#"
DRONE_NAMESPACE = "http://localhost:8083/api/vocab#"

global DRONE_URL, CENTRAL_SERVER_URL
DRONE_URL = "http://localhost:8083"
CENTRAL_SERVER_URL = "http://localhost:8080"

global IRI_CS, IRI_DRONE
IRI_CS = "http://localhost:8080/api"
IRI_DRONE = "http://localhost:8083/api"

# Default drone object with DroneID -1000 for initialization.
# Speed and MaxSpeeds are in Km/h"""
DRONE_DEFAULT = {
    "@type": "Drone",
    "DroneID": "-1000",
    "Name": "Drone 3",
    "Model": "xyz",
    "MaxSpeed": "200",
    "Sensor": "Temperature",
    "DroneState": {
        "@type": "State",
        "Speed": "180",
        "Position": "0,0",
        "Battery": "100",
        "Direction": "S",
        "Status": "Active",
    }
}
