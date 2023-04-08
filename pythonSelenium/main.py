print("Kodlamaio")
print("    -----    ")

class Human:
    name ="Fatih"
    # build-in 
    # constuructor
    def __init__(self, name):
        self.name=name 
        print("Human Nesnesi Üretildi...")
    
    def __str__(self):
        return f"STR fonsiyonundan dönen değer: {self.name}"

    def talk(self,sentence):
        print( f"{sentence} : {self.name}")
    def walk(self):
        print("human is walking...")
        
human1=Human("Fatih")
print(human1)
human1.talk("Merhaba")
human1.walk()









