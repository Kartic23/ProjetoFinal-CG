from core_ext.obj_reader import my_obj_reader
from geometry.geometry import Geometry


class Model(Geometry):
    def __init__(self, file):
        super().__init__()
        
        folder_path = "obj/"  # Specify the folder path
        file_path = folder_path + file  # Create the full file path
        
        result = my_obj_reader(file_path)
        position_data = result[0]
        uv_data = result[1]
        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec2", "vertexUV", uv_data)
        self.count_vertices()
