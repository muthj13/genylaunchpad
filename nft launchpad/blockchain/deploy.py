import subprocess
import yaml
import os

CONFIG_FILE = os.path.join(os.path.dirname(__file__), "config.yaml")

def deploy_contract():
    with open(CONFIG_FILE, 'r') as f:
        config = yaml.safe_load(f)

    wasm_path = config.get("wasm_path", "./target/wasm32-unknown-unknown/release/hyperliquid_nft.wasm")
    deployer = config.get("deployer_address", "HLQ1234ABCD")
    network = config.get("network", "testnet")

    # Fictional command for Hyperliquid
    deploy_cmd = [
        "hlq-cli",
        "deploy",
        "--wasm", wasm_path,
        "--network", network,
        "--from", deployer
    ]

    print("[deploy.py] Deploying contract with command:", " ".join(deploy_cmd))
    subprocess.run(deploy_cmd, check=True)

if __name__ == "__main__":
    deploy_contract()
