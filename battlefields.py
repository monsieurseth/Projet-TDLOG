from typing import Tuple
from vessel import  Vessel, Cruiser
from custom_exceptions import OccupedError,FullBattlefieldError, OutOfRangeError


class Battlefield:
    
    def __init__(self) -> None:
        self.vessels_list = []
    
    def add_vessel(self, vessel: Vessel) -> None:
        if not self.is_available(vessel.coordinates):
            raise OccupedError(f'The coordinate {vessel.coordinates} is occuped')
        elif self.sum_max_hits() > 22:
            raise FullBattlefieldError('No more space')
        else :
            self.vessels_list.append(vessel)
    
    def is_target_touch(self, coordinates : Tuple[int,int,int]) -> bool:
        return self.is_available(coordinates)
        pass
    
    
    def is_available(self,coordinates : Tuple[int,int,int]):
        for vessel in self.vessels_list:
            if vessel.get_coordinates()==coordinates:
                return False
        return True

    
    def sum_max_hits(self) -> int:
        total = 0
        for vessel in self.vessels_list:
            total = total + vessel.max_hits
        return total
           

champ_de_bataille = Battlefield ()
vaisseau1 = Cruiser((0,0,0))
vaisseau2 = Cruiser ((0,1,0))
vaisseau3 = Cruiser((0,0,0))
champ_de_bataille.add_vessel(vaisseau1)
champ_de_bataille.add_vessel(vaisseau2)
#champ_de_bataille.add_vessel(vaisseau3)
print (champ_de_bataille.vessels_list)




