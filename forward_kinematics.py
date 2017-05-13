from actuator import Actuator
import sys
import math

actuator = Actuator(['y', [80, 0., 0.], 'z', [80, 0., 0.], 'z', [120, 0., 0.]])

args = sys.argv
point = actuator.forward_kinematics([int(args[1]), int(args[2]), int(args[3])])
output = round(point.x, 2), round(point.y, 2), round(point.z, 2)
sys.stdout.write(output)
