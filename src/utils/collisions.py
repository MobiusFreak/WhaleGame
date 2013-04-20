import pygame, math
from pygame.locals import *

COLLISION_THRESHOLD = 0.01

# Physics
def simple_physics_collision(A, B):
    obj_separation(A,B)
    A.speed, B.speed = (((A.mass-B.mass)/(A.mass+B.mass)) * A.speed + ((2*B.mass)/(A.mass+B.mass)) * B.speed), (((B.mass-A.mass)/(A.mass+B.mass)) * A.speed + ((2*A.mass)/(A.mass+B.mass)) * A.speed)

    A.angular_speed, B.angular_speed = -B.angular_speed, -A.angular_speed


def advanced_physics_collision(A, B):
    rad_a, rad_b = radius(A,B)
    wsp_a, wsp_b = w_speed(A,B,rad_a,rad_b)
    obj_separation(A,B)

    A.speed, B.speed = (((A.mass-B.mass)/(A.mass+B.mass)) * A.speed + ((2*B.mass)/(A.mass+B.mass)) * B.speed) , (((B.mass-A.mass)/(A.mass+B.mass)) * A.speed + ((2*A.mass)/(A.mass+B.mass)) * A.speed)
    A.angular_speed, B.angular_speed = -B.angular_speed + wsp_b, -A.angular_speed + wsp_a


def obj_separation(A, B):
    dif2 = B.pos - A.pos
    dif2 *= COLLISION_THRESHOLD
    while pygame.sprite.collide_mask(A,B) != None:
        A.pos -= dif2
        A.update_rect()
        B.pos += dif2
        B.update_rect()

def radius(A, B):
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

def w_speed(A,B,rad_a,rad_b):
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


def collisions(group1, group2, kill1 = False, kill2 = False, function = simple_physics_collision):
    colldic = pygame.sprite.groupcollide(group1, group2, kill1, kill2,
                                         collided = pygame.sprite.collide_mask)

    for A in colldic:
        for B in colldic[A]:
            if A != B:
                function(A, B)
            if group1 == group2:
                colldic[B].remove(A)

