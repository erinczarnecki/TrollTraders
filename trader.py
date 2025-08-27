import random
from base_trader import BaseTrader


class Trader(BaseTrader):
    def decide_action(self, market):
        if self.inventory:
            action = random.choice(['buy', 'sell', 'wait'])
        else:
            action = random.choice(['buy', 'wait'])  # no 'sell' if inventory empty
    
        if action == 'buy':
            print(f"\n{self.name} is considering a purchase...")
            self.buy_random(market)
        elif action == 'sell':
            print(f"\n{self.name} is considering selling something...")
            self.sell_random(market)
        else:
            print(f"\n{self.name} wants to wait today.")

    def buy_random(self, market):

        # market.items[item]['quantity'] : The # of units available in the market
        # determine what items player can afford
        affordable = [
            item for item in market.items 
            if market.prices[item] <= self.gold and market.items[item]['quantity'] > 0
            ]

        if not affordable:
            print(f"{self.name} wants to buy, but cannot afford anything in the market.")
            return
        
        item = random.choice(affordable)
        # returns smaller of 2 values: # of units avail or # units player can afford
        max_qty = min(market.items[item]['quantity'], self.gold // market.prices[item])
        # random # between 1 - max avail/afford
        quantity = random.randint(1, max_qty)

        success = self.buy_item(market, item, quantity)
        if success:
            print(f"{self.name} bought {quantity} {item}(s).")
        if not success:
            print(f"{self.name}'s purchase failed.")


    def sell_random(self, market):
        if not self.inventory:
            print(f"{self.name} wants to sell but has nothing.")
            return
        
        item = random.choice(list(self.inventory.keys()))
        quantity = random.randint(1, self.inventory[item])
        success = self.sell_item(market, item, quantity)
        if success:
            print(f"{self.name} sold {quantity} {item}(s).")
        if not success:
            print(f"{self.name}'s sale failed.")
