#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import requests
import json

# DEBUG_MODE
# 0 NO DEBUG
# 1 STD OUTPUT ONLY
# 2 BOTH BOT + STD OUTPUT

# Set up environment variables and constants. Do not modify this unless you know what you are doing!
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/797638558093017169/NkL-dl3Zb2v0hT8G_hc4-KrKH-ZWaNz713X_iCqqjbYR7EW8ANMNtLNFC7dz76LeQ-Fn'

def discord_notification(product):
    data = {
        "content": "{}".format(product),
        "username": "RisiboTX"
    }
    result = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

def alert(args, debug_mode = 1):
    if (debug_mode != 1):
        discord_notification(args)
    if (debug_mode != 0):
        print(args)
    sleep(1)

def alerte_ban_ip():
    print("Ban \033[31mip\033[0m ou timeout... désolé!")
    exit()
