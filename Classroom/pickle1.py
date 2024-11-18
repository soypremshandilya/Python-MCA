import pickle

my_list = ['apple', 'banana', 'cherry']
my_dict = {'fruits': my_list}

with open('data.pkl', 'wb') as file:
    pickle.dump(my_dict, file)

print("Data has been saved to 'data.pkl'")
