import requests
import json


url = 'https://rest.fra-02.braze.eu/messages/send'

api_key = ''

# Gönderilecek veri
data = {
    "api_key": api_key,
    "messages": {
        "en": "Denemeeee :) EBS"
    },
    "audience": {
        "segment": "test_segment"
    }
}

# JSON formatında POST isteği gönderme
response = requests.post(url, json=data)

# Yanıtı yazdırma
print(response.status_code)
print(response.json())
