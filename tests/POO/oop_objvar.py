class Robot:
    population = 0

    def __init__(self,name):
        self.name = name
        Robot.population +=1
        print("initializing {}".format(self.name))

    def die(self):
        print("I'm dying")
        Robot.population -=1

        if Robot.population == 0:
            print("All robots dead")
        else:    
            print("There is {} robots left".format(Robot.population))

    def sayHi(self):
        print("Hi there my name is {}".format(self.name))

    @classmethod
    def howMany(cls):
        print("We have {} Robots alive".format(cls.population))
