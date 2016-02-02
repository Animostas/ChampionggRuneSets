'''Dictionary of Rune Information'''

RuneCost = {

    'Quintessence': {
        'Offensive': {
            'Greater Quintessence of Attack Damage': 512,
            'Greater Quintessence of Scaling Attack Damage': 515,
            'Greater Quintessence of Attack Speed': 1025,
            'Greater Quintessence of Critical Damage': 1025,
            'Greater Quintessence of Critical Chance': 1025,
            'Greater Quintessence of Armor Penetration': 1025,
            'Greater Quintessence of Ability Power': 512,
            'Greater Quintessence of Scaling Ability Power': 1025,			
            'Greater Quintessence of Magic Penetration': 1025,
            'Greater Quintessence of Spell Vamp': 2050,
            'Greater Quintessence of Life Steal': 2050,
            'Greater Quintessence of Hybrid Penetration': 2050
        },

        'Defensive': {		
	    'Greater Quintessence of Health': 2050,
            'Greater Quintessence of Scaling Health': 2050,
            'Greater Quintessence of Armor': 1025,
            'Greater Quintessence of Scaling Armor': 1025,
            'Greater Quintessence of Magic Resist': 1025,
            'Greater Quintessence of Scaling Magic Resist': 1025,
            'Greater Quintessence of Health Regeneration': 2050,
            'Greater Quintessence of Scaling Health Regeneration': 2050,
            'Greater Quintessence of Revival': 1025,
            'Greater Quintessence of Percent Health': 2050
        },

        'Utility': {
            'Greater Quintessence of Cooldown Reduction': 2050,
            'Greater Quintessence of Scaling Cooldown Reduction': 1025,
            'Greater Quintessence of Mana': 1025,
            'Greater Quintessence of Scaling Mana': 515,
            'Greater Quintessence of Mana Regeneration': 1025,
            'Greater Quintessence of Scaling Mana Regeneration': 1025,
            'Greater Quintessence of Movement Speed': 2050,
            'Greater Quintessence of Gold': 515,
            'Greater Quintessence of Experience': 2050,
            'Greater Quintessence of Energy Regeneration': 2050,
            'Greater Quintessence of Energy': 1025
        },

        'Other': {
            'Greater Quintessence of Piercing Present': 0,
            'Greater Quintessence of Deadly Wreath': 0,
            'Greater Quintessence of Frosty Health': 0,
            'Greater Quintessence of Sugar Rush': 0,
            'Greater Quintessence of Studio Rumble': 0,
            'Razer Quintessence of Speed': 0
        }
    },

    'Glyph': {
        'Offensive': {
            'Greater Glyph of Attack Damage': 205,
            'Greater Glyph of Scaling Attack Damage': 410,
            'Greater Glyph of Attack Speed': 410,
            'Greater Glyph of Critical Damage': 820,
            'Greater Glyph of Critical Chance': 410,
            'Greater Glyph of Armor Penetration': 410,
            'Greater Glyph of Magic Penetration': 410,
            'Greater Glyph of Ability Power': 410,
            'Greater Glyph of Scaling Ability Power': 410
        },

        'Defensive': {
            'Greater Glyph of Health': 410,
            'Greater Glyph of Scaling Health': 820,
            'Greater Glyph of Armor': 205,
            'Greater Glyph of Scaling Armor': 0,
            'Greater Glyph of Magic Resist': 102,
            'Greater Glyph of Scaling Magic Resist': 205,
            'Greater Glyph of Health Regeneration': 820,
            'Greater Glyph of Scaling Health Regeneration': 0
        },
		
        'Utility': {
	    'Greater Glyph of Cooldown Reduction': 820,
            'Greater Glyph of Scaling Cooldown Reduction': 410,
            'Greater Glyph of Mana': 410,
            'Greater Glyph of Scaling Mana': 410,
            'Greater Glyph of Mana Regeneration': 410,
            'Greater Glyph of Scaling Mana Regeneration': 205,
            'Greater Glyph of Energy': 820,
            'Greater Glyph of Scaling Energy': 820
        }
    },
	
    'Mark': {
        'Offensive': {
            'Greater Mark of Attack Damage': 102,
            'Greater Mark of Scaling Attack Damage': 205,
            'Greater Mark of Attack Speed': 410,
            'Greater Mark of Critical Damage': 820,
            'Greater Mark of Critical Chance': 410,
            'Greater Mark of Armor Penetration': 410,
            'Greater Mark of Magic Penetration': 205,		
            'Greater Mark of Ability Power': 410,
            'Greater Mark of Scaling Ability Power': 410,
            'Greater Mark of Hybrid Penetration': 820,
            'Razer Mark of Precision': 0
        },
		
        'Defensive': {
            'Greater Mark of Health': 410,
            'Greater Mark of Scaling Health': 820,
            'Greater Mark of Armor': 205,
            'Greater Mark of Magic Resist': 205,
            'Greater Mark of Scaling Magic Resist': 205
        },
		
        'Utility': {
            'Greater Mark of Cooldown Reduction': 410,
            'Greater Mark of Mana': 410,
            'Greater Mark of Scaling Mana': 410,
            'Greater Mark of Mana Regeneration': 205
        }
    },

    'Seal': {
        'Offensive': {
            'Greater Seal of Attack Damage': 205,
            'Greater Seal of Scaling Attack Damage': 205,
            'Greater Seal of Attack Speed': 410,
            'Greater Seal of Critical Damage': 820,
            'Greater Seal of Critical Chance': 410,
            'Greater Seal of Ability Power': 410,
            'Greater Seal of Scaling Ability Power': 410
        },

        'Defensive': {
            'Greater Seal of Health': 410,
            'Greater Seal of Scaling Health': 410,
            'Greater Seal of Armor': 102,
            'Greater Seal of Scaling Armor': 410,
            'Greater Seal of Magic Resist': 205,
            'Greater Seal of Scaling Magic Resist': 410,
            'Greater Seal of Health Regeneration': 820,		
            'Greater Seal of Scaling Health Regeneration': 410,
            'Greater Seal of Percent Health': 820
        },
		
        'Utility': {
            'Greater Seal of Cooldown Reduction': 410,
            'Greater Seal of Mana': 410,
            'Greater Seal of Scaling Mana': 205,
            'Greater Seal of Mana Regeneration': 205,
            'Greater Seal of Scaling Mana Regeneration': 205,
            'Greater Seal of Energy Regeneration': 820,		
            'Greater Seal of Scaling Energy Regeneration': 820,		
            'Greater Seal of Gold': 410
        }
    }
}

listOffensive = ['Attack', 'Critical', 'Penetration', 'Ability', 'Vamp', 'Steal', 'Precision']
listDefensive = ['Health', 'Armor', 'Resist', 'Revival']
listUtility = ['Cooldown', 'Mana', 'Energy', 'Movement', 'Gold', 'Experience', 'Energy']
