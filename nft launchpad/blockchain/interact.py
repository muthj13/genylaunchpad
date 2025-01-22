import yaml
import os
import subprocess

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")

def set_token_uri(new_uri: str):
    """
    Example function to call the 'set_token_uri' message on the NFT contract.
    """
    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)

    contract_address = config.get("contract_address", "HLQ_CONTRACT_XYZ")
    network = config.get("network", "testnet")

    # Example hypothetical command
    cmd = [
        "hlq-cli",
        "call",
        "--contract", contract_address,
        "--message", "set_token_uri",
        "--args", new_uri,
        "--network", network
    ]
    print("[interact.py] Setting token URI with:", cmd)
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    # Example usage
    set_token_uri("ipfs://example_new_uri.json")
