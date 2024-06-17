import requests

TOKEN = '7130288254:AAE4VjerfC21vlLFl6jP5PXjAKXPODwsuaU'
WEBHOOK_URL = 'https://uh0hhp.onrender.com/webhook'

def set_webhook():
    url = f"https://api.telegram.org/bot{7130288254:AAE4VjerfC21vlLFl6jP5PXjAKXPODwsuaU}/setWebhook"
    data = {"url": WEBHOOK_URL}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print("Webhook set successfully")
    else:
        print("Failed to set webhook", response.text)

if __name__ == '__main__':
    set_webhook()
