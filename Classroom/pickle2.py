import pickle

with open('data.pkl', 'rb') as file:
    loaded_dict = pickle.load(file)

if 'fruits' in loaded_dict:
    print("Data loaded successfully!")
    print("Fruits:", loaded_dict['fruits'])
else:
    print("Data verification failed!")
