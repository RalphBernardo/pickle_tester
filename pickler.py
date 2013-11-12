import pickle

def list_pickler(my_list, file_pickled):
    """
    list file -> None
    pickles the list into the file
    """
    pickle.dump(my_list, file_pickled)

def unpickler(file_pickled):
    """
    file -> object
    unpickles file data and returns the relevant object
    """
    my_object = pickle.load(file_pickled)
    return my_object