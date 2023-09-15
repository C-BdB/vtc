import azure.functions as func
import logging
import os
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy
import json

QUEUE_CONNECT_STRING = os.environ.get("QUEUE_CONNECT_STRING")
def main(req: func.HttpRequest, context: func.Context) -> str:
    message = req.get_json()
    logging.info(f"The message is {message}")
    queue_client = QueueClient.from_connection_string(
        conn_str=QUEUE_CONNECT_STRING, queue_name="fee")
    message_utf8 = json.dumps((message)).encode('utf-8')
    queue_client.message_encode_policy = BinaryBase64EncodePolicy()
    queue_client.send_message(
        queue_client.message_encode_policy.encode(content=message_utf8))
    body = {
        "status": "OK",
        "request": context.invocation_id
    }
    headers = {"Content-Type": "application/json"}
    return func.HttpResponse(
        status_code=200,
        body=json.dumps(body),
        headers=headers
    )