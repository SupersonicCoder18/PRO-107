import pandas as pd
import csv
import plotly.express as ps

df = pd.read_csv("Students.csv")
print(df.groupby("level")["attempt"].mean())
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()
fig = ps.scatter(mean, x = "student_id", y = "level", color = "attempt", size = "attempt")
fig.show()