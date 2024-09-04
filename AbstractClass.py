from abc import ABC , abstractmethod

#  abstract class
class Animal(ABC):

    # abstract method
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Bark")


class Cat(Animal):
    def speak(self):
        print("Meow")


dog=Dog()
cat=Cat()

dog.speak()
cat.speak()