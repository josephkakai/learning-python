#Shopping software
#Authored by: Joseph Kakai

shopping_basket = {}
# print("Welcome to 'KAKS SHOP'\nThe best place to shop\nwhat we have for:\n1. 2Kg Kakai Maize flour: KES 100\n2. 2Kg kakai Baking flour: KES 250\n3. 1 Litre Kakai Cooking Oil: KES 400\n4. 1 Litre Cocacola soda: KES 100")

price = {"2Kg Maize Flour" : 100, "2Kg Baking flour": 250, "1 Litre Cooking Oil": 400, "1 Litre Cocacola soda": 120 }

buy_another_product = 1
total_cost, total = 0 ,0

while buy_another_product != 0:
    try:
        option = input("Welcome to 'KAKS SHOP'\nThe best place to shop\nwhat we have for:\nS/N Product Name\n1. 2Kg Maize flour: Ksh 100\n2. 2Kg Baking flour: Ksh 250\n3. 1 Litre Cooking Oil: Ksh 400\n4. 1 Litre Cocacola soda: Ksh 100\nInput index number of product you need:")
        num = int(option)
    except:
        "Wrong input please try again"
    
    if num == 1:
        Quantity = int(input("Enter quantity:"))
        Total = Quantity * 100 
        print(f"The total price for 2Kg Maize Flour is:\nVAT Tax - 0%\nTotal Ksh{Total}" )
        # total_cost += total
        # try:
        #     please_buy = ("Thank you for shopping!")
        #     buy = (please_buy)
        #     print(buy)
        #     if please_buy == 1:
        #         print('Great!')
        #     elif please_buy == 2:
        #         print('Thank you for buying')
        #     # else:
        #     #     print("invalid input")
        # except ValueError as x:
        #     print("wrong input")
        #     print(x)
        total_cost += Total    

        if not input(f"Total price of your basket is:{total_cost}\nWould you like to continue shopping?\nEnter Yes'1' or No'0' to continue"):
            break
        
    elif num == 2:
        Quantity = int(input("Enter quantity:"))
        Total = Quantity * 250
        print(f"The total price for 2Kg Baking flour is:\nVAT Tax - 50%\nTotal Ksh{Total}")
        total_cost += total
        try:
            please_buy = input("Would you like any other item?\nEnter Yes'1' or No'0' to continue")
            buy = int(please_buy)
            print(buy)
            if please_buy == 1:
                print('Great!')
            elif please_buy == 2:
                print('Thank you for buying')
            # else:
            #     print("invalid input")
        except ValueError as x:
            print("wrong input")
            print(x)
        total_cost += Total    

        if not input(f"Total price of your basket is:{total_cost}\nWould you like to continue shopping?\nEnter Yes'1' or No'0' to continue"):
            break
    elif num == 3:
        Quantity = int(input("Enter quantity:"))
        Total = Quantity * 400 
        print(f"The price for Cooking Oil is:\nVAT Tax - 13%\nTotal Ksh{Total}")
        total_cost += total
        try:
            please_buy = input("Would you like any other item?\nEnter Yes'1' or No'0'to continue")
            buy = int(please_buy)
            print(buy)
            if please_buy == 1:
                print('Great!')
            elif please_buy == 2:
                print('Thank you for buying')
            # else:
            #     print("invalid input")
        except ValueError as x:
            print("wrong input")
            print(x)
        total_cost += Total    

        if not input(f"Total price of your basket is:{total_cost}\nWould you like to continue shopping?\nEnter Yes'1' or No'0' to continue"):
            break
    elif num == 4:
        Quantity = int(input("Enter quantity:"))
        Total = Quantity * 120 
        print(f"The total price for 1 Litre Cocacola soda is:\nVAT Tax - 17%\nTotal Ksh{Total}")
        total_cost += total
        try:
            please_buy = input("Would you like any other item?\nEnter Yes'1' or No'0' to continue")
            buy = int(please_buy)
            print(buy)
            if please_buy == 1:
                print('Great!')
            elif please_buy == 2:
                print('Thank you for buying')
            # else:
            #     print("invalid input")
        except ValueError as x:
            print("wrong input")
            print(x)
        total_cost += Total    

        if not input(f"Total price of your basket is: KES{total_cost}\nWould you like to continue shopping?\nEnter Yes'1' or No'0' to continue"):
            break
    elif num > 4:
        try:
            option > 4
        except:
               print("Wrong input, sorry!")        
        finally:
            print("Wrong input, sorry!")
               
        total_cost += Total
        try:
            please_buy = input("Would you like any other item?\
                ")
            buy = int(please_buy)
            print(buy)
            if please_buy == 1:
                print('Great!')
            elif please_buy == 2:
                print('Thank you for buying')
            else:
                print("invalid input")
        except ValueError as x:
            print("wrong input")
            print(x)

    
    else:
        Total = price * Quantity
        print(f"Total price of your basket is:{total_cost}")