echo "Starting Simulation Central Controller"
cd sim_controller
python -m flock_controller.main &
cd ../
echo "Central Controller started successfully!"

## Wait for 8 seconds.
/bin/sleep 8


echo "Initializing Central Controller Location"
python -m controller_settings.set_location

## Wait for 2 seconds
/bin/sleep 2


echo "Starting Drone1"
cd sim_drone1
python -m flock_drone.main &
cd ../
echo "Drone1 successfully started!"

echo "Starting Drone2"
cd sim_drone2
python -m flock_drone.main &
cd ../
echo "Drone2 successfully started!"

echo "Starting Drone3"
cd sim_drone3
python -m flock_drone.main &
cd ../
echo "Drone3 successfully started!"

echo "Starting Drone4"
cd sim_drone4
python -m flock_drone.main &
cd ../
echo "Drone4 successfully started!"


echo "Starting Simulation GUI"
cd sim_gui
python app.py &
cd ../
echo "Simulation GUI started successfully"

## Wait for 8 seconds.
/bin/sleep 8

echo "Initializing Drone1"
cd sim_drone1
python -m flock_drone.mechanics.drone_init
cd ../
/bin/sleep 2

echo "Initializing Drone2"
cd sim_drone2
python -m flock_drone.mechanics.drone_init
cd ../
/bin/sleep 2

echo "Initializing Drone3"
cd sim_drone3
python -m flock_drone.mechanics.drone_init
cd ../
/bin/sleep 2

echo "Initializing Drone4"
cd sim_drone4
python -m flock_drone.mechanics.drone_init
cd ../
/bin/sleep 2

## Wait for 8 seconds.
/bin/sleep 8

echo "Starting Drone1 main mechanics Loop"
cd sim_drone1
python -m flock_drone.mechanics.simulate &
cd ../

echo "Starting Drone2 main mechanics Loop"
cd sim_drone2
python -m flock_drone.mechanics.simulate &
cd ../

echo "Starting Drone3 main mechanics Loop"
cd sim_drone3
python -m flock_drone.mechanics.simulate &
cd ../

echo "Starting Drone4 main mechanics Loop"
cd sim_drone4
python -m flock_drone.mechanics.simulate &
cd ../

/bin/sleep 8
echo "Starting Central Controller main mechanics Loop"
cd sim_controller
python -m flock_controller.mechanics.simulate &
cd ../
