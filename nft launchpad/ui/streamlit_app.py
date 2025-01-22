import streamlit as st
import requests

API_BASE = "http://localhost:8080"

def main():
    st.title("Hyperliquid AI-NFT Launchpad")
    st.write("Generate and mint NFTs on the fictional Hyperliquid blockchain.")

    prompt = st.text_input("Prompt", "A futuristic neon city with flying cars")
    resolution = st.selectbox("Resolution", [256, 512, 1024], index=1)
    if st.button("Generate"):
        with st.spinner("Generating image..."):
            resp = requests.post(f"{API_BASE}/generate", json={
                "prompt": prompt,
                "resolution": resolution
            })
            if resp.status_code == 200:
                data = resp.json()
                if "imageUrl" in data:
                    st.image(data["imageUrl"], caption="AI-Generated Preview")
                    if st.button("Mint This NFT"):
                        mint_resp = requests.post(f"{API_BASE}/mint", json={
                            "imageUrl": data["imageUrl"]
                        })
                        if mint_resp.status_code == 200:
                            tx_data = mint_resp.json()
                            st.success(f"NFT Minted! TX Hash: {tx_data['transactionHash']}")
                        else:
                            st.error(f"Minting failed: {mint_resp.text}")
                else:
                    st.error("No imageUrl in the response.")
            else:
                st.error(f"Generation failed: {resp.text}")

if __name__ == "__main__":
    main()
