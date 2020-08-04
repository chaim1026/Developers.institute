from django.shortcuts import render

people = [
  {
    'id': 1,
    'name': 'Bob Smith',
    'age': 35,
    'country': 'USA'
  },
  {
     'id': 2,
    'name': 'Martha Smith',
    'age': 60,
    'country': 'USA'
  },
  {
     'id': 3,
    'name': 'Fabio Alberto',
    'age': 18,
    'country': 'Italy'
  },
  {
     'id': 4,
    'name': 'Dietrich Stein',
    'age': 85,
    'country': 'Germany'
  }
]

sorted_people = sorted(people, key=lambda k: k['age'])

def all_people(request):
    sorted_people = sorted(people, key=lambda k: k['age'])
    return render(request, 'people_info/people.html', context = {'all': sorted_people})


def person_id(request, x):
    return render(request, 'people_info/person_id.html', context = {'person': people[x - 1]})