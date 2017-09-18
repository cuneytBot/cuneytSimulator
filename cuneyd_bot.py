import math
import random
import requests
import sensor

class CuneydBot(object):
    ''' function init: constructor for CuneydBot Simulator class
        @param pos: starting position vector([x,y,th])
	@param d: wheel distance
	@param vl: left wheel starting velocity
	@param vr: right wheel starting velocity
	@id: robot unique id
	@param p: starting certainty
	@param sensors: an object extending the sensor class
	@param gr: granularity -how many steps per seconds- for integration
	@param encoder_error: max error of the encoder,in radians per revolution
	@return: CuneydBot object
    '''
    def __init__(self, pos, d, vl=0, vr=0, id=0,p = 1,sensors=[],gr=100,encoder_error = 0.05,server_address="localhost:5000"):
	self.pos = pos
	self.wheel_vel = [vl,vr]
	self.sensed_pos = pos
	self.err_p = p
        self.ID = ID
        self.p = p
	self.d = d
        self.sensors = sensors
	self.gr=gr
	self.encoder_error = encoder_error
	self.server_address = server_address
        try:
	    data = {'x': self.pos[0], 'y': self.pos[1], 't': self.pos[2], 'ID': self.ID, 'p': self.p}
	    data_err = {'x': self.pos[0], 'y': self.pos[1], 't': self.pos[2], 'ID': -self.ID, 'p': self.p}

	    requests.post(self.server_address+"/create_cuneyd", json=data)
	    requests.post(self.server_address+'/create_cuneyd', json=data_err)
        except Exception as e:
	    print "Connection error: "+repr(e)
	    
	
    def post_position(self):
	try:
	    data = {'x': self.pos[0], 'y': self.pos[1], 't': self.pos[2], 'p': self.p, 'ID': self.ID}
	    requests.post(self.server_address+'/update_cuneyd', json=data)
        except Exception as e:
	    print "Connection error: " + repr(e)
	
    def post_err_position(self):
	try:
	    data = {'x': self.err_pos[0], 'y': self.err_pos[1], 't': self.err_pos[2], 'p': self.err_p, 'ID': - self.ID}
	    request.post(self.server_address+'/update_cuneyd',json=data)
	except Exception as e:
	    print "Connection error: " + repr(e)
    
    def add_sensor(self,x,y,th,sensor_type = sensor.ProximitySensor):
        #adds sensor to the according place
        self.sensors.append(Sensor.sensor_type(x,y,th))
        pass

    ''' function diff_drive: updates the robots position after simulating a continuous drive
        for t seconds.
	@param t: number of seconds to simulate drive with current configuration
    '''
    def diff_drive_overtime(self,t):
        #calculates the robots position with respect to itself after t seconds
	vr_err = self.wheel_vel[1] * random.random() * encoder_error / math.pi
	vl_err = self.wheel_vel[0] * random.random() * encoder_error / math.pi
	
	W = (self.wheel_vel[1] - self.wheel_vel[0]) / self.d
	V = sum(self.wheel_vel) / 2
	
	W_err = (vr_err - vl_err) / self.d
	V_err = (vr_err + vl_err) / 2
	
        x,y,th = 0
	x_err,y_err,th_err = 0
        for dt in range(0,t, 1.0/self.gr):
            th += dt * W / 2
	    th_err += dt * W_err / 2
		
            x += math.cos(th) * V * dt
	    x_err += math.cos(th_err) * V_err * dt
		
            y += math.sin(th) * V * dt
	    y_err += math.sin(th_err) * V_err * dt
            th += dt * W / 2	
	    th_err += dt * W_err / 2
	
	#Update real coordinates
	#TODO: make this into a transform matrix
        self.pos[0] += x * math.cos(self.pos[2]) - y * math.sin(self.pos[2])
	self.pos[1] += x * math.sin(self.pos[2]) + y * math.cos(self.pos[2])
	self.pos[2] += th
	
	#Update sensed coordinates
	#TODO: make this into a transform matrix
	self.sensed_pos[0] += x_err * math.cos(self.sensed_pos[2]) - y_err * math.sin(self.sensed_pos[2])
	self.sensed_pos[1] += x_err * math.sin(self.sensed_pos[2]) + y_err * math.cos(self.sensed_pos[2])
	self.sensed_pos[2] += th_err








