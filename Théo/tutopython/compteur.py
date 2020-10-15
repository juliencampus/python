import requests

def compteur(url) -> int:
    return requests.get(url).text.count("<img")



print(compteur("https://www.google.com/search?q=chat&rlz=1C1GCEA_enFR879FR879&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiuzfu1h7bsAhVuZxUIHd9oBtwQ_AUoAXoECCcQAw&biw=1920&bih=969"))