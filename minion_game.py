import unicodedata

def minion_game( string ):
    """ This function prints the winner and their score in the minion minion_game
    Each player earns points for the number of occurrences of their substrings
    in the string. Stuart gets the words that begin with a consonant, whereas
    Kevin gets the words that begin with a vowel """
    # Validate and clean input
    string = str( string.strip().upper() )
    string = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode('ASCII')
    if len(string) <= 1:
        print("Draw")
        return
    # Create empty lists and vowel list
    stuart_substrings = [] # words starting with a consonant
    kevin_substrings = [] # words starting with a vowel
    vowels = ['A', 'E', 'I', 'O', 'U']
    # Iterate through the word and classify substrings for each player
    for i in range( 0, len( string ) + 1 ):
        for j in range( 0, len( string ) + 1 ):
            if i < j:
                substring = string[i:j]
                if( substring[0] in vowels ):
                    kevin_substrings.append( substring )
                else:
                    stuart_substrings.append( substring )

    # Count the points for unique kevin_substrings
    kevin_substrings = list( set ( kevin_substrings ) )
    stuart_substrings = list( set ( stuart_substrings ) )
    kevin_points = sum( [ string.count( substring ) for substring in kevin_substrings ] )
    stuart_points = sum( [ string.count( substring ) for substring in stuart_substrings ] )
    # Define the winner
    if kevin_points == stuart_points:
        print( "Draw" )
    elif kevin_points > stuart_points:
        print( "Kevin " + str(kevin_points) )
        print(kevin_substrings)
        print([ string.count( substring ) for substring in kevin_substrings ])
    else:
        print( "Stuart " + str(stuart_points) )
    return

minion_game('BAANANAS')
