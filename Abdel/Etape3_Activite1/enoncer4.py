# Fonction repertoire/phone ==> dictionnaire =  variable locale/globale
def phone_number(phone_directory, char="A"):
    find_number_A = [x + ' : ' + phone_directory[x] for x in phone_directory if x[0] == char]
    print(f'le num de tel commençant par la lettre A est : {find_number_A}')


directory = {'Claire': '0612345678', 'Maman': '0601020304', 'Mamie': '0709080706', 'Vivien': '0712326545',
             'Angèle': '0102030405'}
phone_number(directory)
