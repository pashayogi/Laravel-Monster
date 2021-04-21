from colorama import Fore, Style, Back
import os
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
bgr = Back.GREEN
RED = Fore.RED
sres = Style.RESET_ALL
bred = Back.RED
def screen_clear():
    _ = os.system('cls')
screen_clear()
print(f"""                                                             
   {RED}                                            . .:'                                           
                                                   ..  'c;.                                         
                                                 .'.    'c:.                                        
                                                .'..     .:c.                                       
                                      ...      .,.        'cc.                                      
                                   .... ..    ',.         .;lc'                                     
                                  .'.   .'  .,.            .clc.                                    
                                .;.      .....              .:l:.      .                            
                               ,:.        .                  .;c'     .'.                           
                              ;l'    ..                . ... .,l,     .;'                           
                            .:o;.  ...   .'.           ...',. .c;     .::.                          
                            ;o:. .,.    .:'            ...';, .;.     .:l'                          
                    ..     ,c,. ',.    'l;    ..      .' ',,:...      .co:.                         
                    ;:.   .:' .:,.    ,oc.    ...    .'. ''':;.       .coc.                         
                    ;dc.  '..'c,     ,cl'      .'   ..   ...;c,.      .lll,                         
                    ;ddl'   .c;     ;:..       .'.       ...::;.      'lll,     ..           {sres}       
                    ;doc:,. .'    .;l.          ''        .:l:;'   .. ,lll'    .;.                  
       {bl}         ,dd,..'..     ;l,           .''.      .col:,   .,.;ooc.  ..::.                  
                    'l:'.  ..    'c,             .;.      .cllc;.  .,':ol,  .';l;                   
                    .c'         ...              .,.      .llll;.  .,,clc.....:c.                   
                    .;.                           .       'clcc;   ..;ll;..  .:'                    
                    .'.                                   .';';,   ..,lc.   .;' .                   
                 .'...            .....  ......     ....   .. ''     .,'    ..            {sres}          
                 .c;..'....     .;:,...;cc:;,............  .....      ..    ..                      
                  'c,. ...     .:;. .:odl,. .....           ...,'....           ...                 
                   .l:'.      .:,  ,lc,... ......    ...       .::..'.       .'',.                  
                    .col,.   .:c. .l:.      .,'. ...'''...,:'   .::..'     .';:;.                   
                     .:do,   ;o;. ;o;.     .;. ..... .,;;;'';.   'c..;.   .';:;.                    
                       ,c'  ':'.  :o'   . .,.         ;kXNKd:'   .c,.,. .':lc'                      
                       ... .,.   .::  'xk'....         .lXWWO'   'l' .. .,,'.     Join US for Free Tools & much more                  
      {RED}            ....'.  ...;..lKNXl.cc.        . .dWWNl. .c:. .. ..                          
                           .;;;c:..'xd;:ddk0;      .;l;.;odlxo..::... .''..                         
                             ..'::.:XO;,,,:lc'     .;;,;c;,'lc.,,.,,.....                           
                                 .''kWklclc;,'.     .,;;:lcdk:...,'                                 
                                    cNNd,'....       ....,xX0l...                                   
                                    :KK;         ...      oW0cc;      {sres}    {gr} ./OiBoy SecLinux.                        
                                   .dK0o.        .'.     .xN0:''..   {RED}  ► LARAVEL MONSTER V1 ◄ {sres}                       
                                   .O0:lx,              'ccd0;                                        
                                   ;XX:;Ol..           .'.'dx;.               https://pashakun.com                         
                                  .oNWd.oo.             .,lxO0:                                     
                              .;codOKNK;.c;             .',oXXd;'.                                  
                           ..';,'....,ll'...               .do..''..                                
                                       ..                   ..               """)

print(f"{RED}[{sres}{gr}1{sres}{RED}]{sres}: Mass Grabb SMTP + Random Informations.")
print(f"{RED}[{sres}{gr}2{sres}{RED}]{sres}: Mass Reformat File + Remove Duplicated.")
print(f"{RED}[{sres}{gr}3{sres}{RED}]{sres}: Mass Check Working SMTP.")
print(f"{RED}[{sres}{gr}4{sres}{RED}]{sres}: Mass Grabb Valid MySQL.")
print(f"{RED}[{sres}{gr}5{sres}{RED}]{sres}: Mass Panel Admin Finder.")
print(f"{RED}[{sres}{gr}6{sres}{RED}]{sres}: Check Updates.")
choice = input("Please Enter Your Choice: ")
if choice == '1':
        os.system('cmd /k "python Script/tool1/grab.py"')

if choice == '2':
        os.system('cmd /k "py Script/tool2/v3.py"')
if choice == '3':
        os.system('cmd /k "py Script/tool3/checker.py"')

if choice == '4':
        os.system('cmd /k "py Script/tool4/mysql.py"')
if choice == '5':
        os.system('cmd /k "py Script/tool5/finder.py"')
if choice == '6':
    print(f" Contact the seller for more information:\n {bgr}https://t.me/Pashayogiptanata{sres}")
