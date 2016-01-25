#import os
#import re
#from collections import Counter
#from html.parser import HTMLParser
#from urllib import request
import json
import requests
from texttable import Texttable
import RuneInfo
 
def championGGrequest(Champion,API,type):
	api_args = {'api_key' : 'API'}
	URL = 'http://api.champion.gg/champion/' + Champion + '/runes/' + type
	r = requests.get(URL, params=api_args)
	status = r.status
	if (status = 404)
		print("No Champion Found")
	if (status = 200)
		r.json()
		return r[0]['runes']
		
	

def createTableValues(Champion):
	for i in range(len(Champion)):
		name = Champion[i]['name']
		number = Champion[i]['number']
		description = Champion[i]['description']
		cost = RuneCost[findType1(name)][findType2(name)][name]
		acc_cost = cost * number
		
		runes_names.append(name)
		runes_numbers.append(number)
		runes_description.append(description)
		individual_costs.append(cost)
		accumulated_costs.append(acc_cost)
	
		t.add_rows([name,number,description,cost,acc_cost])		

def findType1(name):
	runeType1 = ['Quintessence','Glyph','Mark','Seal']
	for word in runeType1:
		if word in name:
			return word

def findType2(name):
	for word in listOffensive:
		if word in name:
			return 'Offensive'	
	for word in listDefensive
		if word in name:
			return 'Defensive'
	for word in listUtility
		if word in name:
			return 'Utility'
			
if __name__ == "__main__":
	rune_names = []
	rune_numbers = []
	rune_description = []
	individual_costs = []
	acculumated_costs = []
	URL = ''
	status = 0
	t = Texttable()
	t.add_rows(['Name','#','Description','Cost (IP)','Accumulated Cost (IP)'])
	
	Caitlyn = [{"games":2015,"winPercent":49.67,"runes":[{"id":5245,"name":"Greater Mark of Attack Damage","description":"+0.95 attack damage","number":9},{"id":5289,"name":"Greater Glyph of Magic Resist","description":"+1.34 magic resist","number":9},{"id":5317,"name":"Greater Seal of Armor","description":"+1 armor","number":9},{"id":5337,"name":"Greater Quintessence of Attack Speed","description":"+4.5% attack speed","number":3}],"role":"ADC"}]

	Champion = Caitlyn[0]['runes']
#	Champion = championGGrequest
	
	createTableValues(Champion)

	total_cost = sum(accumulated_costs)
	
	print(t.draw())
	print("\nTotal IP: " + total_cost)
