from django.shortcuts import render
import json

def family_list(request, x):
    with open('../animal.json', 'r') as f:
        animal = json.load(f)
    animal_list = [animal[a]["name"] for a in animal.keys() if animal[a]["family"] == x]
    return render(request,'info/family.html', context = {'family': animal_list})


def animal(request, x):
    with open('../animal.json', 'r') as f:
        animal = json.load(f)
    with open('../family.json', 'r') as f:
        family = json.load(f)
    pick = {"info": animal[x], "name": family[animal[x]["family"]]["name"]}   
    return render(request, 'info/animal.html', pick)

    

