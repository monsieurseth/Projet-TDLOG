
class Weapon:
    def __init__(self,x,y,z, ammunitions,range):
        self.ammunitions = ammunitions
        self.range = range 
        self.x = x 
        self.y = y 
        self.z = z
        assert isinstance(ammunitions,int), "Veuillez donner un entier"
        assert isinstance(range,int),"Veuilez donner un entier"
    def fire_at(self):
        pass

class Missile_antisurface(Weapon):
    def __init__(self,x,y,z,ammunitions=40,range=30):
        Weapon.__init__(self,x,y,z,ammunitions,range)
    def fire_at(self):
        if self.ammunitions ==0:
            raise Exception("NoAmmunitionError")
        if self.z != 0:
            self.ammunitions =-1
            raise Exception("OutOfRangeError","Nbr_munition:-->",self.ammunitions)
class Missile_anti_air(Weapon):
    def __init__(self,x,y,z,ammunitions=50,range=30):
        Weapon.__init__(self,x,y,z,ammunitions,range)
    def fire_at(self):
        if self.ammunitions ==0:
            raise Exception("NoAmmunitionError")
        if self.z <=0:
            self.ammunitions -=1
            raise Exception("OutOfRangeError","Nbr_munition:-->",self.ammunitions)

class Torpille(Weapon):
    def __init__(self,x,y,z,ammunitions=15,range=20):
        Weapon.__init__(self,x,y,z,ammunitions,range)
    def fire_at(self):
        if self.ammunitions ==0:
            raise Exception("NoAmmunitionError")
        if self.z>0:
            self.ammunitions -=1
            raise Exception("OutOfRangeError","Nbr_munition:-->",self.ammunitions)


        
        
p = Torpille(23,12,4)

print(p.ammunitions)
print(p.fire_at())

