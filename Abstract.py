from abc import ABC, abstractmethod

class hiddenClass(ABC):
    
    def print(self, x):
        print("Passed value:", x)
        
    @abstractmethod
    def task(self): 
        print("We are inside Absclass task")
        
class testClass(hiddenClass):
    
    def task(self):
        print("We are inside test_class task")
        

ob1 = testClass()
ob1.task()
ob1.print(100)

hidden = hiddenClass()
hidden.task()