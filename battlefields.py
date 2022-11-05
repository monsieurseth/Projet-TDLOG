from typing import Tuple
from vessel import  Vessel, Cruiser
from custom_exceptions import OccupedError,FullBattlefieldError, OutOfRangeError


class Battlefield:
    
    def __init__(self) -> None:
        self.vessels_list = []
        self.grid = np.zeros((100,100,3)) 
    
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
           






