class Robot:

    # private attribute counter
    __counter = 0

    def __init__(self,name):
        type(self).__counter += 1
        self.name = name
        
    def sayHi(self):
        print("Hi")
    #def __str__(self):
        #return("I'm instance of robot class")
    # class method to access the private attribute via class name or via instance
    @staticmethod
    def RobotInstances():
        return cls.__counter

if __name__ == "__main__":
    """print(Robot.RobotInstances())
    x = Robot()
    x.sayHi()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())"""
    x = Robot("test")
    #print(x)
    y = repr(x)
    print(x.name)
    print(y.name)
    
