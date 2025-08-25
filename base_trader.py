# This class is a shared class with the core logic for transactions


class BaseTrader:
    def __init__(self, name, gold=100):
        self.name = name
        self.gold = gold
        self.inventory = {}


    def buy_item(self, market, item_name, quantity):
        # can only purchase items if they are available in the market
        if item_name not in market.items:
            print(f"{self.name}: Item not available in market.")
            return False
        
        price = market.prices[item_name]
        cost = price * quantity

        # cannot purchase items if total cost is more than gold
        if cost > self.gold:
            print(f"{self.name}, you do not have enough gold")
            return False
        
        # cannot purchase items if total number greater than available inventory
        if quantity > market.items[item_name]['quantity']:
            print(f"{self.name}, there aren't enough items in stock.")
            return False
        
        # update player's gold balance 
        self.gold -= cost

        # update the quantity in the market
        market.items[item_name]['quantity'] -= quantity

        # update the player's inventory
        self.inventory[item_name] = self.inventory.get(item_name, 0) + quantity
        print(f"{self.name} purchased {quantity} x {item_name} for {cost} gold.")
        return True
    
    

    def sell_item(self, market, item_name, quantity):

        # can only sell items if available in player's inventory
        if item_name not in self.inventory:
            print(f"{self.name}, you cannot sell items that are not in your inventory.")
            return False

        # can only sell quantity available in inventory
        if self.inventory[item_name] < quantity:
            print(f"{self.name}, you only have {self.inventory[item_name]} x {item_name}, and cannot sell {quantity}.")
            return False
        
        price = market.prices[item_name]
        profit = price * quantity

        # update player's gold balance
        self.gold += profit

        # update the market quantity
        market.items[item_name]['quantity'] += quantity

        # update player's inventory
        self.inventory[item_name] -= quantity
        
        # remove items with 0 from the inventory list
        if self.inventory[item_name] == 0:
            del self.inventory[item_name]

        print(f"{self.name} sold {quantity} x {item_name} for {profit} gold.")
        return True
