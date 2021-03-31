def print_info(name, *, gender, city='Beijing', age):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


print_info('Bob', gender='male', age=20)
print_info('Lisa', gender='female', city='Shanghai', age=18)
