# Once everyone has contributed their name, this file can be used to print out a list
# of members of COMP491

def print_names():
    names = ['John MacCormick',
             'fake student 1',
             'fake instructor 1',
             'fake student 2', 'Aaron Stern']
    print('Here are COMP491 members in alphabetical order:')
    sorted_names = sorted(names)
    for name in sorted_names:
        print(name)
    print('Good luck to everyone for a great semester!')


print_names()