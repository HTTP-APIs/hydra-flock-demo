echo "Starting Simulation Central Controller"
python sim_controller/flock_controller/main.py &
echo "Central Controller started successfully!"

echo "Initializing Central Controller Location"
python sim_controller/flock_controller/mechanics/update_location.py

echo "Starting Drone1"
python sim_drone/flock_drone/main.py &
echo "Drone1 successfully started!"

echo "Starting Simulation GUI"
python sim_gui/app.py &
echo "Simulation GUI started successfully"

## Wait for 4 seconds.
/bin/sleep 4

echo "Initializing Drone1"
python sim_drone/flock_drone/mechanics/drone_init.py

## Wait for 2 seconds.
/bin/sleep 2
echo "Starting Listner.py"
python sim_drone/flock_drone/mechanics/listner.py &
