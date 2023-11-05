## *********************************************************
##
## File autogenerated for the tello_driver package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 246, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 291, 'description': 'Video rate', 'max': 4, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'fixed_video_rate', 'edit_method': "{'enum_description': 'Video rate options', 'enum': [{'srcline': 9, 'description': 'Let drone automatically decide', 'srcfile': '/home/tom/Dev/tello_ws/src/tello_driver/cfg/Tello.cfg', 'cconsttype': 'const int', 'value': 0, 'ctype': 'int', 'type': 'int', 'name': 'Auto'}, {'srcline': 10, 'description': 'Set to 1.0Mb/s fixed rate (~4.5KB/frame @ 30fps)', 'srcfile': '/home/tom/Dev/tello_ws/src/tello_driver/cfg/Tello.cfg', 'cconsttype': 'const int', 'value': 1, 'ctype': 'int', 'type': 'int', 'name': '1p0Mbps'}, {'srcline': 11, 'description': 'Set to 1.5Mb/s fixed rate (~6.6KB/frame @ 30fps)', 'srcfile': '/home/tom/Dev/tello_ws/src/tello_driver/cfg/Tello.cfg', 'cconsttype': 'const int', 'value': 2, 'ctype': 'int', 'type': 'int', 'name': '1p5Mbps'}, {'srcline': 12, 'description': 'Set to 2.0Mb/s fixed rate (~8.5KB/frame @ 30fps)', 'srcfile': '/home/tom/Dev/tello_ws/src/tello_driver/cfg/Tello.cfg', 'cconsttype': 'const int', 'value': 3, 'ctype': 'int', 'type': 'int', 'name': '2p0Mbps'}, {'srcline': 13, 'description': 'Set to 2.5Mb/s fixed rate ( ~11KB/frame @ 30fps)', 'srcfile': '/home/tom/Dev/tello_ws/src/tello_driver/cfg/Tello.cfg', 'cconsttype': 'const int', 'value': 4, 'ctype': 'int', 'type': 'int', 'name': '2p5Mbps'}]}", 'default': 0, 'level': 0, 'min': 0, 'type': 'int'}, {'srcline': 291, 'description': 'Rate for regularly requesting SPS data from drone (0: disabled)', 'max': 4.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'video_req_sps_hz', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 291, 'description': 'Limit altitude of Tello', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'altitude_limit', 'edit_method': '', 'default': 10, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Limit attitude of Tello', 'max': 25, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'attitude_limit', 'edit_method': '', 'default': 15, 'level': 0, 'min': 15, 'type': 'int'}, {'srcline': 291, 'description': 'Set low battery threshold of Tello', 'max': 100, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'low_bat_threshold', 'edit_method': '', 'default': 7, 'level': 0, 'min': 1, 'type': 'int'}, {'srcline': 291, 'description': 'Scale (down) vel_cmd value', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/melodic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'vel_cmd_scale', 'edit_method': '', 'default': 0.5, 'level': 0, 'min': 0.01, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Tello_Auto = 0
Tello_1p0Mbps = 1
Tello_1p5Mbps = 2
Tello_2p0Mbps = 3
Tello_2p5Mbps = 4
