__author__ = "jay"

def get_multiples(num, factor1, factor2):
    multiples = list()
    for i in range(1, num):
        if i % factor1 == 0 or i % factor2 == 0:
            print i
            multiples.append(i)
    return multiples

def main():
    num = int(raw_input("Enter a number to find sum of multiples: "))
    factor1 = int(raw_input("Enter factor 1: "))
    factor2 = int(raw_input("Enter factor 2: "))
    print sum(get_multiples(num, factor1, factor2))

if __name__ == "__main__":
    main()
