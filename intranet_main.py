import subprocess
import time

while True:

    subprocess.Popen("py C:\\boleta\\folios.py", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    subprocess.Popen("py C:\\boleta\\biller.py", stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    time.sleep(3600) #Wait 600s (10 min) before re-entering the cycle
