import pytest
from unittest.mock import patch
from ai_nft.nft_minting import mint_nft

@patch("ai_nft.nft_minting.send_mint_transaction")
def test_mint_nft(mock_send_tx):
    mock_send_tx.return_value = "HLQ987654321"
    tx_hash = mint_nft("http://example.com/gen_image.png")
    assert tx_hash == "HLQ987654321"

def test_mint_nft_no_image_url():
    with pytest.raises(ValueError, match="image_url is required"):
        mint_nft("")
