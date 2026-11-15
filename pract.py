from abc import ABC,abstractmethod

class animal(ABC):
    def __init__(self,name,habitat):
     self.name= name
     self.habitat= habitat

    def display(self):
     print("name",self.name,"habitat",self.habitat)

    @abstractmethod
    def speak(self):
      pass

class dog(animal):
    def __init__(self,name,habitat,breed):
        super().__init__(name,habitat)
        self.breed=breed

    def speak(self):
        print(self.name, "and" ,self.breed , "says: woof! wooof!")

class parrot(animal):
    def __init__(self,name,habitat,phrase):
        super().__init__(name,habitat)
        self.phrase=phrase

    def speak(self):
       print(self.name,"says:" ,self.phrase)

class lion(animal):
    def __init__(self,name,habitat,pride):
        super().__init__(name,habitat)
        self.pride =pride

    def speak(self):
        print(self.name,"pride:",self.pride,"says:roarr!")

Dog  =dog("bruno","home","labrador")
Parrot  =parrot("polly","jungle","squawk")
Lion  =lion("simba","savannah","pride rock")

print("=== aniaml sound show ===\n")
for aniaml in [Dog,Parrot,Lion]:
    aniaml.display()
    aniaml.speak()
    print()