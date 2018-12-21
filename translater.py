from urllib import parse
import re
import urllib.request


def check_lang(source_text):
    if re.search(r'[^\x00-\x7F]', source_text):
        return 'ja'
    else:
        return 'en'


def translate(source_text, source_lang='', target_lang=''):
    if source_lang == '':
        source_lang = check_lang(source_text)
    if target_lang == '':
        target_lang = 'en' if source_lang == 'ja' else 'ja'
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl="\
        + source_lang + "&tl=" + target_lang + "&dt=t&q=" + parse.quote(source_text)
    headers = {"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"}
    req = urllib.request.Request(url, None, headers)
    with urllib.request.urlopen(req) as res:
        # print(res.read().decode('utf-8'))
        return re.sub(r'[b\'\[\]\"]', '', str(res.read().decode('utf-8')).split(',')[0])


if __name__ == '__main__':
    print(translate('hello'))
    print(translate('hello', target_lang='de'))
    print(translate('hello', target_lang='ko'))
