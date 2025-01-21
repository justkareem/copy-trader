# Pump and Trade Automation Bot

Welcome to the Pump and Trade Automation Bot! This tool helps you monitor and automatically trade tokens on the Pump Portal platform. With this bot, you can watch specified accounts, automatically buy tokens, and set sell triggers based on specific conditions.

---

## 🚀 Features
- **Automated Trading**: Tracks specific wallet addresses for new token buys and performs trades automatically.
- **Customizable Parameters**: Set trade amounts, slippage, priority fees, and more to suit your needs.
- **Sell Trigger**: Automatically initiates a sell order based on your custom-defined conditions.

---

## 📋 Prerequisites
1. **Python 3.8+**: Make sure you have Python installed.
---

## ⚙️ Setup Instructions

### 1. Clone the Repository
To get started, clone this repository to your local machine:
```bash
git clone https://github.com/your-username/pump-trade-bot.git
cd pump-trade-bot
```
**Install Required Libraries**:
   Run the following command in your terminal to install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### 2. Generate Your Wallet
Before using the bot, you need to generate a wallet:
1. Run `generate_wallet.py` to get your wallet details:
   ```bash
   python generate_wallet.py
   ```
2. Save the generated `API Key`, `Public Wallet Address`, and `Private Key` securely. You'll need the API Key for the bot.

**Important**:
- Securely save your private key and API key. They **cannot be recovered** if lost.
- Do not share your keys with anyone.

### 3. Configure the Bot
1. Open `main.py` and update the following:
   - **API Key**: Replace the `API_KEY` variable with the key you generated.
   - **COPY_ADDRESSES**: Add the wallet addresses you want to monitor.
   - **Customize Trade Settings**: Adjust the trade amount, slippage, and priority fee as desired.

---

## ▶️ How to Use
1. Start the bot by running:
   ```bash
   python main.py
   ```
2. The bot will:
   - Monitor specified wallet addresses.
   - Automatically execute buy trades when conditions are met.
   - Trigger sell orders if your sell conditions are satisfied.

---

## 🛠️ Notes
- **Security**: Keep your API key and private key secure. Do not share them with anyone.
- **Customization**: You can tweak the logic in the `main.py` file to better suit your trading strategy.
- **Monitoring**: Check the terminal logs for updates about transactions and potential issues.

---

## ❤️ Support
If you have questions or need help, feel free to reach out.

Happy Trading! 🚀
```

