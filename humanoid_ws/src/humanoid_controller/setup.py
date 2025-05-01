from setuptools import find_packages, setup
from glob import glob


package_name = 'humanoid_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/humanoid_launch.py']),
        ('share/' + package_name + '/resource', ['resource/humanoid_meshes.urdf']),
        ('share/' + package_name + '/resource/meshes', glob('resource/meshes/*.dae')),
        ('share/' + package_name + '/rviz', ['rviz/humanoid.rviz']),
    ],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tisyasingh',
    maintainer_email='tisyasingh@todo.todo',
    description='Humanoid robot joint controller package',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'humanoid_controller = humanoid_controller.joint_controller:main'
        ],
    },
    package_data={
        'humanoid_controller': [
            'resource/*.urdf',
            'resource/meshes/*.dae',  #Automatically adds all .dae files
        ],
    },
)
