#!/usr/bin/python

from sets import Set
import sys
import copy


def count(num, l):
    rst = 0
    for i in range(l):
        tmp = Set([])
        j = i
        while j < len(num):
            if num[j] not in tmp:
                tmp.add(num[j])
            else:
                rst += 1
            j += l
    return rst


# crack multi-byte key one by one
def auto_guess(num, index, l):
    if index == l:
        return num_to_text(num)
    # determine the most possible one, with english letter and whitespace
    maxA = 0
    best_num = copy.copy(num)
    for key in range(256):
        i = index
        new_num = copy.copy(num)
        cwn = 0
        while i < len(new_num):
            new_num[i] = new_num[i] ^ key
            if chr(new_num[i]).isalpha() or new_num[i] == ord(' '):
                cwn += 1
            i += l
        if cwn > maxA:
            maxA = cwn
            best_num = copy.copy(new_num)
    return auto_guess(best_num, index+1, l)


# change ord to chr
def num_to_text(num):
    rst = ""
    for i in range(len(num)):
        rst += (chr(num[i]))
    return rst


def solve(num):
    # guess key length
    for i in range(5, 20):
        print "length=%d, having %d duplicates" % (i, count(num, i))
    print "type in the length you what to test:"
    l = int(raw_input())
    # break each of them
    return auto_guess(num, 0, l)


def gcd(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a+b


def usage():
    print("Usage: %s [in_file]\n" % sys.argv[0])
    exit()


def main():
    if len(sys.argv) < 2:
        usage()
    input_data = open(sys.argv[1], 'r').read()
    input_data = input_data.replace('\n', '').decode('hex')
    input_num = [ord(ch) for ch in input_data]
    print solve(input_num)

main()
