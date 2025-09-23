from aircrackFunctions import get_password, start_monitor, end_monitor, recon_scan, capture_n_deauth, attempt_crack
from enhancements import monitor_check
import sys

menu1 = ["========CrackIt========", "1. Turn on monitor mode", "2. Scan for networks", "3. Deauth and capture", "4. Attempt crack", "5. Exit"]
menu2 = ["========CrackIt========", "1. Turn off monitor mode", "2. Scan for networks", "3. Deauth and capture", "4. Attempt crack", "5. Exit"]
pw = get_password()
interface = input("Enter your standard monitor mode interface name: ")
while True:
    monitor_on = monitor_check()
    if not monitor_on:
        while True:
            for choices in menu1:
                print(choices)
            option = str(input("Welcome to CrackIt!\nPlease choose: "))
            if option == "1":
                print("Starting monitor mode...")
                start_monitor(pw)
                print("\n")
                break
            elif option == "2":
                print("Scanning for networks...")
                recon_scan(pw, interface, duration=30)
                print("\n")
            elif option == "3":
                network = input(str("Enter target BSSID: "))
                channel = input(str("Enter target channel: "))
                capture_n_deauth(network, channel, interface)
                print("\n")
            elif option == "4":
                target = input("Reenter target BSSID: ")
                wordlist = input("Input wordlist filename: ")
                attempt_crack(target, wordlist)
                print("\n")
            elif option == "5":
                sys.exit(0)
            else:
                print("Invalid option, please try again.")
                print("\n")
                continue
    elif monitor_on:
        while True:
            for choices in menu2:
                print(choices)
            option = str(input("Welcome to CrackIt!\nPlease choose: "))
            if option == "1":
                print("Turning off monitor mode...\n")
                end_monitor(pw, interface)
                print("\n")
                break
            elif option == "2":
                print("Scanning for networks...")
                recon_scan(pw, interface, duration=30)
                print("\n")
            elif option == "3":
                network = input(str("Enter target BSSID: "))
                channel = input(str("Enter target channel: "))
                capture_n_deauth(network, channel, interface)
                print("\n")
            elif option == "4":
                target = input("Reenter target BSSID: ")
                wordlist = input("Input wordlist filename: ")
                attempt_crack(target, wordlist)
                print("\n")
            elif option == "5":
                sys.exit(0)
            else:
                print("Invalid option, please try again.\n")
                continue