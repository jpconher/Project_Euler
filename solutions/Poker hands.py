# Problem 54

import pandas as pd
from collections import Counter

def poker_round(cards):
    values = [card[0] for card in cards]
    suits = [card[1] for card in cards]
    result = {}
    for player in range(0,2):
        # royal flush (10)
        if is_royal_flush(values[0+5*player:5+5*player],
                          suits[0+5*player:5+5*player]):
            result[player] = 10
            continue
        if is_straight_flush(values[0+5*player:5+5*player],
                          suits[0+5*player:5+5*player]):
            result[player] = 9
            continue
        if four_of_a_kind(values[0+5*player:5+5*player]):
            result[player] = 8
            continue
        if full_house(values[0+5*player:5+5*player]):
            result[player] = 7
            continue
        if flush(suits[0+5*player:5+5*player]):
            result[player] = 6
            continue    
        if straight(values[0+5*player:5+5*player]):
            result[player] = 5
            continue  
        if three_of_a_kind(values[0+5*player:5+5*player]):
            result[player] = 4
            continue
        if two_pairs(values[0+5*player:5+5*player]):
            result[player] = 3
            continue
        if one_pair(values[0+5*player:5+5*player]):
            result[player] = 2
            continue
        else:
            result[player] = 1
    if result[0] > result[1]:
        return "player 1"
    elif result[0] < result[1]:
        return "player 2"
    else:
        # replace non-numeric values by numeric values to easy comparison
        values = list(map(lambda x: x.replace('T', '10'), values))
        values = list(map(lambda x: x.replace('J', '11'), values))
        values = list(map(lambda x: x.replace('Q', '12'), values))
        values = list(map(lambda x: x.replace('K', '13'), values))
        values = list(map(lambda x: x.replace('A', '14'), values)) 
        values = [eval(i) for i in values]
        return tiebreaker(result[0],values)
            
def is_royal_flush(values,suits):
    if sorted(values) == ["A","J","K","Q","T"] and len(set(suits)) == 1:
        return True
    else:
        return False

def is_straight_flush(values,suits):
    if len(set(suits)) != 1:
        return False
    else:
        if int(min(values)) < 6:
            if ''.join(sorted(values)) in ['12345', '23456', '34567', '45678', '56789']:
                return True
            else:
                return False
        elif ''.join(sorted(values)) in ['6789T', '789JT', '89JQT', '9JKQT']: # 'AJKQT' would be royal flush 
            return True
        else:
            return False
        
def four_of_a_kind(values):
    if max(Counter(values).values()) == 4:
        return True
    else:
        return False
    
def full_house(values):
    if len(set(values)) == 2:
        return True
    else:
        return False
    
def flush(suits):
    if len(set(suits)) == 1:
        return True
    else:
        return False
    
def straight(values):
    if all(value.isdigit() for value in values):
        if ''.join(sorted(values)) in ['12345', '23456', '34567', '45678', '56789']:
            return True
        else:
            return False
    elif ''.join(sorted(values)) in ['6789T', '789JT', '89JQT', '9JKQT', 'AJKQT']:
        return True
    else:
        return False 

def three_of_a_kind(values):
    if max(Counter(values).values()) == 3:
        return True
    else:
        return False
    
def two_pairs(values):
    if len(set(values)) == 3:
        return True
    else:
        return False
    
def one_pair(values):
    if len(set(values)) == 4:
        return True
    else:
        return False    
    
def tiebreaker(rank, values):
    if rank == 10:
        return "draw"
    elif rank == 9:
        if min(values[0:5]) > min(values[5:10]):
            return "player 1"
        elif min(values[0:5]) < min(values[5:10]):
            return "player 2"
        else:
            return "draw"
    elif rank == 8:
        if (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(4)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(4)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(4)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(4)]):
            return "player 2"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(1)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(1)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(1)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(1)]):
            return "player 2" 
        else:
            return "draw"
    elif rank == 7:
        if (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(3)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(3)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(3)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(3)]):
            return "player 2"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)]):
            return "player 2" 
        else:
            return "draw"  
    elif rank == 6 or rank == 5:
        values_player1 = sorted(values[0:5], reverse = True)
        values_player2 = sorted(values[5:10], reverse = True)
        for i in range(0,5):
            if values_player1[i] > values_player2[i]:
                return "player 1"
            elif values_player1[i] < values_player2[i]:
                return "player 2"
        return "draw"
    elif rank == 4:
        if (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(3)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(3)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(3)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(3)]):
            return "player 2"
        else:
            values_player1 = sorted(values[0:5], reverse = True)
            values_player2 = sorted(values[5:10], reverse = True)
            for i in range(0,5):
                if values_player1[i] > values_player2[i]:
                    return "player 1"
                elif values_player1[i] < values_player2[i]:
                    return "player 2"
                return "draw"
    elif rank == 3:
        if (max(list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)]) > 
        max(list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)])):
            return "player 1"
        elif (max(list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)]) < 
        max(list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)])):
            return "player 2"
        if (min(list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)]) > 
        min(list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)])):
            return "player 1"
        elif (min(list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)]) < 
        min(list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)])):
            return "player 2"
        if (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(1)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(1)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(1)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(1)]):
            return "player 2"    
        else:
            return "draw"
    elif rank == 2:
        if (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)] > 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)]):
            return "player 1"
        elif (list(Counter(values[0:5]).keys())[list(Counter(values[0:5]).values()).index(2)] < 
        list(Counter(values[5:10]).keys())[list(Counter(values[5:10]).values()).index(2)]):
            return "player 2"    
        else:
            values_player1 = sorted(values[0:5], reverse = True)
            values_player2 = sorted(values[5:10], reverse = True)
            for i in range(0,5):
                if values_player1[i] > values_player2[i]:
                    return "player 1"
                elif values_player1[i] < values_player2[i]:
                    return "player 2"
                return "draw"  
    else:
        values_player1 = sorted(values[0:5], reverse = True)
        values_player2 = sorted(values[5:10], reverse = True)
        for i in range(0,5):
            if values_player1[i] > values_player2[i]:
                return "player 1"
            elif values_player1[i] < values_player2[i]:
                return "player 2"
            return "draw"          
    
game = pd.read_csv('C:/Users/O000185/Downloads/p054_poker.txt', delimiter = " ",
                   header = None, dtype = str)
player1_wins = 0
player2_wins = 0
for r in range(0,len(game)):
    result = poker_round(list(game.iloc[r,:]))
    if result == "player 1":
        player1_wins += 1
    if result == "player 2":
        player2_wins += 1