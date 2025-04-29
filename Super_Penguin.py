class Bird:
    def __init__(self):
        print("Bird is ready")
    def whoisThis(self):
        print("this is a bird")
    def swim(self):
        print("swim faster")
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("this is a penguin")
    def run(self):
        print("run faster")   
ob=Penguin()
ob.whoisThis()
ob.run()
ob.swim()
