import requests
import datetime
import time

starttime=time.time()

while True:

    # your Steam API key
    API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    # user's Steam ID 64 - only works on friends
    user = "76561197960435530"

    # path to the file you wish for the logs to be written to
    logfile = "path/to/file"

    apiurl = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={}&steamids={}".format(API_KEY, user)

    r = requests.get(apiurl)

    json = r.json()

    personastate = json["response"]["players"][0]["personastate"]

    now = datetime.datetime.now().strftime("%Y-%m-%d %#I:%M:%S %p")

    log = open("{}".format(logfile), "a")

    if  personastate == 0:
        log.write(str(now) + " - Offline" + "\n")
    elif personastate == 1:
        log.write(str(now) + " - Online" + "\n")
    elif personastate == 3:
        log.write(str(now) + " - Away" + "\n")
        log.close()

    # loop time in seconds
    time.sleep(900 - ((time.time() - starttime) % 900))