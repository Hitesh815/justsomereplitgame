import random, os, time
firstnames=('john','smith','wang','ari')
secondnames=('kumar','chhabra','raj','sharma','rai')
char_type=('wizrad','human','imp','elf')
def namegen():
  fullname=random.choice(firstnames)+" "+random.choice(secondnames)
  return fullname
def heal():
  side_6=random.randint(1,6)
  side_12=random.randint(1,12)
  health=((side_6*side_12)/2)+10
  return health
def att():
  side_6=random.randint(1,6)
  side_12=random.randint(1,12)
  attack=((side_6*side_12)/2)+12
  return attack
def typegen():
  type=random.choice(char_type)
  return type
while True:
  os.system("clear")
  print("character optimaztion")
  print()
  print()
  print()
  time.sleep(1)
  print("the name of the legend of player1 is:")
  name=namegen()
  time.sleep(2)
  print(name)
  print()
  time.sleep(1)
  print("charcter type:")
  time.sleep(2)
  type=typegen()
  print(type)
  time.sleep(2)
  print()
  print()
  health=int(heal())
  attack=int(att())
  print("so you are the almighty",name,"you are a",type)
  time.sleep(1)
  print()
  print("health:",health)
  print("attack:",attack)
  print()
  print()
  time.sleep(3)
  print("the name of the legend of player2 is:")
  name2=namegen()
  time.sleep(2)
  print(name2)
  print()
  time.sleep(1)
  print("charcter type:")
  time.sleep(2)
  type2=typegen()
  print(type2)
  print()
  print()
  time.sleep(2)
  health2=int(heal())
  attack2=int(att())
  print("so you are the almighty",name2,"you are a",type2)
  time.sleep(1)
  print()
  print("health:",health2)
  print("attack:",attack2)
  players=(name,name2)
  time.sleep(6)
  os.system("clear")
  i=1
  while health>=0 and health2>=0:
    os.system("clear")
    print("the battle begins")
    time.sleep(1)
    print()
    print()
    print("round",i)
    time.sleep(1)
    print()
    hit=random.choice(players)
    print(hit,"takes the first blow")
    time.sleep(2)
    hitnum=int(random.uniform(1,(max(attack,attack2))))
    print(hitnum,"=damage")
    time.sleep(2)
    print()
    print()
    if hit==name:
      health=health-hitnum
      if health<=0:
        print(hit,"has taken a huge damage and he's done for now")
        print(name2,"wins","after",i,"rounds")
        break
      else:
         print(hit,"has taken some damage and their new health is",health)
         i+=1
    else:
      health2=health2-hitnum
      if health2<=0:
        print(hit,"has taken a huge damage and he's done for now")
        print(name,"wins","after",i,"rounds")
        break
      else:
        print(hit,"has taken some damage and their new health is",health2)
        i+=1
    print(name)
    print("health=",health)
    time.sleep(2)
    print()
    print(name2)
    print("health=",health2)
    time.sleep(2)
    time.sleep(6)
  print("want to play again?")
  choice=input("type yes to go again")
  if choice=="no":
    break