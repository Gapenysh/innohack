
import json

import requests


def proccess_lama(prompt, reviews):
    url = "https://vk-scoreworker-case.olymp.innopolis.university/generate"
    data = {
        "prompt": [prompt],
        "apply_chat_template": True,
        "system_prompt": "Вы полезный помощник.",
        "max_tokens": 500,
        "n": 1,
        "temperature": 0.7
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(url, data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code} - {response.text}"
