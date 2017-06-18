import os, sys
import requests


def create_dir():
    if not os.path.exists("Target"):
        os.makedirs("Target")

def get_lang(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    params = {
        'key': key,
        'text': text
    }
    response = requests.get(url, params=params).json()
    return response

def append_name(filename):
    name, ext = os.path.splitext(filename)
    return "{name}_{type}{ext}".format(name=name, type="output", ext=ext)

def translate_it(source, target_lang="ru"):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    with open(source, "r") as f:
        text = f.read()
        source_lang = get_lang(text)["lang"]
        params = {
            'key': key,
            'lang': "{}-{}".format(source_lang, target_lang),
            'text': text
        }
        response = requests.get(url, params=params).json()
    create_dir()
    target = os.path.join("Target", append_name(source))
    with open(target, "w", encoding="UTF-8") as target_file:
        for item in response["text"]:
            target_file.write(item)

translate_it("DE.txt")
