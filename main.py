import csv
from pickletools import read_bytes1
from wsgiref.handlers import read_environ
from datetime import datetime


pathOfDeliveriesFile="/home/raveena/Desktop/iplProject/deliveries.csv"
DeliveriesFile=open(pathOfDeliveriesFile, newline='')
readDeliveriesFile =csv.reader(DeliveriesFile)
headerInDeliveriesFile=next(readDeliveriesFile)
dataofDeliveries=[]
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

  dataofDeliveries.append([match_id, inning, batting_team, bowling_team, over, ball, batsman, non_striker, bowler, is_super_over, wide_runs, bye_runs, legbye_runs, noball_runs, penalty_runs, batsman_runs, extra_runs, total_runs, player_dismissed, dismissal_kind, fielder])



pathOfMatchesFile="/home/raveena/Desktop/iplProject/matches.csv"
matchesFile=open(pathOfMatchesFile, newline='')
readMatchesFile =csv.reader(matchesFile)
headerInMatchesFile=next(readMatchesFile)
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
 with open("outputNumberOfMatchesPlayedPerYear..txt", 'wt') as f:
  print(yearswithTheirCount, file=f)


numberOfMatchesPlayedPerYear()

def numberOfMatchesWonByAllTeamsOverAllTheYears():
  teamsAndItsWonCount={}
  for data in dataOfMatches:
    lines=[line for line in data]
    wonTeamNames=lines[10]
    if wonTeamNames in teamsAndItsWonCount.keys():
       teamsAndItsWonCount[wonTeamNames]+=1
    else:
       teamsAndItsWonCount[wonTeamNames]=1
  print(teamsAndItsWonCount)
  with open("outputNumberOfMatchesWonByAllTeamsOverAllTheYears..txt", 'wt') as f:
   print(teamsAndItsWonCount, file=f)
  
  

numberOfMatchesWonByAllTeamsOverAllTheYears()

def getExtraRunsConcededPerTeamIn2016():
    ids=[]
    for data in dataOfMatches:
     lines=[line for line in data]
     years=lines[1]
     if years==2016:
      ids.append(lines[0])
    extraRunsConcededPerYear={}
    for data in dataofDeliveries:
     lines=[line for line in data]
     idsInDeliveries=lines[0]
     bowlingTeam=lines[3]
     extraRuns=lines[16]
     if idsInDeliveries in ids:
        if bowlingTeam in extraRunsConcededPerYear.keys():
          extraRunsConcededPerYear[bowlingTeam]+=extraRuns
        else :
          extraRunsConcededPerYear[bowlingTeam]=extraRuns 
    print(extraRunsConcededPerYear)       
    with open("outputExtraRunsConcededPerTeamIn2016..txt", 'wt') as f:
     print(extraRunsConcededPerYear, file=f)         

getExtraRunsConcededPerTeamIn2016()    

def topEconomicalBowlersIn2015():
    ids=[]
    for data in dataOfMatches:
     lines=[line for line in data]
     years=lines[1]
     if years==2015:
      ids.append(lines[0]) 
    totalBalls={}  
    for data in dataofDeliveries:
     lines=[line for line in data]
     idsInDeliveries=lines[0]
     bowlerr=str(lines[8])
     if idsInDeliveries in ids:
       if bowlerr in totalBalls.keys():
        totalBalls[bowlerr]+=1
       else:
        totalBalls[bowlerr]=1 
    totalRuns={}  
    for data in dataofDeliveries:
      lines=[line for line in data]
      idsInDeliveries=lines[0]
      runs=lines[17]
      bowler=lines[8]
      if idsInDeliveries in ids:
       if bowler in totalRuns.keys():
        totalRuns[bowler]+=runs
       else:
        totalRuns[bowler]=runs
    economy={}
    for key in totalBalls.keys():
        balls =float(totalBalls.get(key))
        runs=float(totalRuns.get(key))
        economyRate = runs / (balls / 6);
        trim="%.2f" % economyRate
        economy[key]=trim 
    result=sorted(economy.items(), key=lambda kv:float(kv[1]))
    economicalBowlers=[]
    i=0
    while i<5:
       economicalBowlers.append(result[i])
       i+=1
    print(economicalBowlers)  
    with open("outputTopEconomicalBowlersIn2015..txt", 'wt') as f:
     print(economicalBowlers, file=f)
    

topEconomicalBowlersIn2015()    


def getWinnerTeamNamesIn2017():
    teamNames=set()
    for data in dataOfMatches:
     lines=[line for line in data]
     years=lines[1]
     winners=lines[10]
     if years==2017:
       teamNames.add(winners)
    print(teamNames)
    with open("outputWinnerTeamNamesIn2017..txt", 'wt') as f:
     print(teamNames, file=f)      
getWinnerTeamNamesIn2017()      