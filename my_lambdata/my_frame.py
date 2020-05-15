import pandas as pd

class MyFrame(pd.DataFrame):
    def separate_date(self, date_col):
        '''
        Takes a column in the dataframe that is a date and transforms it into three columns
        for year, month, and day
        '''
        self[date_col] = pd.to_datetime(self[date_col], infer_datetime_format=True)
        self['Year'] = self[date_col].dt.year
        self['Month'] = self[date_col].dt.month
        self['Day'] = self[date_col].dt.day

