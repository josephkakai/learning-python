try:
    x = 10 / 0
except:
    "hiyo haiwezekani bro!"

try:
    answer = (input("niaje bro, 'swali' weka number tu divide by 10:"))
    num = int(answer)
    print(10 / num)

except ZeroDivisionError as e:
    print("pole huwezi divide by zero!")
    print(e)
except ValueError as e:
    print("rada, hauja weka number valid!")
    print(e)
finally:
    print("natutaendelea, karibu tena")