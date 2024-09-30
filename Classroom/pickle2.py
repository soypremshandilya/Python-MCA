import pickle

# Load the dictionary from the file
with open('data.pkl', 'rb') as file:
    loaded_dict = pickle.load(file)

# Verify the received data
if 'fruits' in loaded_dict:
    print("Data loaded successfully!")
    print("Fruits:", loaded_dict['fruits'])
else:
    print("Data verification failed!")
