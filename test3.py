class A():
    def __init__(self):
        print("is A")

class B(A):
    def __init__(self):
        print("is B")

class C(B):
    def __init__(self):
        print("is C")

asa = C()

if not issubclass(asa.__class__, A):
    print (asa.__class__)

else:
    print "YES"


from GSMaya.ProjectManager.Scene.BaseScene import BaseScene
from GSMaya.ProjectManager.Scene.AnimationScene import AnimationScene


