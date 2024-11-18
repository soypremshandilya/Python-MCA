import pickle
data = {"name": "Alice", "age": 30, "occupation": "Engineer"}
open("data.pickle", "wb") as file:
pickle.dump(data, file)