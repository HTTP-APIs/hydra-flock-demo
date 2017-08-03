echo "Starting Simulation Central Controller"
python sim_controller/flock_controller/main.py &
echo "Central Controller started successfully!"

## Wait for 2 seconds.
/bin/sleep 2


echo "Initializing Central Controller Location"
python sim_controller/flock_controller/mechanics/update_location.py


echo "Starting Drone1"
cp drone_settings/drone1_settings.py sim_drone1/flock_drone/settings.py
python sim_drone1/flock_drone/main.py &
echo "Drone1 successfully started!"

echo "Starting Drone2"
cp drone_settings/drone2_settings.py sim_drone2/flock_drone/settings.py
python sim_drone2/flock_drone/main.py &
echo "Drone2 successfully started!"

echo "Starting Drone3"
cp drone_settings/drone3_settings.py sim_drone3/flock_drone/settings.py
python sim_drone3/flock_drone/main.py &
echo "Drone3 successfully started!"

echo "Starting Drone4"
cp drone_settings/drone4_settings.py sim_drone4/flock_drone/settings.py
python sim_drone4/flock_drone/main.py &
echo "Drone4 successfully started!"


echo "Starting Simulation GUI"
python sim_gui/app.py &
echo "Simulation GUI started successfully"

## Wait for 4 seconds.
/bin/sleep 4

echo "Initializing Drone1"
python sim_drone1/flock_drone/mechanics/drone_init.py

echo "Initializing Drone2"
python sim_drone2/flock_drone/mechanics/drone_init.py

echo "Initializing Drone3"
python sim_drone3/flock_drone/mechanics/drone_init.py

echo "Initializing Drone4"
python sim_drone4/flock_drone/mechanics/drone_init.py

## Wait for 2 seconds.
/bin/sleep 2

echo "Starting Drone1 main mechanics Loop"
python sim_drone1/flock_drone/mechanics/lisetner.py &

echo "Starting Drone2 main mechanics Loop"
python sim_drone2/flock_drone/mechanics/lisetner.py &

echo "Starting Drone3 main mechanics Loop"
python sim_drone3/flock_drone/mechanics/lisetner.py &

echo "Starting Drone4 main mechanics Loop"
python sim_drone4/flock_drone/mechanics/lisetner.py &
