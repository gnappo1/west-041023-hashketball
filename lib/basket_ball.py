# import ipdb
from functools import reduce

def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

#! Helpers
def all_players_in_dict():
    all_players_dict = {}
    for team in ['home', 'away']:
        for player in game_dict()[team]['players']:
            all_players_dict[player.get('name')] = player
    return all_players_dict
# print(all_players_in_dict())

def all_players_in_list():
    return game_dict().get('home').get('players') + game_dict().get('away').get('players')
# print(all_players_in_list())

#! Deliverables
def num_points_per_game(player_name):
    game_obj = game_dict()
    for key in game_obj.keys():
        team_players = game_obj.get(key).get('players')
        # filtered_players_scores = [player.get('points_per_game') for player in team_players if player_name == player.get('name')]
        # if len(filtered_players_scores) > 0:
        if filtered_players_scores := [
            player.get('points_per_game')
            for player in team_players
            if player_name == player.get('name')
        ]:
            return filtered_players_scores[0]
    return "Player is not in any teams!"

# print(num_points_per_game("Davis Bertanssss"))

def player_age_old(player_name):
    game_obj = game_dict()
    for key in game_obj.keys():
        team_players = game_obj.get(key).get('players')
        # filtered_players_scores = [player.get('points_per_game') for player in team_players if player_name == player.get('name')]
        # if len(filtered_players_scores) > 0:
        if filtered_players_scores := [
            player.get('age')
            for player in team_players
            if player_name == player.get('name')
        ]:
            return filtered_players_scores[0]
    return "Player is not in any teams!"

def player_age(player_name):
    return all_players_in_dict().get(player_name).get('age') if all_players_in_dict().get(player_name) else "Player's not in here!!!"
    # research options for the safe navigation operator!
    
    # if player_name in all_players_in_dict().keys():
    #     return all_players_in_dict().get(player_name).get('age')
    # return "Player's not in our teams!"

print(player_age("Davis Bertans"))

def logic_for_reduce(sum, el):
    return sum + el

def average_rebounds_by_shoe_brand():
    total_rebounds_by_brand = {}
    for player in all_players_in_list():
        current_player_brand = player.get('shoe_brand')
        current_player_rebounds = player.get('rebounds_per_game')
        
        #line under: check if the brand is already a key inside the final dict
        if current_player_brand in total_rebounds_by_brand:
            total_rebounds_by_brand.get(current_player_brand).append(current_player_rebounds)
        else:
            total_rebounds_by_brand[current_player_brand] = [current_player_rebounds]
    for k, v in total_rebounds_by_brand.items():
        avg = reduce(lambda sum, el: sum + el, v) / len(v)
        # print(f"{k}: {format(avg, '.2f')}")
        print(f"{k}: {avg:.2f}")
        
average_rebounds_by_shoe_brand()