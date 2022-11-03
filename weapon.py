
class Weapon:
    def __init__(self,ammunitions,range):
        self.ammunitions = ammunitions
        self.range = range 
        # Exception pour verifier les instances des attributs 
        assert isinstance(ammunitions,int), "Veuillez donner un entier"
        assert isinstance(range,int),"Veuilez donner un entier"
    def fire_at(self,x,y,z):
        pass

class Missile_antisurface(Weapon):
    def __init__(self,ammunitions=40,range=30):
        Weapon.__init__(self,ammunitions,range)
    def fire_at(self,x,y,z):
        # Verifier s'il le nombre de munition est 0. 
        if self.ammunitions ==0:
            raise Exception("NoAmmunitionError")
        # Verifier si la z est 0 et dans le cas contraire soustraire ammunitions d'une unité
        if z != 0:
            self.ammunitions =-1
            raise Exception("OutOfRangeError","Nbr_munition:-->",self.ammunitions)
        else:
            si 
            return f"Bien, Munition {self.ammunitions}"
class Missile_anti_air(Weapon):
    def __init__(self,ammunitions=50,range=30):
        Weapon.__init__(self,ammunitions,range)
    def fire_at(self,x,y,z):
        if self.ammunitions ==0:
            raise Exception("NoAmmunitionError")
        # Verifier la condition sur z > 0 et lever une exception dans le cas contraire soustraire ammunitions d'une unité
        if z <=0:
            self.ammunitions -=1
            raise Exception("OutOfRangeError","Nbr_munition:-->",self.ammunitions)
        else:
            return f"Bien, Munition {self.ammunitions}"

class Torpille(Weapon):
    def __init__(self,ammunitions=15,range=20):
        super().__init__(ammunitions,range)
    def fire_at(self,x,y,z):
        if self.ammunitions ==0:
            raise Exception("NoAmmunitionError")
        # Verifier la condition z <=0 et lever une exception sinon  soustraire ammunitions d'une unité
        elif z>0:
            self.ammunitions -=1
            raise Exception("OutOfRangeError","Nbr_munition:-->",self.ammunitions)
        else:
            return f"Bien, Munition {self.ammunitions}"



        
p = Missile_anti_air()
print(p.fire_at(12,23,7))