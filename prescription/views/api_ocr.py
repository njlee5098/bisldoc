import requests
import uuid
import time
import base64
import json


def ocr_api(img_path):
    api_url = 'https://8b46200444744ddc8389158320fe9a85.apigw.ntruss.com/custom/v1/5694/2983c06b7741589b81e041e84d251e377073b9ba7cf2dd6a7f010aad998eb5b4/infer'
    secret_key = 'eUtxTFV3TXBRalNBQUdQcE1JQWVHamlpUmxFQnF5bFM='
    # image_url = img_url
    image_file = img_path
    with open(image_file,'rb') as f:
        file_data = f.read()

    request_json = {
        'images': [
            {
                'format': 'jpg',
                'name': 'demo',
                'data': base64.b64encode(file_data).decode()
                # 'url': image_url
            }
        ],
        'requestId': str(uuid.uuid4()),
        'version': 'V2',
        'timestamp': int(round(time.time() * 1000))
    }

    payload = json.dumps(request_json).encode('UTF-8')
    headers = {
      'X-OCR-SECRET': secret_key,
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", api_url, headers=headers, data = payload)

    print(response.text)

    return response.json()

#%%

