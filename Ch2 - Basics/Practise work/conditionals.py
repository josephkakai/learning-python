def main():
    x,y = 10,100
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else: 
        result = "x is greater than y"
    print(result)

    result = "x is less than y" if (x < y) else "x is greater than or equal to  y"
    print(result)

if __name__ == "__main__":
    main()


