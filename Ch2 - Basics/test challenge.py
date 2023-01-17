def is_palindrome(teststr):
    if teststr == teststr[::-1]:
        return True
    return  False

run = True
while (run):
    teststr = input("enter string to test palindrome or exit: ")  

    if teststr == "exit":
        run = False
        break


    teststr = teststr.lower()

    newstr = ""
    for x in teststr:
            if x.isalnum():
                newstr += x

    print("palindrome test", is_palindrome(newstr))