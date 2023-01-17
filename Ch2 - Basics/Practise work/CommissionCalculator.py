#shop of Dales
import math
class commission1:
                name = str(input("What is your name as per your ID?"))
                sales = int(input("Enter your sales:"))
                commissionPersale = int(30) 
                salaryPerSale = int(1000)
                salary = int(sales * salaryPerSale)
                commission = int(salary * commissionPersale / 100)

                print(f"Hi {name}  , your total commission for this month is:  {commission}")
commission1()