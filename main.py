import csv
from pickletools import read_bytes1
from wsgiref.handlers import read_environ
from datetime import datetime

pathOfDeliveriesFile="/home/raveena/Desktop/pythonIPLproject/deliveries.csv"
DeliveriesFile=open(pathOfDeliveriesFile, newline='')
readDeliveriesFile =csv.reader(DeliveriesFile)
headerInDeliveriesFile=next(readDeliveriesFile)
data=[]
for row in readDeliveriesFile:
  match_id=int(row[0])
  inning=int(row[1])
  batting_team=str(row[2])
  bowling_team=str(row[3])
  over=int(row[4])
  ball=int(row[5])
  batsman=str(row[6])
  non_striker=str(row[7])
  bowler=str(row[8])
  is_super_over=int(row[9])
  wide_runs=int(row[10])
  bye_runs=int(row[11])
  legbye_runs=int(row[12])
  noball_runs=int(row[13])
  penalty_runs=int(row[14])
  batsman_runs=int(row[15])
  extra_runs=int(row[16])
  total_runs=int(row[17])
  player_dismissed=str(row[18])
  dismissal_kind=str(row[19])
  fielder=str(row[20])

  data.append([match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder])



pathOfMatchesFile="/home/raveena/Desktop/pythonIPLproject/matches.csv"
matchesFile=open(pathOfMatchesFile, newline='')
readMatchesFile =csv.reader(matchesFile)
headerInMatchesFile=next(readMatchesFile)
#print(headerInMatchesFile)
dataOfMatches=[]
for row in readMatchesFile:
  id=int(row[0])
  season=int(row[1])
  city=str(row[2])
  date=datetime.strptime(row[3],'%Y-%m-%d')
  team1=str(row[4])
  team2=str(row[5])
  toss_winner=str(row[6])
  toss_decision=str(row[7])
  result=str(row[8])
  dl_applied=int(row[9])
  winner=str(row[10])
  win_by_runs=int(row[11])
  win_by_wickets=int(row[12])
  player_of_match=str(row[13])
  venue=str(row[14])
  umpire1=str(row[15])
  umpire2=str(row[16])
  umpire3=str(row[17])

  dataOfMatches.append([id, season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, umpire1, umpire2, umpire3])


def numberOfMatchesPlayedPerYear():
 yearswithTheirCount={}
 for data in dataOfMatches:
    lines=[line for line in data]
    yearIndex=lines[1]
    if yearIndex in yearswithTheirCount.keys():
       yearswithTheirCount[yearIndex]+=1
    else:
       yearswithTheirCount[yearIndex]=1
 print(yearswithTheirCount)    


numberOfMatchesPlayedPerYear()

