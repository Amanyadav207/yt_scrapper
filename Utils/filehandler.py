# utils/file_handler.py
import pandas as pd

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_to_csv(self, usernames, comments):
        data = {'Username': usernames, 'Comment': comments}
        df = pd.DataFrame(data)
        df.to_csv(self.filename, index=False)
