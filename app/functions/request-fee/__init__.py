import azure.functions as func
import logging
import os
from azure.storage.queue import QueueClient

CONNECT_STRING ="AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;QueueEndpoint=http://127.0.0.1:10001/devstoreaccount1;TableEndpoint=http://127.0.0.1:10002/devstoreaccount1;"
def main(req: func.HttpRequest) -> str:
    message = req.get_json()
    logging.info(f"The message is {message}")
    queue_client = QueueClient.from_connection_string(
        conn_str=CONNECT_STRING, queue_name="fee")
    queue_client.send_message(message)
    return message