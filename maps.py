
class Maps(object):

    def __init__(self,walls = "default",thickness = 5,color = (100,100,100)):
        #walls is a a nested list of closed geometries made out of
        #a list of points e.g.:
        #[[(20,30),(120,40),(54,23),(25,230)],[(20,230),(239,129),(239,430)]]
        self.thickness = thickness
        self.color = color
        self.defualt_maps = {
        "custom1" :  [[(60,340),(600,600),(630,70),(50,60)]],
        "custom2" : [[(60,340),(600,600),(630,70),(50,60)],[(170,160),(160,200),(130,140)]],
        "default" : [[(0,0),(0,500),(500,500),(500,0)]]
        }

        try:
            self.walls = self.defualt_maps[walls]
        except TypeError:
            self.walls = walls
        except KeyError:
            self.walls = self.defualt_maps["default"]

'''
        if type(walls) == str:
            if walls == "custom1":
                self.walls = [[(60,340),(600,600),(630,70),(50,60)]]
            else:
                #default
                self.walls = [[(0,0),(0,500),(500,500),(500,0)]]
        else:
            self.walls = walls'''