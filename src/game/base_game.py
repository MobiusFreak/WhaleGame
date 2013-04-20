import pygame, sys, math
from pygame.locals import *



from utils import Vector

COLLISION_THRESHOLD = 0.01

class BaseGame(object):
    def init(self, App):
        self.app = App

    def draw(self, screen):
        pass

    def update(self, t):
        pass

    def collisions(self, group1, group2):
        colldic = pygame.sprite.groupcollide(group1, group2,False,False,
                                       collided = pygame.sprite.collide_mask)

        for A in colldic:
            for B in colldic[A]:
                if A != B:
                    rad_a, rad_b = self.radius(A,B)
                    wsp_a, wsp_b = self.w_speed(A,B,rad_a,rad_b)
                    self.obj_separation(A,B)

                    A.speed, B.speed = (((A.mass-B.mass)/(A.mass+B.mass)) * A.speed + ((2*B.mass)/(A.mass+B.mass)) * B.speed) , (((B.mass-A.mass)/(A.mass+B.mass)) * A.speed + ((2*A.mass)/(A.mass+B.mass)) * A.speed) 
                    A.angular_speed, B.angular_speed = -B.angular_speed + wsp_b, -A.angular_speed + wsp_a

                if group1 == group2:
                    colldic[B].remove(A)

    def exit(self):
        pass

    def obj_separation(self,A,B):
        dif2 = B.pos - A.pos
        dif2 *= COLLISION_THRESHOLD
        while pygame.sprite.collide_mask(A,B) != None:
            A.pos -= dif2
            A.update_rect()
            B.pos += dif2
            B.update_rect()

    def radius(self, A,B):
        cent_a = Vector(A.mask.centroid())
        cent_b = Vector(B.mask.centroid())
        
        dif =  cent_b - cent_a

        mask = A.mask.overlap_mask(B.mask, (0,0))
        cent_overlap = Vector(mask.centroid())
        
        proycent_overlap = (cent_overlap - cent_a).project(dif) + cent_a
        
        rad_a = (proycent_overlap - cent_a).module
        rad_b = dif.module - rad_a

        if rad_a < 1:
            rad_a = 1
        if rad_b < 1:
            rad_b = 1

        return [rad_a,rad_b]

    def w_speed(self,A,B,rad_a,rad_b):
        cent_a = Vector(A.mask.centroid())
        cent_b = Vector(B.mask.centroid())
        
        dif =  cent_b - cent_a

        orientation_a = dif.orientation(A.speed)
        orientation_b = dif.orientation(B.speed) 
        
        proy_a = (A.speed.project(dif.orthogonal(True)))
        proy_b = (B.speed.project(dif.orthogonal(True)))
            
        if orientation_b > 0:
            w_a = math.degrees(proy_a.module/rad_a)
        else:
            w_a = math.degrees(proy_a.module/rad_a * (-1))
            
        if orientation_a > 0:
            w_b = math.degrees(proy_b.module/rad_b * (-1))
        else:
            w_b = math.degrees(proy_b.module/rad_b)

        return [w_a,w_b]
