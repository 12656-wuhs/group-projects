#Names: Logan Rasciner, Nathaniel Rodriguez, James Nickell, Jaidyn Li, James Lawson
#Period: 6
#Assignment: String Methods Group Project
#Time Spent (LR): An hour and 45 minutes roughly

#Method: Find and replace.
#Situation: You run a bread store. One of your clients has called you saying they submitted an order incorrectly, and now you \
#must write a program to scan through your master file of clients and orders to find their order, and replace it with the correct one.

#variable = to a readline function to scan through the file line by line.
#between each line switch, compare that variable to the clients name to check if its the right person.
#find and replace function to then swap their order for something else, we'll figure out what later
#May need to find a way to isolate the scope of the find and replace function, as it will swap out EVERYTHING in the file = to the criteria
#Make a variable = to the line containing an order, modify that and then write it into the function.

#Above here is all old pseudocode used when brainstorming, was unsure if I should remove or not so I left it there.

import random
#list of items shared with ClientListGen.py. It was brought here so a new order could be randomly generated to replace the old one.
items = ["Classic Sourdough",
    "Roasted Garlic Batard",
    "Seeded Rye Loaf",
    "Heritage Whole Wheat",
    "Rosemary & Sea Salt Focaccia",
    "Kalamata Olive Ciabatta",
    "Cranberry Walnut Pull-Apart",
    "Jalapeño Cheddar Loaf",
    "Brioche Nanterre",
    "Honey Oat Sandwich Bread",
    "French Baguette (Traditional)",
    "Multi-Grain Boule",
    "Pumpkin Seed Spelt",
    "Chocolate Ganache Babka",
    "Cinnamon Swirl Brioche",
    "Everything Bagel 6-Pack",
    "Sesame Semolina",
    "Fig and Anise Loaf",
    "Pumpernickel Round",
    "English Muffin 4-Pack"
]
#generates new items to replace the old ones with
newitem1 = random.choice(items)
newitem2 = random.choice(items)
newitem3 = random.choice(items)
#concatenates all the new items together into one string for use with the .replace method.
neworder = f'{newitem1}\n{newitem2}\n{newitem3}\n'

def replaceorder(fulltext, oldtext, newtext):
    replacedorder = fulltext.replace(oldtext, newtext)
    return replacedorder
    #This takes the mashed together lines from the main function and looks to replace the users old order in that string with the new one.
         

def findorder():
    global newitems
    target = 'Graham, Alex' #Name of the hypothetical client 

    with open('ClientList.txt', 'r') as clientnamesearch:
            lines = clientnamesearch.readlines()
            for line in range(len(lines)):
                
                if target in lines[line]:
                    print(f'User found at line {line + 1}. Identifying old items...')
                    #We know all orders make up three lines, meaning we can simply scan the next three lines and concatenate them together to find the old order.
                    olditem1 = lines[line + 1].strip()
                    olditem2 = lines[line + 2].strip()
                    olditem3 = lines[line + 3].strip()
                    #used .strip on each old item to ensure the concatenation proceeded smoothly.
                    oldorder = f'{olditem1}\n{olditem2}\n{olditem3}\n'
                    print(f'Old order identified. \n {oldorder} \n Replacing...')
                    #with this, this function has served its purpose will now pass data to the function responsible for actually altering the file.
                    #mushing the list of lines created in the readlines method will also allow us to use .replace properly.
                    fullfile = ''.join(lines)
                    replacedwith = replaceorder(fullfile, oldorder, neworder)
                    with open('ClientList.txt', 'w') as blahblah:
                         #This uses .w to ensure the entire old file is swapped out for the altered one.
                         blahblah.write(replacedwith)
                         print('Replacment completed succesfully!')
findorder()