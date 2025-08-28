from market import Market
from player import Player
from trader import Trader
import random
import time

# --- Game Play Config ---
STARTING_GOLD = 100 # Gold balance player will start the game with

NUM_DAYS = 5 # Number of rounds played

NUM_TRADERS = 3 # Number of NPC traders to include in each round of this session

# --- Pool of Possible NPC Traders ---

NPC_OPTIONS = [
    {"name": "Bogwort the Wise", "gold": 80},
    {"name": "Toadilda the Trader", "gold": 95},
    {"name": "Fungus Fred", "gold": 105},
    {"name": "Warty Wanda", "gold": 100},
    {"name": "Mossbelly the Merchant", "gold": 88},
    {"name": "Groonk the Greedy", "gold": 75},
    {"name": "Snarla the Sharp", "gold": 90},
    {"name": "Meep the Muddler", "gold": 110}
    ]

def print_troll_art():
    print(r"""
       ,      ,
      /(.-""-.)\
  |\  \/      \/  /|
  | \ / =.  .= \ / |
  \( \   o\/o   / )/
   \_, '-/  \-' ,_/
     /   \__/   \
     \ \__/\__/ /     
   ___\ \|--|/ /___
 /`    \      /    `\
    """)

def main():
    print("\n\nWelcome to Troll Traders!\n")
    print_troll_art()  # <-- print the troll face first!
    player_name = input("\nEnter you name, brave swamp merchant: ").strip() or "Player"

    # Initial Game State
    market = Market()
    player = Player(name=player_name, gold=STARTING_GOLD)

    # Cap NUM_TRADERS to max available NPCs
    actual_num_traders = min(NUM_TRADERS, len(NPC_OPTIONS))

    # Randomly select NPC traders
    npc_choices = random.sample(NPC_OPTIONS, k=actual_num_traders)
    traders = [Trader(config["name"],gold=config["gold"]) for config in npc_choices]

    # --- GAME PLAY ---
    for day in range(1, NUM_DAYS + 1):
        print(f"\n📆 Day {day} Trading Begins\n")
        
        # Show market list and player inventory
        market.print_status()
        print() # add blank line for readability
        player.show_inventory()
        print() # add blank line for readability

        # --- Player Turn ---
        while True:
            if player.inventory:
                action = input("Do you want to [b]uy, [s]ell, or [w]ait? ").strip().lower()
            else:
                action = input("Do you want to [b]uy or [w]ait? ").strip().lower()

            if action in ("buy", "b"):
                item_input = input("What item do you want to buy? ").strip()
                item = market.find_item(item_input)
                if item is None:
                    print(f"❌ Item '{item_input}' not found in the market.")
                    continue

                qty = input("How many would you like? ").strip()
                if qty.isdigit():
                    success = player.buy_item(market, item, int(qty))
                    if success:
                        break
                    else:
                        print("❌ Purchase failed. Check your gold, item name, or availability.")
                else:
                    print("Invalid quantity entered - Must be a number!")

            elif action in ("sell", "s"):
                item_input = input("What item do you want to sell? ").strip()
                if item_input not in player.inventory:
                    print(f"❌ Item '{item_input}' not found in your inventory.")
                    continue
                item = item_input

                qty = input("How many do you want to sell? ").strip()
                if qty.isdigit():
                    success = player.sell_item(market, item, int(qty))
                    if success:
                        break
                    else:
                        print("❌ Sale failed. Check your inventory or item name.")
                else:
                    print("Invalid quantity entered - Must be a number!")

            elif action in ("wait", "w"):
                print(f"{player.name} chooses to wait this round.")
                break

            else:
                print("Invalid option selected. Please enter buy (b), sell (s), or wait (w).")
        
        # --- NPC Trader Turns ---
        print("\n--- Other Traders' Turns ---")
        for trader in traders:
            trader.decide_action(market)
            time.sleep(2)

        # --- Update Market Prices ---
        market.update_price()
        print("-" * 50)
        print("\n📈 Market prices have been updated based on supply and demand!")

    # --- GAME END ---
    print("\n🎉 The Troll Trading Season Has Ended!")
    player.show_inventory()
    print(f"💰 Final Gold: {player.gold}")

    # Show NPC stats
    print("\n📊 Final NPC Trader Stats:")
    for trader in traders:
        print(f"{trader.name}: {trader.gold} gold")
    print("\nThanks for playing Troll Traders!")

# --- Entry Point ---
if __name__ == "__main__":
    main()
