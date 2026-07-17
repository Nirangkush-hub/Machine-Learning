def en():
    class BankAccount:
        def __init__(self, owner: str, balance: float):
            self.owner = owner
            self.bal = balance 
        def get_balance(self):
            return self.bal

    
        def deposit(self, amount: float):
            if amount > 0:
                self.bal += amount
                print(self.bal)
            else:
                print("Error: Deposit amount must be positive.")

    account = BankAccount("Sunku", 1000)
# print(account.bal)  # ERROR! This will not work because bal(balance) is hidden.

    account.deposit(500)
    print("Final Balance: Rs.",account.get_balance())



def inher():
    # Parent Class
    class Animal:
        def __init__(self, name: str):
            self.name = name

        def eat(self):
            return f"{self.name} is eating."

    # Child Class (Single Inheritance)
    class Dog(Animal):
        def bark(self):
            return f"{self.name} says Woof!"

    # Grandchild Class (Multilevel Inheritance)
    class Puppy(Dog):
        def weep(self):
            return f"{self.name} is whimpering softly."


    barky = Dog("Buddy")
    print(barky.eat())   
    print(barky.bark())  

    small_puppy = Puppy("Pip")
    print(small_puppy.eat())  
    print(small_puppy.weep())    
def poly():
    class Cat:
        def make_sound(self):
            return "Meow!"

    class Cow:
        def make_sound(self):
            return "Moo!"

    
    def play_sound(animal_object):
        print(animal_object.make_sound())

  
    kitty = Cat()
    dairy = Cow()

    play_sound(kitty)  
    play_sound(dairy)  

def abb():
    from abc import ABC, abstractmethod

    # Abstract Base Class (Blueprint)
    class Appliance(ABC):
        @abstractmethod
        def turn_on(self):
            """Every appliance must define how it turns on."""
            pass

    # Concrete Class implementing the blueprint
    class Toaster(Appliance):
        def turn_on(self):
            return "Heating coils glowing red. Toasting started!"

   
    
    my_toaster = Toaster()
    print(my_toaster.turn_on())   # Works perfectly because Toaster fulfilled the blueprint rule

while(True):
    print("\n\nThis program shows the four pillars of Object Oriented Program in Python:")
    print("\n1.Encaptulation\n2.Inheritance\n3.Polymorphism\n4.Abstraction\n5.Exit")
    ch=input("Select an option:")
    if ch=="1":
        print("Encaptulation demonstrated")
        en()
    elif ch=="2":
        print("Inheritance demonstrated")
        inher()
    elif ch=="3":
        print("Polymorphism demonstrated")
        poly()
    elif ch=="4":
        print("Abstractioin demonstrated")
        abb()
    elif ch=="5":
        print("Exitting program")
        break
    else:    
        print("Enter a valid choice.")