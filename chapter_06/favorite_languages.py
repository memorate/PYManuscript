favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

check_list = {"jen": 1, "sarah": 2, "edward": 3, "phil": 4, "mark": 5, "blight": 6}
for name in sorted(check_list.keys()):
    if name in favorite_languages.keys():
        print(name.title() + "'s favorite language is " + favorite_languages[name].title() + ".")
    else:
        print(name.title() + ", you should take the poll!")
