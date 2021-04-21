import os
import requests
from colorama import Fore, Style, Back


def screen_clear():
    _ = os.system('cls')


count = 0
count2 = 0
nb = 0
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
screen_clear()
print(f" {Fore.BLUE}                                                                                ")
print(f" {Fore.BLUE}                                                    ,                            ")
print(f" {Fore.BLUE}                                                    @*                           ")
print(f" {Fore.BLUE}                                       %           @.#.                          ")
print(f" {Fore.BLUE}                                   ..( %        .@#(  @                          ")
print(f" {Fore.BLUE}                                 .@(* %.     .@@%(#    @                         ")
print(f" {Fore.BLUE}                        &      @@#(   @   .@@#(((*     .#                        ")
print(f" {Fore.BLUE}                       ,@    @@( ..  % *@#(###(   ...   @                        ")
print(f" {Fore.BLUE}                       @.@  @(      @(((( *#. . &#.     ..                       ")
print(f" {Fore.BLUE}                      .( ..@/ . .@((#.  .,.(@((..      .@                        ")
print(f" {Fore.BLUE}                      @(  @    ,#(  .  .@@#(( .        .                         ")
print(f" {Fore.BLUE}                      @# #.  .#       @#. /          . @@,@                      ")
print(f" {Fore.BLUE}                     (#(           .&,          . /#(#. @                        ")
print(f" {Fore.BLUE}                     @(( /   .&.  .       . .(.  .#   @.  ..@@                   ")
print(f" {Fore.BLUE}     VEGETA          @/#@      .               .   .@(.@@%.                      ")
print(f" {Fore.BLUE}                    *%* .        .               .@@&((  .@.                     ")
print(f" {Fore.BLUE}                    %@           @ &    .   ,(, /(#/   .@@                       ")
print(f" {Fore.BLUE}                    @            .      .              .@                        ")
print(f" {Fore.BLUE}                   .@  ...              *           @                            ")
print(f" {Fore.BLUE}                   @( #*@.             #.      *@@@@#/@.                         ")
print(f" {Fore.BLUE}                   @.*@@. ..               ((* ..@.                              ")
print(f" {Fore.BLUE}                    @..(  @.         .       .#.                                 ")
print(f" {Fore.BLUE}                   @ .  .@@.         /.         (..                              ")
print(f" {Fore.BLUE}                   .    ,,           *.                                          ")
print(f" {Fore.BLUE}                            @    .., ./                                          ")
print(f" {Fore.BLUE}                           ./.  .* (       {Fore.WHITE} Credit: {Fore.GREEN}./OiBoy SecLinux.         ")
print(f" {Fore.BLUE}                                   .                {Fore.WHITE}Admin Panel {Fore.GREEN}Finder")
print(f" {Fore.BLUE}                                   . .          {Fore.WHITE}  Find me On {Fore.BLUE}Website")
print(f"                                                     {Back.GREEN} https://pashakun.com")
print(f"{Style.RESET_ALL}")

link = input("Enter your list.txt: ")
if not os.path.isfile(link):
    print(f'Enter a valid .txt file in the some folder')

screen_clear()
with open(link) as fp:
    for star in fp:
        if not star:
            break
        count += 1
        with open("config/panel.txt") as fp2:
            for star2 in fp2:
                if not star2:
                    break
                count2 += 1
                ahawa = star.strip() + '/' + star2.strip()
                resp = requests.get(ahawa, headers=headers)
                if (resp.status_code == 200) or (resp.status_code == 301):
                    resf = open("Results/!Valid_admin_panel.txt", "a")
                    resf.write(f'{ahawa}\n')
                    print(f"{ahawa} {Fore.BLUE}=> {Fore.GREEN} OK! {Style.RESET_ALL}")
                    resf.close()
                    star = fp.readline()
                    fp2.seek(0, 0)
                    nb += 1
                    if star not in '\n':
                        continue
                    else:
                        break
                else:
                    print(f"{ahawa} {Fore.BLUE}=> {Fore.RED} NO!{Style.RESET_ALL}")
fp.close()
fp2.close()
print(f"Total Website Admin Panel {Fore.GREEN}Finded: {Fore.CYAN}{nb}{Style.RESET_ALL}")
print(f"{Fore.RED}./OiBoy SecLinux.{Fore.WHITE}Thank You For Using My Tool\n Join US On {Fore.BLUE}Telegram {Fore.WHITE}For More: {Back.WHITE}{Fore.BLACK}https://t.me/xproadx {Style.RESET_ALL}")
