#portfolio : is a list of dictionaries
portfolio=[
    #share 
    {
        "name":"Apple",
        "symbol":"AAPL",
        "strike":50,
        "quantity":10
    },
    {
        "name":"Microsoft",
        "symbol":"MSFT",
        "strike":35,
        "quantity":120
    },
    {
        "name":"Google",
        "symbol":"GOOGL",
        "strike":70,
        "quantity":135
    },
    
]

#Function: Display a share from the portfolio by its index
#Parameters: index (int) - the position of the share in the portfolio
#Returns: None - prints the share information
def get_action(index:int)->None:
    if index < 0 or index >= len(portfolio):
        print("Indice invalide. Vérifiez l'indice.")
    else:
        print(portfolio[index])

#call the function
# index:int = int(input("Donner la valeur de l'indice:"))
# get_action(index)

#Function: Find a share in the portfolio by its name
#Parameters: name (str) - the name of the share to find
#Returns: dict - the share dictionary if found, empty dict otherwise
def find_share(name:str)->dict:
    for share in portfolio:
        if share["name"]==name:
            return share
        
    return dict()

#Function: Modify the strike price and quantity of an existing share
#Parameters: name (str) - the name of the share to modify
#           new_strike (float) - the new strike price
#           new_quantity (int) - the new quantity
#Returns: None - updates the share and prints confirmation
def modify_share(name:str, new_strike:float, new_quantity:int)->None:
    share=find_share(name)
    if len(share)==0:
        print("Verifier le nom de l'action.")
    else:
        share["strike"]=new_strike
        share["quantity"]=new_quantity
        print('action modifiée.')

#call of the function

# name:str = input("Donner le nom de l'action à modifier:")
# new_strike:float = float(input("Donner le nouveau strike:"))
# new_quantity:int = int(input("Donner la nouvelle quantité:"))
# modify_share(name, new_strike, new_quantity)

#Function: Add a new share to the portfolio
#Parameters: name (str) - the name of the share
#           symbol (str) - the stock symbol
#           strike (float) - the strike price
#           quantity (int) - the quantity of shares
#Returns: None - adds the share to portfolio and prints confirmation
def add_share(name:str, symbol:str, strike:float, quantity:int)->None:
    share={
        "name":name,
        "symbol":symbol,
        "strike":strike,
        "quantity":quantity
    }
    portfolio.append(share)
    print('action ajoutée.')

#call of the function
# name:str = input("Donner le nom de l'action à ajouter:")
# symbol:str = input("Donner le symbole de l'action:")
# strike:float = float(input("Donner le strike de l'action:"))
# quantity:int = int(input("Donner la quantité de l'action:"))
# add_share(name, symbol, strike, quantity)

#Function: Get share information from keyboard input and add it to the portfolio
#Parameters: None - gets all data from user input
#Returns: None - calls add_share() with the input data
def get_share_from_keyboard()->None:
    name:str = input("Donner le nom de l'action à ajouter:")
    symbol:str = input("Donner le symbole de l'action:")
    strike:float = float(input("Donner le strike de l'action:"))
    quantity:int = int(input("Donner la quantité de l'action:"))
    add_share(name, symbol, strike, quantity)

#Function: Get modification data from keyboard input and update a share
#Parameters: None - gets all data from user input
#Returns: None - calls modify_share() with the input data
def modify_share_from_keyboard()->None:
    name:str = input("Donner le nom de l'action à modifier:")
    new_strike:float = float(input("Donner le nouveau strike:"))
    new_quantity:int = int(input("Donner la nouvelle quantité:"))
    modify_share(name, new_strike, new_quantity)

#Function: Delete a share from the portfolio by its name
#Parameters: name (str) - the name of the share to delete
#Returns: None - removes the share from portfolio and prints confirmation
def delete_share(name:str)->None:
    share=find_share(name)
    if len(share)==0:
        print("Verifier le nom de l'action.")
    else:
        portfolio.remove(share)
        print('action supprimée.')

#Function: Get share name from keyboard input and delete the share
#Parameters: None - gets the share name from user input
#Returns: None - calls delete_share() with the input name
def delete_share_from_keyboard()->None:
    name:str = input("Donner le nom de l'action à supprimer:")
    delete_share(name)

#call of the function
# name:str = input("Donner le nom de l'action à supprimer:")
# delete_share(name)

#Function: Display all shares in the portfolio
#Parameters: None
#Returns: None - prints all shares in the portfolio
def display_portfolio()->None:
    for share in portfolio:
        print(share)

#call of the function
# display_portfolio()

#Function: Add new key-value pairs to an existing share
#Parameters: name (str) - the name of the share to modify
#           new_keys (dict) - dictionary containing new keys and values to add
#Returns: None - updates the share with new keys and prints confirmation
def add_keys_to_share(name:str, new_keys:dict)->None:
    share=find_share(name)
    if len(share)==0:
        print("Verifier le nom de l'action.")
    else:
        share.update(new_keys)
        print('Nouvelles clés ajoutées à l\'action.')

#Function: Get new keys from keyboard input and add them to a share
#Parameters: None - gets all data from user input (share name, number of keys, key names, types, and values)
#Returns: None - calls add_keys_to_share() with the input data
#Note: Handles type conversion for int, float, and string values with error handling
def add_keys_to_share_from_keyboard()->None:
    name:str = input("Donner le nom de l'action:")
    try:
        num_keys:int = int(input("Donner le nombre de nouvelles clés à ajouter:"))
        if num_keys <= 0:
            print("Le nombre de clés doit être positif.")
            return
        new_keys:dict = {}
        for i in range(num_keys):
            key:str = input(f"Donner le nom de la clé {i+1}:")
            value_type:str = input(f"Donner le type de la valeur (str/int/float) pour '{key}':")
            try:
                if value_type.lower() == "int":
                    value = int(input(f"Donner la valeur (int) pour '{key}':"))
                elif value_type.lower() == "float":
                    value = float(input(f"Donner la valeur (float) pour '{key}':"))
                else:
                    value = input(f"Donner la valeur (str) pour '{key}':")
                new_keys[key] = value
            except ValueError:
                print(f"Erreur: valeur invalide pour '{key}'. Clé ignorée.")
        add_keys_to_share(name, new_keys)
    except ValueError:
        print("Erreur: nombre de clés invalide.")

#Function: Main menu function that provides an interactive menu for portfolio management
#Parameters: None
#Returns: None - runs an infinite loop until user chooses to quit
#Description: Displays a menu with options to:
#           1. Display a share by index
#           2. Modify a share (strike and quantity)
#           3. Add a new share
#           4. Delete a share
#           5. Display all shares in the portfolio
#           6. Add new keys to an existing share
#           7. Quit the program
def main()->None:
    while True:
        print("1. Afficher une action")
        print("2. Modifier une action")
        print("3. Ajouter une action")
        print("4. Supprimer une action")
        print("5. Afficher le portefeuille")
        print("6. Ajouter des clés à une action")
        print("7. Quitter")
        choice:int = int(input("Donner votre choix:"))
        #using match case
        match choice:
            case 1:
                index:int = int(input("Donner la valeur de l'indice:"))
                get_action(index)
            case 2:
                modify_share_from_keyboard()
            case 3:
                get_share_from_keyboard()
            case 4:
                delete_share_from_keyboard()
            case 5:
                display_portfolio()
            case 6:
                add_keys_to_share_from_keyboard()
            case 7:
                break

#call of the main function
if __name__=="__main__":
    main()