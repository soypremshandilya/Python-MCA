import pickle

# Sample data: list of items
my_list = ['apple', 'banana', 'cherry']
my_dict = {'fruits': my_list}

# Save the dictionary to a file using pickle
with open('data.pkl', 'wb') as file:
    pickle.dump(my_dict, file)

print("Data has been saved to 'data.pkl'")
