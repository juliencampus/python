notes = [12.5, 13.6, 18.4, 9.7]
coefficients = [2, 3, 5, 4]

notes_par_coeff = [note * coefficients[i] for i, note in enumerate(notes)]

print(round((sum(notes_par_coeff)/sum(coefficients)),2))