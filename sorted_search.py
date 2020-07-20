def count_numbers(sorted_list, less_than):
    # Validate input (non empty list and less_than is an int)
    if( type( less_than ) != int ):
        ## Log an error
        return None
    elif( len( sorted_list ) == 0 ):
        return 0
    ### We can ignore the half that does not have the number 
    ### (The right half when middle is >= less_than)
    ### Repeat halving until:
    ### less_than is found in middle
    ### middle or right_half[0] >= less_than 
    ### or the searching half cannot be halved again (len of 1 or 2)
    # Slice the sorted_list by half
    # to have a right and left sublist
    # if the len is even => equal sizes; check at the middle and decide
    # if the len is odd => check first and last element of each half
    middle = len( sorted_list )//2
    left = sorted_list[ : middle]
    right = sorted_list[ middle : ]
    if( right[ 0 ] < less_than ):
        # Continue the search at the right
        return len( left ) + count_numbers( less_than, right )
    elif( left[ -1 ] < less_than ):
        return len( left )
    
    else:
        return 0
    

if __name__ == "__main__":
    sorted_list = [1, 3, 5, 7]
    print( count_numbers( sorted_list, 4 ) ) # should print 2