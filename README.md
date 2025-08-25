# 🧌 Troll Traders

A whimsical fantasy market simulator where swamp trolls barter strange goods, hoard glowing moss, and try to get rich trading jars of fireflies.

## 🛍️ What is Troll Traders?

Troll Traders is a turn-based, Python-powered economy simulation game inspired by fantasy trading systems. You play as a swamp troll merchant trying to outwit AI traders in a shifting market of oddball items like Glowing Moss, Troll Soap, and Bog Water Flasks.

## ✨ Features

- 📈 Dynamic pricing driven by supply and demand
- 🤖 Simple AI traders with quirky buying habits
- 🛒 Buy, sell, and stockpile troll-friendly goods
- 🎨 Fully CLI-based for fast, focused gameplay
- 🔄 Easily configurable with YAML or JSON

## 🧪 Example Items

| Item               | Base Price | Notes                    |
| ------------------ | ---------- | ------------------------ |
| Swamp Mushroom     | 5          | Edible... technically    |
| Troll Gold         | 50         | Shiny but mostly useless |
| Rotten Turnip      | 2          | Surprisingly popular     |
| Firefly Jar        | 11         | Glows in the dark        |
| Troll Soap         | 6          | Nobody uses it           |
| Glowing Moss       | 7          | Used in swamp lanterns   |
| Slime Gel          | 4          | Multipurpose goo         |
| Mud-Covered Mirror | 18         | Shows your worst side    |

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/erinczarnecki/troll-traders.git
   cd troll-traders

2. Run the game:
   python troll_traders.py

   ✅ Python 3.9+ recommended
   🐍 No external dependencies required (pure Python)

## 🧠 How It Works

- Each item has a **base price** and a **market quantity**.
- The **market** updates prices based on current supply and demand.
- The **player** and **AI traders** take turns buying and selling items.
- The player's **inventory and gold** are tracked each turn.
- Item prices **fluctuate** depending on scarcity and trading activity.
- The goal is to **maximize your profit** and become the wealthiest troll in the swamp!

## 🔮 Stretch Goals

- 📊 Add a **price history chart** or trend tracker for each item
- 🌪️ Introduce **random market events** (e.g. "Firefly Festival" or "Moss Mold Outbreak")
- 🧠 Implement **smarter AI** traders with strategies like hoarding or price manipulation
- 🧾 Allow **configurable player traits** (e.g. "Greedy", "Patient", "Risky")
- 🎨 Build a **GUI** using Tkinter or a web front-end (e.g. Flask or React)
- 💬 Add **dialogue or flavor text** for trader personalities
- 🎮 Create a **turn replay system** or game summary at the end
- 🪙 Introduce **rare collectible items** with special rules or effects


## Folder Structure

troll-traders/
├── troll_traders.py       # Main game loop
├── market.py              # Market logic
├── trader.py              # Player & AI traders
├── items.yaml (optional)  # Configurable item data
├── README.md              # This file

## 📜 License

This project is licensed under the [MIT License](LICENSE).

You are free to use, modify, and distribute this code for personal or commercial use. Attribution is appreciated but not required.

## 💬 Credits & Inspiration

**Troll Traders** was created by Erin Czarnecki as a creative side project to explore:

- Game loops and turn-based logic in Python
- Simple AI behavior dynamic market mechanics
- Fantasy themes with a humorous twist

Inspired by:
- Classic trading sims and fantasy marketplaces
- Idle games with economic systems
- The question: *"What would trolls sell, anyway?"*

Feel free to fork, remix, or expand this project in your own trollish direction.
