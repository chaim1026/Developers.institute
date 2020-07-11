"""num_list = [
    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7],
    [44, 9, 8, 24, -6, 0, 56, 8, 100, 2], 
    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76], 
    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
]

first_last = []
for lists in num_list:
    print(lists)
    lists.sort(reverse=True)
    print(lists)
    total = sum(lists)
    print(total)
    first = lists[0]
    last = lists[-1]
    first_last.append(first) 
    first_last.append(last)
    print(first_last)"""

"""
import re

interesting_paragraph = "The National Football League NFl is a professional American football league consisting of 32 teams, divided equally between the National Football Conference NFC and the American Football Conference AFC. The NFL is one of the four major professional sports leagues in North America, the highest professional level of American football in the world, the wealthiest professional sport league by revenue, and the sport league with the most valuable teams. The NFL's 17-week regular season runs from early September to late December, with each team playing 16 games and having one bye week. Following the conclusion of the regular season, seven teams from each conference four division winners and three wild card teams advance to the playoffs, a single-elimination tournament culminating in the Super Bowl, which is usually held on the first Sunday in February and is played between the champions of the NFC and AFC."
new_interesting_paragraph = interesting_paragraph.replace(" ", "") 
length = len(new_interesting_paragraph)
list_of_sentences = new_interesting_paragraph.split(".")
num_of_sentences = len(list_of_sentences) - 1
list_of_words = interesting_paragraph.split(" ")
length_list_of_words = len(list_of_words)
unique_words = set(list_of_words)
print(unique_words)"""



"""duplacate_words = {}
i = 1
input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
input_list = input.split(" ")
for word in input_list:
    appears = input_list.count(word)
    duplacate_words[word] = appears
print(duplacate_words)"""

"""duplacate_words = {}

input = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
input_list = input.split(" ")
for word in input_list:
    if word in duplacate_words:
        duplacate_words[word] = duplacate_words[word] + 1
    else:
         duplacate_words[word] = 1
print(duplacate_words)"""



#exercize 5


"""numbers = input("please enter a group of numbers seperated by commas:\n")
number_list = numbers.split(",")
number_set = set(number_list)
number_tuple = tuple(number_list)
print(number_set)
print(number_tuple)
print(number_list)"""


import math
C = 50
H = 30
nums = input("enter numbers seperated by commas:\n")
list_D = nums.split(",")
new_list = []
for number in list_D:
    D = int(number)
    Q = int(math.sqrt((2 * C * D)/H))
    Q = str(Q)
    new_list += [Q]
final = ",".join(new_list)
print(final)