import azure.functions as func
import logging
from azure.storage.queue import QueueClient, BinaryBase64EncodePolicy
import json
from schema import Schema, And, Use
from dataclasses import dataclass


@dataclass
class Message():

    def sanitize(self):
        self.schema.validate(self.message)
        self.data_schema.validate(self.message.get("data"))

@dataclass
class ReqMessage(Message):
    """Class to process the http request

    Parent:
        Message
    """
    req: func.HttpRequest
    context: func.Context
    queue_connect_string: str
    message: dict = None
    schema: Schema = Schema(
        {'callback_url': str, 'data': dict}, ignore_extra_keys=True)
    data_schema: Schema = Schema({
        "hour": And(Use(int), lambda n: 0 <= n < 24),
        "rain_level": Use(bool),
        "temperature": Use(int),
        "distance": Use(float),
        "day_of_week": And(str, lambda s: s in {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}),
        "arrondissement_start": And(Use(int), lambda n: 0 < n <= 20),
        "arrondissement_end": And(Use(int), lambda n: 0 < n <= 20)
    })

    def __post_init__(self) -> None:
        # Get body from message
        self.message = self.req.get_json()
        logging.info(f"The message is {self.message}")

    def post_in_queue(self) -> None:
        """Post message in the queue connected to self.queue_connect_string
        """
        # Open queue client
        queue_client = QueueClient.from_connection_string(
            conn_str=self.queue_connect_string, queue_name="fee")

        # Encode message
        message_utf8 = json.dumps((self.message)).encode('utf-8')
        queue_client.message_encode_policy = BinaryBase64EncodePolicy()

        # Send message into the queue
        queue_client.send_message(
            queue_client.message_encode_policy.encode(content=message_utf8))
