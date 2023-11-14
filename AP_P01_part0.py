import random
import re
import pandas as pd


class Inventory():

    def __init__(self, code, name, price, quantity, size):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity
        self.size = size

    def __str__(self):
        return f'{self.code},{self.name},{self.price},{self.quantity},{self.size}'
    def copy(self):
        return Inventory(self.code,self.name,self.price,self.quantity,self.size)


class Committing_order():

    def __init__(self):
        self.Cart = []

    def addItem(self,item):
        self.Cart.append(item)

    def removeItem(self,item):
        self.Cart.remove(item)

    def viewCart(self):
        for cart in self.Cart:
            print(cart)

    def run(self):
        buy_products = []

def valid_postalcode(postlcode):
    pattern1 = re.compile(r'^\d{10}$')
    return bool(pattern1.match(postalcode))

def valid_cardnumber(cardnumber):
    pattern2 = re.compile(r'^\d{16}$')
    return bool(pattern2.match(cardnumber))


class outgoing_orders():
    instance = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(outgoing_orders,cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.morning_orders = 0
        self.noon_orders = 0
        self.afternoon_orders = 0

    def determine_delivery_time(self):
        print("Please choose sending time :")

        print("Morning")

        if self.noon_orders < 3:
            print("Noon")

        if self.afternoon_orders < 3:
            print("Afternoon")

        time = input()

        if time == 'Morning':
            self.morning_orders += 1

        if time == 'Noon':
            self.noon_orders += 1

        if time == 'Afternoon':
            self.afternoon_orders += 1

        return time


logestic = outgoing_orders()

while True:

    print("Please Select Your Role :", "\n", "1: Sellers' Panel", "\n", "2: Buyers' Panel", "\n",
          "3: Close the application")

    panel = int(input())

    if panel == 1:

        while True:

            print(''' 
                  1: Add products to your inventory.
                  2: Change quantity of your products.
                  3: Show My Inventory Objects.
                  4: َAccounting
                  5: Back to select role menu.
                  ''')

            work = int(input())

            if work == 1:

                n = int(input("How many products do you want to add to your inventory: "))
                inventory = []

                for i in range(n):
                    pro = Inventory(
                        code = int(input('Enter the Code of Your Product : ')),
                        name = input('Enter the Name of Your Product : '),
                        price = int(input('Enter the Price of Your Product :  ')),
                        quantity = int(input('Enter the Quantity of Your Product : ')),
                        size = int(input('Enter the Size of Your Product : '))
                    )
                    inventory.append(pro)

            elif work == 2:

                p = []
                p = inventory
                print('''
                      1: Edit with csv File.
                      2: Manual Edit.
                      ''')

                how = int(input())

                if how == 1:

                    df = pd.read_excel("add File location")

                    rows = df.values.tolist()

                    code = []

                    for i in rows:

                        for j in p:

                            code.append(j.code)

                            if i[0] in code:
                                a = code.index(i[0])

                                p[a].quantity = i[1]

                elif how == 2:

                    how_many = int(input("How many products do you want to change their quantity ?   "))

                    for i in range(how_many):

                        code = int(input("Enter the code of your product: "))
                        new_quantity = int(input("Enter the new quantity of your product: "))

                        for j in p:

                            if j.code == code:
                                j.quantity = new_quantity

            elif work == 3:

                c = []
                q = []
                l = []

                for i in range(len(inventory)):
                    c.append(inventory[i].code)
                    q.append(inventory[i].quantity)
                    l.append(1)

                dict = {"Code": c, "Quantity": q, "Inventory_code": l}

                df = pd.DataFrame(dict)
                df.to_csv("inventory.csv")
                print(df)

            elif work == 4:
                acc = open('Accounting.txt', "r")
                accountant = acc.read()
                print(accountant)
                acc.close()

            elif work == 5:

                break


    elif panel == 2:

        buy_products = []

        while True:
            print('''
                    1: Add an Item
                    2: Remove an Item
                    3: View Cart
                    4: Checkout
                    5: Back to select role menu.
                    ''')

            Command = int(input())

            if Command == 1:

                for product in inventory:
                    print(product)

                name = input("Input Product Name: ")
                count = int(input("Input Quantity: "))
                size = int(input("Input Product Size: "))

                for i in range(len(inventory)):
                    if inventory[i].name == name and inventory[i].size == size:

                        if count <= inventory[i].quantity:

                            myproduct = inventory[i].copy()
                            myproduct.quantity = count
                            #inventory[i].quantity -= count
                            buy_products.append(myproduct)

                        elif count > inventory[i].quantity:

                            print("Failed to add to your Cart. ")


            if Command == 2:

                name = input("Input Product Name: ")

                for buy_product in buy_products:
                    if buy_product.name == name:

                        buy_products.remove(buy_product)

                        for product in inventory:
                            if product.name == name:

                                product.quantity += buy_product.quantity

            if Command == 3:

                for buy_product in buy_products:
                    print(buy_product)

            if Command == 4:

                trakingnumbers = []
                cardnumbers = []
                addresses = []
                receipts = []
                portal = []

                while True:
                    accountname = input("Your Full Name: ")
                    phonenumber = int(input("Your Phone Number: "))
                    province = int(input("Your Delivery Address Province:\n 1- Tehran\n 2- Isfahan\n 3- East Azarbaijan \n"))

                    if province == 1:

                            city = int(input("Your Delivery Address City:\n 1- Tehran\n 2- Parand \n"))

                    elif province == 2:

                            city = int(input("Your Delivery Address City:\n 1- Isfahan\n 2- kashan \n"))

                    elif province == 3:

                            city = int(input("Your Delivery Address City:\n 1- Tabriz\n 2- Miyaneh \n"))

                    details = input("Delivery Details: ")
                    postalcode = str(input("Your Postal Code: "))
                    time = int(input("Delivery Time: "))



                    if (province in range(1,4) ) and (city in range(1,3) ) and (valid_postalcode(postalcode)) and (time in range(25) ):

                        addresses.append([province,city,details,postalcode])
                        break

                    else:

                        print("Unvalid Answers","Please Input Correct Answers", sep="\n")

                while True:
                    trackingnumber = random.randrange(10**10 , 10**11)

                    if trackingnumber not in trakingnumbers:
                        trakingnumbers.append(trackingnumber)
                        break

                while True:
                    cardnumber = input("Please Input Your Card Number: ")

                    if valid_cardnumber(cardnumber):

                        purchase_list = [str(trackingnumber),cardnumber, "Successfully Purchased",str(province),str(city),details,postalcode]
                        buy_history = buy_products.copy()

                        linesforportal=["Card Number: " + str(cardnumber),"Purchase Status:  " + "Successfully Purchased", "Account Name: " + accountname]
                        with open('Portal.txt', 'a') as f:
                            for line in linesforportal:
                                f.write(line)
                                f.write('\n')
                            f.write('\n')
                            f.write('\n')


                        for i in range(len(inventory)):
                            for j in range(len(buy_products)):
                                    if inventory[i].name == buy_products[j].name and inventory[i].size == buy_products[j].size:

                                        inventory[i].quantity -= buy_products[j].quantity

                                        if province == 1:

                                            delivery_type = 'Delivery Bike'

                                        else:

                                            delivery_type = 'Post'

                        delivery_time = logestic.determine_delivery_time()


                        sumofproducts = 0
                        totalprice = 0
                        tax = 0
                        for i in range(len(buy_products)):
                            sumofproducts += buy_products[i].quantity
                            for j in inventory:
                                if buy_products[i].name == j.name:
                                    totalprice += buy_products[i].quantity * j.price

                        if province == 1:
                            shippingcost = 10
                        else:
                            shippingcost = 30
                        tax = totalprice * (9 / 100)

                        with open('Receipt.txt', 'a') as Receipt:

                            for i in buy_products:
                                Receipt.write("Name: " + i.name)
                                Receipt.write('\n')
                                Receipt.write("Price: " + str((i.quantity)*(i.price)))
                                Receipt.write('\n')

                            linesforreceipt = ["Trakving Number: " + str(trackingnumber), "Address Details: " + details, "Full Name: " + accountname, "Delivery Time: " + delivery_time, "Delivery Type: " + delivery_type, "Final Price: " + str(tax + totalprice + shippingcost)]
                            for line in linesforreceipt:
                                Receipt.write('\n')
                                Receipt.write(line)

                        break


                    else:

                        purchase_list = [str(trackingnumber), cardnumber, "Purchased Failed", str(province), str(city), details, postalcode]

                        linesforportal=["Card Number: " + str(cardnumber),"Purchase Status:  " + "Purchased Failed", "Account Name: " + accountname]
                        with open('Portal.txt', 'a') as f:
                            for line in linesforportal:
                                f.write(line)
                                f.write('\n')
                            f.write('\n')
                            f.write('\n')


                        commiting_order = Committing_order()
                        commiting_order.run()
                        # print(*portal)

                        break


            if Command == 5:

                n = 0
                k = 0
                t = 0
                for i in range(len(buy_products)):
                    n += buy_products[i].quantity

                    for j in inventory:
                        if buy_products[i].name == j.name:

                            k += buy_products[i].quantity * j.price

                if province == 1:

                    c = 10

                else:

                    c = 30

                t = k * (9 / 100)

                with open('Accounting.txt', 'a') as Accounting:
                    Accounting.write("Sum of Products: " + str(n))
                    Accounting.write('\n')
                    Accounting.write("Trakcing Number: " + str(trackingnumber))
                    Accounting.write('\n')
                    Accounting.write("Price before Taxes and Shipping Cost: " + str(k))
                    Accounting.write('\n')
                    Accounting.write("Shipping Cost: " + str(c))
                    Accounting.write('\n')
                    Accounting.write("Tax: " + str(t))
                    Accounting.write('\n')
                    Accounting.write("Final Cost to Purcahse: " + str(t + k + c))
                    Accounting.write('\n')
                    Accounting.write('\n')

                buy_products = []

                break


    if panel == 3:

        break