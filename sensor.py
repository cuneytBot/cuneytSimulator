#Can also add specific sensor error rates

class Sensor(object):
    def __init__(self,x,y,th):
        self,x = x
        self.y = y
        self.th = th
        pass

class ProximitySensor(Sensor):
    def __init__(self,x,y,th,r):
        #r is range
        super(ProximitySensor, self,x,y,th).__init__()
        self.r = r
    def sense(self,map):
        #check if there is any obstacles
        pass

class DistanceSensor(Sensor):
    def __init__(self,x,y,th,r):
        #r is range
        super(ProximitySensor, self,x,y,th).__init__()
        self.r = r
    def sense(self,map):
        #check if there is any obstacles and how far is it
        pass
