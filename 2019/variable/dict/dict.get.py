# coding=utf-8
# Syntax:
#     dict.get(k[, d])
# Usage:
#     D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.

person = {
    'name': 'linda',
    'gender': 'female',
    'work': 'Apple',
    'site': 'California'
}

print('person = \n{}'.format(person))
print("person.get('name', 'ernie') = \n{}".format(person.get('name',
                                                             'ernie')))  # linda
print("person.get('age', 25) =\n {}".format(person.get('age', 25)))  # 25
print('person = \n{}'.format(person))
