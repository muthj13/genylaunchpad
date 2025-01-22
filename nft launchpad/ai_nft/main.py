import os
from flask import Flask, request, jsonify
from image_generation import generate_image
from nft_minting import mint_nft
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/generate", methods=["POST"])
def generate_endpoint():
    data = request.json
    prompt = data.get("prompt")
    resolution = data.get("resolution", 512)
    if not prompt:
        return jsonify({"error": "Missing prompt"}), 400
    
    try:
        image_url = generate_image(prompt, resolution=resolution)
        return jsonify({"imageUrl": image_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/mint", methods=["POST"])
def mint_endpoint():
    data = request.json
    image_url = data.get("imageUrl")
    if not image_url:
        return jsonify({"error": "Missing imageUrl"}), 400
    
    try:
        tx_hash = mint_nft(image_url)
        return jsonify({"transactionHash": tx_hash})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # e.g., read port from environment
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
