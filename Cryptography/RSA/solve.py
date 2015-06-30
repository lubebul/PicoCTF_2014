import sys
import re


def usage():
    print("Usage: %s [ciphertext] [key_data]\n" % sys.argv[0])
    exit()


def main():
    if len(sys.argv) < 3:
        usage()
    ciphertext = open(sys.argv[1], 'r').read()
    key_data = open(sys.argv[2], 'r').read()
    regex_kv = re.compile('(\w+) = ([^\s]+)')
    pairs = regex_kv.findall(key_data)
    N, p, q, e, d = 0, 0, 0, 0, 0
    for pair in pairs:
        num = int(pair[1], 0)
        if pair[0] == 'N':
            N = num
        elif pair[0] == 'p':
            p = num
        elif pair[0] == 'q':
            q = num
        elif pair[0] == 'e':
            e = num
        elif pair[0] == 'd':
            d = num
    C = int(ciphertext, 16)
    M = pow(C, d, N)
    m = '%x' % M
    print m.decode('hex')
main()
