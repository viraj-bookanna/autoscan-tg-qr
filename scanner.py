import pyautogui, base64, logging, os, sys, time
from pyzbar.pyzbar import decode
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.auth import AcceptLoginTokenRequest
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
load_dotenv(override=True)

API_ID = os.getenv('TG_API_ID')
API_HASH = os.getenv('TG_API_HASH')
SESSION_STRING = input('SESSION_STRING: ')

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
client.connect()
if not client.is_user_authorized():
    print('session invalid')
    client.disconnect()
    sys.exit()
token = None
while True:
    data = decode(pyautogui.screenshot())
    for code in data:
        auth_url = code.data.decode()
        if "tg://login" in auth_url:
            token = base64.urlsafe_b64decode(auth_url.split('token=')[1])
            break
    if token is not None:
        break
    time.sleep(2)
result = client(AcceptLoginTokenRequest(token=token))
client.disconnect()
print(result.stringify())