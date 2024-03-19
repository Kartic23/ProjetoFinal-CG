import OpenGL.GL as GL
from core_ext.mesh import Mesh


class Renderer:
    def __init__(self, clear_color=[0, 0, 0]):
        GL.glEnable(GL.GL_DEPTH_TEST)
        # required for antialiasing
        GL.glEnable(GL.GL_MULTISAMPLE)
        GL.glClearColor(clear_color[0], clear_color[1], clear_color[2], 1)

        # Enable lighting
        GL.glEnable(GL.GL_LIGHTING)
        GL.glEnable(GL.GL_LIGHT0)

        # Set the ambient light color to a dark tone
        ambient_color = [0.1, 0.1, 0.1, 1.0]
        GL.glLightModelfv(GL.GL_LIGHT_MODEL_AMBIENT, ambient_color)

        # Initialize the gray filter program
        self.gray_filter_program = self.create_gray_filter_program()

    def create_gray_filter_program(self):
        # Create a simple shader program for the gray filter
        vertex_shader = """
        #version 330
        in vec3 position;

        void main() {
            gl_Position = vec4(position, 1.0);
        }
        """

        fragment_shader = """
            #version 330
            uniform vec4 filterColor;
            out vec4 fragColor;

            void main() {
                fragColor = vec4(filterColor.rgb, filterColor.a);  // Set the color based on the filterColor uniform
            }
        """


        program_ref = GL.glCreateProgram()
        vertex_shader_ref = GL.glCreateShader(GL.GL_VERTEX_SHADER)
        fragment_shader_ref = GL.glCreateShader(GL.GL_FRAGMENT_SHADER)

        GL.glShaderSource(vertex_shader_ref, vertex_shader)
        GL.glCompileShader(vertex_shader_ref)
        GL.glShaderSource(fragment_shader_ref, fragment_shader)
        GL.glCompileShader(fragment_shader_ref)

        GL.glAttachShader(program_ref, vertex_shader_ref)
        GL.glAttachShader(program_ref, fragment_shader_ref)
        GL.glLinkProgram(program_ref)

        GL.glDeleteShader(vertex_shader_ref)
        GL.glDeleteShader(fragment_shader_ref)

        return program_ref

    def render(self, scene, camera):
        # Clear color and depth buffers
        GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
        # blending
        GL.glEnable(GL.GL_BLEND)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

        # Render the scene objects
        self.render_scene(scene, camera)

        # Render the gray filter on top of the scene
        self.render_gray_filter()

    def render_scene(self, scene, camera):
        # Update camera view (calculate inverse)
        camera.update_view_matrix()
        # Extract list of all Mesh objects in scene
        descendant_list = scene.descendant_list
        mesh_filter = lambda x: isinstance(x, Mesh)
        mesh_list = list(filter(mesh_filter, descendant_list))

        for mesh in mesh_list:
            # If this object is not visible, continue to next object in list
            if not mesh.visible:
                continue
            GL.glUseProgram(mesh.material.program_ref)

            if mesh._texture != "":
                GL.glBindTexture(GL.GL_TEXTURE_2D, mesh._texture.texture_ref[mesh._value])

            # Bind VAO
            GL.glBindVertexArray(mesh.vao_ref)
            # Update uniform values stored outside of material
            mesh.material.uniform_dict["modelMatrix"].data = mesh.global_matrix
            mesh.material.uniform_dict["viewMatrix"].data = camera.view_matrix
            mesh.material.uniform_dict["projectionMatrix"].data = camera.projection_matrix
            # Update uniforms stored in material
            for uniform_object in mesh.material.uniform_dict.values():
                uniform_object.upload_data()
            # Update render settings
            mesh.material.update_render_settings()
            GL.glDrawArrays(mesh.material.setting_dict["drawStyle"], 0, mesh.geometry.vertex_count)

    def render_gray_filter(self):
        # Use the gray filter program
        GL.glUseProgram(self.gray_filter_program)

        # Render a fullscreen quad
        GL.glBegin(GL.GL_QUADS)
        GL.glVertex2f(-1.0, -1.0)
        GL.glVertex2f(1.0, -1.0)
        GL.glVertex2f(1.0, 1.0)
        GL.glVertex2f(-1.0, 1.0)
        GL.glEnd()

    
    def set_light(self, color):
        # Use the gray filter program
        GL.glUseProgram(self.gray_filter_program)
        # Get the uniform location for the filterColor variable
        filter_color_location = GL.glGetUniformLocation(self.gray_filter_program, "filterColor")
        # Set the uniform value
        GL.glUniform4f(filter_color_location, color[0], color[1], color[2], color[3])
