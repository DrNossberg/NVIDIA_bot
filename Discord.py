#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import requests
import json

# DEBUG_MODE
# 0 NO DEBUG
# 1 STD OUTPUT ONLY
# 2 BOTH BOT + STD OUTPUT

# Set up environment variables and constants
# You have to set this one up, depending on your server ! 
Your_discord_server_webhook = "https://discord.com/api/webhooks/798686087672758292/vq01IiQ1e2T87BfbMfWbyj5z6dup7iYfQGP7qZM841NVyo4N9-mI44jgkRxQGFwSJqmi"

def discord_notification(product):
    data = {
        "content": "{}".format(product),
        "username": "TARS"
    }
    result = requests.post(Your_discord_server_webhook, data=json.dumps(data), headers={"Content-Type": "application/json"})
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
