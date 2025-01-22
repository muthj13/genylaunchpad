from hyperliquid_api import send_mint_transaction

def mint_nft(image_url: str) -> str:
    """
    Logic to create an NFT on the Hyperliquid chain.
    We'll assume we store 'image_url' as part of the token's metadata.
    Returns a transaction hash.
    """
    if not image_url:
        raise ValueError("image_url is required to mint NFT")
    
    # Possibly wrap image_url into IPFS or another storage
    # For now, directly pass it to the chain
    tx_hash = send_mint_transaction(image_url)
    return tx_hash
