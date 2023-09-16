import pytest
import pandas as pd
import json
from services.fee_service import Fee


class MockQueueMessage():
    def __init__(self, body):
        self.body = body

    def get_json(self):
        return self.body


# Path from functions/
with open("./mocks/mock_http.json", 'r') as json_file:
    test_message_body = json.load(json_file)

test_message = MockQueueMessage(test_message_body)


def test_fee_class():
    # Create a Fee instance with the input data
    fee_instance = Fee(test_message)

    # Test the prepare_data method
    df = fee_instance.prepare_data()
    assert isinstance(df, pd.DataFrame)

    # Test the load_and_predict method
    result = fee_instance.load_and_predict()
    assert isinstance(result, float)

    # Test the prepare_response method
    response_body, response_headers = fee_instance.prepare_response()
    assert isinstance(response_body, dict)
    assert "fee" in response_body
    assert response_headers == {"Content-Type": "application/json"}

