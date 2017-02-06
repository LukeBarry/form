{"changed":true,"filter":false,"title":"bartender.pirated.py","tooltip":"/bartender.pirated.py","value":"# Pirate Bartender Project\n\nquestions = {\n\n    'strong': 'Do ye like yer drinks strong?',\n    'salty': 'Do ye like it with a satly tang?',\n    'bitter': 'Are ye a lubber who likes it bitter?',\n    'sweet': 'Would ye like a bit of sweetness with yer poison?',\n    'fruity': 'Are ye one for a fruity finish?'\n}\n\ningredients = {\n    'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],\n    'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],\n    'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],\n    'sweet': ['sugar cube', 'spoonful of honey', 'splash of cola'],\n    'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']\n}\n\n\n# key -> value\n# ingredient -> amount\nstock = {}\n\ndef stock_all():\n    for taste in ingredients.values():\n        for ingred in taste:\n            stock[ingred] = 10\n\ndef preferences():\n    answers = {}\n    for question in questions:\n        answer = raw_input(questions[question])\n        if answer == 'y' or answer == 'yes':\n            answers[question] = True\n        else:\n            answers[question] = False\n    return answers\n\ndef name():\n    adjectives = ['Salty', 'Fluffy', 'Sappy', 'Crispy', 'Groggy']\n    nouns = ['Seahorse', 'Log', 'Giraffe']\n    drinkname = str(random.choice(adjectives)) + ' ' + str(random.choice(nouns))\n    return drinkname\n\ndef drink(tastes): # tastes should be a dictionary of preferences\n    contents = []\n    for taste in tastes:\n        if tastes[taste] == True:\n            ingredient = random.choice(ingredients[taste])\n            if not stock[ingredient] == 0:\n                contents.append(ingredient)\n                stock[ingredient] -= 1\n            if stock[ingredient] < 3:\n                restock = raw_input(ingredient, 'low! Do you want to restock?')\n                if restock == 'y' or restock == 'yes':\n                    stock[ingredient] = 10\n    return contents\n\nif __name__ == '__main__':\n    stock_all()\n    customers = {}\n    customer = raw_input('What is your name?')\n    while True:\n        if customer == 'quit':\n            break\n        elif customer in customers:\n            answers = customers[customer]\n        else:\n            customers[customer] = preferences() \n\t    answers = customers[customer]\n        while True:\n            print 'Ah, the', name()\n            print drink(answers)\n            cont = raw_input('Would you like another drink?')\n            if not (cont == 'y' or cont == 'yes'):\n                break\n\tcustomer = raw_input('Next customer! What is your name? Type \\\"quit\\\" to exit.')\n\t\n\nanswers = {}\n\ndef preferences():\n  for question in questions:\n    answer = raw_input(questions[question])\n    if answer == 'y' or answer == 'yes':\n      answers[question] = True\n    else:\n      answers[question] = False\n  return answers\n\ndef drink(dictionary):\n  contents = []\n  for i in dictionary:\n    if dictionary[i] == True:\n      ingredient = random.choice(ingredients[i])\n      contents.append(ingredient)\n  return contents\n\nif __name__ == '__main__':\n  preferences()\n  print drink(answers)\n","undoManager":{"mark":0,"position":15,"stack":[[{"start":{"row":0,"column":0},"end":{"row":117,"column":48},"action":"insert","lines":["# Pirate Bartender Project","import random","","questions = {","<<<<<<< HEAD","    'strong': 'Do ye like yer drinks strong?',","    'salty': 'Do ye like it with a satly tang?',","    'bitter': 'Are ye a lubber who likes it bitter?',","    'sweet': 'Would ye like a bit of sweetness with yer poison?',","    'fruity': 'Are ye one for a fruity finish?'","}","","ingredients = {","    'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],","    'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],","    'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],","    'sweet': ['sugar cube', 'spoonful of honey', 'splash of cola'],","    'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']","}","","","# key -> value","# ingredient -> amount","stock = {}","","def stock_all():","    for taste in ingredients.values():","        for ingred in taste:","            stock[ingred] = 10","","def preferences():","    answers = {}","    for question in questions:","        answer = raw_input(questions[question])","        if answer == 'y' or answer == 'yes':","            answers[question] = True","        else:","            answers[question] = False","    return answers","","def name():","    adjectives = ['Salty', 'Fluffy', 'Sappy', 'Crispy', 'Groggy']","    nouns = ['Seahorse', 'Log', 'Giraffe']","    drinkname = str(random.choice(adjectives)) + ' ' + str(random.choice(nouns))","    return drinkname","","def drink(tastes): # tastes should be a dictionary of preferences","    contents = []","    for taste in tastes:","        if tastes[taste] == True:","            ingredient = random.choice(ingredients[taste])","            if not stock[ingredient] == 0:","                contents.append(ingredient)","                stock[ingredient] -= 1","            if stock[ingredient] < 3:","                restock = raw_input(ingredient, 'low! Do you want to restock?')","                if restock == 'y' or restock == 'yes':","                    stock[ingredient] = 10","    return contents","","if __name__ == '__main__':","    stock_all()","    customers = {}","    customer = raw_input('What is your name?')","    while True:","        if customer == 'quit':","            break","        elif customer in customers:","            answers = customers[customer]","        else:","            customers[customer] = preferences() ","\t    answers = customers[customer]","        while True:","            print 'Ah, the', name()","            print drink(answers)","            cont = raw_input('Would you like another drink?')","            if not (cont == 'y' or cont == 'yes'):","                break","\tcustomer = raw_input('Next customer! What is your name? Type \\\"quit\\\" to exit.')","=======","  'strong': 'Do ye like yer drinks strong?',","  'salty': 'Do ye like it with a satly tang?',","  'bitter': 'Are ye a lubber who likes it bitter?',","  'sweet': 'Would ye like a bit of sweetness with yer poison?',","  'fruity': 'Are ye one for a fruity finish?'","}","","ingredients = {","  'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],","  'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],","  'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],","  'sweet': ['sugar cube', 'spoonful of honey', 'splash of cola'],","  'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']","}","","answers = {}","","def preferences():","  for question in questions:","    answer = raw_input(questions[question])","    if answer == 'y' or answer == 'yes':","      answers[question] = True","    else:","      answers[question] = False","  return answers","","def drink(dictionary):","  contents = []","  for i in dictionary:","    if dictionary[i] == True:","      ingredient = random.choice(ingredients[i])","      contents.append(ingredient)","  return contents","","if __name__ == '__main__':","  preferences()","  print drink(answers)",">>>>>>> e36793b48ac6f563cb47ca5e6134ef0bb52468c0"],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":13},"action":"remove","lines":["import random"],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":3}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":12},"action":"remove","lines":["<<<<<<< HEAD"],"id":4}],[{"start":{"row":78,"column":6},"end":{"row":78,"column":7},"action":"remove","lines":["="],"id":5}],[{"start":{"row":78,"column":5},"end":{"row":78,"column":6},"action":"remove","lines":["="],"id":6}],[{"start":{"row":78,"column":4},"end":{"row":78,"column":5},"action":"remove","lines":["="],"id":7}],[{"start":{"row":78,"column":3},"end":{"row":78,"column":4},"action":"remove","lines":["="],"id":8}],[{"start":{"row":78,"column":2},"end":{"row":78,"column":3},"action":"remove","lines":["="],"id":9}],[{"start":{"row":78,"column":1},"end":{"row":78,"column":2},"action":"remove","lines":["="],"id":10}],[{"start":{"row":78,"column":0},"end":{"row":78,"column":1},"action":"remove","lines":["="],"id":11}],[{"start":{"row":77,"column":81},"end":{"row":78,"column":0},"action":"remove","lines":["",""],"id":12}],[{"start":{"row":77,"column":81},"end":{"row":78,"column":0},"action":"insert","lines":["",""],"id":13},{"start":{"row":78,"column":0},"end":{"row":78,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":79,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["  'strong': 'Do ye like yer drinks strong?',","  'salty': 'Do ye like it with a satly tang?',","  'bitter': 'Are ye a lubber who likes it bitter?',","  'sweet': 'Would ye like a bit of sweetness with yer poison?',","  'fruity': 'Are ye one for a fruity finish?'","}","","ingredients = {","  'strong': ['glug of rum', 'slug of whisky', 'splash of gin'],","  'salty': ['olive on a stick', 'salt-dusted rim', 'rasher of bacon'],","  'bitter': ['shake of bitters', 'splash of tonic', 'twist of lemon peel'],","  'sweet': ['sugar cube', 'spoonful of honey', 'splash of cola'],","  'fruity': ['slice of orange', 'dash of cassis', 'cherry on top']","}"],"id":14}],[{"start":{"row":79,"column":0},"end":{"row":80,"column":0},"action":"remove","lines":["",""],"id":15}],[{"start":{"row":102,"column":0},"end":{"row":102,"column":48},"action":"remove","lines":[">>>>>>> e36793b48ac6f563cb47ca5e6134ef0bb52468c0"],"id":16}]]},"ace":{"folds":[],"scrolltop":780,"scrollleft":0,"selection":{"start":{"row":102,"column":0},"end":{"row":102,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":54,"state":"start","mode":"ace/mode/python"}},"timestamp":1470009953296}