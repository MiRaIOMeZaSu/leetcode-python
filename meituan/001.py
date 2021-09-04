if __name__ == "__main__":
    wrong = "Wrong"
    accept = "Accept"
    count = int(input())
    for i in range(count):
        string = input()
        if not string[0].isalpha():
            print(wrong)
            continue
        a = 0
        b = 0
        flag = True
        for c in string:
            if c.isdigit():
                a += 1
            elif c.isalpha():
                b += 1
            else:
                print(wrong)
                flag = False
                break
        if flag:
            if a == 0 or b == 0:
                print(wrong)
                continue
            print(accept)
