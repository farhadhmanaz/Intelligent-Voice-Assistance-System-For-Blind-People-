import subprocess
subprocess.run("python3 audio.py & python3 tfdet.py & python3 gps_sms.py &", shell=True)
