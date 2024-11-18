import pickle

def save_data(filename, data_list, data_dict):
    with open(filename, 'wb') as file:
        pickle.dump(data_list, file)
        pickle.dump(data_dict, file)
    print("Data saved successfully.")

def load_data(filename):
    with open(filename, 'rb') as file:
        data_list = pickle.load(file)
        data_dict = pickle.load(file)
    return data_list, data_dict

my_list = [1, 2, 3, 4, 5]
my_dict = {'a': 1, 'b': 2, 'c': 3}

save_data('data.pkl', my_list, my_dict)

loaded_list, loaded_dict = load_data('data.pkl')
print("Loaded List:", loaded_list)
print("Loaded Dictionary:", loaded_dict)
