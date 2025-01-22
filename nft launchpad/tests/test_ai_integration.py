import pytest
from unittest.mock import patch
from ai_nft.image_generation import generate_image

@pytest.mark.parametrize("resolution", [256, 512, 1024])
@patch("ai_nft.image_generation.requests.post")
def test_generate_image(mock_post, resolution):
    mock_resp = {
        "data": [
            {"url": f"https://fake_cdn.com/gen_image_{resolution}.png"}
        ]
    }
    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = mock_resp

    result_url = generate_image("test prompt", resolution=resolution)
    assert f"gen_image_{resolution}.png" in result_url
    mock_post.assert_called_once()

def test_generate_image_no_api_key(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    with pytest.raises(ValueError, match="OpenAI API key not found"):
        generate_image("some prompt")
