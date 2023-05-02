import csv

req_result = {'Rising Pune Supergiants': 30, 'Mumbai Indians': 26,
              'Kolkata Knight Riders': 30, 'Delhi Daredevils': 24,
              'Gujarat Lions': 19, 'Kings XI Punjab': 27, 'Sunrisers Hyderabad': 12,
              'Royal Challengers Bangalore': 25}

def get_match_id():
    """Returns the match id's of 2016 year"""
    ids = set()
    with open('data/mock_matches.csv',encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:

            if row['season'] == '2016':
                ids.add(row['id'])

    return ids
def extras_eachteam():
    """Function calculate extras of each team"""

    eachteam_extras = {}

    ids = get_match_id()
    with open('data/mock_deliveries.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:

            if row['match_id'] in ids:

                if row['bowling_team'] in eachteam_extras:
                    eachteam_extras[row['bowling_team']] += int(float(row['extra_runs']))
                else :
                    eachteam_extras[row['bowling_team']] = int(float(row['extra_runs']))
    return eachteam_extras



def main():
    """Main function """
    print(extras_eachteam())

if __name__=='__main__':
    main()
