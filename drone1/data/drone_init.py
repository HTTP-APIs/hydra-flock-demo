# Initialize drone
from hydrus.data.db_models import main as initialize_db
from hydrus.data.insert_classes import main as insert_classes
from hydrus.data.crud import insert, get

# Initialize database
initialize_db()

# Insert drone related classes
insert_classes()

# Initialize drone Props
drone_specs = {
    "name": "drone1",
    "@type": "drone",
    "object": {
            "Identifier": -1,
            "Speed": 0,
            "Position": "0,0",
            "Battery": 100,
            "Destination":"0,0",
            "Sensor": "temprature",
            "Status": "Started"
    }
}

print(insert(drone_specs, id_=1))
print(get("1", "drone"))
