star, stripe, check, col, counter = '*', "˭", 0, 15, 0
for a in range(col):
    if a == 0:
        for s in range(57):
            if s == 0:
                print(end='↗')
            print('Ξ', end='')
        print('↖')
    if check >= 0 and check <= 5:
        for i in range(10):
            if i == 0:
                print('||', end='')
            print(star, end=' ')
            counter +=1
    if a == 6:
        for w in range(20):
            if w == 0:
                print(end='||')
            print('Ξ', end='')
        for r in range(21, 56):
            if r == 21:
                print(end="↙")
            print('˭', end='')
        print("||")
    if a == 6:
        for w in range(56):
            if w == 0:
                print(end='||')
            print('˭', end='')
        print("||")
    if counter >= 10:
        for j in range(34):
            if j == 0:
                print('||', end='')
            print(stripe, end='')
    check += 1    
    if check > 6 and check <=15:
        for j in range(22):
           print(stripe, end='')
    print('||')
    if a == 14:
        for s in range(57):
            if s == 0:
                print('↘', end='')
            print('Ξ', end='')
        print('↙')
