echo "Starting Simulation Central Controller"
python sim_controller/flock_controller/main.py &
echo "Central Controller started successfully!"

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
