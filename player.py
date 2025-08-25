# This class inherits the logic from the BaseTrader class and is intended for the user-led game flow

from base_trader import BaseTrader

class Player(BaseTrader):
    def show_inventory(self):
        print(f"\n{self.name}")
        print(f"Gold: {self.gold}")

        if not self.inventory: # Check if inventory is empty
            print("Inventory: Empty")
        else:
            print("Inventory:")
            for item, qty in self.inventory.items():
                print(f". {item}: {qty}")
        print()
    
