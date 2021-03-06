#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
import random
import glob
from math import sin, cos, radians, pi

window = pyglet.window.Window(1000, 800)
batch = pyglet.graphics.Batch()   # pro optimalizované vyreslování objektů


class SpaceObject(object):

    def __init__(self, img_file, x=None, y=None):

        # nečtu obrázek
        self.image = pyglet.image.load(img_file)
        # střed otáčení dám na střed obrázku
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        # z obrázku vytvořím sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        # pokud není atribut zadán vytvořím ho náhodně
        self._x = x if x is not None else random.randint(0, window.width)
        self._y = y if y is not None else random.randint(0, window.height)
        # musím správně nastavit polohu sprite
        self.x = self._x
        self.y = self._y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new):
        self._x = self.sprite.x = new

    @property
    def y(self):        
        return self._y

    @y.setter
    def y(self, new):
        self._y = self.sprite.y = new

    def tick(self, dt):

        # do promenne dt se uloží doba od posledního tiknutí
        self.x += dt * self.speed * cos(pi / 2 - radians(self.direction))
        self.sprite.x = self.x
        self.y += dt * self.speed * sin(pi / 2 - radians(self.direction))
        self.sprite.y = self.y
        self.sprite.rotation += 0.01 * self.rspeed

class Meteor(SpaceObject):
    
    def __init__(self, x=None, y=None, direction=None,
                 speed=None, rspeed=None):
        y = window.height + 50
        file_list = glob.glob('img/meteor*.png')
        img_file = random.choice(file_list)
        super().__init__(img_file, x,y)
        self.speed = speed if speed is not None else random.randint(50,200) 
        self.rspeed = rspeed if rspeed is not None else random.randint(-40,40)
        self.direction = direction if direction is not None else random.randint(120,240)
 
class SpaceShip(SpaceObject):
    def __init__(self):
        super().__init__('img/ship.png', x=200, y=200)
        
        
    def tick(self):
        pass
       
class Meet():
    meteors = []
    
    def __init__(self, count):
        for i in range(count):
            self.add_meteor()
    
    def add_meteor(self, dt=None):
        self.meteors.append( Meteor() )
        
    def tick(self, dt):
        for meteor in self.meteors:
            meteor.tick(dt)
            if meteor.x < 0 or meteor.y < 0 or meteor.y > window.width:
                meteor.sprite.delete()
                self.meteors.remove(meteor)

#a = SpaceObject('SpaceShooterRedux/PNG/playerShip1_red.png')
#m = Meteor()


@window.event
def on_draw():
    window.clear()
    batch.draw()
    
meet = Meet(15)
ship = SpaceShip()
pyglet.clock.schedule_interval(meet.tick, 1/30)
pyglet.clock.schedule_interval(meet.add_meteor, 1/5)
pyglet.app.run()
