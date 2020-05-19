import sys


def prime_test(test_num):
    if test_num == 1:
        return False
    elif test_num == 2:
        return True
    elif test_num % 2 == 0:
        return False
    else:
        hi = int((test_num ** 0.5) + 1)
        for num in range(3, hi, 2):
            if test_num % num == 0:
                return False
        else:
            return True

def main():
    mynum = int(sys.argv[1])
    if prime_test(mynum):
        print("%s is print" % mynum)
    else:
        print("%s is not prime" % mynum)


if __name__ == '__main__':
    main()