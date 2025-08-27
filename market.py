import random

class Market:
    """A market in a fantasy swamp market where players can buy and sell troll-themed items."""

    def __init__(self, items=None):
        # Default market items with base prices and quantities
        default_items = {
            'Swamp Mushroom':     {'base_price': 5,  'quantity': 50},
            'Troll Gold':         {'base_price': 5,  'quantity': 5},
            'Bog Water Flask':    {'base_price': 3,  'quantity': 25},
            'Sticky Webbing':     {'base_price': 8,  'quantity': 10},
            'Rotten Turnip':      {'base_price': 2,  'quantity': 30},
            'Glowing Moss':       {'base_price': 7,  'quantity': 9},
            'Gnarly Root':        {'base_price': 6,  'quantity': 11},
            'Slime Gel':          {'base_price': 4,  'quantity': 18},
            'Singing Pebble':     {'base_price': 12, 'quantity': 14},
            'Warty Toad':         {'base_price': 9,  'quantity': 20},
            'Mud-Covered Mirror': {'base_price': 18, 'quantity': 10},
            'Firefly Jar':        {'base_price': 11, 'quantity': 30},
            'Swamp Herb Bundle':  {'base_price': 7,  'quantity': 9},
            'Lumpy Candle':       {'base_price': 10, 'quantity': 6},
            'Troll Soap (Unlabeled)': {'base_price': 6, 'quantity': 10}
        }

        # Use provided items or default troll items
        self.items = items if items is not None else default_items

        # Start with current prices equal to base prices
        self.prices = {item: details['base_price'] for item, details in self.items.items()}

    def print_status(self):
        print("\n📦 Market Status:")
        print("-" * 60)
        print(f"{'No.':<4} {'Item':<25} {'Price:':^15} {'Quantity':^10}")
        print("-" * 60)

        for i, (item, details) in enumerate(self.items.items(), start=1):
            price = self.prices[item]
            quantity = details['quantity']
            print(f"{i:<4} {item:<25} {price:^15} {quantity:>7}")

        print("-" * 60)

    def find_item_case_insensitive(self, item_name):
        """Returns the correctly cased item name if a case-insensitive match is found."""
        item_name_lower = item_name.lower()
        for name in self.items:
            if name.lower() == item_name_lower:
                return name
        return None
    
    def find_item(self, user_input):
        # Try to parse as integer index
        if user_input.isdigit():
            index = int(user_input) - 1
            if 0 <= index < len(self.items):
                return list(self.items.keys())[index]
            else:
                return None
        else:
            return self.find_item_case_insensitive(user_input)


    def update_price(self):
        """Update prices based on supply and demand."""
        for item, details in self.items.items():
            base_price = details['base_price']
            quantity = details['quantity']

            # Defined thresholds
            if quantity < 15:
                multiplier = random.uniform(1.20, 1.40)  # 20% to 40% increase
            elif quantity < 30:
                multiplier = random.uniform(1.10, 1.25) # 10% to 25% increase
            elif quantity > 40:
                multiplier = random.uniform(0.60, 0.85) # 15% to 40% decrease
            else:
                multiplier = random.uniform(0.90, 1.10) # ±10%

            # Price should never be less than 1 gold piece
            new_price = max(1, round(base_price * multiplier))
            self.prices[item] = new_price

# Run this section only if the script is executed directly
if __name__ == "__main__":
    market = Market()
    market.print_status()
