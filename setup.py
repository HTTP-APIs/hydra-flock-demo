#!/usr/bin/env python

from distutils.core import setup

setup(name='hydra-flock-demo',
      version='0.0.1',
      description='A simulation for HYDRA: flying a flock of commercial drones',
      author='Hydra Ecosystem',
      author_email='collective@hydraecosystem.org',
      url='https://github.com/HTTP-APIs/hydra-flock-demo',
#      install_requires=['-e git+git://github.com/HTTP-APIs/hydra-flock-central-controller.git',
#                        '-e git+git://github.com/HTTP-APIs/hydra-flock-drone.git'],
      packages=[
        'flock_controller', 'flock_drone'
      ],
      package_dir={
          'flock_controller': 'flock_controller',
          'flock_drone': 'flock_drone'},
)
