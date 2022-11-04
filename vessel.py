import math
from typing import Tuple
from weapons import Weapon, LanceMissilesAntiair, LanceMissilesAntisurface , LanceTorpilles
from custom_exceptions import OutOfRangeError,DestroyedError


class Vessel:
    
    def __init__(self,coordinates : Tuple[int,int,int], max_hits : int , weapon : Weapon) -> None:
        self.coordinates = coordinates
        self.max_hits = max_hits
        self.weapon = weapon
        
    
    def go_to(self,x,y,z) -> None:
        pass

    def fire_at(self, x:int, y:int, z:int) -> None:
        pass
    
    def get_coordinates(self) -> Tuple[int,int,int]:
        return self.coordinates
    
    def get_target_distance(self, target_coordinate : Tuple[int,int,int]) -> float:
        d = 0.0
        d = math.sqrt((target_coordinate[0] - self.coordinates[0])**2 + (target_coordinate[1] - self.coordinates[1])**2 + (target_coordinate[2] - self.coordinates[2])**2)
        return int(d)
    

class Cruiser(Vessel):
    
    def __init__(self, coordinates: Tuple[int,int,int]) -> None:
        super().__init__(coordinates, 
                         max_hits = 6,
                         weapon = LanceMissilesAntiair())
        
    def go_to(self, x, y, z) -> None:
        super().go_to(x, y, z)
        
        if z != 0:
            raise OutOfRangeError('Cruiser only move on z = 0')
        else:
            if self.max_hits == 0:
                raise DestroyedError('The cruiser has been destroyed')
            self.coordinates = (x,y,z)
    
    def fire_at(self, x, y, z) -> None :
        if self.max_hits == 0:
            raise DestroyedError('The cruiser has been destroyed')
        
        elif self.get_target_distance((x, y, z)) > self.weapon.range :
            self.weapon.fire_at(x, y, z)
            raise OutOfRangeError('Missed : Target is out of range')
        else :
            self.weapon.fire_at(x, y, z)
    
    

class Submarine(Vessel):
    
    def __init__(self, coordinates: Tuple[int,int,int]) -> None:
        super().__init__(coordinates, 
                         max_hits = 2,
                         weapon = LanceTorpilles())
        
    def go_to(self, x, y, z) -> None:
        super().go_to(x, y, z)
        
        if ((z != 0) or (z!=-1)):
            if self.max_hits ==0:
                raise DestroyedError('The Submarine has been destroyed')
            raise OutOfRangeError('Submarine only move on z = 0 or z = -1')
        else:
            self.coordinates = (x,y,z)
    
    def fire_at(self, x, y, z) -> None :
        if self.max_hits == 0:
            raise DestroyedError('The Submarine has been destroyed')
        
        elif self.get_target_distance((x, y, z)) > self.weapon.range :
            self.weapon.fire_at(x, y, z)
            raise OutOfRangeError('Missed : Target is out of range')
        else :
            self.weapon.fire_at(x, y, z)
    
   


class Fregate(Vessel):
    
    def __init__(self, coordinates: Tuple[int,int,int]) -> None:
        super().__init__(coordinates, 
                         max_hits = 5 ,
                         weapon = LanceMissilesAntisurface())
        
    def go_to(self, x, y, z) -> None:
        super().go_to(x, y, z)
        
        if z != 0:
            if self.max_hits == 0:
                 raise DestroyedError('The Fregate has been destroyed')
            raise OutOfRangeError('Fregate only move on z = 0 ')
        else:
            self.coordinates = (x,y,z)
    
    def fire_at(self, x, y, z) -> None :
        if self.max_hits == 0:
            raise DestroyedError('The Fregate has been destroyed')
        
        elif self.get_target_distance((x, y, z)) > self.weapon.range :
            self.weapon.fire_at(x, y, z)
            raise OutOfRangeError('Missed : Target is out of range')
        else :
            self.weapon.fire_at(x, y, z)
            


class Destroyer(Vessel):
    
    def __init__(self, coordinates: Tuple[int,int,int]) -> None:
        super().__init__(coordinates, 
                         max_hits = 4 ,
                         weapon = LanceTorpilles())
        
    def go_to(self, x, y, z) -> None:
        super().go_to(x, y, z)
        
        if z != 0:
            if self.max_hits == 0:
                raise DestroyedError('The Destroyer has been destroyed')
            raise OutOfRangeError('Destroyer only move on z = 0 ')
        else:
            self.coordinates = (x,y,z)
    
    def fire_at(self, x, y, z) -> None :
        if self.max_hits == 0:
            raise DestroyedError('The Destroyer has been destroyed')
        
        elif self.get_target_distance((x, y, z)) > self.weapon.range :
            self.weapon.fire_at(x, y, z)
            raise OutOfRangeError('Missed : Target is out of range')
        else :
            self.weapon.fire_at(x, y, z)
            
            

class Aircraft(Vessel):
    
    def __init__(self, coordinates: Tuple[int,int,int]) -> None:
        super().__init__(coordinates, 
                         max_hits = 1 ,
                         weapon = LanceMissilesAntisurface())
        
    def go_to(self, x, y, z) -> None:
        super().go_to(x, y, z)
        
        if z != 1:
            if self.max_hits == 0:
                raise DestroyedError('The Aircraft has been destroyed')
            raise OutOfRangeError('Aircraft only move on z = 0 ')
        else:
            self.coordinates = (x,y,z)
    
    def fire_at(self, x, y, z) -> None :
        if self.max_hits == 0:
            raise DestroyedError('The Aircraft has been destroyed')
        
        elif self.get_target_distance((x, y, z)) > self.weapon.range :
            self.weapon.fire_at(x, y, z)
            raise OutOfRangeError('Missed : Target is out of range')
        else :
            self.weapon.fire_at(x, y, z)