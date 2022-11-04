import unittest
from custom_exceptions import OutOfRangeError,DestroyedError
from vessel import Cruiser, Submarine, Fregate, Destroyer, Aircraft


class TestCruiser(unittest.TestCase):
    # good guess of all situations
    TARGET_COORDINATES = ((0,0,0),(0,0,100))
    MAX_HITS = (0,1) 
    X,Y,Z_VALUES = 1,1,(-1,0,1)
    
    def test_go_to(self):
        # we set up loops to test all situations
        # testing the raise of OutOfRangeError 
        vessel = Cruiser((0,0,0))
        for value in self.Z_VALUES:
            if value != 0 :
                with self.assertRaises(OutOfRangeError):
                    vessel.go_to(
                        x=self.X,
                        y=self.Y,
                        z=value) 
                    
                
    def test_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of DestroyedError
        vessel = Cruiser((0,0,0)) 
        for value in  self.MAX_HITS:
            vessel.max_hits = value
            if value == 0 :
                with self.assertRaises(DestroyedError):
                    vessel.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)

        # testing the raise of OutOfRangeError
        vessel = Cruiser((0,0,0))
        for target_coordinate in self.TARGET_COORDINATES:
            if vessel.get_target_distance(target_coordinate) > vessel.weapon.range :
                with self.assertRaises(OutOfRangeError):
                    vessel.fire_at(x=target_coordinate[0],
                    y=target_coordinate[1],
                    z=target_coordinate[2]) 
                    


class TestFregate(unittest.TestCase):
    # good guess of all situations
    TARGET_COORDINATES = ((0,0,0),(0,0,100))
    MAX_HITS = (0,1) 
    X,Y,Z_VALUES = 1,1,(-1,0,1)
    
    def test_go_to(self):
        # we set up loops to test all situations
        # testing the raise of OutOfRangeError 
        vessel = Fregate((0,0,0))
        for value in self.Z_VALUES:
            if value != 0 :
                with self.assertRaises(OutOfRangeError):
                    vessel.go_to(
                        x=self.X,
                        y=self.Y,
                        z=value) 
                    
                
    def test_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of DestroyedError
        vessel = Fregate((0,0,0)) 
        for value in  self.MAX_HITS:
            vessel.max_hits = value
            if value == 0 :
                with self.assertRaises(DestroyedError):
                    vessel.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)

        # testing the raise of OutOfRangeError
        vessel = Fregate((0,0,0))
        for target_coordinate in self.TARGET_COORDINATES:
            if vessel.get_target_distance(target_coordinate) > vessel.weapon.range :
                with self.assertRaises(OutOfRangeError):
                    vessel.fire_at(x=target_coordinate[0],
                    y=target_coordinate[1],
                    z=target_coordinate[2]) 
                    
        

class TestSubmarine(unittest.TestCase):
    # good guess of all situations
    TARGET_COORDINATES = ((0,0,0),(0,0,100))
    MAX_HITS = (0,1) 
    X,Y,Z_VALUES = 1,1,(-1,0,1)
    
    def test_go_to(self):
        # we set up loops to test all situations
        # testing the raise of OutOfRangeError 
        vessel = Submarine((0,0,0))
        for value in self.Z_VALUES:
            if ((value != 0 ) or (value != -1)):
                with self.assertRaises(OutOfRangeError):
                    vessel.go_to(
                        x=self.X,
                        y=self.Y,
                        z=value) 
                    
                
    def test_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of DestroyedError
        vessel = Submarine((0,0,0)) 
        for value in  self.MAX_HITS:
            vessel.max_hits = value
            if value == 0 :
                with self.assertRaises(DestroyedError):
                    vessel.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)

        # testing the raise of OutOfRangeError
        vessel = Submarine((0,0,0))
        for target_coordinate in self.TARGET_COORDINATES:
            if vessel.get_target_distance(target_coordinate) > vessel.weapon.range :
                with self.assertRaises(OutOfRangeError):
                    vessel.fire_at(x=target_coordinate[0],
                    y=target_coordinate[1],
                    z=target_coordinate[2]) 
                    
                


class TestDestroyer(unittest.TestCase):
    # good guess of all situations
    TARGET_COORDINATES = ((0,0,0),(0,0,100))
    MAX_HITS = (0,1) 
    X,Y,Z_VALUES = 1,1,(-1,0,1)
    
    def test_go_to(self):
        # we set up loops to test all situations
        # testing the raise of OutOfRangeError 
        vessel = Destroyer((0,0,0))
        for value in self.Z_VALUES:
            if value != 0 :
                with self.assertRaises(OutOfRangeError):
                    vessel.go_to(
                        x=self.X,
                        y=self.Y,
                        z=value) 
                    
                
    def test_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of DestroyedError
        vessel = Destroyer((0,0,0)) 
        for value in  self.MAX_HITS:
            vessel.max_hits = value
            if value == 0 :
                with self.assertRaises(DestroyedError):
                    vessel.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)

        # testing the raise of OutOfRangeError
        vessel = Destroyer((0,0,0))
        for target_coordinate in self.TARGET_COORDINATES:
            if vessel.get_target_distance(target_coordinate) > vessel.weapon.range :
                with self.assertRaises(OutOfRangeError):
                    vessel.fire_at(x=target_coordinate[0],
                    y=target_coordinate[1],
                    z=target_coordinate[2]) 

class TestAircraft(unittest.TestCase):
    # good guess of all situations
    TARGET_COORDINATES = ((0,0,0),(0,0,100))
    MAX_HITS = (0,1) 
    X,Y,Z_VALUES = 1,1,(-1,0,1)
    
    def test_go_to(self):
        # we set up loops to test all situations
        # testing the raise of OutOfRangeError 
        vessel = Aircraft((0,0,0))
        for value in self.Z_VALUES:
            if value != 1 :
                with self.assertRaises(OutOfRangeError):
                    vessel.go_to(
                        x=self.X,
                        y=self.Y,
                        z=value) 
                    
                
    def test_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of DestroyedError
        vessel = Aircraft((0,0,0)) 
        for value in  self.MAX_HITS:
            vessel.max_hits = value
            if value == 0 :
                with self.assertRaises(DestroyedError):
                    vessel.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)

        # testing the raise of OutOfRangeError
        vessel = Aircraft((0,0,0))
        for target_coordinate in self.TARGET_COORDINATES:
            if vessel.get_target_distance(target_coordinate) > vessel.weapon.range :
                with self.assertRaises(OutOfRangeError):
                    vessel.fire_at(x=target_coordinate[0],
                    y=target_coordinate[1],
                    z=target_coordinate[2]) 
                    


def test_all_vessels():
    # we check here if all the weapons have passed the tests
    test_cases = [TestCruiser,TestSubmarine,TestFregate,TestDestroyer,TestAircraft]
    loader = unittest.TestLoader()
    test_suite_list = []
    for test_case in test_cases:
        element = loader.loadTestsFromTestCase(test_case)
        test_suite_list.append(element)
        
    test_suite = unittest.TestSuite(test_suite_list)

    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
   
   
   
   

 
if __name__ == '__main__':
    test_all_vessels()



