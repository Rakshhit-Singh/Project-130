import pandas as pd 
import csv 

df = pd.read_csv("final.csv")
del df["luminosity"]
df.to_csv("actual.csv")

print(df.shape)
print(list(df))