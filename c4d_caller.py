import c4d
import math
import sys
from subprocess import Popen, PIPE, STARTUPINFO, STARTF_USESHOWWINDOW


# Welcome to the world of Python

def main():
    def tool():
        return c4d.plugins.FindPlugin(c4d.doc.GetAction(), c4d.PLUGINTYPE_TOOL)

    def object():
        return c4d.doc.GetActiveObject()

    def tag():
        return c4d.doc.GetActiveTag()

    def renderdata():
        return c4d.doc.GetActiveRenderData()

    def prefs(id):
        return c4d.plugins.FindPlugin(id, c4d.PLUGINTYPE_PREFS)

    document = c4d.documents.GetActiveDocument()
    gamma = document.SearchObject("gamma")
    alpha = document.SearchObject("alpha")
    beta = document.SearchObject("beta")
    target = document.SearchObject("target")

    target_pos = target.GetRelPos()
    angles = get_angles([int(target_pos.x), int(target_pos.y), int(target_pos.z)])

    gamma[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_X] = math.radians(float(angles[0]))
    alpha[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z] = math.radians(float(angles[1]))
    beta[c4d.ID_BASEOBJECT_REL_ROTATION, c4d.VECTOR_Z] = math.radians(float(angles[2]))


def get_angles(location):
    startupinfo = STARTUPINFO()
    startupinfo.dwFlags |= STARTF_USESHOWWINDOW

    output, _ = Popen(
        ["python", "inverse_kinematics.py", str(location[0]), str(location[1]),
         str(location[2])],
        stdin=PIPE, stdout=PIPE, stderr=PIPE, startupinfo=startupinfo).communicate()

    return str(output).split(" ")


if __name__ == '__main__':
    main()
    c4d.EventAdd()
