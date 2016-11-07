import string
import random


def passwordgen():
    password = ""
    for i in range(0, random.randint(8, 15)):
        x = random.randint(1, 4)
        if x == 1:
            password += str(get_lowerc())
        elif x == 2:
            password += str(get_upperc())
        elif x == 3:
            password += str(get_number())
        elif x == 4:
            password += str(get_symbol())

    return password


def get_lowerc():
    x = string.ascii_lowercase
    c = x[random.randint(0, 25)]
    return c


def get_upperc():
    x = string.ascii_uppercase
    c = x[random.randint(0, 25)]
    return c


def get_number():
    num = random.randint(0, 9)
    return num


def get_symbol():
    sym = "!@#$%^&*()?"
    s = sym[random.randint(0, 10)]
    return s

def main():
    return


if __name__ == '__main__':
    main()
