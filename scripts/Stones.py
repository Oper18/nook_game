
from pymjin2 import *

class StonesImpl(object):
    def __init__(self, c):
        self.c = c
    def __del__(self):
        self.c = None

class Stones(object):
    def __init__(self, sceneName, nodeName, env):
        self.c = EnvironmentClient(env, "Stones/" + nodeName)
        self.impl = StonesImpl(self.c)
        self.c.setConst("SCENE",  sceneName)
    def __del__(self):
        # Tear down.
        self.c.clear()
        # Destroy.
        del self.impl
        del self.c

def SCRIPT_CREATE(sceneName, nodeName, env):
    return Stones(sceneName, nodeName, env)

def SCRIPT_DESTROY(instance):
    del instance

