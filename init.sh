echo "Starting Simulation Central Controller"
python -m sim_controller.flock_controller.main &
echo "Central Controller started successfully!"

## Wait for 2 seconds.
/bin/sleep 8


echo "Initializing Central Controller Location"
python -m sim_controller.flock_controller.mechanics.update_location


echo "Starting Drone1"
python -m sim_drone1.flock_drone.main &
echo "Drone1 successfully started!"

echo "Starting Drone2"
python -m sim_drone2.flock_drone.main &
echo "Drone2 successfully started!"

echo "Starting Drone3"
python -m sim_drone3.flock_drone.main &
echo "Drone3 successfully started!"

echo "Starting Drone4"
python -m sim_drone4.flock_drone.main &
echo "Drone4 successfully started!"


echo "Starting Simulation GUI"
python -m sim_gui.app &
echo "Simulation GUI started successfully"

## Wait for 4 seconds.
/bin/sleep 8

echo "Initializing Drone1"
python -m sim_drone1.flock_drone.mechanics.drone_init

echo "Initializing Drone2"
python -m sim_drone2.flock_drone.mechanics.drone_init

echo "Initializing Drone3"
python -m sim_drone3.flock_drone.mechanics.drone_init

echo "Initializing Drone4"
python -m sim_drone4.flock_drone.mechanics.drone_init

## Wait for 2 seconds.
/bin/sleep 8

echo "Starting Drone1 main mechanics Loop"
python -m sim_drone1.flock_drone.mechanics.listener &

echo "Starting Drone2 main mechanics Loop"
python -m sim_drone2.flock_drone.mechanics.listener &

echo "Starting Drone3 main mechanics Loop"
python -m sim_drone3.flock_drone.mechanics.listener &

echo "Starting Drone4 main mechanics Loop"
python -m sim_drone4.flock_drone.mechanics.listener &
