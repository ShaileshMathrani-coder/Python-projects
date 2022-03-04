class animal:
    def __init__(self,name,age,gender,voice):
        self.name=name
        self.age=age
        self.gender=gender
        self.voice=voice
    def speak(self):
        print("Name:",self.name," ","Age:",self.age," ","Gender:",self.gender," ","voice:",self.voice)
#You can add you own frther classes.
class dog(animal):
    def __init__(self,name,age,gender,voice):
        self.name = name
        self.age = age
        self.gender = gender
        self.voice = voice
        self.type="dog"
class cat(animal):
    def __init__(self,name,age,gender,voice):
        self.name = name
        self.age = age
        self.gender = gender
        self.voice = voice
        self.type="cat"
class parrot(animal):
    def __init__(self,name,age,gender,voice):
        self.name = name
        self.age = age
        self.gender = gender
        self.voice = voice
        self.type="bird"


obj1=dog("tim",3,"Male","bhow bhow")
obj1.speak()


obj2=cat("rim",5,"feMale","meow meow")
obj2.speak()


obj3=parrot("jim",6,"feMale","No voice")
obj3.speak()




