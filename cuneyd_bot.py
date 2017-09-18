import math
import random
import sensor
class CuneydBot(object):
    def __init__(self, x, y, th, vl=0, vr=0, id=0,p = 1,sensors_xyt = [(-1,1,math.pi),(1,1,0),(0,1,math.pi/2)],gr=100):
	self.pos = [x,y,th]
	self.wheel_vel = [vl,vr]
	self.sensed_pos = [x,y,th]
        self.ID = ID
        self.p = p
        self.sensors = []
	self.gr=gr
	
    def diff_drive(self,v,w):
        x = math.sin(w*t)*v*t
        y = math.cos(w*t)*v*t
        return (x,y)

    def noisefy(self,data,percent_error):
		#noisefies input by percent_error
        return data + data*(2*random.random()-1)*percent_error

    def add_sensor(self,x,y,th,sensor_type = sensor.ProximitySensor):
        #adds sensor to the according place
        self.sensors.append(Sensor.sensor_type(x,y,th))
        pass

    def diff_drive_overtime(self,t):
        #calculates the robots position with respect to itself after t seconds,
        #with dt in miliseconds, with the selected drive method and updates it
        #relative to cardinal coordinates
	W = self.wheel_vel[1] - self.wheel_vel[0]
	V = sum(self.wheel_vel)/2
        x,y,th = 0
        for dt in range(0,t, 1.0/self.gr):
            th += dt * W / 2
            x += math.cos(th)*V*dt
            y += math.sin(th)*V*dt
            th += dt * W / 2	
        #update coordinates
        self.x = x*math.cos(self,th) - y*math.sin(self.th)
        self.y = x*math.sin(self.th) + y*math.cos(self,th) 








