

import unittest
from factoriel_funct import factorielle 


class Test_factorielle(unittest.TestCase):
    n=6
    def test_parametre_int(self):
        self.assertIsInstance(self.n,int)
        
    def test_parametre_negatif(self):
        self.assertLess(0,self.n)
   


if __name__ =="__main__":
    unittest.main()
    




























# import unittest 
# from factoriel_funct import Math

# class Test_factoriel(unittest.TestCase):
#     def setUp(self):
#         self.p = Math(4)
#     def test_parametre_vide(self):
#         self.assertIsNotNone(self.p.n,msg="Entrez le paramètre de la fonction")
#     def test_instance(self):
#         self.assertNotIsInstance(self.p.n,str)

# if __name__ =="__main__":
#     unittest.main()
