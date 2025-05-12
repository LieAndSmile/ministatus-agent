#!/usr/bin/env python3

import os
import socket
import shutil
import subprocess
import requests
from dotenv import load_dotenv
from datetime import datetime

# Load environment config
load_dotenv()

API_URL = os.getenv("MINISTATUS_URL")
API_KEY = os.getenv("MINISTATUS_KEY")
SERVICE_NAME = os.getenv("MINISTATUS_NAME", socket.gethostname())

def get_uptime():
    return subprocess.check_output("uptime -p", shell=True).decode().strip()

def get_load_avg():
    return os.getloadavg()[0]

def get_disk_free():
    total, used, free = shutil.disk_usage("/")
    return f"{free // (2**30)} GB free"

def send_report():
    if not API_URL or not API_KEY:
        print("[ERROR] Missing MINISTATUS_URL or MINISTATUS_KEY in .env")
        return

    description = f"{get_uptime()}, Load: {get_load_avg():.2f}, Disk: {get_disk_free()}"

    payload = {
        "name": SERVICE_NAME,
        "status": "up",
        "description": description
    }

    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=5)
        if response.ok:
            print(f"[{datetime.now()}] Report sent for {SERVICE_NAME}: {response.json().get('message')}")
        else:
            print(f"[{datetime.now()}] Failed to report: {response.status_code} {response.text}")
    except Exception as e:
        print(f"[{datetime.now()}] Exception during report: {e}")

if __name__ == "__main__":
    send_report()

