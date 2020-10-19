import requests
# compter le nombre d'image dans une page HTML
r = requests.get("https://validator.w3.org/")
print(r.text.count("<img"))
