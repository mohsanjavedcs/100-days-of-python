import pandas as pd

df = pd.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

# print(df)

# print(df["Primary Fur Color"].value_counts())

data = pd.DataFrame()

grey = len(df[df["Primary Fur Color"] == "Gray"])
red = len(df[df["Primary Fur Color"] == "Cinnamon"])
black = len(df[df["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey, red, black]
}

data = pd.DataFrame(data_dict)

data.to_csv("Squirrel_Counts.csv")