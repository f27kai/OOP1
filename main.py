class Animal:

    def __init__(self, name, color, age):
        self.__name = name
        self.__color = color
        self.__age = age

    def getName(self):
        return self.__name

    def getColor(self):
        return self.__color

    def getAge(self):
        return self.__age

    def setName(self, newName):
        self.__name = newName

    def setColor(self, newColor):
        self.__color = newColor

    def setAge(self, newAge):
        self.__age = newAge



    def info(self):
        print(f"name: {self.__name}\n"
              f"color: {self.__color}\n"
              f"age: {self.__age}")


bars = Animal('Reks', 'black', 4)
print(f"Setke cheyin {bars.getName()}")
bars.setName("Barser")
print(f"Setten kiyin {bars.getName()}")
bars.info()



bars1 = Animal("Bars", "yellow", 6)
bars1.info()
