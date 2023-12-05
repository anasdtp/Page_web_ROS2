from setuptools import find_packages, setup

package_name = 'pg_web_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    zip_safe=True,
    maintainer='anas',
    maintainer_email='mohamed-anas.daggag@universite-paris-saclay.fr',
    description='ROS 2 Python package for pubsub functionality',  # Ajoutez une description appropriée ici
    license='Apache License 2.0',  # Ajoutez la déclaration de licence appropriée
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = pg_web_ros.publisher_member_function:main',
            'listener = pg_web_ros.subscriber_member_function:main',
        ],
    },
)
