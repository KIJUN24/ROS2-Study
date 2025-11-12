from setuptools import setup

# 우리가 정한 package 이름
package_name = 'my_package'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    py_modules=[],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='My ROS2 Python package example',
    license='Apache License 2.0',
    tests_require=['pytest'],
  
    # 우리가 건드릴 곳
    entry_points={
        'console_scripts': [
            # '터미널 상에서 실행시킬 이름 = <패키지명>.<.py의 노드명>:main',
            'talker = py_pubsub.ros2_publish_study:main', # ros2_publish_study.py의 main() 함수 실행
            'listener = py_pubsub.ros2_subscribe_study:main', # ros2_subscribe_study.py의 main() 함수 실행
        ],
    },
)
