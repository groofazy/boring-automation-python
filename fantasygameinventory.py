# inventory for a fantasy game

def addtoInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] = inventory[addedItems[i]] + 1
        
        else:
            inventory.setdefault(addedItems[i],1)
    return inventory
    
def displayInventory(inventory):
    print("Inventory: ")
    item_total = 0
    for k, v in inventory.items(): # for loop that iterates through inventory dictionary
        item_total += v # 
        print(str(v) + " " + k)

    print("Total number of items: " + str(item_total))

inv = {'rope': 1, 'gold coin':42 }
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'dagger']
inv = addtoInventory(inv, dragon_loot)
displayInventory(inv)