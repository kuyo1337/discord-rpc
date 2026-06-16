import platform
import locale
import base64
import json
import time

start_time = time.time()

def getxsuper():
    payload = {
        "os": platform.system(),
        "browser": "Discord Client",
        "system_locale": locale.getlocale()[0] or "en-US"
    }
    return base64.b64encode(json.dumps(payload).encode()).decode()
