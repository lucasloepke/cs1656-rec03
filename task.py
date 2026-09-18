import json
from datetime import datetime, timedelta
import requests
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

class Task(object):
    def __init__(self):
        self.df = pd.read_csv('bank-data.csv')

    def t1(self):
        pdf = self.df[['sex', 'income']]
        return pdf.groupby('sex')['income'].mean()

    def t2(self):
        return pd.crosstab(self.df["save_act"],self.df["mortgage"],margins=True)

    def t3(self):
        df_crosstab = self.t2()
        def get_percent(group):
            x = group / df_crosstab.loc['All', 'All']
            return x

        return df_crosstab.apply(get_percent, axis=1)

if __name__ == "__main__":
    t = Task()
    print("----T1----" + "\n")
    print(str(t.t1()) + "\n")
    print("----T2----" + "\n")
    print(str(t.t2()) + "\n")
    print("----T3----" + "\n")
    print(str(t.t3()) + "\n")
