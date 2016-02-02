import json
import requests
import RuneInfo
from prettytable import PrettyTable

# Type your API here in quotes
API = ''

# Method to send request to Champion.gg
def championGGrequest(Champion,choice):
    type = ''
    if choice == 0:
        type = 'mostPopular'
    if choice == 1:
        type = 'mostWins'
    api_args = {'api_key' : API}
    URL = 'http://api.champion.gg/champion/' + Champion + '/runes/' + type
    r = requests.get(URL, params=api_args)
    if r.status_code == 404:
        print('Invalid Input')
        raise SystemExit
    if r.status_code == 200:
        r.json()
        return r.json()[0]['runes']
    elif (r.json()['error'] == 'ChampionNotFound'):
        print('Champion not found')
        raise SystemExit

# Adds a row to PrettyTable for each rune
def createTableValues(Champion):
    for i in range(len(Champion)):
        name = Champion[i]['name']
        number = Champion[i]['number']
        description = Champion[i]['description']
        cost = RuneInfo.RuneCost[findType1(name)][findType2(name)][name]
        acc_cost = cost * number
		
        rune_names.append(name)
        rune_numbers.append(number)
        rune_description.append(description)
        individual_costs.append(cost)
        accumulated_costs.append(acc_cost)
	
        t.add_row([name,number,description,cost,acc_cost])		

# Searches name of rune to find first keyword
def findType1(name):
    runeType1 = ['Quintessence','Glyph','Mark','Seal']
    for word in runeType1:
        if word in name:
            return word

# Searches name of rune to find second keyword
def findType2(name):
    for word in RuneInfo.listOffensive:
        if word in name:
            return 'Offensive'	
    for word in RuneInfo.listDefensive:
        if word in name:
            return 'Defensive'
    for word in RuneInfo.listUtility:
        if word in name:
            return 'Utility'
			
if __name__ == "__main__":
    rune_names = []
    rune_numbers = []
    rune_description = []
    individual_costs = []
    accumulated_costs = []
    URL = ''
    status = 0
    t = PrettyTable(['Name','#','Description','Cost (IP)','Accumulated Cost (IP)'])

    print('Type name of champion')

    name = input()
    name.lower().capitalize()
	
    print('Input 0 for Most Popular')
    print('Input 1 for Most Wins')

    choice = input()

    Champion = championGGrequest(name,int(choice))
	
    createTableValues(Champion)

    total_cost = sum(accumulated_costs)
	
    print(t)
    print('{}{}'.format('\nTotal IP: ', total_cost))
