import json
from unittest.mock import MagicMock
import pytest

from api.predict import bigfive_handler, preview_handler


@pytest.fixture
def mock_request():
    return MagicMock()

def test_bigfive_handler(mock_request):
    # Set the mock request method and JSON data
    mock_request.method = 'POST'
    mock_request.get_json.return_value = "What this film has is its realism , you really do get the feeling"

    # Call the bigfive_handler function with the mock request
    response = bigfive_handler(mock_request)

    # Assert that the response has the expected status code
    assert response.status_code == 200

    # Assert that the response contains the expected prediction keys
    response_json = json.loads(response.get_body())
    prediction = response_json["prediction"]
    assert "pred_sOPN" in prediction
    assert "pred_sOPN_normalized" in prediction
    assert "pred_sCON" in prediction
    assert "pred_sCON_normalized" in prediction
    assert "pred_sEXT" in prediction
    assert "pred_sEXT_normalized" in prediction
    assert "pred_sAGR" in prediction
    assert "pred_sAGR_normalized" in prediction
    assert "pred_sNEU" in prediction
    assert "pred_sNEU_normalized" in prediction
    assert "pred_sentiment" in prediction

def test_preview_handler():
    # Create a mock request object
    mock_request = MagicMock()

    # Call the preview_handler function with the mock request
    response = preview_handler(mock_request)

    # Assert that the response has the expected status code
    assert response.status_code == 200

    # Assert that the response contains the expected prediction keys
    response_json = json.loads(response.get_body())
    prediction = response_json["prediction"]
    assert "pred_sOPN" in prediction
    assert "pred_sOPN_normalized" in prediction
    assert "pred_sCON" in prediction
    assert "pred_sCON_normalized" in prediction
    assert "pred_sEXT" in prediction
    assert "pred_sEXT_normalized" in prediction
    assert "pred_sAGR" in prediction
    assert "pred_sAGR_normalized" in prediction
    assert "pred_sNEU" in prediction
    assert "pred_sNEU_normalized" in prediction
    assert "pred_sentiment" in prediction
