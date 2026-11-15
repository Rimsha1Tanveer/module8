class Parrot:
    
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a ",blu.species)
print("Woo is also a",woo.species)

# access the instance attributes
print(blu.name," is  years old", blu.age)
print(woo.name," is years old",  woo.age)