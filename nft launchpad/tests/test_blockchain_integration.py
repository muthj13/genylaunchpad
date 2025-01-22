import pytest
from unittest.mock import patch
from ai_nft.hyperliquid_api import send_mint_transaction

@patch("ai_nft.hyperliquid_api.requests.post")
def test_send_mint_transaction(mock_post):
    mock_response = {
        "transactionHash": "HLQ1234567890"
    }
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_response

    tx_hash = send_mint_transaction("http://example.com/image.png")
    assert tx_hash == "HLQ1234567890"

@patch("ai_nft.hyperliquid_api.requests.post")
def test_send_mint_transaction_fail(mock_post):
    mock_post.return_value.status_code = 400
    mock_post.return_value.text = "Some error"

    with pytest.raises(RuntimeError, match="Mint transaction failed"):
        send_mint_transaction("http://example.com/image.png")
