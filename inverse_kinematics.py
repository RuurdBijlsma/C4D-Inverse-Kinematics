from datetime import time

from actuator import Actuator
import sys
from point import Point3D
import math

actuator = Actuator(['y', [80, 0., 0.], 'z', [80, 0., 0.], 'z', [120, 0., 0.]])

args = sys.argv

angles = actuator.inverse_kinematics(Point3D(int(args[1]), int(args[2]), int(args[3])))
for i, angle in enumerate(angles):
    angles[i] = round(angle, 2)
sys.stdout.write("{0} {1} {2}".format(angles[0], angles[1], angles[2]))
