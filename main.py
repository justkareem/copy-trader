import asyncio
import requests
import websockets
import json
import base64
import threading

API_KEY = ""  # API key for the wallet you created
COPY_ADDRESSES = ["", ]  # List of accounts to watch

# Clean up the list of copy addresses by stripping any extra whitespace
COPY_ADDRESSES = [address.strip() for address in COPY_ADDRESSES]

# Constants for the trade details
TRADE_AMOUNT = 100000  # Amount of SOL or tokens per buy trade
DENOMINATED_IN_SOL = "false"  # "true" if amount is in SOL, "false" if in tokens
SLIPPAGE = 10  # Percent slippage allowed
PRIORITY_FEE = 0.005  # Amount used to enhance transaction speed


# Construct URLs and WebSocket URI
url = base64.b64decode("aHR0cHM6Ly9wdW1wcG9ydGFsLmZ1bi9hcGkvdHJhZGU/YXBpLWtleT0=").decode("utf-8") + API_KEY
uri = base64.b64decode("d3NzOi8vcHVtcHBvcnRhbC5mdW4vYXBpL2RhdGE=").decode("utf-8")


def should_trigger_sell(mint, pool):
    """
    This function triggers a sell order if certain conditions are met.
    Running in a separate thread to handle multiple buy events concurrently.
    """
    async def trigger_sell():
        async with websockets.connect(uri) as mint_websocket:
            # Subscribing to trades on tokens
            payload = {
                "method": "subscribeTokenTrade",
                "keys": [mint]  # Array of token contract addresses to watch
            }
            await mint_websocket.send(json.dumps(payload))
            async for message in mint_websocket:
                data = json.loads(message)
                if data.get("txType") == "buy" and data.get("pool") == "pump" and data.get("solAmount") >= 50:
                    response = requests.post(url="https://pumpportal.fun/api/trade?api-key=your-api-key-here", data={
                        "action": "sell",  # Action to perform, "buy" or "sell"
                        "mint": mint,  # Contract address of the token you want to trade
                        "amount": "100%",  # Amount of SOL or tokens to trade
                        "denominatedInSol": DENOMINATED_IN_SOL,  # "true" if amount is in SOL
                        "slippage": SLIPPAGE,  # Percent slippage allowed
                        "priorityFee": PRIORITY_FEE,  # Amount used to enhance transaction speed
                        "pool": pool  # Exchange to trade on. "pump", "raydium", or "auto"
                    })
                    response_data = response.json()  # Tx signature or error(s)
                    signature = response_data.get("signature")
                    if signature is not None:
                        print(f'Transaction to dump tokens successful: https://solscan.io/tx/{response_data["signature"]}')
                    else:
                        print(f"Transaction to dump tokens not successful: {response_data}")
                    await mint_websocket.close()

    threading.Thread(target=asyncio.run, args=(trigger_sell(),)).start()


async def subscribe():
    async with websockets.connect(uri) as websocket:
        payload = {
            "method": "subscribeAccountTrade",
            "keys": COPY_ADDRESSES
        }
        await websocket.send(json.dumps(payload))

        async for message in websocket:
            data = json.loads(message)
            print(data)
            if data.get("txType") == "buy" and data.get("pool") == "pump":
                print("Found a new buy")
                pool = data.get("pool")
                response = requests.post(url=url, data={
                    "action": "buy",  # Action to perform, "buy" or "sell"
                    "mint": data["mint"],  # Contract address of the token you want to trade
                    "amount": TRADE_AMOUNT,  # Amount of SOL or tokens to trade
                    "denominatedInSol": DENOMINATED_IN_SOL,  # "true" if amount is in SOL
                    "slippage": SLIPPAGE,  # Percent slippage allowed
                    "priorityFee": PRIORITY_FEE,  # Amount used to enhance transaction speed
                    "pool": "pump"
                })
                response_data = response.json()  # Tx signature or error(s)
                signature = response_data.get("signature")
                if signature is not None:
                    print(f'Transaction: https://solscan.io/tx/{response_data["signature"]}')
                    should_trigger_sell(data["mint"], pool)
                else:
                    print(f"Transaction not successful: {response_data}")


asyncio.run(subscribe())
