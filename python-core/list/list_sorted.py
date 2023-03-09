"""
    Sort by length: list.sort(key=len) = sorted(list, key=len)
"""""


def sort_in_place():
    thelist = [1, 2, 0, -1, -3, 4]
    thelist.sort(reverse=True)
    print(thelist)


def sort_complex():
    thelist = [
        {"name": "Java", "year": 1991, "author": "James Gosling"},
        {"name": "Python", "year": 1991, "author": "Guido van Rossum"},
        {"name": "C", "year": 1972, "author": "Dennis Ritchie"},
        {"name": "C++", "year": 1985, "author": "Bjarne Stroustrup"},
    ]
    sorted_data = sorted(thelist, key=lambda x: (x['year'], x['name']))
    print(sorted_data)


# sort_in_place()
sort_complex()
