import sys
import pexpect
import re
import optparse
from sage.all import *

HOST, PORT = "vuln2014.picoctf.com", 51818
GET_KEY = "(?<=\n)(\w*)"
PRIME_FILE = "primes.txt"
COLLECT = "collect_key"
DECRYPT = "decrypt_key"
FLAG = "flag"
GET_MSG = "(?<=:\s)(\w*)"


def parse_arg():
    parser = optparse.OptionParser('usage %prog -k <public key file>' +
                                   '-c <cipher message>')
    parser.add_option('-k', dest='public_key', type='string',
                      help='Public Key you get from capture package')
    parser.add_option('-c', dest='cipher_msg', type='string',
                      help='Cipher message you get from capture package')
    (options, args) = parser.parse_args()
    key_file = options.public_key
    cipher_file = options.cipher_msg
    if key_file is None or cipher_file is None:
        print parser.usage
        exit(0)
    key = read_txt(key_file)[0].strip().decode('hex')
    msg = read_txt(cipher_file)[0].strip().decode('hex')
    key = re.findall(GET_MSG, key)
    if key == []:
        print '[-] You should give valid public key'
        exit(0)
    msg = re.findall(GET_MSG, msg)
    if msg == []:
        print '[-] You should give valid cipher message'
        exit(0)
    print '[+] key:\n%s' % key[0]
    print '[+] msg:\n%s' % msg[0]
    return (key[0], msg[0])


def read_txt(filename):
    try:
        f = open(filename, 'r')
        try:
            print '[+] Reading from %s...' % filename
            return f.readlines()
        finally:
            f.close()
    except:
        print '[-] %s not exist!' % filename
        exit(0)


def get_key(host, port, mul_set, prime_pool):
    child = pexpect.spawn('nc %s %d' % (host, port))
    child.logfile = sys.stdout
    child.expect(pexpect.EOF)
    if child.before is not None:
        message = child.before
        key = re.findall(GET_KEY, message)
        if key != []:
            mul_set.add(int(key[0], 16))
            return find_primes(mul_set, prime_pool)


def collect_key(host, port, prime_file):
    prime_pool = set()
    mul_set = set()
    while len(prime_pool) < 30:
        (mul_set, prime_pool) = get_key(HOST, PORT, mul_set, prime_pool)
    prime_file = open(prime_file, "w+")
    for p in prime_pool:
        prime_file.write('%d\n' % p)
    prime_file.close()
    return prime_pool


def find_primes(mul_set, prime_pool):
    new_mul = mul_set.copy()
    for s in mul_set:
        s_defactored = False
        for p in prime_pool:
            if s % p == 0:
                prime_pool.add(s/p)
                new_mul.remove(s)
                s_defactored = True
                break
        if s_defactored:
            continue
        for s1 in new_mul:
            if s1 == s:
                break
            gcd_p = gcd(s, s1)
            if gcd_p != 1:
                prime_pool.add(gcd_p)
                prime_pool.add(s1/gcd_p)
                prime_pool.add(s/gcd_p)
                new_mul.remove(s)
                break
    return (new_mul, prime_pool)


def get_primes():
    try:
        prime_lines = read_txt(PRIME_FILE)
        primes = set()
        for line in prime_lines:
            for p in line.split():
                primes.add(long(p))
        return primes
    except:
        print '[+] Collecting keys from %s:%d...' % (HOST, PORT)
        return collect_key(HOST, PORT, PRIME_FILE)


def decrypt_msg(key, cipher_msg):
    print '[+] Decrypting message using retrieved key and msg...'
    prime_set = get_primes()
    p, q = -1, -1
    for i in prime_set:
        if key % i == 0:
            p, q = i, key/i
            break
    e = 65537
    N = p*q
    d = inverse_mod(e, (p-1)*(q-1))
    M = pow(cipher_msg, d, N)
    T = ('%x' % M).decode('hex')
    print '[+] Getting message:\n%s' % T


def main():
    (key, cipher_msg) = parse_arg()
    decrypt_msg(int(key, 16), int(cipher_msg, 16))

if __name__ == '__main__':
    main()
