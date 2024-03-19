"""Textures examples"""

import numpy as np
import math
import pathlib
import sys
import pygame
import os
import OpenGL.GL as GL



from pygame.locals import *

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from core_ext.texture import Texture
from geometry.model import Model
from geometry.rectangle import RectangleGeometry
from material.texture import TextureMaterial

from core.base import Base
from core_ext.camera import Camera
from core_ext.mesh import Mesh
from core_ext.renderer import Renderer
from core_ext.scene import Scene
from extras.axes import AxesHelper
from extras.grid import GridHelper
from extras.movement_rig import MovementRig




from material.surface import SurfaceMaterial
from geometry.colher import Colher


class Example(Base):
    """ Render a textured square """
    def initialize(self):
        print("Initializing program...")
        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera(aspect_ratio=800/600)
        self.rig = MovementRig()
        self.rig.add(self.camera)
        self.rig.set_position([3.5, 2.5, 5])
        self.scene.add(self.rig)
        axes = AxesHelper(axis_length=0)
        self.scene.add(axes)
        self.jon=self.camera.global_position
        



        geometry_terra = Model('terra_debaixo_do_chao.obj')
        terra_texture = Texture(file_name="images/Earth.jpg",value=1)
        terra_material = TextureMaterial(texture=terra_texture)
        self.mesh_terra = Mesh(geometry_terra, terra_material,terra_texture,value=1)
        self.scene.add(self.mesh_terra)

        geometry_relva = Model('relva_fora_de_casa.obj')
        relva_texture = Texture(file_name="images/Grassl.jpg",value=2)
        relva_material = TextureMaterial(texture=relva_texture)
        self.mesh_relva = Mesh(geometry_relva, relva_material,relva_texture,value=2)
        self.scene.add(self.mesh_relva)

        geometry_troncos = Model('troncos_arvores.obj')
        troncos_texture = Texture(file_name="images/bark.jpg",value=3)
        troncos_material = TextureMaterial(texture=troncos_texture)
        self.mesh_troncos = Mesh(geometry_troncos, troncos_material,troncos_texture,value=3)
        self.scene.add(self.mesh_troncos)

        geometry_fundo_casa = Model('fundo_casa.obj')
        fundo_casa_texture = Texture(file_name="images/lead.jpg",value=4)
        fundo_casa_material = TextureMaterial(texture=fundo_casa_texture)
        self.mesh_fundo_casa = Mesh(geometry_fundo_casa, fundo_casa_material,fundo_casa_texture,value=4)
        self.scene.add(self.mesh_fundo_casa)

        geometry_chamine = Model('chamine.obj')
        chamine_texture = Texture(file_name="images/brick.jpg",value=5)
        chamine_material = TextureMaterial(texture=chamine_texture)
        self.mesh_chamine = Mesh(geometry_chamine, chamine_material,chamine_texture,value=5)
        self.scene.add(self.mesh_chamine)

        geometry_vejetacao = Model('vejetacao.obj')
        vejetacao_texture = Texture(file_name="images/leaf.jpg",value=6)
        vejetacao_material = TextureMaterial(texture=vejetacao_texture)
        self.mesh_vejetacao = Mesh(geometry_vejetacao, vejetacao_material,vejetacao_texture,value=6)
        self.scene.add(self.mesh_vejetacao)

        geometry_telhado_casa = Model('telhado_casa.obj')
        telhado_casa_texture = Texture(file_name="images/Roof.jpg",value=7)
        telhado_casa_material = TextureMaterial(texture=telhado_casa_texture)
        self.mesh_telhado_casa = Mesh(geometry_telhado_casa, telhado_casa_material,telhado_casa_texture,value=7)
        self.scene.add(self.mesh_telhado_casa)

        geometry_parede_fora = Model('parede_dentro.obj')
        parede_fora_texture = Texture(file_name="images/Wood_walnut.jpg",value=9)
        parede_fora_material = TextureMaterial(texture=parede_fora_texture)
        self.mesh_parede_fora = Mesh(geometry_parede_fora, parede_fora_material,parede_fora_texture,value=9)
        self.scene.add(self.mesh_parede_fora)

        geometry_escadas_rodape = Model('escadas_rodape.obj')
        escadas_rodape_texture = Texture(file_name="images/Wood_walnut.jpg",value=10)
        escadas_rodape_material = TextureMaterial(texture=escadas_rodape_texture)
        self.mesh_escadas_rodape = Mesh(geometry_escadas_rodape, escadas_rodape_material,escadas_rodape_texture,value=10)
        self.scene.add(self.mesh_escadas_rodape)

        geometry_janelas = Model('janelas.obj')
        janelas_texture = Texture(file_name="images/handle.jpg",value=10)
        janelas_material = TextureMaterial(texture=janelas_texture)
        self.mesh_janelas = Mesh(geometry_janelas, janelas_material,janelas_texture,value=10)
        self.scene.add(self.mesh_janelas)

        geometry_floor = Model('floor.obj')
        floor_texture = Texture(file_name="images/rooling_pin.jpg",value=10)
        floor_material = TextureMaterial(texture=floor_texture)
        self.mesh_floor = Mesh(geometry_floor, floor_material,floor_texture,value=10)
        self.scene.add(self.mesh_floor)

        geometry_celing = Model('celing.obj')
        celing_texture = Texture(file_name="images/Wood_walnut.jpg",value=10)
        celing_material = TextureMaterial(texture=celing_texture)
        self.mesh_celing = Mesh(geometry_celing, celing_material,celing_texture,value=10)
        self.scene.add(self.mesh_celing)

        geometry_table_chairs_outside = Model('table_chairs_outside.obj')
        table_chairs_outside_texture = Texture(file_name="images/handle.jpg",value=10)
        table_chairs_outside_material = TextureMaterial(texture=table_chairs_outside_texture)
        self.mesh_table_chairs_outside = Mesh(geometry_table_chairs_outside, table_chairs_outside_material,table_chairs_outside_texture,value=10)
        self.scene.add(self.mesh_table_chairs_outside)

        geometry_telhado_interior = Model('telhado_interior.obj')
        telhado_interior_texture = Texture(file_name="images/Wood_walnut.jpg",value=10)
        telhado_interior_material = TextureMaterial(texture=telhado_interior_texture)
        self.mesh_telhado_interior = Mesh(geometry_telhado_interior, telhado_interior_material,telhado_interior_texture,value=10)
        self.scene.add(self.mesh_telhado_interior)

        geometry_front_door = Model('front_door.obj')
        front_door_texture = Texture(file_name="images/handle.jpg",value=10)
        front_door_material = TextureMaterial(texture=front_door_texture)
        self.mesh_front_door = Mesh(geometry_front_door, front_door_material,front_door_texture,value=10)
        self.scene.add(self.mesh_front_door)

        geometry_cama = Model('cama.obj')
        cama_texture = Texture(file_name="images/Wood_grain.jpg",value=10)
        cama_material = TextureMaterial(texture=cama_texture)
        self.mesh_cama = Mesh(geometry_cama, cama_material,cama_texture,value=10)
        self.scene.add(self.mesh_cama)

        geometry_cabeceira = Model('cabeceira.obj')
        cabeceira_texture = Texture(file_name="images/Wood_grain.jpg",value=10)
        cabeceira_material = TextureMaterial(texture=cabeceira_texture)
        self.mesh_cabeceira = Mesh(geometry_cabeceira, cabeceira_material,cabeceira_texture,value=10)
        self.scene.add(self.mesh_cabeceira)

        geometry_cabeceira_gavetas = Model('cabeceira_gavetas.obj')
        cabeceira_gavetas_texture = Texture(file_name="images/handle.jpg",value=10)
        cabeceira_gavetas_material = TextureMaterial(texture=cabeceira_gavetas_texture)
        self.mesh_cabeceira_gavetas = Mesh(geometry_cabeceira_gavetas, cabeceira_gavetas_material,cabeceira_gavetas_texture,value=10)
        self.scene.add(self.mesh_cabeceira_gavetas)

        geometry_tv_remote = Model('tv_remote.obj')
        tv_remote_texture = Texture(file_name="images/black.jpg",value=10)
        tv_remote_material = TextureMaterial(texture=tv_remote_texture)
        self.mesh_tv_remote = Mesh(geometry_tv_remote, tv_remote_material,tv_remote_texture,value=10)
        self.scene.add(self.mesh_tv_remote)

        geometry_tv_remote_button = Model('tv_remote_button.obj')
        tv_remote_button_texture = Texture(file_name="images/Marble.jpg",value=10)
        tv_remote_button_material = TextureMaterial(texture=tv_remote_button_texture)
        self.mesh_tv_remote_button = Mesh(geometry_tv_remote_button, tv_remote_button_material,tv_remote_button_texture,value=10)
        self.scene.add(self.mesh_tv_remote_button)

        geometry_porta_cada_de_banho = Model('porta_cada_de_banho.obj')
        porta_cada_de_banho_texture = Texture(file_name="images/Wood_walnut.jpg",value=10)
        porta_cada_de_banho_material = TextureMaterial(texture=porta_cada_de_banho_texture)
        self.mesh_porta_cada_de_banho = Mesh(geometry_porta_cada_de_banho, porta_cada_de_banho_material,porta_cada_de_banho_texture,value=10)
        self.scene.add(self.mesh_porta_cada_de_banho)

        geometry_parte_porta = Model('parte_porta.obj')
        parte_porta_texture = Texture(file_name="images/Wood_walnut.jpg",value=10)
        parte_porta_material = TextureMaterial(texture=parte_porta_texture)
        self.mesh_parte_porta = Mesh(geometry_parte_porta, parte_porta_material,parte_porta_texture,value=10)
        self.scene.add(self.mesh_parte_porta)


        geometry_corrimao_varanda = Model('corrimao_varanda.obj')
        corrimao_varanda_texture = Texture(file_name="images/blade.jpg",value=11)
        corrimao_varanda_material = TextureMaterial(texture=corrimao_varanda_texture)
        self.mesh_corrimao_varanda = Mesh(geometry_corrimao_varanda, corrimao_varanda_material,corrimao_varanda_texture,value=11)
        self.scene.add(self.mesh_corrimao_varanda)

        geometry_interior_casa_de_banho = Model('interior_casa_de_banho.obj')
        interior_casa_de_banho_texture = Texture(file_name="images/lead.jpg",value=12)
        interior_casa_de_banho_material = TextureMaterial(texture=interior_casa_de_banho_texture)
        self.mesh_interior_casa_de_banho = Mesh(geometry_interior_casa_de_banho, interior_casa_de_banho_material,interior_casa_de_banho_texture,value=12)
        self.scene.add(self.mesh_interior_casa_de_banho)

        geometry_TV = Model('TV.obj')
        TV_texture = Texture(file_name="images/black.jpg",value=12)
        TV_material = TextureMaterial(texture=TV_texture)
        self.mesh_TV = Mesh(geometry_TV, TV_material,TV_texture,value=12)
        self.scene.add(self.mesh_TV)

        geometry_lava_loica_complemento_movel_cozinha = Model('lava_loica_complemento_movel_cozinha.obj')
        lava_loica_complemento_movel_cozinha_texture = Texture(file_name="images/lead.jpg",value=12)
        lava_loica_complemento_movel_cozinha_material = TextureMaterial(texture=lava_loica_complemento_movel_cozinha_texture)
        self.mesh_lava_loica_complemento_movel_cozinha = Mesh(geometry_lava_loica_complemento_movel_cozinha, lava_loica_complemento_movel_cozinha_material,lava_loica_complemento_movel_cozinha_texture,value=12)
        self.scene.add(self.mesh_lava_loica_complemento_movel_cozinha)

        geometry_porta_cabinete_cozinha = Model('porta_cabinete_cozinha.obj')
        porta_cabinete_cozinha_texture = Texture(file_name="images/handle.jpg",value=12)
        porta_cabinete_cozinha_material = TextureMaterial(texture=porta_cabinete_cozinha_texture)
        self.mesh_porta_cabinete_cozinha = Mesh(geometry_porta_cabinete_cozinha, porta_cabinete_cozinha_material,porta_cabinete_cozinha_texture,value=12)
        self.scene.add(self.mesh_porta_cabinete_cozinha)

        geometry_mesa_cozinha = Model('mesa_cozinha.obj')
        mesa_cozinha_texture = Texture(file_name="images/handle.jpg",value=12)
        mesa_cozinha_material = TextureMaterial(texture=mesa_cozinha_texture)
        self.mesh_mesa_cozinha = Mesh(geometry_mesa_cozinha, mesa_cozinha_material,mesa_cozinha_texture,value=12)
        self.scene.add(self.mesh_mesa_cozinha)

        geometry_colher = Model('colher.obj')
        colher_texture = Texture(file_name="images/lead.jpg",value=12)
        colher_material = TextureMaterial(texture=colher_texture)
        self.mesh_colher = Mesh(geometry_colher, colher_material,colher_texture,value=12)
        self.scene.add(self.mesh_colher)


        geometry_fork = Model('fork.obj')
        fork_texture = Texture(file_name="images/lead.jpg",value=12)
        fork_material = TextureMaterial(texture=fork_texture)
        self.mesh_fork = Mesh(geometry_fork, fork_material,fork_texture,value=12)
        self.scene.add(self.mesh_fork)

        geometry_faca_blade = Model('faca_blade.obj')
        faca_blade_texture = Texture(file_name="images/lead.jpg",value=12)
        faca_blade_material = TextureMaterial(texture=faca_blade_texture)
        self.mesh_faca_blade = Mesh(geometry_faca_blade, faca_blade_material,faca_blade_texture,value=12)
        self.scene.add(self.mesh_faca_blade)

        geometry_faca_handle = Model('faca_handle.obj')
        faca_handle_texture = Texture(file_name="images/handle.jpg",value=12)
        faca_handle_material = TextureMaterial(texture=faca_handle_texture)
        self.mesh_faca_handle = Mesh(geometry_faca_handle, faca_handle_material,faca_handle_texture,value=12)
        self.scene.add(self.mesh_faca_handle)

        geometry_cilindro = Model('cilindro.obj')
        cilindro_texture = Texture(file_name="images/rooling_pin.jpg",value=12)
        cilindro_material = TextureMaterial(texture=cilindro_texture)
        self.mesh_cilindro = Mesh(geometry_cilindro, cilindro_material,cilindro_texture,value=12)
        self.scene.add(self.mesh_cilindro)

        geometry_telefone = Model('telefone.obj')
        telefone_texture = Texture(file_name="images/red.jpg",value=12)
        telefone_material = TextureMaterial(texture=telefone_texture)
        self.mesh_telefone = Mesh(geometry_telefone, telefone_material,telefone_texture,value=12)
        self.scene.add(self.mesh_telefone)

        geometry_numeros_telefone = Model('numeros_telefone.obj')
        numeros_telefone_texture = Texture(file_name="images/Marble.jpg",value=12)
        numeros_telefone_material = TextureMaterial(texture=numeros_telefone_texture)
        self.mesh_numeros_telefone = Mesh(geometry_numeros_telefone, numeros_telefone_material,numeros_telefone_texture,value=12)
        self.scene.add(self.mesh_numeros_telefone)

        geometry_ecran_telefone = Model('ecran_telefone.obj')
        ecran_telefone_texture = Texture(file_name="images/ecran_telefone.jpg",value=12)
        ecran_telefone_material = TextureMaterial(texture=ecran_telefone_texture)
        self.mesh_ecran_telefone = Mesh(geometry_ecran_telefone, ecran_telefone_material,ecran_telefone_texture,value=12)
        self.scene.add(self.mesh_ecran_telefone)


        geometry_porta_cozinha = Model('porta_cozinha.obj')
        porta_cozinha_texture = Texture(file_name="images/handle.jpg",value=12)
        porta_cozinha_material = TextureMaterial(texture=porta_cozinha_texture)
        self.mesh_porta_cozinha = Mesh(geometry_porta_cozinha, porta_cozinha_material,porta_cozinha_texture,value=12)
        self.scene.add(self.mesh_porta_cozinha)

        geometry_base_lareira = Model('base_lareira.obj')
        base_lareira_texture = Texture(file_name="images/lead.jpg",value=10)
        base_lareira_material = TextureMaterial(texture=base_lareira_texture)
        self.mesh_base_lareira = Mesh(geometry_base_lareira, base_lareira_material,base_lareira_texture,value=10)
        self.scene.add(self.mesh_base_lareira)

        geometry_escada_interior_central = Model('escada_interior_central.obj')
        escada_interior_central_texture = Texture(file_name="images/handle.jpg",value=10)
        escada_interior_central_material = TextureMaterial(texture=escada_interior_central_texture)
        self.mesh_escada_interior_central = Mesh(geometry_escada_interior_central, escada_interior_central_material,escada_interior_central_texture,value=10)
        self.scene.add(self.mesh_escada_interior_central)

        geometry_lareira = Model('lareira.obj')
        lareira_texture = Texture(file_name="images/lead.jpg",value=10)
        lareira_material = TextureMaterial(texture=lareira_texture)
        self.mesh_lareira = Mesh(geometry_lareira, lareira_material,lareira_texture,value=10)
        self.scene.add(self.mesh_lareira)

        geometry_vidro_mesa = Model('vidro_mesa.obj')
        vidro_mesa_texture = Texture(file_name="images/Marble.jpg",value=10)
        vidro_mesa_material = TextureMaterial(texture=vidro_mesa_texture)
        self.mesh_vidro_mesa = Mesh(geometry_vidro_mesa, vidro_mesa_material,vidro_mesa_texture,value=10)
        self.scene.add(self.mesh_vidro_mesa)

        geometry_pes_sofa = Model('pes_sofa.obj')
        pes_sofa_texture = Texture(file_name="images/lead.jpg",value=10)
        pes_sofa_material = TextureMaterial(texture=pes_sofa_texture)
        self.mesh_pes_sofa = Mesh(geometry_pes_sofa, pes_sofa_material,pes_sofa_texture,value=10)
        self.scene.add(self.mesh_pes_sofa)


        geometry_sofa = Model('sofa.obj')
        sofa_texture = Texture(file_name="images/Fabric.jpg",value=10)
        sofa_material = TextureMaterial(texture=sofa_texture)
        self.mesh_sofa = Mesh(geometry_sofa, sofa_material,sofa_texture,value=10)
        self.scene.add(self.mesh_sofa)
        
        geometry_mesa_sala = Model('mesa_sala.obj')
        mesa_sala_texture = Texture(file_name="images/lead.jpg",value=10)
        mesa_sala_material = TextureMaterial(texture=mesa_sala_texture)
        self.mesh_mesa_sala = Mesh(geometry_mesa_sala, mesa_sala_material,mesa_sala_texture,value=10)
        self.scene.add(self.mesh_mesa_sala)

        geometry_monster = Model('monster.obj')
        monster_texture = Texture(file_name="images/corpo.png",value=10)
        monster_material = TextureMaterial(texture=monster_texture)
        self.mesh_monster = Mesh(geometry_monster, monster_material,monster_texture,value=10)
        self.scene.add(self.mesh_monster)

        geometry_monster_2 = Model('monster_2.obj')
        monster_2_texture = Texture(file_name="images/corpo.png",value=15)
        monster_2_material = TextureMaterial(texture=monster_2_texture)
        self.mesh_monster_2 = Mesh(geometry_monster_2, monster_2_material,monster_2_texture,value=15)
        self.scene.add(self.mesh_monster_2)

        geometry_monster_3 = Model('monster_3.obj')
        monster_3_texture = Texture(file_name="images/corpo.png",value=15)
        monster_3_material = TextureMaterial(texture=monster_3_texture)
        self.mesh_monster_3 = Mesh(geometry_monster_3, monster_3_material,monster_3_texture,value=15)
        self.scene.add(self.mesh_monster_3)
        
        geometry_monster_4 = Model('monster_4.obj')
        monster_4_texture = Texture(file_name="images/corpo.png",value=15)
        monster_4_material = TextureMaterial(texture=monster_4_texture)
        self.mesh_monster_4 = Mesh(geometry_monster_4, monster_4_material,monster_4_texture,value=15)
        self.scene.add(self.mesh_monster_4)



        self.contador=-15  #usado como medida de tempo para as animacoes
   

        #som
        pygame.init()
        pygame.font.init()
        pygame.mixer.init()


        #add sounds
        self.breaking_plate = pygame.mixer.Sound(os.path.join('sound/breaking_plate.ogg'))
        self.breaking_plate.set_volume(0.06)

        self.tap_water = pygame.mixer.Sound(os.path.join('sound/tap_water.ogg'))
        self.tap_water.set_volume(0.3)

        self.scream = pygame.mixer.Sound(os.path.join('sound/scream.ogg'))
        self.scream.set_volume(1)

        self.not_again = pygame.mixer.Sound(os.path.join('sound/not_again.ogg'))
        self.not_again.set_volume(1)

        self.demon = pygame.mixer.Sound(os.path.join('sound/demon.ogg'))
        self.demon.set_volume(1)

        self.what = pygame.mixer.Sound(os.path.join('sound/what.ogg'))
        self.what.set_volume(0.5)

        self.horror = pygame.mixer.Sound(os.path.join('sound/horror.ogg'))
        self.horror.set_volume(0.7)

        self.hello = pygame.mixer.Sound(os.path.join('sound/hello.ogg'))
        self.hello.set_volume(0.4)

        self.scream_2 = pygame.mixer.Sound(os.path.join('sound/scream_2.ogg'))
        self.scream_2.set_volume(1.5)

        self.oh_no = pygame.mixer.Sound(os.path.join('sound/oh_no.ogg'))
        self.oh_no.set_volume(1)

        self.scared_breath = pygame.mixer.Sound(os.path.join('sound/scared_breath.ogg'))
        self.scared_breath.set_volume(1)

        self.phone = pygame.mixer.Sound(os.path.join('sound/phone.ogg'))
        self.phone.set_volume(1)

        self.switch = pygame.mixer.Sound(os.path.join('sound/switch.ogg'))
        self.switch.set_volume(1)





    def update(self):


        def render_text(screen, text, font_size, x, y):
            font = pygame.font.Font('extras/font.otf', font_size)
            text_rendered = font.render(text, True, (255, 255, 255))
            text_rect = text_rendered.get_rect(center=(x, y))
            screen.blit(text_rendered, text_rect)   

        self.rig.update(self.input, self.delta_time)

        

        if(self.contador==10):
            self.keep=self.camera.global_position
            self.mesh_monster_2.translate(0, -9999999, 0)
            self.breaking_plate.play()
        if(self.contador==40):
            self.what.play()
            self.horror.play()
        if(self.contador>10 + 20 and self.contador<400 +20):
            self.camera.rotate_y(0.00180235837034216)
        if(self.contador>400 + 20 and self.contador<540 +20):
            self.camera.translate(-0.01, 0, -0.01)
        if(self.contador>540 + 20 and self.contador<630 +20):
            self.camera.rotate_y(-0.00680235837034216)
        if(self.contador>630 + 20 and self.contador<1230 +20):
            self.camera.translate(-0.0001, 0, -0.015)
        if(self.contador>1230 + 20 and self.contador<1440 +20):
            self.camera.rotate_y(0.00680235837034216)
        if(self.contador>1440 + 20 and self.contador<1550 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador>1550 + 20 and self.contador<1570 +20):
            self.camera.rotate_x(-0.00680235837034216)
        if(self.contador>1570 + 20 and self.contador<1730 +20):
            self.camera.translate(0, -0.004, -0.015)
        if(self.contador>1730 + 20 and self.contador<1750 +20):
            self.camera.rotate_x(0.00680235837034216)
        if(self.contador>1750 + 20 and self.contador<1850 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador>1850 + 20 and self.contador<1900 +20):
            self.camera.rotate_y(-0.03880235837034216)
        if(self.contador>1900 + 20 and self.contador<1950 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador>1950 + 20 and self.contador<1970 +20):
            self.camera.rotate_y(-0.03880235837034216)
        if(self.contador>1970 + 20 and self.contador<2020 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador==2119):
            self.switch.play()
            self.renderer.set_light([0.0, 0.0, 0.0, 0.8])
        if(self.contador>2020 + 20 and self.contador<2030 +20):
            self.camera.rotate_y(-0.03880235837034216)
        if(self.contador>2030 + 20 and self.contador<2050 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador>2050 + 20 and self.contador<2070 +20):
            self.camera.rotate_x(-0.00680235837034216)
        if(self.contador>2070 + 20 and self.contador<2480 +20):
            self.camera.translate(0, -0.0045, -0.015)
        if(self.contador>2480 + 20 and self.contador<2500 +20):
            self.camera.rotate_x(0.00680235837034216)
        if(self.contador>2500 + 20 and self.contador<2535 +20):
            self.camera.rotate_y(-0.03880235837034216)
        if(self.contador>2535 + 20 and self.contador<2655 +20):
            self.camera.translate(0, -0.0045, -0.015)
        if(self.contador>2655 + 20 and self.contador<2675 +20):
            self.camera.rotate_y(-0.02880235837034216)
        if(self.contador>2655 + 20 and self.contador<2835 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador>2835 + 20 and self.contador<2875 +20):
            self.camera.rotate_y(0.02880235837034216)
        if(self.contador>2875 + 20 and self.contador<2995 +20):
            self.camera.translate(0, 0, -0.015)
        if(self.contador==2958):
            self.hello.play()
        if(self.contador==2978):
            self.renderer.set_light([0.0, 0.0, 0.0, 0.0])
        if(self.contador>2995 + 20 and self.contador<3002 +20):
            self.camera.rotate_y(0.2880235837034216)
        if(self.contador>3002 + 20 and self.contador<3400 +20):
            self.mesh_faca_blade.translate(0,0,0.045)
            self.mesh_faca_handle.translate(0,0,0.045)
            self.mesh_fork.translate(0,0,0.045)
        if(self.contador==3140):
            self.scream.play()
        if(self.contador==3150 +20):
            self.camera.translate(0, -99999, 0)
            self.mesh_monster.translate(0, -9999999, 0)
        if(self.contador==3190 +20):
            self.renderer.set_light([0.0, 0.0, 0.0, 0.8])
            self.camera.translate(0, 99999, 0)
            self.scared_breath.play()
        if(self.contador>3190 + 20 and self.contador<3350 +20):
            self.camera.translate(0, 0.0015, -0.015)
        if(self.contador>3350 + 20 and self.contador<3370 +20):
            self.camera.rotate_y(-0.02880235837034216)
        if(self.contador>3370 + 20 and self.contador<3500 +20):
            self.camera.rotate_y(0.002880235837034216)
            self.camera.translate(0, 0, -0.020)
        if(self.contador>3500 + 20 and self.contador<3545 +20):
            self.camera.translate(0, 0, -0.020)
            self.camera.rotate_y(-0.002880235837034216)
        if(self.contador>3525 + 20 and self.contador<3620 +20):
            self.camera.rotate_x(-0.00980235837034216)
            self.camera.rotate_y(-0.002880235837034216)
        if(self.contador==3620 +20):
            self.mesh_monster_2.translate(0, 9999999, 0)
            self.phone.play()
            self.renderer.set_light([0.0, 0.0, 0.0, 0.0])
        if(self.contador>3640 + 20 and self.contador<3665 +20):
            self.camera.rotate_x(0.05580235837034216)
        if(self.contador>3665 + 20 and self.contador<3700 +20):
            self.camera.translate(0, 0, 0.015)
        if(self.contador==3700 +20):
            self.camera.translate(0, -99999, 0)  
            self.scared_breath.stop()
            self.renderer.set_light([0.0, 0.0, 0.0, 0.8])
        if(self.contador==3840+100):
            self.camera=Camera(aspect_ratio=800/600)
            self.camera.set_position(self.keep)  
            self.tap_water.play()
        if(self.contador==3940+100):
            self.not_again.play()
        if(self.contador>4000 + 150 and self.contador<4200 + 150):
            self.camera.rotate_y(-0.004180235837034216)
        if(self.contador>4199 + 150 and self.contador<4350 + 150):
            self.camera.translate(-0.001, 0, -0.01)
            self.camera.rotate_y(0.000003180235837034216)
        if(self.contador>4349 + 150 and self.contador<4450 + 150):
            self.camera.translate(-0.01, 0, -0.01)
            self.camera.rotate_y(-0.003180235837034216)
        if(self.contador>4449 + 150 and self.contador<4465 + 150):
            self.camera.translate(-0.01, 0, -0.01)
            self.camera.rotate_y(-0.003180235837034216)
        if(self.contador>4464 + 150 and self.contador<4585 + 150):
            self.camera.rotate_y(-0.002180235837034216)
            self.camera.translate(0, 0, +0.001)
        if(self.contador==4500+100):
            self.oh_no.play()            
        if(self.contador==4590+100):
            self.camera.translate(0, -99999, 0)
            self.scared_breath.play()
        if(self.contador==4620+100):
            self.camera.translate(0, +99999, 0)
            self.renderer.set_light([0.0, 0.0, 0.0, 0.0])
        if(self.contador>4584 + 150 and self.contador<4605 + 150):
            if(self.contador%2):
                self.renderer.set_light([0.0, 0.0, 0.0, 0.0])
            else:
                self.renderer.set_light([0.0, 0.0, 0.0, 0.8])
            self.camera.translate(0, 0, +0.001)
            self.mesh_monster_4.translate(-0.1, 0, 0)
            self.scared_breath.stop()
            self.scream_2.play()
        if(self.contador==4665+100):
            self.scream_2.stop()
            self.camera.translate(0, -99999, 0)
            self.horror.stop()
            self.demon.play()

            # Create a Pygame screen
            pygame.init()
            screen = pygame.display.set_mode((800, 600))
            clock = pygame.time.Clock()

            # Clear the screen
            screen.fill((0, 0, 0))

            # Render the text on the screen
            render_text(screen, "The End", 60, 400, 250)  # Upper text with larger font size
            render_text(screen, "Thanks For Watching", 30, 400, 350)  # Lower text with smaller font size

            # Update the Pygame display
            pygame.display.flip()

            # Wait for a few seconds before exiting
            pygame.time.wait(6000)
            pygame.quit()
            sys.exit()        
                



        self.renderer.render(self.scene, self.camera)



        if(self.rig.start):
            self.contador+=1




        

# Instantiate this class and run the program
Example(screen_size=[800, 600]).run()
