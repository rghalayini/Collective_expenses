a=input("Enter the date from which calculations will begin in DD-MM-YY format: ")
b=input("Enter the date from which calculations will end in DD-MM-YY format: ")
import datetime
d1=datetime.datetime.strptime(a,'%d-%m-%y')
d2=datetime.datetime.strptime(b,'%d-%m-%y')
D=(d2-d1).days
xp1=int(input("Enter the expenses of person 1: "))
xp2=int(input("Enter the expenses of person 2: "))
xp3=int(input("Enter the expenses of person 3: "))
xp4=int(input("Enter the expenses of person 4: "))
xp5=int(input("Enter the expenses of person 5: "))
xlist=[xp1, xp2, xp3, xp4, xp5]
x=sum(xlist)
print("The total sum of the household expenses during the specified time is", x, "SEK")
np1=int(input("Enter the nights when person 1 was away: "))
np2=int(input("Enter the nights when person 2 was away: "))
np3=int(input("Enter the nights when person 3 was away: "))
np4=int(input("Enter the nights when person 4 was away: "))
np5=int(input("Enter the nights when person 5 was away: "))
dp1=D-np1
dp2=D-np2
dp3=D-np3
dp4=D-np4
dp5=D-np5
Dlist=[dp1, dp2, dp3, dp4, dp5]
Dtotal=sum(Dlist)
xdp1=int((x/Dtotal)*dp1)
xdp2=int((x/Dtotal)*dp2)
xdp3=int((x/Dtotal)*dp3)
xdp4=int((x/Dtotal)*dp4)
xdp5=int((x/Dtotal)*dp5)
xdplist=[xp1, xp2, xp3, xp4, xp5]
xdpsum=sum(xdplist)
print("During the period of ", D, "days, person 1 has a total expenses of: ", xdp1, "SEK")
print("During the period of ", D, "days, person 2 has a total expenses of: ", xdp2, "SEK")
print("During the period of ", D, "days, person 3 has a total expenses of: ", xdp3, "SEK")
print("During the period of ", D, "days, person 4 has a total expenses of: ", xdp4, "SEK")
print("During the period of ", D, "days, person 5 has a total expenses of: ", xdp5, "SEK")
expenses_total_perday={"Person 1":xdp1, "Person 2": xdp2, "Person 3":xdp3, "Person 4": xdp4, "Person 5":xdp5}
contributions={"Person 1":xp1, "Person 2": xp2, "Person 3":xp3, "Person 4": xp4, "Person 5":xp5}
paid_more={}
paid_less={}
for (k1, v1), (k2, v2) in zip(contributions.items(), expenses_total_perday.items()):
    if v1 > v2:
        paid_more[k1]=v1-v2
    elif v1 < v2:
        paid_less[k1]=v2-v1
    else:
        None
print("The people who paid more:")
for k1,v1 in paid_more.items():
    print(k1,":", v1, "SEK")
print("The people who paid less:")
for k1,v1 in paid_less.items():
    print(k1,":", v1, "SEK")

remainder_topay={}
remainder_toget={}
no_debt={}
for k1, v1 in paid_more.items():
    for k2, v2 in paid_less.items():
        if v1==v2 and k1 not in no_debt and k2 not in no_debt:
            no_debt[k1]=0
            no_debt[k2]=0
            print(k2, "should pay ", k1,":", v1, "SEK")
        else:
            None 

for k1, v1 in paid_more.items():
    for k2, v2 in paid_less.items():   
        if k1 not in no_debt and k2 not in no_debt:
            if k1 not in remainder_toget and k2 not in remainder_topay:
                if v2>v1:
                    remainder_topay[k2]=v2-v1
                    no_debt[k1]=0
                    print(k2, "should pay ", k1,":", v1, "SEK")
                elif v2<v1:
                    no_debt[k2]=0
                    remainder_toget[k1]=v1-v2
                    print(k2, "should pay ", k1,":", v2, "SEK")
                else:
                    pass
        else :
            None
for k, v in paid_more.items():
    if k not in remainder_toget and k in paid_more:
        remainder_toget[k]=v
for k, v in paid_less.items():
    if k not in remainder_topay and k in paid_less:
        remainder_topay[k]=v 
for k1, v1 in remainder_topay.items():
    for k2, v2 in remainder_toget.items():
        if k1 not in no_debt.keys() and k2 not in no_debt.keys():
            if v1==v2:
                print(k1, "should pay ", k2,":", v1, "SEK")
            elif v1>v2:
                print(k1, "should pay ", k2,":", v1-v2, "SEK")
            elif v1<v2:
                print(k1, "should pay ", k2,":", v1, "SEK")
            else:
                None 
