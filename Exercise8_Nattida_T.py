UName = input("Username : ")
passv = input("Pass : ")

if UName == "admin" and passv == "1169":
    print("\n      Wellcom to PETSHOP !!!    \n")
    print("รายการสินค้า     : 1. CAT  1:500 ")
    print("              : 2. DOG  1:300 ")
    print("--------------------------------------\n")
    userSelect = int(input("โปรดเลือกรายการสินค้า   : "))
    if userSelect == 1:

        amount = int(input("แมว ราคา 500ต่อตัว ท่านต้องการซื้อกี่ตัว :"))
        print("Total = ",amount*500)
    elif userSelect == 2:
        amount = int(input("หมา ราคา 300ต่อตัว ท่านต้องการซื้อกี่ตัว :"))
        print("Total = ",amount*300)

else :
    print("ล๊อกอินผิดพลาด !!")
