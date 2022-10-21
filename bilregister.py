class Car():
    '''
    En klass som håller reda på några egenskaper hos en bil.
    '''
    # Metoden __init__, körs alltid då ett objekt skapas

    def __init__(self, brand, color, mileage):
        # Nedanstående variabler kallas för attribut.
        # Alla objekt av klassen Car har egna värden på dessa.
        self.brand = brand
        self.color = color
        self.mileage = mileage

    def get_brand(self):
        '''
        Skriver ut bilmärket
        '''
        print(self.brand)

    def set_brand(self, new_brand):
        '''
        Parameter: new_brand | sträng
        Uppdaterar bilmärket om det existerar. Om det inte existerar
        så tilldelas aktuellt objekt märket enligt parametern.
        '''
        self.brand = new_brand
    
    def set_color(self, new_color):
        self.color = new_color
    
    def set_mileage(self,new_mileage):
        self.mileage = new_mileage
    
    def get_mileage(self,):
        return self.mileage


# ----------Huvudprogram----------
# Nu när klassen finns kan vi skapa objekt (variabler) med denna typ.
# Dessa objekt har också tillgång till klassens metoder (funktioner).
# a_car = Car('Volvo', 'Blå', 1587)
# a_car.get_brand()
# a_car.set_brand('Renault')
# a_car.get_brand()




b_car = Car("Aid","Röd",1984)
b_car.get_brand()
b_car.set_brand('Renault')
b_car.get_brand()
b_car.set_color("blå")
print(b_car.color)
a_car = Car('Volvo', 'Blå', 1587)
b_car = Car("Aid","Röd",1984)
c_car = Car("Toyota","Vit",42)
d_car = Car("Volkswagen","Svart",42000)

my_cars = [a_car,b_car,c_car,d_car]

for car in my_cars:
    print(car.brand)
def menu(list):
    for item in list:
        print(item)

menu = ["1. Brand","2. Color","3. Mileage"]

def main_menu(*args):
    args_list = [arg for arg in args]
    while True:
        accepted_choices = ["1","2","3"]
        menu(menu)
        choice = input("What would you like to list?")
        if choice not in accepted_choices:
            print("Not a valid attribute!")
            continue
        elif choice == "1":
            print(args_list.sort())
        break
