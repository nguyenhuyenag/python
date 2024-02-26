# DataFrame like a 2 dimensional array, or a table with rows and columns
import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)
