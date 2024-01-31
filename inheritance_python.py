# Inheritance
# Parent class
# class Animal:
#     def make_sound(self):
#         print("Animal Sound")
#
#
# # Child class 1
# class Dog(Animal):
#     def dog_sound(self):
#         print('worf worf')
#
#
# # Child class 2
# class Cat(Dog):
#     def cat_sound(self):
#         print("Meow Meow!")
#
#
# # Child class 3
# class DomesticAnimals(Cat):
#     pass
#
#
# # Instances and method calls
# # Creating an instance of Cat
# cat_instance = Cat()
# cat_instance.make_sound()
# cat_instance.cat_sound()
#
# # Creating an instance of Dog
# dog_instance = Dog()
# dog_instance.make_sound()
# dog_instance.dog_sound()
#
# # Creating an instance of DomesticAnimals
# domestic_instance = DomesticAnimals()
# domestic_instance.make_sound()
# domestic_instance.cat_sound()
# domestic_instance.make_sound()
# domestic_instance.dog_sound()

# Parent class
class Animal:
    def make_sound(self):
        print("Generic Animal Sound")


# Child class 1
class Mammal(Animal):
    def give_birth(self):
        print("Mammals give birth to live young")


# Child class 2
class Dog(Mammal):
    def dog_sound(self):
        print('Woof!')


# Child class 3
class Cat(Mammal):
    def cat_sound(self):
        print("Meow!")


# Grandchild class
class DomesticDog(Dog):
    def domestic_dog_behavior(self):
        print("Loyal and friendly behavior")


# Grandchild class
class DomesticCat(Cat):
    def domestic_cat_behavior(self):
        print("Independent and playful behavior")


# Instances and method calls
# Creating an instance of DomesticDog
domestic_dog = DomesticDog()
domestic_dog.make_sound()
domestic_dog.give_birth()
domestic_dog.dog_sound()
domestic_dog.domestic_dog_behavior()

# Creating an instance of DomesticCat
domestic_cat = DomesticCat()
domestic_cat.make_sound()
domestic_cat.give_birth()
domestic_cat.cat_sound()
domestic_cat.domestic_cat_behavior()
