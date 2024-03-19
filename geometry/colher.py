from geometry.geometry import Geometry
from core_ext.obj_reader_2 import my_obj_reader
import random
import OpenGL.GL as GL

class Colher(Geometry):

    def __init__(self):
        super().__init__()
        color_data = []
        self.position_data = my_obj_reader('spoon.obj')
        colors = [(0.221, 0.221, 0.221)]  
        for vertex in self.position_data:
            color_data.extend(colors[0])
        self.add_attribute("vec3", "vertexPosition", self.position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.count_vertices()