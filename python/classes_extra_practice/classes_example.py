class Pet: #Define a class
     #  pass    #We havent defined any attributes or methods y
    def __init__ (self)
    self.name = "Cujo"
    self.fullness = 50
    self.happiness = 20
    cujo = Pet()    #New instance of the Pet class
    print(cujo.name)
    #"Cujo"
    benji = Pet()
    print(benji.name)
    #"Cujo"----If you make another instance of Pet, it has all the same attribute values as the other one.

#We need a way to configure each instance with its own attribute values. 
#We can achieve this by defining additional parameters for  __init__  and using those values for the instance's attributes:

class Pet:
    def __init__(self,name,fullness,happiness):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
#When we create new Pet instances, we pass in the values for the attributes:
        cujo = ("Cujo, 50,20")
        print(cujo.name)
        #"Cujo"

        benji = Pet("Benji", 50, 100)
        print(benji.name)
        #"Benji"

#As with regular functions, we can define default argument values:

class Pet:
    def __init__(self, name, fullness=50, happiness=50):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness

#After this modification, we only need to provide a name for each Pet instance:

        cujo = Pet("Cujo")
        print(cujo.name)
        #"Cujo"

        benji = Pet("Benji")
        print(benji.name)
        #"Benji"

#We now have a class that we can use to create instances with their own attribute values.
#We will now define custom methods that make use of those attribute values.

#We can add the methods eat_food() and get_love() for the Pet class.
#Each modifies the instance's attributes accordingly:

        def eat_food(self:
            self.fullness += 30
            
        def get_love(self):
            self.happiness += 30
#The first parameter is self, which is how the body of the method access the instance.

        cujo = Pet("Cujo")
        cujo.eat_food()
        print(cujo.fullness)
        #80
        print(cujo.happiness)
        #50

        benji = Pet("Benji")
        benji.get_love()
        print(cujo.fullness)
        #50
        print(benji.happiness)
        #80

#Each instance has its own eat_food() and get_love() methods. Calling cujo.eat_food() only affects the value of cujo.fullness.
#Likewise, calling benji.get_love only affects the value of benji.happiness.

#Encapsulation= classes provide a way to bundle state(attributes) and behavior(methods).
    #good practice is deciding the minimum amount of info an object needs to store in its state in order to do its work via its behaviors.

#Implementing be_alive() so that it decrements a certain amount of fullness and happiness:

        def be_alive(self):
            self.fullness -= 5
            self.happiness -= 5

#Modifying be_alive() so that the amounts are parameterized:

        def be_alive(self, hunger, mopiness):
            self.fullness -= hunger
            self.happiness -= mopiness

# This moves those to the constructor, but are not configurable:

     Class Pet:
        def __init__(self,name, fullness =50, happiness=50):
            self.name = name
            self.fullness = fullness
            self.happiness = happiness
            self.hunger = 5
            self.mopiness = 5

        def eat_food(self):
            self.fullness += 30

        def get_love(self):
            self.happiness += 30

        def be_alive(self):
            self.fullness -= self.hunger
            self.happiness -= self.mopiness         

# And this makes them configurable:
    

     Class Pet:
        def __init__(self,name, fullness =50, happiness=50, hunger=5, mopiness=5):
            self.name = name
            self.fullness = fullness
            self.happiness = happiness
            self.hunger = hunger
            self.mopiness = mopiness

        def eat_food(self):
            self.fullness += 30

        def get_love(self):
            self.happiness += 30

        def be_alive(self):
            self.fullness -= self.hunger
            self.happiness -= self.mopiness    

    benji = Pet("Benji", 50, 20, 20, 1)
    lassie Pet("Lassie", 50, 20, 20, 1)
    clifford = Pet("Old Yeller", 50, 20, 20,1)



