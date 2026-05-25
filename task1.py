#smart cafe and billing and inventory system
inventory={"coffee":10,
                   "cold coffee":15,
                   "tea":50,
                   "patties":30,
                   "sand which":40
        }
while True:
 User_=input("who are you (user/admin): ")
 if User_.lower()=="exit":
     print("logging out")


     break
 if User_.lower()=="admin":
    password=input("enter your password: ")
    if password=="admin1111":
        print("welcome admin")
        print(inventory)
        upd=input("what do you want to update: ")
        numb = int(input("enter the number you want to update"))
        if upd=="coffee":
            inventory["coffee"]=numb
            print(inventory["coffee"])
        elif upd=="cold coffee":
            inventory["cold coffee"]=numb
            print(inventory["cold coffee"])
        elif upd=="tea":
            inventory["tea"]=numb
            print(inventory["tea"])
        elif upd=="patties":
            inventory["patties"]=numb
            print(inventory["patties"])
        elif upd=="sand which":
            inventory["sand which"]=numb
            print(inventory["sand which"])
        else:
            print("invalid input")
    else:
        print("wrong password")

 else:
  total_price=0
  while True:

   menu={"coffee":40,
      "cold coffee":60,
      "tea":20,
      "patties":25,
      "sand which":40
  }
   print(menu,"\nsingle order at a time please \ntotal price = ",total_price)
   print( "write exit to final the bill")
   var_1=input("what do you want to order :")
   if var_1.lower() == "exit":
    print("total bill = ",total_price)
    break
   number=int(input("how many you want to order : "))
   if var_1=="coffee":
    inventory["coffee"]=10-number
    total_price=(total_price+40)*number
    print(total_price)
   elif var_1=="sand which":
      inventory["sand which"] = 40 - number
      total_price = (total_price + 40) * number
      print(total_price)
   elif var_1=="cold coffee":
    inventory["cold coffee"] = 15 - number
    total_price = (total_price +60)*number
    print(total_price)
   elif var_1=="tea":
    inventory["tea"] = 50 - number
    total_price = (total_price + 20)*number
    print(total_price)
   elif var_1=="patties":
    inventory["patties"] = 30 - number
    total_price = (total_price + 25)*number
    print(total_price)
   else:
    print("invalid input")
print(inventory)


