# This class inherits the buy/sell logic from BaseTrader and is intended for the NPC 'Traders' with random decision-making

# traders will have a name and gold 
# have inventory
# decide daily to buy or sell items
# impact market prices and quantities


import random
from base_trader import BaseTrader


class Trader(BaseTrader):
    def decide_action(self, market):
        action = random.choice(['buy', 'sell', 'wait'])

        if action == 'buy':
            self.buy_random(market)
        elif action == 'sell':
            self.sell_random(market)
        else:
            print(f"{self.name} wants to wait today.")

    def buy_random(self, market):

        # market.items[item]['quantity'] : The # of units available in the market

        # determine what items player can afford
        affordable = [item for item in market.items if market.prices[item] <= self.gold and market.items[item]['quantity']>0]

        if not affordable:
            print(f"{self.name} wants to buy, but cannot afford anything in the market.")
            return
        
        item = random.choice(affordable)

        # returns smaller of 2 values: # of units avail or # units player can afford
        max_qty = min(market.items[item]['quantity'], self.gold // market.prices[item])

        # random # between 1 - max avail/afford
        quantity = random.randint(1, max_qty)
        
        self.buy_item(market, item, quantity)

    def sell_random(self, market):
        if not self.inventory:
            print(f"{self.name} wants to sell but has nothing.")
            return
        
        item = random.choice(list(self.inventory.keys()))
        quantity = random.randint(1, self.inventory[item])
        self.sell_item(market, item, quantity)
