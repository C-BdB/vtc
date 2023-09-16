import azure.functions as func
import logging
import os
import json
from services.message_service import ReqMessage


# Global variables
QUEUE_CONNECT_STRING = os.environ.get("QUEUE_CONNECT_STRING")


def main(req: func.HttpRequest, context: func.Context) -> str:
    try:
        req_message = ReqMessage(req=req, context=context, queue_connect_string=QUEUE_CONNECT_STRING)
        req_message.sanitize()
        req_message.post_in_queue()

        # Prepare synchronous response
        body = {
            "status": "OK",
            "request": context.invocation_id
        }
        headers = {"Content-Type": "application/json"}
        status_code = 200

    except Exception as e:
        body = {
            "status": "failed",
            "sub_status": str(e),
            "request": context.invocation_id
        }
        headers = {"Content-Type": "application/json"}
        status_code = 500
        logging.info(f"Exception is: {e}")

    finally:
        # Return Response
        return func.HttpResponse(
            status_code=status_code,
            body=json.dumps(body),
            headers=headers
        )
