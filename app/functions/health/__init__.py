import azure.functions as func
import logging


# Use absolute import to resolve shared_code modules

# Define an http trigger which accepts ?value=<int> query parameter
# Double the value and return the result in HttpResponse
def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Executing health.')
    return func.HttpResponse(
        body="OK",
        status_code=200
    )
