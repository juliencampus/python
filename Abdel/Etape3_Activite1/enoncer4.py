def phone_number(phone_directory, char="a"):
    find_number_A = [x + ' : ' + phone_directory[x] for x in phone_directory if x[0] == char]
    print(f'Le numero de tel. qui commence par la lettre {char} est : {find_number_A}')


directory = {'Abdel': '0612345678',
             'Vivi': '0601020304',
             'Ben': '0709080706',
             'Clem': '0712326545',
             'Mlo': '0102030405'}
phone_number(directory)
