# Champion.gg Rune Sets

### Introduction
I made this as a resouce to calculate the IP cost to create a semi-competitive rune page for a specific champion. It first pulls information from Champion.gg's API, and saves the rune information into a table. Rune cost info can be hard to find and tedious to calculate, and so I created a module that uses nested dictionaries in order to search for the cost of the rune. All of the information is then formatted using PrettyTable, and prints directly into the command prompt

### Required Modules
The only module required that is not included in the default Python 3.5.1 installation is [prettytable](https://code.google.com/archive/p/prettytable/)

### Usage
To use, you first need to type your Champion.gg API key into ChampionggRune.py where it is shown, as this is needed to send a request to Champion.gg. Afterwards, run ChampionggRune.py and it will prompt the user for a champion name (not case sensitive), and either the most popular rune set or the rune set with the most wins.

##### Example
```
$ python ChampionggRuneSets.py
Type name of champion
$ Lucian
Input 0 for Most Popular
Input 1 for Most Wins
$ 0
+--------------------------------------+---+---------------------+-----------+-----------------------+
|                 Name                 | # |     Description     | Cost (IP) | Accumulated Cost (IP) |
+--------------------------------------+---+---------------------+-----------+-----------------------+
|    Greater Mark of Attack Damage     | 9 | +0.95 attack damage |    102    |          918          |
|    Greater Glyph of Magic Resist     | 9 |  +1.34 magic resist |    102    |          918          |
|        Greater Seal of Armor         | 9 |       +1 armor      |    102    |          918          |
| Greater Quintessence of Attack Speed | 3 |  +4.5% attack speed |    1025   |          3075         |
+--------------------------------------+---+---------------------+-----------+-----------------------+

Total IP: 5829
```

### Future Changes & Notes
To improve the run time, it would probably be best to have RuneInfo.py refer to a single dictionary that maps rune ID to rune cost, and have the request to Champion.gg save the rune ID instead of the rune name. Nested dictionaries improves the run time from O(n), but may in fact make the run time worse due to having to search for a word in each rune name. The rune ID information is not readily available by either Riot API or Champion.gg API, and would thus require an entirely new module.

Any promotional runes (Holiday, Razer, etc.) are given values of 0 IP and are in a seperate category, as it is highly unlikely those will be returned as a potential valuie.

### Resources
[prettytable](https://code.google.com/archive/p/prettytable/)

[Champion.gg](http://champion.gg/)

[Champion.gg API](http://api.champion.gg/)
