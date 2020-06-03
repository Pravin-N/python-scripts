import pyinputplus as pyip, random, re

#prices of options
prices = {'Wheat': 1.5, 'White': 1, 'Sourdough': 1, 'Chicken': 2, 'Turkey': 3, 'Ham': 1, 'Vegan': 4,
          'Cheddar': 0.5, 'Swiss': 0.75, 'Mozzarella': 1.25, 'Mayo': 0.25, 'Mustard': 0.25, 'Lettuce': 0.25, 'Tomato': 0.25, 'Zero': 0}


#Ask for type of bread
bread = pyip.inputMenu(['Wheat', 'White', 'Sourdough'], prompt='What bread would you like?\n1. Wheat\n2. White\n3. Sourdough\n', numbered=True)

#Ask for type of protein
protein = pyip.inputMenu(['Chicken', 'Turkey', 'Ham', 'Vegan'], prompt='What kind of protein would you like?\n1. Chicken\n2. Turkey\n3. Ham\n4. Vegan\n', numbered=True) 

# Asks if user wants cheese.
cheese = pyip.inputYesNo('Would you like some cheese?') 

#if yes what kind of cheese.
if cheese == 'yes':
    cheesetype = pyip.inputMenu(['Cheddar', 'Swiss', 'Mozzarella'], prompt='What type of cheese do you want?\n1. Cheddar\n2. Swiss\n3. Mozzarella\n', numbered=True)
else:
    cheesetype = 'Zero'
    
# Asks if user wants Mayo, mustard, lettuce and tomato.

mayoyesno = pyip.inputYesNo('Would you like some mayo?')
if mayoyesno == 'Yes':
    mayo = 'Mayo'
else:
    mayo = 'Zero'


mustardyesno = pyip.inputYesNo('Would you like some mustard?')
if mustardyesno == 'Yes':
    mustard = 'Mustard'
else:
    mustard = 'Zero'


lettuceyesno = pyip.inputYesNo('Would you like some lettuce?')
if lettuceyesno == 'Yes':
    lettuce = 'Lettuce'
else:
    lettuce = 'Zero'
                    
tomatoyesno = pyip.inputYesNo('Would you like some tomato?')
if tomatoyesno == 'Yes':
    tomato = 'Lettuce'
else:
    tomato = 'Zero'

#Asks for how many sandwiches.
numofsand = pyip.inputInt('How many sandwiches would you like of these: ', min=1)

costofsandwich = (prices[bread] + prices[protein] + prices[cheesetype] + prices[mayo] + prices[mustard] + prices[lettuce] + prices[tomato])*numofsand
print(f'Total amount to pay is %s' % costofsandwich)

                   
