import os
import azure.functions as func
import pandas as pd
import joblib
import logging
from dataclasses import dataclass, field


PRED_FEATURES = os.environ.get("PRED_FEATURES").replace(' ', '').split(',')


@dataclass
class Fee():
    """Class to predict the fee from input data
    """
    queue_item: func.QueueMessage
    body: dict = field(default_factory=dict)
    callback_url: str = ""
    data: dict = field(default_factory=dict)
    df: pd.DataFrame = pd.DataFrame()
    result: float = None

    def __post_init__(self) -> None:
        # Get body from message
        self.body = self.queue_item.get_json()
        self.callback_url = self.body.get("callback_url")
        self.data = self.body.get("data")
        logging.info(f"The message is {self.body}")

    def prepare_data(self) -> pd.DataFrame:
        """Prepare the dataframe for prediction

        Returns:
            pd.DataFrame: Dataframe ready for prediction
        """
        self.df = pd.DataFrame(self.data, index=[0])
        self.df['day_of_week'] = pd.Categorical(self.df['day_of_week'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ordered=True)
        self.df["day_of_week_encoded"] = self.df["day_of_week"].cat.codes
        self.df = self.df[PRED_FEATURES]
        return self.df

    def load_and_predict(self) -> float:
        """Load the trained model and predict from input data

        Returns:
            float: predicted fee
        """
        predictor = joblib.load("../../training/random_forest.pkl")
        self.result = predictor.predict(self.df)[0]
        logging.info(f"the result is {self.result}")
        return float(self.result)

    def prepare_response(self) -> (dict, dict):
        """Prepare body and headers for http request

        Returns:
            (dict, dict): body and headers for http response
        """
        body = {"fee": self.result}
        headers = {"Content-Type": "application/json"}
        return body, headers
