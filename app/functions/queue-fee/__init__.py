import azure.functions as func
import logging
import os
from azure.storage.queue import QueueClient
import pandas as pd
import pickle as pkl
import logging

def main(myQueueItem: func.QueueMessage) -> str:
    message = myQueueItem.get_json()
    logging.info(f"The message is {type(message)}")
    df = pd.DataFrame(message, index=[0])
    predictor = pkl.load("../training/random_forest.pkl")
    resp = predictor.predict(df)
    logging.info(resp)
