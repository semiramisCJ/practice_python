from collections import Counter
from collections import OrderedDict

### TO DO:
# Avoid repeating code
# Consider the cases when:
# Players tied by score: Wrong answer
# Players tied by games played: Wrong answer 
# Use python's built-in method sorted()

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score
    
    def player_rank(self, rank):
        # Check if rank is valid
        if( type(rank) != int or rank > len( self.standings.keys() ) ):
            print("Invalid index")
            return None
        sorted_list = list(self.standings.keys())
        # Sort players by score
        for player1 in self.standings.keys():
            for player2 in self.standings.keys():
                if player1 == player2: 
                    continue # Skip self-comparison
                # Get player indexes for easy access when they will be switched
                pl1_idx = sorted_list.index( player1 )
                pl2_idx = sorted_list.index( player2 )
                # Store players score in another variable
                score_pl1 = self.standings[player1]['score']
                score_pl2 = self.standings[player2]['score']
                # If the scores are the same, check by number of games and orig order
                if score_pl1 == score_pl2:
                    games_pl1 = self.standings[player1]['games_played']
                    games_pl2 = self.standings[player2]['games_played']
                    # If they have the same number of games, keep the original order
                    if games_pl1 == games_pl2:
                        # We keep the order, so we go to the next comparison
                        # because the initial order is given by the sorted dict keys
                        continue
                    elif( games_pl1 < score_pl2 ):
                        # prev = player1
                        # second = player2
                        # We check the indexes to know if we have to make a switch
                        if( pl1_idx < pl2_idx ):
                            # They are already sorted
                            continue
                        else:
                            # We switch indexes
                            sorted_list[ pl1_idx ] = player2
                            sorted_list[ pl2_idx ] = player1
                    else:
                        # prev = player2
                        # second = player1
                        # We check the indexes to know if we have to make a switch
                        if( pl1_idx > pl2_idx ):
                            # They are already sorted
                            continue
                        else:
                            # We switch indexes
                            sorted_list[ pl1_idx ] = player2
                            sorted_list[ pl2_idx ] = player1
                        
                elif( score_pl1 > score_pl2 ):
                        # prev = player1
                        # second = player2
                        # We check the indexes to know if we have to make a switch
                        if( pl1_idx < pl2_idx ):
                            # They are already sorted
                            continue
                        else:
                            # We switch indexes
                            sorted_list[ pl1_idx ] = player2
                            sorted_list[ pl2_idx ] = player1
                else:
                    # prev = player2
                    # second = player1
                    # We check the indexes to know if we have to make a switch
                    if( pl1_idx > pl2_idx ):
                        # They are already sorted
                        continue
                    else:
                        # We switch indexes
                        sorted_list[ pl1_idx ] = player2
                        sorted_list[ pl2_idx ] = player1
        print(sorted_list)
        return sorted_list[rank-1]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 3)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(3))