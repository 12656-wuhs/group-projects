import random
clientfirstnames = ['John', 'Clara', 'Sally', 'Sarah', 'Billy', 'Jack', 'Alex', 'Alan', 'Charles', 'Chuck', 'Oscar']
clientlastnames = ['Graham', 'Mullins', 'Williamson', 'Weaver', 'Shelton', 'Rogers', 'Drew', 'Bird', 'McCoy', 'Meyer']
orders = [
    "Classic Sourdough",
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

def writelist():
    numclients = 10
    while numclients >= 0:
        with open('ClientList.txt', 'a') as clientlist:
            clientlist.write(f'{random.choice(clientlastnames)}, {random.choice(clientfirstnames)} \n')
            clientlist.write(f'{random.choice(orders)} \n')
            clientlist.write(f'{random.choice(orders)}\n')
            clientlist.write(f'{random.choice(orders)}\n')
            clientlist.write('\n')

        
        numclients -= 1
    if numclients == -1:
        print('List generated.')
writelist()

