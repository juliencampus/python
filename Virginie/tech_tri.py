from operator import itemgetter, attrgetter


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


student_objects = [
            Student('john', 'A', 15),
            Student('jane', 'B', 12),
            Student('dave', 'C', 10),
            Student('moi', 'D', 10),
            Student('ami', 'C', 12),
       ]
# liste trier avec la fonction sorted() ==> qui accepte n'importe quel litérable (string, float, int...)
# met1 = Tri sur des objets avec des attributs nommés.(selon l'âge)
met1 = sorted(student_objects, key=lambda student: student.age)
print(f'la liste des objets triés est : {met1}')
index1 = sorted(student_objects, key=attrgetter('grade', 'age'))
print(f'la liste triée selon grade, puis age est : {index1}')


student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'C', 10),
    ('moi', 'D', 10),
    ('ami', 'C', 12),
]

#met2 = Tri (selon l'age) En utilisant les fonctions itemgetter et attrgetter contenues dans le module operator
met2 = sorted(student_tuples, key=itemgetter(2))
print(f'la liste des tulpes triée, avec  itemgetter est : {met2}')


# Plusieurs niveaux de tri possibles.
index2 = sorted(student_tuples, key=itemgetter(1,2))
print(f'la liste triée selon le grade et age est : {index2}')
