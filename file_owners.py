import logging

# Config log file and verbosity level
logging.basicConfig(
            level=logging.DEBUG,
            filename="file_owners.log",
            filemode="w"
)

def group_by_owners( files_dict ):
    # Make sure the input is a dictionary because the keys must be unique
    if ( type( files_dict ) != dict ):
        logging.error("The input must be a dictionary")
        return {}
    # Make sure the input dictionary is not empty
    # Make sure the input is not composed by lists or other structures
    # (there should be only string pairs)
    if ( len( files_dict ) == 0 ):
        logging.error("The input dictionary is empty")
        return {}
    #
    # Get the unique owner values to create a new dictionary
    # with those keys with an empty list as value 
    owners_dict = { owner : [] for owner in files_dict.values() }
    #
    # Iterate trough the file dictionary and use the value
    # (owner name) to access the list of files in the new dict
    # add the key of the file dict to the new list with append()
    for file_name in files_dict.keys() :
        owner = files_dict[ file_name ]
        owners_dict[ owner ].append( file_name )
    #
    # Return the new dictionary
    return owners_dict

if __name__ == "__main__":    
    files_dict = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'
    }
    print( group_by_owners( files_dict ) )
