class Node:
    def __init__(self, id, lat, lon, elevation):
        self.id = id 
        self.lat = lat 
        self.lon = lon
        self.elevation = elevation 
        self.cost = 0
        self.g = 0
        self.h = 0
    
    def __repr__(self):
        return f"Node({self.id} lat: {self.lat}, lon: {self.lon}, elevation: {self.elevation})"
    
    def __str__(self):
        return str(self.__dict__)