import psutil
from pypresence import Presence 
import time
import threading

client_id = "1051036569261318216" # ID вашего приложения в Discord
RPC = Presence(client_id)
RPC.connect()

javaw_running = False
start_time = None

def update_presence():
    while True:
        if javaw_running:
            RPC.update(
                large_image="new",  # name of your asset
                large_text="This Logo NewEra",
                details="loading...",
                state="Play for NewEra",
                start=start_time,
                buttons=[
                    {"label": "Map NewEra", "url": "https://newera.asvdev.com/map.php"},
                    {"label": "Discord", "url": "https://discord.gg/zHMFEkAFfB"},
                ],  # up to 2 buttons
            )
        else:
            RPC.clear()
        time.sleep(10)

t = threading.Thread(target=update_presence)
t.start()

while True:
    for proc in psutil.process_iter():
        name = proc.name()
        if name == "javaw.exe":
            if not javaw_running:
                start_time = time.time()
                javaw_running = True
            break
    else:
        if javaw_running:
            javaw_running = False
            start_time = None
        time.sleep(10)
        continue

    if not psutil.pid_exists(proc.pid):
        if javaw_running:
            javaw_running = False
            start_time = None
        time.sleep(10)
        continue
    time.sleep(1)
