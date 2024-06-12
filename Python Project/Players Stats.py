#players status and current score
#JSON

from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links

def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    data = get(BASE_URL + scoreboard).json()['games']
    
    for game in data:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        #printer.pprint(data.keys())
        print('-----------------------------------------')
        print(f'{home_team['triCode']} vs {away_team['triCode']}')
        print(f'{home_team['score']} vs {away_team['score']}')
        print(f'{clock} - {period['current']}')
        
def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != "Team", teams))
    teams.sort(key=lambda x: int(x['ppg']['avg']))

    #printer.pprint(teams[0].key())
    for i, team in enumerate(teams):
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']

        print(f'{i+1}. {name} - {nickname} - {ppg}')


#printer.pprint(get_links())
#get_scoreboard()



