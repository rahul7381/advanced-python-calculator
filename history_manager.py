import pandas as pd
import os

class HistoryManager:
    def __init__(self, filename="history.csv"):
        self.filename = filename

    def save(self, data):
        df = pd.DataFrame(data, columns=["A", "B", "Operation", "Result"])
        df.to_csv(self.filename, index=False)

    def load(self):
        if os.path.exists(self.filename):
            return pd.read_csv(self.filename)
        return None

