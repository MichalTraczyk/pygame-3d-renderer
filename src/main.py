#from Screen import Screen
from pygame import Vector3

from src.Math.Transform import Transform

#screen = Screen(500)

t = Transform(Vector3(0,0,0),0)

print(t.InverseTransformPoint(Vector3(0, 0, 0)))
print(t.InverseTransformPoint(Vector3(0, 0, 0)))