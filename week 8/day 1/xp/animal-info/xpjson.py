import json

animal = {
    '1': {'name': 'dog',
              'legs': 4,
              'weight': 15,
              'height': 12,
              'speed': 25,
              'family': 'bunnies'
    },
    '2':{
            'name': 'snake',
            'legs' : 0,
            'weight' : 20,
            'height' : 50,
            'speed' : 45,
            'family' : 'snakes'
    }
}


family = {
    '1':{
        'name': 'mammal'
    },
    '2':{
        'id': 2,
        'name': 'reptile'
    }
}

with open('animal.json', 'w') as f:
    json.dump(animal, f)

with open('family.json', 'w') as f2:
    json.dump(family, f2)



