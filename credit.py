from cs50 import get_string


def main():
    n = get_string("Number: ")
    l = len(n)
    if valid(n, l) == True:
        if l == 15 and n[0] == "3" and (n[1] == "7" or n[1] == "4"):
            print("AMEX")
        elif l == 16 and n[0] == "5" and (int(n[1]) in range(1, 6)):
            print("MASTERCARD")
        elif (l == 13 or l == 16) and n[0] == "4":
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")


def valid(n, l):
    used = 0
    sum1 = 0
    for i in range(2, l + 1, 2):
        t = n[l - i]
        used = used + int(t)
        if int(t) < 5:
            sum1 = sum1 + int(t) * 2
        else:
            sum1 = sum1 + 1 + (int(t) * 2 % 10)
    if (sum1 + (sum(int(i) for i in str(n))) - used) % 10 == 0:
        return True
    else:
        return False


main()

