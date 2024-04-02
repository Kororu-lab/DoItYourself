import pandas as pd

class DataStreamer:
    def __init__(self, file_path, usecols, text_preprocessor):
        self.file_path = file_path
        self.usecols = usecols
        self.text_preprocessor = text_preprocessor

    def stream_data(self):
        for chunk in pd.read_csv(self.file_path, usecols=self.usecols, chunksize=10000):
            chunk.fillna('', inplace=True)
            for _, row in chunk.iterrows():
                text = row['body'] if 'body' in row else row['title'] + ' ' + row.get('selftext', '')
                processed_text = self.text_preprocessor.preprocess_text(text)
                yield row['subreddit'], row['author'], processed_text
