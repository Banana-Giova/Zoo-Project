from unittest import TestCase
import unittest
from src.zoo import Zoo, Fence, Animal, ZooKeeper

class TestZoo(TestCase):

    def setUp(self) -> None:
        pass
    
    def test_the_vilgax(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        result:int = len(fence_test.animals)
        message:str = f"Error, the function didn't add the animal to the fence."

        if result != 1:
            while True:
                print("V I L G A X")

        self.assertEqual(result, 1, message)

    def test_gar(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        zoo_keeper_test.remove_animal(animal_test, fence_test)
        message:str = f"Error, the function didn't remove the animal from the fence."
        result:int = len(fence_test.animals)

        self.assertEqual(result, 0, message)

    def test_eatle(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        zoo_keeper_test.feed(animal_test)
        result:int = round(animal_test.area, 3)
        message:str = f"Error, the function didn't feed the animal correctly {result}."

        self.assertEqual(result, 11.444, message)

    def test_sudato(self):
        zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
        fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
        animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                    height=5.5, width=2.0, 
                                    preferred_habitat="Steppa")
        zoo_keeper_test.add_animal(animal_test, fence_test)
        result = round(zoo_keeper_test.clean(fence_test), 3)
        message:str = f"Error, the function didn't clean the fence correctly."

        self.assertEqual(result, 0.124, message)

    def test_golgoroth(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
            fence_test:Fence = Fence(area=100, temperature=25.0, habitat="Steppa")
            animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                        height=5.5, width=2.0, 
                                        preferred_habitat="Steppa")
            zoo_keeper_test.feed(animal_test)
            result:int = round(animal_test.area, 3)
            message:str = f"Error, the function feed the animal even if the animal wasn't in a fence."

            self.assertEqual(result, 11, message)
        except Exception:
            raise RuntimeError("The code crashed.")
        
    def test_vilgax1(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name="Gianni", surname="Rossi", id="1")
            fence_test:Fence = Fence(area=0, temperature=25.0, habitat="Steppa")
            animal_test:Animal = Animal(name="Pluto", species="Canide", age=5,
                                        height=0, width=0, 
                                        preferred_habitat="Steppa")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            zoo_keeper_test.feed(animal_test)
            result:int = round(animal_test.area, 3)
            message:str = f"Error, the result has to be zero since the test result is evil."

            self.assertEqual(result, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        
    def test_vilgax2(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat="Alfonso")
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            counter:int = animal_test.area
            zoo_keeper_test.feed(animal_test)
            result:int = animal_test.area
            message:str = f"Error, the result has to be zero since the test result is evil."

            self.assertEqual(result, counter, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        
    def test_vilgax3(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat="Alfonso")
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            result:int = round(zoo_keeper_test.clean(fence_test), 3)
            message:str = f"Error, the result has to be zero or None since the test result is evil."
            if result != 0 or result != None:
                counter:bool = False
            else:
                counter:bool = True

            self.assertEqual(counter, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        
    def test_vilgax4(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat=None)
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            result:int = round(zoo_keeper_test.clean(fence_test), 3)
            message:str = f"Error, the result has to be zero since the test result is evil."
            if result != 0 or result != None:
                counter:bool = False
            else:
                counter:bool = True

            self.assertEqual(counter, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
    
    def test_vilgax5(self):
        try:
            zoo_keeper_test:ZooKeeper = ZooKeeper(name=None, surname=None, id=None)
            fence_test:Fence = Fence(area=None, temperature=None, habitat=None)
            animal_test:Animal = Animal(name=None, species=None, age=None,
                                        height=None, width=None, 
                                        preferred_habitat="Alfonso")
            zoo_keeper_test.add_animal(animal_test, fence_test)
            result:int = round(zoo_keeper_test.clean(fence_test), 3)
            message:str = f"Error, the result has to be zero since the test result is evil."
            if result != 0 or result != None:
                counter:bool = False
            else:
                counter:bool = True

            self.assertEqual(counter, 0, message)
        except Exception:
            raise RuntimeError("VILGAX CONQUERED YOUR PC MORTAL, SURREDER OR YOU'LL BE ENDED.")
        

if __name__ == "__main__":
    unittest.main()