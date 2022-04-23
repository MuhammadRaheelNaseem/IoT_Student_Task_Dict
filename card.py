import random
card = {
        'AD':5, 'QD':25,'JD':7,'KD':30,
        'AC':20,'QC':10,'JC':37,'KC':40,
        'AS':70,'QS':10,'JS':65,'KS':100,
        'AH':10,'QH':20,'JH':30,'KH':40,
        }

print(card)
keys = []
values = []
pl_1 = []
pl_2 = []
pl_3 = []
pl_4 = []

for key in card:
    keys.append(key)

random.shuffle(keys)

for i in range(0,4):
    pl_1.append(keys[i])
for j in range(4,8):
    pl_2.append(keys[j])
for k in range(8,12):
    pl_3.append(keys[k])
for l in range(12,16):
    pl_4.append(keys[l])
print(keys)
print("Player 1 :",pl_1)
print("Player 2 :",pl_2)
print("Player 3 :",pl_3)
print("Player 4 :",pl_4)

# count=0
while True:
#     count+=1
    print("Round No # 1")
    ope = input("Please select operation: \n1.) Play game \n2.) Exit game")
    if ope == '1':
#         player 1 turn
        print("*************Player 1! Please Select Card *************")
        num = 0
        for i in pl_1:
            num+=1
            print(f"{num}.) {i}")
        select_card = input("Enter Card Number: ")
        if select_card == '1':
            print(f"You Select {pl_1[0]} Card")
        elif select_card == '2':
            print(f"You Select {pl_1[1]} Card")
        elif select_card == '3':
            print(f"You Select {pl_1[2]} Card")
        elif select_card == '4':
            print(f"You Select {pl_1[3]} Card")
        else:
            print("Invalid Enter!")
#         player 2 turn
        print("*************Player 2! Please Select Card *************")
        num = 0
        for j in pl_2:
            num+=1
            print(f"{num}.) {j}")
        select_card_2 = input("Enter Card Number: ")
        if select_card_2 == '1':
            print(f"You Select {pl_2[0]} Card")
        elif select_card_2 == '2':
            print(f"You Select {pl_2[1]} Card")
        elif select_card_2 == '3':
            print(f"You Select {pl_2[2]} Card")
        elif select_card_2 == '4':
            print(f"You Select {pl_2[3]} Card")
        else:
            print("Invalid Enter!")
#         Condition for checking who player win the match
#         if select_card == pl_1[0] 
        break
    elif ope == '2':
        print("Quit Game!")
        break
    else:
        print("Invalid Enter!")
        break
