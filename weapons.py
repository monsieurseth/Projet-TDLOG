from custom_exceptions import NoAmmunitionError,OutOfRangeError


class Weapon:
    def __init__(self, ammunition:int,range:int) -> None:
        self.ammunition = ammunition
        self.range = range
        
    def fire_at(self, x:int, y:int, z:int):
        if self.ammunition == 0:
            raise NoAmmunitionError('We are out of ammunition')
       
    

class LanceMissilesAntisurface(Weapon):
    def __init__(self, ammunition : int = 40, range: int = 30) -> None:
        super().__init__(ammunition, range)
        
    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x, y, z)
        self.ammunition -=1
        if z != 0:
            raise OutOfRangeError('Antisurface Missiles only fire at z=0')
        
        

class LanceMissilesAntiair(Weapon):
    def __init__(self, ammunition : int = 50, range: int = 40) -> None:
        super().__init__(ammunition, range)
        
    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x, y, z)

        self.ammunition -=1
        if z <= 0:
            raise OutOfRangeError('Antiair Missiles only fire at z>0')
        
            
        

class   LanceTorpilles(Weapon):
    def __init__(self, ammunition : int = 15, range: int = 20) -> None:
        super().__init__(ammunition, range)
        
    def fire_at(self, x: int, y: int, z: int):
        super().fire_at(x, y, z)

        self.ammunition -=1
        if z > 0:
            raise OutOfRangeError('Torpilles only fire at z≤0')
        
            

   
        

        
