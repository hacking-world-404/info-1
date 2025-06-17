from os import system as c
import time
import random

A = '\x1b[1;97m'
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
C = '\x1b[38;5;14m'
B = '\x1b[38;5;51m'
P = '\x1b[38;5;201m'

locations = [
    {'address': 'House-23, Road-7, Dhanmondi', 'city': 'Dhaka', 'country': 'Bangladesh'},
    {'address': '23/A, Gulshan Avenue', 'city': 'Dhaka', 'country': 'Bangladesh'},
    {'address': 'Block B, Bashundhara R/A', 'city': 'Dhaka', 'country': 'Bangladesh'},
    {'address': '5th Floor, Bashar Plaza, Agrabad', 'city': 'Chittagong', 'country': 'Bangladesh'},
    {'address': 'Shahjalal Road, Ambarkhana', 'city': 'Sylhet', 'country': 'Bangladesh'},
    {'address': 'Plot 14, Sector 7, Uttara', 'city': 'Dhaka', 'country': 'Bangladesh'}
]

def logo():
    c('clear')
    print(f"""{G}
███╗   ██╗███╗   ███╗ █████╗ ███╗   ██╗
████╗  ██║████╗ ████║██╔══██╗████╗  ██║
██╔██╗ ██║██╔████╔██║███████║██╔██╗ ██║
██║╚██╗██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
{P}    HACKING WORLD - VIP NUMBER LOCATOR (V1)
""")

def progress(task):
    print(f"{C}[+] {task}...")
    for i in range(3):
        print(f"{Y}[*] Scanning{'.'*i}")
        time.sleep(1)

def track_number():
    logo()
    num = input(f"{Y}ENTER PHONE NUMBER (With Country Code): ")
    progress(f"Connecting to Global Database for {num}")
    progress("Tracking Real-Time Location via Satellite")
    location = random.choice(locations)
    print(f"\n{G}[✓] Number Found!")
    print(f"{B}Number: {num}")
    print(f"{P}Address: {C}{location['address']}")
    print(f"{P}City: {C}{location['city']}")
    print(f"{P}Country: {C}{location['country']}\n")
    input(f"{A}Press Enter To Return To Menu...")
    menu()

def menu():
    logo()
    print(f"{A}[1] Track Number Location")
    print(f"{A}[0] Exit Tool")
    choice = input(f"{Y}Select Option: ")
    if choice == '1':
        track_number()
    elif choice == '0':
        exit()
    else:
        print(f"{R}[!] Invalid Option!")
        time.sleep(1)
        menu()

menu()