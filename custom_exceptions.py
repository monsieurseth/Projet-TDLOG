#In this section, we define the different types of error that we will have to use when implementing weapons, vessel and battlefield.
class NoAmmunitionError(Exception):  # The NoAmmunitionError exception inherits from the "Exception" class which groups all python exceptions
    def __init__(self, *args: object) -> None: # The __init__ special method does not return anything 
        if args:
            self.message = args[0]
        else:
            self.message = None 
       
    def __str__(self) -> str:
        if self.message:
            return f'NoAmmunitionError , {self.message}'
        else:
            return 'NoAmmunitionError has been raised'
    # If during the instantiation of NoAmmunitionError, no argument is entered an error message << NoAmmunitionError has been raised >> otherwise the argument is returned.

class OutOfRangeError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None 
            
    def __str__(self) -> str:
        if self.message:
            return f'OutOfRangeError , {self.message}'
        else:
            return 'OutOfRangeError has been raised'


class DestroyedError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None 
            
    def __str__(self) -> str:
        if self.message:
            return f'DestroyedError , {self.message}'
        else:
            return 'DestroyedError has been raised'
    

class OccupedError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None 
            
    def __str__(self) -> str:
        if self.message:
            return f'OccupedError , {self.message}'
        else:
            return 'OccupedError has been raised'
        

class FullBattlefieldError(Exception):
    def __init__(self, *args: object) -> None:
        if args:
            self.message = args[0]
        else:
            self.message = None 
            
    def __str__(self) -> str:
        if self.message:
            return f'FullBattlefieldError , {self.message}'
        else:
            return 'FullBattlefieldError has been raised'
        

