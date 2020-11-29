import requests
from bs4 import BeautifulSoup
import random
import os
from colorama import Fore
os.system('clear')
g = Fore.GREEN
r = Fore.RED
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
c = Fore.CYAN

color = [g, r, w, b, y, c]
venom = random.choice(color)

banner = '''
██╗   ██╗███████╗███╗   ██╗ ██████╗ ███╗   ███╗    ███████╗██╗  ██╗██╗███████╗██╗     ██████╗                                                            
██║   ██║██╔════╝████╗  ██║██╔═══██╗████╗ ████║    ██╔════╝██║  ██║██║██╔════╝██║     ██╔══██╗                                                             
██║   ██║█████╗  ██╔██╗ ██║██║   ██║██╔████╔██║    ███████╗███████║██║█████╗  ██║     ██║  ██║                                                             
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║    ╚════██║██╔══██║██║██╔══╝  ██║     ██║  ██║                                                             
 ╚████╔╝ ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║    ███████║██║  ██║██║███████╗███████╗██████╔╝  Created by Venom
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚═════╝   Hacker Banno Chutiya nhi
                                                                                              
        [+] Do You have the proxy list? 
        
        [1] Yes
        [2] No 
                                                                                        
'''
print(venom + banner + venom)
choice = str(input(w + '        [-] Choose : ' + w))
if choice == '1':
    print(' ')
    path = str(input('        [+] Enter the path to the file: '))
    if os.path.exists(path) is False:
        print(w + '        [-] ' + w + r + "Either File doesn't exit or path is wrong." + r)
        print(' ')
    else:
        print(' ')
        print(w + '        [+] File Exits: ' + w + g + 'True' + g)
        file = open(path, 'r')
        read = file.readlines()
        x = len(read)
        x = str(x)
        print(w + '        [+] Total Proxies: ' + w + g + x + g)
        file = open(path, 'r')
        f = file.readlines()
        for i in f:
            i.replace(':', ' ')
            print(i)
elif choice == '2':
    print(' ')
    no = '''
        [+] Do you want to generate proxies?
            
        [1] Yes
        [2] No
            
    '''
    print(venom + no + venom)
    generate = str(input(w + '        [-] Choose : ' + w))
    if generate == '1':
        print(' ')
        url = 'https://free-proxy-list.net/'
        print(" ")
        count = int(input(w + '        [-] ' + w + venom + 'Enter the number of proxies you want: ' + w))
        print(" ")
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        table = soup.find(class_='table table-striped table-bordered')
        proxy = table.findAll('td')
        ip_add = []
        port_no = []
        code = []
        country = []
        anonymity = []
        google = []
        https = []
        last = []
        final = []
        j = 0
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            ip_add.append(a)
            j = j + 8
        j = 1
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            port_no.append(a)
            j = j + 8
        j = 2
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            code.append(a)
            j = j + 8
        j = 3
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            country.append(a)
            j = j + 8
        j = 4
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            anonymity.append(a)
            j = j + 8
        j = 5
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            google.append(a)
            j = j + 8
        j = 6
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            https.append(a)
            j = j + 8
        j = 7
        while (j < (8 * count)):
            a = str(proxy[j].contents[0])
            last.append(a)
            j = j + 8
        for k in range(0, count):
            print(w + "        [+] IP: " + w + g + ip_add[k] + g)
            print(w + "        [+] Port: " + w + g + port_no[k] + g)
            print(w + "        [+] Code: " + w + g + code[k] + g)
            print(w + "        [+] Country: " + w + g + country[k] + g)
            print(w + "        [+] Anonymity: " + w + g + anonymity[k] + g)
            print(w + "        [+] Google: " + w + g + google[k] + g)
            print(w + "        [+] https: " + w + g + https[k] + g)
            print(w + "        [+] Last Updated: " + w + g + last[k] + g)
            print(w + "        [+] Status: " + w + r + 'Checking...' + r)
            url = 'https://onlinechecker.proxyscrape.com/index.php'
            headers = {'Host': 'onlinechecker.proxyscrape.com',
                       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0',
                       'Accept': '*/*',
                       'Accept-Language': 'en-US,en;q=0.5',
                       'Accept-Encoding': 'gzip, deflate',
                       'Referer': 'https://proxyscrape.com/online-proxy-checker',
                       'Content-Type': 'multipart/form-data; boundary=---------------------------37720812130963496262511744541',
                       'Origin': 'https://proxyscrape.com',
                       'Connection': 'close'}
            data = '-----------------------------37720812130963496262511744541\x0d\x0aContent-Disposition: form-data; name=\"ip_addr\"\x0d\x0a\x0d\x0a' + \
                   ip_add[
                       k] + '\x0d\x0a-----------------------------37720812130963496262511744541\x0d\x0aContent-Disposition: form-data; name=\"port\"\x0d\x0a\x0d\x0a' + \
                   port_no[k] + '\x0d\x0a-----------------------------37720812130963496262511744541--\x0d\x0a'
            response = requests.post(url=url, headers=headers, data=data)
            result = response.content
            result = str(result)
            result1 = result.replace('b', ' ')
            result2 = result.replace(',', " ")
            result3 = result2[2:-1]
            result4 = result3.split()
            if result4[3].startswith("false") is True:
                print(w + "        [-] Working: " + w + r + 'False' + r)
                print(" ")
            else:
                print(w + "        [+] Working: " + w + g + 'True' + g)
                print(" ")