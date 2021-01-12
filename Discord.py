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
Serveur_Panda = 'https://discord.com/api/webhooks/797638558093017169/NkL-dl3Zb2v0hT8G_hc4-KrKH-ZWaNz713X_iCqqjbYR7EW8ANMNtLNFC7dz76LeQ-Fn'
TeaParty = "https://discord.com/api/webhooks/798686087672758292/vq01IiQ1e2T87BfbMfWbyj5z6dup7iYfQGP7qZM841NVyo4N9-mI44jgkRxQGFwSJqmi"

def discord_notification(product):
    data = {
        "content": "{}".format(product),
        "username": "TARS"
    }
    result = requests.post(TeaParty, data=json.dumps(data), headers={"Content-Type": "application/json"})
    result = requests.post(Serveur_Panda, data=json.dumps(data), headers={"Content-Type": "application/json"})
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

def alert(args, debug_mode = 2):
    if (debug_mode != 1):
        discord_notification(args)
    if (debug_mode != 0):
        print(args)
