import csv

result_req = {
              '2017': {'Sunrisers Hyderabad': 1, 'Rising Pune Supergiant': 1, 'Kolkata Knight Riders': 1, 'Kings XI Punjab': 1},
              '2008': {'Kolkata Knight Riders': 1, 'Chennai Super Kings': 1, 'Delhi Daredevils': 1, 'Royal Challengers Bangalore': 1},
              '2009': {'Mumbai Indians': 1, 'Royal Challengers Bangalore': 1, 'Delhi Daredevils': 2, 'Deccan Chargers': 2, 'Chennai Super Kings': 1, 'Kolkata Knight Riders': 1},
              '2011': {'Chennai Super Kings': 1, 'Rajasthan Royals': 1, 'Royal Challengers Bangalore': 1},
              '2016': {'Rising Pune Supergiants': 1, 'Kolkata Knight Riders': 2, 'Gujarat Lions': 3, 'Royal Challengers Bangalore': 1, 'Mumbai Indians': 1, 'Delhi Daredevils': 2, 'Kings XI Punjab': 1}
              }


def matches_won_eachyear_eachteam():

    season_teams_wins = {}

    with open('data/mock_matches.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:

            if row['season'] in season_teams_wins:

                if row['winner'] in season_teams_wins[row['season']]:

                    season_teams_wins[row['season']][row['winner']] += 1
                else :
                    season_teams_wins[row['season']][row['winner']] = 1
            else :
                season_teams_wins[row['season']] = {}
                season_teams_wins[row['season']][row['winner']] = 1
        
    return season_teams_wins

def main():
    print(matches_won_eachyear_eachteam())

if __name__=='__main__':
    main()