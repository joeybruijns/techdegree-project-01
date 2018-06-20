import csv

### FUNCTIONS ###
# divide players function
def divide_players(player, team):
    team["players"].append(player)

    
# write data function
def write_file(team, players):
    # open file
    with open("teams.txt", "w") as file:
        # write to file: team name => player: name, experience and guardian names
        file.write(team + '\n')
        for item in players:
            file.write(str(item["name"]) + ", " + str(item["experience"]) + ", " + str(item["guardian"]) + '\n')
        file.write('\n')  
        
# make sure this code only runs when it's called
if __name__ == '__main__':

    # read the player data from the csv file and turn it into a list with dictionaries    
    with open('soccer_players.csv') as csvfile:
        player_reader = csv.DictReader(csvfile)
        players = list(player_reader)
    
    # two lists, one for players with experience, and one for the other players    
    players_w_experience = []
    other_players = []
    
    # player with experience? append to the experience list
    # player with no experience? append to the other player list
    for player in players:
        player = {
            "name": player["Name"],
            "experience": player["Soccer Experience"],
            "guardian": player["Guardian Name(s)"]}
        if player['experience'] == 'YES':
            players_w_experience.append(player)
        else:
            other_players.append(player)
    
    ### TEAMS ###
    # dictionary with all the teams and the players
    all_teams = {
        "dragons": {
            "team_name": "Dragons",
            "players": []
        },
        "sharks": {
            "team_name": "Sharks",
            "players": []
        },
        "raptors": {
            "team_name": "Raptors",
            "players": []
        }
    }    
    
    # total number of teams
    total_teams = len(all_teams)
    # total number of players per team
    players_per_team = len(players) // total_teams
    # total number of experienced players per team
    experience_per_team = len(players_w_experience) // total_teams
    
    ### DIVIDE PLAYERS ###
    # experienced players divide
    for item in players_w_experience:
        if len(all_teams["dragons"]["players"]) < experience_per_team:
            divide_players(item, all_teams["dragons"])
        elif len(all_teams["sharks"]["players"]) < experience_per_team:
            divide_players(item, all_teams["sharks"])
        else:
            divide_players(item, all_teams["raptors"])    
    
    # non experienced players divide
    for item in other_players:
        if len(all_teams["dragons"]["players"]) < players_per_team:
            divide_players(item, all_teams["dragons"])
        elif len(all_teams["sharks"]["players"]) < players_per_team:
            divide_players(item, all_teams["sharks"])
        else:
            divide_players(item, all_teams["raptors"])   
    
    ### CREATE A TXT FILE ###
    # call the write data function and write to the txt file   
    write_file("Dragons", all_teams["dragons"]["players"])
    write_file("Sharks", all_teams["sharks"]["players"])
    write_file("Raptors", all_teams["raptors"]["players"])
                       
            