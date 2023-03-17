import pandas as pd

# print("Pandas version:", pd.__version__)

dataset = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

frame = pd.DataFrame(dataset)

print(frame)
