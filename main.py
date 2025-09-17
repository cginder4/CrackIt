from aircrackFunctions import get_password, start_monitor, end_monitor, recon_scan, capture_n_deauth, attempt_crack

menu = ["========CrackIt========", "1. Turn on monitor mode", "2. Scan for networks", "3. Deauth and capture", "4. Attempt crack", "5. Turn off monitor mode", "6. Exit"]
pw = get_password()
interface = input("Enter interface name: ")
while True:
    for choices in menu:
        print(choices)
    option = str(input("Welcome to CrackIt!\nPlease choose: "))
    if option == "1":
        print("Starting monitor mode...")
        start_monitor(pw)
    elif option == "2":
        print("Scanning for networks...")
        recon_scan(pw, interface, duration=30)
    elif option == "3":
        network = input(str("Enter target BSSID: "))
        channel = input(str("Enter target channel: "))
        capture_n_deauth(network, channel, interface)
    elif option == "4":
        target = input("Reenter target BSSID: ")
        wordlist = input("Input wordlist filename: ")
        attempt_crack(target, wordlist)
    elif option == "5":
        print("Turning off monitor mode...")
        end_monitor(pw)
    elif option == "6":
        break
    else:
        print("Invalid option, please try again")
        continue