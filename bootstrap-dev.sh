echo "Removing directories in exist"
rm -rf hydrus sim_controller sim_gui sim_drone1 sim_drone2 sim_drone3 sim_drone4

echo "Install requirements..."
pip install -r requirements.txt
#

git clone -b develop http://github.com/HTTP-APIs/hydrus.git hydrus
git clone http://github.com/xadahiya/hydra-flock-central-controller.git sim_controller
git clone http://github.com/xadahiya/hydra-flock-gui.git sim_gui

# Drone1
git clone http://github.com/xadahiya/hydra-flock-drone.git sim_drone1
# Drone2
git clone http://github.com/xadahiya/hydra-flock-drone.git sim_drone2
# Drone3
git clone http://github.com/xadahiya/hydra-flock-drone.git sim_drone3
# Drone4
git clone http://github.com/xadahiya/hydra-flock-drone.git sim_drone4
