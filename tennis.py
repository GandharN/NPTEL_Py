import re

ip=[]

while True:
    line = raw_input()
    if line:
        ip.append(line)
    else:
        break
	
players={}

for match in ip:
	parts=match.split(':')
	winner=parts[0]
	loser=parts[1]
	score=parts[2]

	if winner not in players:
		players[winner]={}
	if loser not in players:
		players[loser]={}

	sets=score.split(',')

	players[winner]['3_sets_won']=players[winner].get('3_sets_won',0)
	players[loser]['3_sets_won']=players[loser].get('3_sets_won',0)
	players[winner]['5_sets_won']=players[winner].get('5_sets_won',0)
	players[loser]['5_sets_won']=players[loser].get('5_sets_won',0)

	if len(sets)<=3:
		players[winner]['3_sets_won']=players[winner].get('3_sets_won',0)+1
	if len(sets)>3:
		players[winner]['5_sets_won']=players[winner].get('5_sets_won',0)+1
	
	for st in sets:
		#NUMBER OF GAMES WON AND LOST
		players[winner]['games_won']=players[winner].get('games_won',0)+int(st[0])
		players[winner]['games_lost']=players[winner].get('games_lost',0)+int(st[2])
		
		players[loser]['games_won']=players[loser].get('games_won',0)+int(st[2])
		players[loser]['games_lost']=players[loser].get('games_lost',0)+int(st[0])


		#NUMBER OF SETS WON OR LOST
		if int(st[0])>int(st[2]):
			players[winner]['sets_won']=players[winner].get('sets_won',0)+1
			players[loser]['sets_lost']=players[loser].get('sets_lost',0)+1

		else:
			players[loser]['sets_won']=players[loser].get('sets_won',0)+1
			players[winner]['sets_lost']=players[winner].get('sets_lost',0)+1			
		
	#FOR LOOP TO GO THROUGH SCORE ENDS

dictsort=sorted(players.keys(), key=lambda x: (players[x]['5_sets_won'],players[x]['3_sets_won',] players[x]['sets_won'], players[x]['games_won'],-players[x]['sets_lost'],-players[x]['games_lost']), reverse=True)

#print(dictsort)

for player in dictsort:
	print(player, players[player]['5_sets_won'], players[player]['3_sets_won'], players[player]['sets_won'], players[player]['games_won'], players[player]['sets_lost'], players[player]['games_lost'])

#print(players)
