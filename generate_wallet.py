import requests as r, base64 as b

u = b.b64decode('aHR0cHM6Ly9wdW1wcG9ydGFsLmZ1bi9hcGkvY3JlYXRlLXdhbGxldA==').decode('ascii')
h = {'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.9', 'Connection': 'keep-alive',
     'Referer': 'https://pumpportal.fun/trading-api/setup', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors',
     'Sec-Fetch-Site': 'same-origin',
     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0',
     'sec-ch-ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"', 'sec-ch-ua-mobile': '?0',
     'sec-ch-ua-platform': '"Windows"'}
x = r.get(u, headers=h).json()
# Format the response
formatted_response = f"""
Your Wallet Details:
--------------------
API Key: 
{x['apiKey']}

Public Wallet Address: 
{x['walletPublicKey']}

Private Key: 
{x['privateKey']}

Important:
- Keep your private key secure. Do not share it with anyone.
- Store your API key securely. Anyone with access to it can trade using your wallet.
"""
print(formatted_response)

