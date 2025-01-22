import os
import requests

HLQ_NODE_RPC = os.getenv("HLQ_NODE_RPC", "https://testnet.hyperliquid.example.org")
HLQ_DEPLOYER_KEY = os.getenv("HLQ_DEPLOYER_KEY", "")

def send_mint_transaction(image_url: str) -> str:
    """
    Hypothetical function that calls a 'mint' method on Hyperliquid
    chain with the image URL as metadata.
    Returns a transaction hash (string).
    """
    if not HLQ_DEPLOYER_KEY:
        raise ValueError("No HLQ_DEPLOYER_KEY found in environment")

    # Example JSON payload
    payload = {
        "action": "mint",
        "metadata_uri": image_url,
        "sender_key": HLQ_DEPLOYER_KEY
    }

    # Fictional endpoint for the chain
    endpoint = f"{HLQ_NODE_RPC}/api/mint"

    resp = requests.post(endpoint, json=payload)
    if resp.status_code != 200:
        raise RuntimeError(f"Mint transaction failed: {resp.text}")

    data = resp.json()
    return data.get("transactionHash", "unknown_hash")
