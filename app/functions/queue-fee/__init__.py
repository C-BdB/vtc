import azure.functions as func
import requests
from services.fee_service import Fee

def main(myQueueItem: func.QueueMessage) -> str:
    fee = Fee(myQueueItem)
    fee.prepare_data()
    fee.load_and_predict()
    body, headers = fee.prepare_response()
    requests.post(url=fee.callback_url, json=body, headers=headers)
