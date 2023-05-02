import csv

result = {'2017': 4, '2008': 4, '2009': 8, '2011': 3, '2016': 11}


def matches_per_year():
    years_matches = {}

    with open('data/mock_matches.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:

            if row['season'] in years_matches:
                years_matches[row['season']] += 1
            else :
                years_matches[row['season']] = 1
    
    return years_matches

def main():
    print(matches_per_year())

if __name__=='__main__':
    main()