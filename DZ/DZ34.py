from random import choice
import json

def get_person():
    name = ''
    tel = ''
    letters = ['a', 'b', 'c', 'd', 'v', 'r']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    ID = ''
    while len(name) != 7:
        name += choice(letters)
    while len(tel) != 10:
        tel += choice(nums)
    while len(ID) < 12:
        ID += choice(nums)
    person = {ID:{
        'name': name,
        'phone_number': tel
    }}
    return person

def write_json(person_dict: dict):
    try:
        persons = json.load(open('person.json'))
    except FileNotFoundError:
        persons = {}
    persons.update(person_dict)
    with open('persons.json', 'w') as fw:
        json.dump(persons, fw, indent = 3)

for i in range(5):
    write_json(get_person())