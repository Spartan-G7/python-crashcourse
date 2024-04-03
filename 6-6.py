favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

name_lists = ['page','madison','jen','phil']

for name in favorite_languages:
    if name in name_lists:
        print('Please take our poll.')
    else:
        print('Thank you for responding')
