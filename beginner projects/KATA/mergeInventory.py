'''
merge invetory of two warehouses
'''
from copy import copy

def merge_inventory(inventory1, inventory2):
    '''
    the function merges two inventories
    this returns a new dictionary
    '''
    total_inventory = {}

    if not (inventory1 or inventory2):
        return {}

    if not inventory1:
        return inventory2.copy()
    elif not inventory2:
        return inventory1.copy()

    for k, v in inventory1.items():
        total_inventory[k] = total_inventory.setdefault(k, inventory2.get(k, 0)) + v

    for k, v in inventory2.items():
        if k in total_inventory:
            continue
        total_inventory[k] = total_inventory.get(k, 0) + v

    return total_inventory

warehouse_a = {
    "keyboard": 10,
    "mouse": 15,
    "monitor": 5
}

warehouse_b = {
}

print(merge_inventory(warehouse_a, warehouse_b))
