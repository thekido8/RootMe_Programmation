import socket, string, codecs
import math

#some user data
SERVER='irc.root-me.org'
PORT=6667
NICK='myNname'
CHANNEL='#root-me_challenge'
BOT_NAME='Guest60187' #another possible name of the bot: Candy
CMD_CHALLENGE="!ep4"

#open a socket o handle the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#open a connection with the server
s.connect((SERVER, PORT))

#log in
s.send("USER myNname irc.root-me.org root-me :ChallengeBot\r\n")
s.send('NICK %s\r\n' % NICK)

#join the channel
s.send("JOIN %s\r\n" % CHANNEL)


def send_result(result):
    print(result)
    s.send('PRIVMSG ' + BOT_NAME + ' :'+ CMD_CHALLENGE +' -rep ' + result + '\r\n')


def challenge1(op):
    nbs = op.split("/")
    send_result(str(round(math.sqrt(int(nbs[0])) * int(nbs[1]), 2)))

def challenge2(op):
    send_result(op.decode('base64', 'strict'))

def challenge3(op):
    send_result(codecs.encode(op, 'rot13'))

def challenge4(op):
    send_result(op.decode('base64').decode('zlib'))

def my_main():
    while (1):
        tmp = s.recv(1024)
        msg = tmp.split(" ") #for example:PING :irc.hackerzvoice.net
        print('debug_1:' + tmp + "*\n")
        if msg[0] == "PING":
            s.send("PONG %s\r\n" % msg[1])
            s.send("PRIVMSG " + BOT_NAME + " :" + CMD_CHALLENGE + "\r\n")
            rep = s.recv(2048)
            #print("rep:%s/>\n" % rep)
            #for example::Guest60187!Candy@hzv-djs.n1p.2olmip.IP PRIVMSG myNname :cWEzNlFETm5tWVNOakE5dQ==
            rep_tab = rep.split(":")
            op = rep_tab[2]
            challenge4(op)

if __name__ == '__main__':
    my_main()
