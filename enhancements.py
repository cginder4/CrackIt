import subprocess

def monitor_check():
    cmd = ["iwconfig"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if "Mode:Monitor" in proc.stdout:
        return True
    else:
        return False


