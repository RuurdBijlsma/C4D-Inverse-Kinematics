import tinyik
import numpy
from point import Point3D


class Actuator:
    def __init__(self, arm_definition):
        for i, val in enumerate(arm_definition):  # Fix axes
            if arm_definition[i] == "z":
                arm_definition[i] = "y"
            elif arm_definition[i] == "y":
                arm_definition[i] = "z"

        self._arm = tinyik.Actuator(arm_definition)

    def inverse_kinematics(self, point):
        self._arm.ee = Actuator.change_format([point.x, point.y, point.z])
        return numpy.rad2deg(self._arm.angles)

    def forward_kinematics(self, angles):
        self._arm.angles = numpy.deg2rad(angles)
        pos = Actuator.change_format(self._arm.ee)
        return Point3D(pos[0], pos[1], pos[2])

    @staticmethod
    def change_format(pos):
        return pos[0], pos[2], pos[1]
