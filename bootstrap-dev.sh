echo "Install requirements..."
pip install -r requirements.txt
#
# git clone -b develop git@github.com:HTTP-APIs/hydrus.git hydrus
# git clone git@github.com:xadahiya/hydra-flock-central-controller.git sim_controller
# git clone git@github.com:xadahiya/hydra-flock-drone.git sim_drone
# git clone git@github.com:xadahiya/hydra-flock-gui.git sim_gui

git clone -b develop http://github.com/HTTP-APIs/hydrus.git hydrus
git clone http://github.com/xadahiya/hydra-flock-central-controller.git sim_controller
git clone http://github.com/xadahiya/hydra-flock-drone.git sim_drone
git clone http://github.com/xadahiya/hydra-flock-gui.git sim_gui
