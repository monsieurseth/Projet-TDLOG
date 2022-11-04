import unittest
from weapons import LanceMissilesAntiair,LanceMissilesAntisurface,LanceTorpilles
from custom_exceptions import NoAmmunitionError,OutOfRangeError


class TestLanceMissilesAntisurface(unittest.TestCase):
    # good guess of all situations
    AMMUNITION_VALUES = (0,1)
    X,Y,Z_VALUES = 1,1, (-1,0,1)
       
    def test_weapon_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of NoAmmunitionError
        for value in self.AMMUNITION_VALUES:
            weapon = LanceMissilesAntisurface(ammunition=value)
            if value == 0 :
                with self.assertRaises(NoAmmunitionError):
                    weapon.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=0) 
        # testing the raise of OutOfRangeError and that we lose an ammunition each time we fire         
        weapon = LanceMissilesAntisurface()   
        ammunition_initial = weapon.ammunition
        weapon.fire_at (x=self.X, y=self.Y, z=self.Z_VALUES[1]) # z must be  0 because LanceMissilesAntiair explains why we chose the value 0 to test that an ammunition is removed
        self.assertEqual (weapon.ammunition, ammunition_initial-1 )

        for value in self.Z_VALUES:
            if value != 0:
                with self.assertRaises(OutOfRangeError):
                    weapon.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)


class TestLanceMissilesAntiair(unittest.TestCase):
    # good guess of all situations
    AMMUNITION_VALUES = (0,1) 
    X,Y,Z_VALUES = 1,1, (-1,0,1) 
    
    def test_weapon_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of NoAmmunitionError
        for value in self.AMMUNITION_VALUES:
            weapon = LanceMissilesAntiair(ammunition=value)
            if value == 0 :
                with self.assertRaises(NoAmmunitionError):
                    weapon.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=0) 
        # testing the raise of OutOfRangeError and that we lose an ammunition each time we fire
        weapon = LanceMissilesAntiair()  
        ammunition_initial = weapon.ammunition
        weapon.fire_at (x=self.X, y=self.Y, z=self.Z_VALUES[2]) # z must be positive because LanceMissilesAntiair explains why we chose the value 1 to test that an ammunition is removed
        self.assertEqual (weapon.ammunition, ammunition_initial-1 )
            
        for value in self.Z_VALUES:   
            if value <= 0:
                with self.assertRaises(OutOfRangeError):
                    weapon.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)


class TestLanceTorpilles(unittest.TestCase):
    # good guess of all situations
    AMMUNITION_VALUES = (0,1)
    X,Y,Z_VALUES = 1,1, (-1,0,1)
    
    
    def test_weapon_fire_at(self):
        # we set up loops to test all situations
        # testing the raise of NoAmmunitionError
        for value in self.AMMUNITION_VALUES:
            weapon = LanceTorpilles(ammunition=value)
            if value == 0 :
                with self.assertRaises(NoAmmunitionError):
                    weapon.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=-1) 
        # testing the raise of OutOfRangeError  and that we lose an ammunition each time we fire        
        weapon = LanceTorpilles()   
        ammunition_initial = weapon.ammunition
        weapon.fire_at (x=self.X, y=self.Y, z=self.Z_VALUES[1]) # z must be negative because LanceMissilesAntiair explains why we chose the value -1 to test that an ammunition is removed
        self.assertEqual (weapon.ammunition, ammunition_initial-1 )
            
        for value in self.Z_VALUES:
            if value > 0:
                with self.assertRaises(OutOfRangeError):
                    weapon.fire_at(
                        x=self.X,
                        y=self.Y,
                        z=value)




def test_all_weapons():
    # we check here if all the weapons have passed the tests
    test_cases = [TestLanceMissilesAntiair,TestLanceMissilesAntisurface,TestLanceTorpilles]
    loader = unittest.TestLoader()
    test_suite_list = []
    for test_case in test_cases:
        element = loader.loadTestsFromTestCase(test_case)
        test_suite_list.append(element)
        
    test_suite = unittest.TestSuite(test_suite_list)

    runner = unittest.TextTestRunner()
    results = runner.run(test_suite)
   
   
   
   

 
if __name__ == '__main__':
    test_all_weapons()
