class phones:
    def __init__(self,brandname,launchyear, price):
        self.brandname=brandname
        self.launchyear=launchyear
        self.price=price
    def speak(self):
        print("BrandName:",self.brandname," ","Year:",self.launchyear," ","price:",self.price)
class Iphone(phones):
    def __init__(self,brandname,launchyear, price):
        self.brandname = brandname
        self.launchyear = launchyear
        self.price = price
        self.type="Phone"
class Samsung(phones):
    def __init__(self,brandname,launchyear, price):
        self.brandname = brandname
        self.launchyear = launchyear
        self.price = price
        self.type="Phone"
class xiaomi(phones):
    def __init__(self,brandname,launchyear, price):
        self.brandname = brandname
        self.launchyear = launchyear
        self.price = price
        self.type="phone"


obj1=Iphone("Apple",1995,100000)
obj1.speak()
class iphone:
    def __init__(self,features1,feature2,feature3):
        self.features1=features1
        self.feature2=feature2
        self.feature3=feature3
p1=iphone("camera","bluetooth","face calling")
print(p1.features1)
print(p1.feature2)
print(p1.feature3)

obj2=Samsung("Android",1996,50000)
obj2.speak()
class samsung:
    def __init__(self,features1,feature2):
        self.features1=features1
        self.feature2=feature2
p2=samsung("camera","bluetooth")
print(p2.features1)
print(p2.feature2)



obj3=xiaomi("android",1997,30000)
obj3.speak()
class xiaomi:
    def __init__(self,features1,feature2):
        self.features1=features1
        self.feature2=feature2
p3=xiaomi("camera","face calling")
print(p3.features1)
print(p3.feature2)





