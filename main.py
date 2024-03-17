import time, threading, random, json, requests, os, httpx, itertools, colorama
from threading import RLock, Thread
from modules.console import Logger, Center
from modules.utils import FileManager
from concurrent.futures import ThreadPoolExecutor
from itertools import cycle
from user_agent import generate_user_agent
from sty import fg, bg, ef, rs
from datetime import datetime
from colorama import init, Fore, Style, Back
from colorama import init as colorama_init
from requests.adapters import HTTPAdapter

colorama_init(autoreset=True)

proxies = itertools.cycle(open("./data/proxies.txt", "r").read().replace(" "," ").splitlines())
data = itertools.cycle(open('./data/data.txt', 'r').read().replace(" "," ").splitlines())

session = requests.Session()
session.mount("", HTTPAdapter(max_retries=1))

isClaimed = None

def changeVanity(token, vanity, proxy, serverID):
    headers = {"Authorization": token, "User-Agent": generate_user_agent()}
    try:
        r =  session.patch(f"https://discord.com/api/v9/guilds/{serverID}/vanity-url", json={"code": vanity}, headers=headers, proxies={"https": proxy}, timeout=5)
        if r.status_code == 200:
            Logger.claimed += 1
            Logger.Print(f"        {fg.grey}{datetime.now().strftime('%H:%M:%S')}{fg.rs} {fg.li_green}Başarıyla Alındı{fg.rs} {fg.li_blue}discord.gg/{vanity}{fg.rs}")
            FileManager.removeLiveFromFile(vanity, "./data/vanity-url.txt")
        else:
            Logger.Print(f"        {fg.grey}{datetime.now().strftime('%H:%M:%S')}{fg.rs} {fg.li_red}URL Alınamadı{fg.rs} {fg.li_blue}discord.gg/{vanity}{fg.rs}")
            Logger.checked += 1
    except Exception:
        Logger.proxyError += 1

def checkVanity(vanity, proxy):
    r =  session.get(f"https://discord.com/api/v9/invites/{vanity}?with_counts=true&with_expiration=true", proxies={"https": proxy}, timeout=5)
    return r.status_code

def checkLoop():
    while True:
        try:
            if isClaimed:
                break

            vanity_url = next(data)
            vanity_code, server_id, token = vanity_url.split(':')
            proxy = next(proxies)

            response = checkVanity(vanity_code, proxy)
            if response == 404:
                changeVanity(token, vanity_code, proxy, server_id)
            elif response == 200:
                Logger.checked += 1
                Logger.Print(f"        {fg.grey}{datetime.now().strftime('%H:%M:%S')}{fg.rs} {fg.li_green}Kontrol Edildi{fg.rs} {fg.li_blue}discord.gg/{vanity_code}{fg.rs}")
            elif response == 429:
                Logger.proxyError += 1
            else:
                Logger.checked += 1
                Logger.Print(f"       {fg.grey}{datetime.now().strftime('%H:%M:%S')}{fg.rs} {fg.li_green}Kontrol Edildi{fg.rs} {fg.li_blue}discord.gg/{vanity_code}{fg.rs}")
        except Exception:
            Logger.proxyError += 1
            #Logger.Debug(err)

def title_thread():
    start_time = time.perf_counter()
    while True:
        time.sleep(0.1)
        elapsed_time = round(time.perf_counter() - start_time, 1)
        os.system(f'title URL Spammer | Checked: {Logger.checked} | Claimed: {Logger.claimed} | Proxy Error: {Logger.proxyError} | Elapsed: {elapsed_time}s'.replace('|', '^|'))

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    Logger.systemSize(130, 40)
    Logger.Print_Logo()
    os.system('title ')

    thread = threading.Thread(target=title_thread)
    thread.start()

    threads = [threading.Thread(target=checkLoop) for i in range(500)]
    for thread in threads:
        thread.start()