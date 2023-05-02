import csv


ids = set(list(range(518 , 577)))

req_result ={'RN ten Doeschate': 4, 'J Yadav': 4,
             'R Ashwin': 5, 'V Kohli': 5, 'Parvez Rasool': 6, 
             'MC Henriques': 6, 'S Nadeem': 6, 'Z Khan': 6, 
             'M Morkel': 7, 'SP Narine': 7}


def economical_bowlers():
    """Doc"""

    bowler_economy = {}
    with open('data/mock_deliveries.csv',encoding='utf-8') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            
            if int(row['match_id']) in ids:
                
                if row['bowler'] in bowler_economy:
                    if int(row['wide_runs']) == 0 and int(row['noball_runs']) == 0:
                        bowler_economy[row['bowler']][0] += 1
                    bowler_economy[row['bowler']][1] += int(float(row['total_runs']))
                else :
                    bowler_economy[row['bowler']] = [0]*2
                    if int(row['wide_runs']) == 0 and int(row['noball_runs']) == 0:
                        bowler_economy[row['bowler']][0] += 1
                    bowler_economy[row['bowler']][1] += int(float(row['total_runs']))

        for bowler , list_count in bowler_economy.items():
            bowler_economy[bowler] = int(list_count[1]/(list_count[0]/6))

        top_ten_bowler_economy = dict(sorted(bowler_economy.items() , key= lambda x:x[1])[:10])
    
    return top_ten_bowler_economy



def main():
    print(economical_bowlers())
if __name__=='__main__':
    main()


