echo "Removing directories if exist"
rm -rf hydrus sim_controller sim_gui sim_drone1 sim_drone2 sim_drone3 sim_drone4

echo "Install requirements..."
pip install -r requirements.txt
#

git clone -b develop https://github.com/chrizandr/hydrus.git hydrus
git clone -b develop --single-branch https://github.com/chrizandr/hydra-flock-central-controller.git sim_controller
git clone -b develop --single-branch https://github.com/chrizandr/hydra-flock-gui.git sim_gui

# Drone1
git clone -b develop --single-branch https://github.com/chrizandr/hydra-flock-drone.git sim_drone1
# Drone2
git clone -b develop --single-branch https://github.com/chrizandr/hydra-flock-drone.git sim_drone2
# Drone3
git clone -b develop --single-branch https://github.com/chrizandr/hydra-flock-drone.git sim_drone3
# Drone4
git clone -b develop --single-branch https://github.com/chrizandr/hydra-flock-drone.git sim_drone4

## Updating drone settings
echo "Updating drone settings"
cp drone_settings/drone1_settings.py sim_drone1/flock_drone/settings.py
cp drone_settings/drone2_settings.py sim_drone2/flock_drone/settings.py
cp drone_settings/drone3_settings.py sim_drone3/flock_drone/settings.py
cp drone_settings/drone4_settings.py sim_drone4/flock_drone/settings.py
echo "Done!"

echo "Generating new docs"
python -m sim_drone1.flock_drone.api_docs.doc_gen
python -m sim_drone2.flock_drone.api_docs.doc_gen
python -m sim_drone3.flock_drone.api_docs.doc_gen
python -m sim_drone4.flock_drone.api_docs.doc_gen
echo "Done!"
