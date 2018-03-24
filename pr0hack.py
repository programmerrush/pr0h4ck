#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3=os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = '''\033[0m 
  mmerRu                                                                              mmerRu                    ra       
  rogramm                                                                             rogramm                   hP       
  Ru   ro                                                                             Ru   ro                   er       
  am   Ru  Prog  mmerRu  Progra   rRus  rogra  erRushProg   merRushPro  ammerR   Prog am   Ru   ro  am  rRushP  gramme   
  Program  rR s  ro  am  rR  hP   ra m     hP  gr  me  us   og  mm  Ru  Pr  ra   rR s Program   Ru  Pr  ra      sh  og   
  rRushP   ra    Ru  Pr  ra  er   hP    ammer  sh  og  mm   us  ro  am  rRushP   ra   rRushP    am  rR  hProg   me  us   
  ra       hP    am  rR  hP  gr   er   hProgr  me  us  ro   mm  Ru  Pr  ramme    hP   ra  er    Pr  ra   rRush  og  mm   
  hP       er    Pr  ra  er  sh   gr   er  sh  og  mm  Ru   ro  am  rR  hP       er   hP   ra   rR  hP      me  us  ro   
  er       gr     Rush    ramme   sh    ramme  us  ro  am   Ru  Pr  ra   rRush   gr   er   hP    ammer  shPro   mm  Ru   
                             og                                                                                          
                         merRus 
                         
           Pr0               4             4          r                       
     0#4ckPr0#          Pr0#4c       kP 0#        ckP              r0#      
     r0#   Pr0  ck r0  ckP 0#4c     4ckPr0#4    0#4ck       Pr0#   Pr0 4ck  
     Pr0  ckPr #4ckPr #4c  r0#4    0#4 kPr     Pr #4c      ckPr0  ckP 0#4c  
    ckPr #4ck  0#4c   0#4  Pr0#    r0# ckPr   ck  0#4     #4c     4ckPr0#   
    4ckPr0#4c  r0#   Pr0#  kPr0  ckPr0#4ckP  #4ckPr0#4c  r0#4     #4ckPr    
    #4ckPr0   kPr0   kPr0  ckPr  4ckPr0#4   r0#4ckPr0#4  Pr0#    r0#4ckPr   
   r0#4       ckPr   ckPr0#4ck    4c  r0#        ckPr    kPr0#4  Pr0# ckPr  
   Pr0#       4ckP   4ckPr0#4c   0#4 kPr         4ckP    ckPr0# ckPr  4ckP  
   kPr0      0#4ck    4ckPr0                    0#4ck     ckPr0 4ckP  #4ckP 
               
                         \033[0m  \033[91m    \033[1m 
       }--{+} Created By Programmer Rushikesh {+}--{
     }----{+}  #4ck 4 Community {+}----{
       }--{+}  Even more .....  {+}--{                               
     '''
menu = '''\033[0m
    {1}--Whois lookup
    {2}--Traceroute
    {3}--DNS Lookup
    {4}--Reverse DNS Lookup
    {5}--GeoIP Lookup
    {6}--Port Scan
    {7}--Reverse IP Lookup
    {99}-Exit                                                                                                                   
 '''
print logo
print menu
def quit():
            con = raw_input('Continue [Y/n] -> ')
            if con[0].upper() == 'N':
                exit()
            else:
                os.system("clear")
                print logo
                print menu
                select()
           
def  select():
  try:
    choice = input("Crips~# ")
    if choice == 1:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \ 
| |/ |/ / __  / /_/ _/ / ___/ / 
|__/|__/_/ /_/\____/___//____/                                  
      """)
      os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
      print("")
      quit()
    elif choice == 0:
	  os.system("clear")
	  print("This tool is only available for Linux and similar systems  ")
	  os.system("git clone https://github.com/Manisso/Crips.git")
	  os.system("cd Crips && sudo bash ./update.sh")
	  os.system("crips")
    elif choice == 2:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
 ____ ____   __   ___ ____ ____ _____ __  __ ____ ____ 
(_  _(  _ \ /__\ / __( ___(  _ (  _  (  )(  (_  _( ___)
  )(  )   //(__)( (__ )__) )   /)(_)( )(__)(  )(  )__) 
 (__)(_)\_(__)(__\___(____(_)\_(_____(______)(__)(____)
""")
      os.system("curl https://api.hackertarget.com/mtr/?q=" + d3 )
      print("")
      quit()
    elif choice == 3:
      d3 = raw_input('Enter Domain : ')
      os.system("clear")
      print("""
______ _   _ _____   _                 _                
|  _  | \ | /  ___| | |               | |               
| | | |  \| \ `--.  | |     ___   ___ | | ___   _ _ __  
| | | | . ` |`--. \ | |    / _ \ / _ \| |/ | | | | '_ \ 
| |/ /| |\  /\__/ / | |___| (_) | (_) |   <| |_| | |_) |
|___/ \_| \_\____/  \_____/\___/ \___/|_|\_\\__,_| .__ / 
                                                 | |    
                                                 |_|     
""")
      os.system("curl http://api.hackertarget.com/dnslookup/?q=" + d3 )
      print("")
      quit()    
    elif choice == 0:
      print "Bye Bye"
      os.system("clear")
      exit()
    elif choice == 4:
	  d3 = raw_input('Enter IP Address - IP Range Or Domain  : ')
	  os.system("clear")
	  print("""
 _____                            ____  _____ _____ 
| __  |___ _ _ ___ ___ ___ ___   |    \|   | |   __|
|    -| -_| | | -_|  _|_ -| -_|  |  |  | | | |__   |
|__|__|___|\_/|___|_| |___|___|  |____/|_|___|_____|
                                                    
	  """)
	  os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3 )
	  print("")
	  quit()
    elif choice == 5:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
   _____           _____ _____  
  / ____|         |_   _|  __ \ 
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/ 
 | |__| |  __| (_) _| |_| |     
  \_____|\___|\___|_____|_|     
                                	
	""")
	  os.system("curl http://api.hackertarget.com/geoip/?q=" + d3 )
	  print("")
	  print("")
	  quit()
    elif choice == 6:
      d3 = raw_input('Enter IP Or Domain : ')
      os.system("clear")
      print("""
     __                         __                 
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __  
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \ 
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|                         
      """)
      os.system("curl http://api.hackertarget.com/nmap/?q=" + d3 )
      print("")
      quit()
    elif choice == 7:
	  d3 = raw_input('Enter IP Or Domain : ')
	  os.system("clear")
	  print("""
 (   (      (                             
 )\ ))\ )   )\ )            )             
(()/(()/(  (()/(         ( /(   (         
 /(_)/(_))  /(_)) (   (  )\()) ))\ `  )   
(_))(_))   (_))   )\  )\((_)\ /((_)/(/(   
|_ _| _ \  | |   ((_)((_| |(_(_))(((_)_\  
 | ||  _/  | |__/ _ / _ | / /| || | '_ \) 
|___|_|    |____\___\___|_\_\ \_,_| .__/  
                                  |_|     
	  """)
	  os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  os.system("clear")
	  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3 )
	  print("")
	  print("\033[91m\033[1mFile Saved On : ")
	  os.system("pwd")
	  print("File : index.html?q=" +d3)
	  print("\033[0m")
	  quit()
  except(KeyboardInterrupt):
    print ""
select()
