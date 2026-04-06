import pandas as pd
import numpy as np

class AnalyticsEngine:

    def __init__(self, data):
        self.df = pd.DataFrame(
            data,
            columns=["ID","Name","Age","Department","Salary","Performance"]
        )

    def department_salary(self):
        return self.df.groupby("Department")["Salary"].mean()

    def numpy_stats(self):
        sal = self.df["Salary"].values

        return {
            "Mean": np.mean(sal),
            "Median": np.median(sal),
            "Std Dev": np.std(sal),
            "Correlation":
                np.corrcoef(self.df["Salary"],
                            self.df["Performance"])[0,1]
        }

    def normalize(self):
        self.df["Normalized"] = (
            (self.df["Salary"] - self.df["Salary"].min()) /
            (self.df["Salary"].max() - self.df["Salary"].min())
        )
        return self.df