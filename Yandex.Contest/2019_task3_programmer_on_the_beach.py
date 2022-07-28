import sys


def read_int():
    return int(sys.stdin.readline())


def read_ints():
    return map(int, sys.stdin.readline().split())


def main():
    number_of_tests = read_int()
    for _ in range(number_of_tests):
        number = read_int()          # reads the number of sunbeds
        sorted_numbers = sorted(read_ints())       # sorting numbers of sunbeds
        xor = sorted_numbers[0] ^ sorted_numbers[1]
        for i in range(1, number):
            xor = min(xor, sorted_numbers[i - 1] ^ sorted_numbers[i])

        print(xor)


if __name__ == '__main__':
    main()
