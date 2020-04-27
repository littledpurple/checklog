#/bin/python
import os, time

# Logs list
# ['path/to/log.file', old time minutes]
logs = [
['/var/log/rsyslog/test.log', 180]
]
out = ""

for line in logs:
    now = time.time()
    old = now - line[1]*60
    fileCreation = os.path.getctime(line[0])
    fileName = os.path.basename(line[0])
    if fileCreation < old:
        if (not os.path.exists(fileName + ".fail")):
            os.mknod(fileName + ".fail")
            out = out + fileName + " is older than " + str(line[1]) + " minutes\                                                                                                                                                             n"
    else:
        if (os.path.exists(fileName + ".fail")):
            os.remove(fileName + ".fail")
            out = out + fileName + " is fresh now\n"

if out != "":
    print(out)
