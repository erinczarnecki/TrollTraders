import random

class Market:
    """A market in a fantasy swamp market where players can buy and sell troll-themed items."""

    def __init__(self, items=None):
        # Default market items with base prices and quantities
        default_items = {
            'Swamp Mushroom':     {'base_price': 5,  'quantity': 200},
            'Troll Gold':         {'base_price': 50, 'quantity': 20},
            'Bog Water Flask':    {'base_price': 3,  'quantity': 150},
            'Sticky Webbing':     {'base_price': 8,  'quantity': 80},
            'Rotten Turnip':      {'base_price': 2,  'quantity': 300},
            'Glowing Moss':       {'base_price': 7,  'quantity': 90},
            'Gnarly Root':        {'base_price': 6,  'quantity': 110},
            'Slime Gel':          {'base_price': 4,  'quantity': 180},
            'Singing Pebble':     {'base_price': 12, 'quantity': 40},
            'Warty Toad':         {'base_price': 9,  'quantity': 70},
            'Mud-Covered Mirror': {'base_price': 18, 'quantity': 30},
            'Firefly Jar':        {'base_price': 11, 'quantity': 55},
            'Swamp Herb Bundle':  {'base_price': 7,  'quantity': 90},
            'Lumpy Candle':       {'base_price': 10, 'quantity': 60},
            'Troll Soap (Unlabeled)': {'base_price': 6, 'quantity': 95}
        }

        # Use provided items or default troll items
        self.items = items if items is not None else default_items

        # Start with current prices equal to base prices
        self.prices = {item: details['base_price'] for item, details in self.items.items()}

    def print_status(self):
        print("Market Status:")
        for item, details in self.items.items():
            price = self.prices[item]
            quantity = details['quantity']
            print(f"{item}: Price: {price} gold, Quantity: {quantity}")

    def update_price(self):
        """Update prices based on supply and demand."""
        for item, details in self.items.items():
            base_price = details['base_price']
            quantity = details['quantity']

            # Defined thresholds
            if quantity < 40:
                # Price should increase for scarce items - price between 105%-115% base_price
                multiplier = random.uniform(1.05, 1.15)
            elif quantity > 210:
                # Price will drop for abundant items - price between 85%-95% base_price
                multiplier = random.uniform(0.85, 0.95)
            else:
                # Price will have slight variation for normal stock - price between 95%-105% base_price
                multiplier = random.uniform(0.95,1.05)

            # Price should never be less than 1 gold piece
            new_price = max(1, round(base_price * multiplier))
            self.prices[item] = new_price

# Run this section only if the script is executed directly
if __name__ == "__main__":
    market = Market()
    market.print_status()
