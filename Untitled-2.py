import random,sys,time,copy,pprint,pyperclip

def im():
    for n in range(5):
       print(random.randint(10, 25))

def s(answer):

    if answer == 2 :
        return 2+2/24
    elif answer == 3:
        return 2+4/25
    elif answer == 5:
        return 2+5+6/24
    elif answer == 6:
        return 65+5/24
    elif  answer == 7:
        return (25+1)-256/23
ss = s(random.randint(1, 8))
print() 
def wn():

    i = 0
    while i < 10:
       print(f'str {i}')
       i = i+1
def randomnumber():
    number_guess =random.randint(1, 55)
    print('i think number between 1 to 55')

    for selction in range(1,6):
        print('enter a number')
        guess = input('>.>>')
           
        if int(guess) > int(number_guess) :
            print('your number is too high')
        elif int(guess) < int(number_guess) :
            print('number too low')
        else:
            break

        if guess == number_guess:
            print( f'your selected corect number {number_guess}')
        else:
            return 'better luck net time'    

def  rock_game():

    print('ROCK SISSOR PAPER')
    win = 0
    loss = 0
    tie = 0

    while True:
        print('%s win, %s loss ,%s tie'%(win,loss,tie))
        while True:#loop the main rool
            print('Enter your move ROck(r) , Scissor(s),Paper(p) or exit(x)')
            move = input()
            if move == 'x':
                print('thank you')
                sys.exit()
            if move == 'r' or move == 's' or move == 'p':
                break
            print('r,p,s, and q')
    
        if move == 'r':
            print('ROCK versus...')
        elif move == 'p':
            print('PAPER versus...')
        elif move == 's':
            print('SCISSORS versus...')
        ran  = random.randint(1,3)
        if ran == 1:
            computer = 'r'
            print('Rock')
        elif ran == 2  :
            computer = 's'
            print('Scissor')
        elif ran == 3 :
            computer = 'p'
            print('Paper')

        if move == computer :
            print('tie')
            tie += 1
        elif move == 'r' and computer == 's':
            print('you won!')
            win += 1
        elif move == 'p' and computer == 'r':
            print('you won!')
            win += 1
        elif move == 's' and computer == 'p':
            print('you won!')
            win += 1
        elif move == 'r' and computer == 'p':
            print('you loss')
            loss += 1
        elif move == 'p' and computer == 's':
            print('you loss')
            loss += 1
        elif move == 's' and computer == 'r':
            print('you loss')
            loss +=1

def exc():
    try:
      print(10/0)
    except ZeroDivisionError:
      print('te')
    s = 100
    print('%s s' %(s))

def whi():
    name = ''
    while True :
        if name != 'jeny':
            name = input( 'what is your name >')
            print(f'hi{name} we will invite soon... ')
                 
def zigzag():
    ind = 0
    incurument = True

    try:
        while True:
           # print(''* ind ,end='')
            ind = print('*******')
            time.sleep(0.1)
            
             
        if ind == 20:
            print('======')
            sys.exit()
        else :
            ind += 1
            if ind == 0:
               incurument = False
    except KeyboardInterrupt:
        exit()

def loop():
    l =[]
    while True:
        print('this is the text '+ str(len(l)+ 1) +'if you want to quit ')
        cat_name = input()

        if cat_name == 'q':
            break
        l = l + [cat_name] # this is appending the data to list
    print(l)
    for i in l:
        print(i)
    
def enum(): # print index number with out len()
    su = ['pen','paper','sissor','user']
    for i, u in enumerate(su):
        print('index ' + str(i) + ' ==>' + u )

    z = ['this','whe','who','wonder']
    print(z[random.randint(0, len(z)-1)])
    #print(random.choice(z))
    #random.shuffle(z)
    print(z)


def cp():
    c =[1,2,4,5,6,87]
    z = ['1,2,3,4','12,12,34,56']
    z = c[:]
    zz = copy.copy(z)
    zc = copy.deepcopy(z)
    print(z)
    print(id(z))
    print(id(c))
    print(zz)
    print(id(zz))
    print(list(z))
    print(c[random.randint(0,len(c)-1)])
    print(z)
    print(len(c))



#for i in range(8):
  #  t = random.randint(0, 8)
  #  print(t)


    
#z = ['1,2,3,4','12,12,34,56']
#print(z)
#for i in z:
 #   print(i)
def sa():
    sample = [random.randint(1, 2) for i in range(0,1)]
    head = sample.count(0)
    tail = sample.count(1)

    for r in sample :
        msg = 'h'  if s == 1 else 't'
    print(msg)
    print('h = %s' , 't =- %s')

    tries = 0
    head = 0
    Tails = 0
    while tries < 1000000:
        tries += 1
        coin = random.randint(1, 2)
        if coin == 1:
            head += 1
            per1 = "{:.0%}".format(head)
        if coin == 2:
          Tails += 1
          per2 = "{:.0%}".format(head)
       
    
def data():
   ''' while True:

        dis ={'name' :'date','demo':'12','demo2':'13'} 
        dis.setdefault('name','wonder')
        print('enter your name ==')
        na = input()
        
        if na == 'q':
            exit()
        
        if na in dis:
            print(dis[na] + 'your birthday is ')
        else:
            print('your name is not in database enter date ==>')
            dpty = input()
            dis[na]  = dpty
            print('name is enterd into database')
        len(dis)
    for i in dis.keys():
        print(i)
dis ={'name' :'date','demo':'12','demo2':'13'} 
print(pprint.pformat(dis))'''

#print('''this is the text we wrote the project fucking fun
#import lots of\\\\ repostires and we\t hdhkh
#nd much more practies we create''')




def Game():

    save_data = {'one' : '' , 'two' :'','three':'','four':'','five':'','six':'','seven':'','eight':'','nine':''}

    def board(s):
      try:
        print(save_data['one'] +    '|' + save_data['two'] +     '|' + save_data['three'])
        print('++')
        print(save_data['four'] +    '|' + save_data['five'] +     '|' + save_data['six'])
        print('++')
        print(save_data['seven'] +    '|' + save_data['eight'] +     '|' + save_data['nine'])
        set1 = 'X'
        for z in range(9):
          
            print('Turn for '+set1+ 'move on white spaces')
            move = input()
            the_board[move] = set1
            if set1 == 'x':
                set1 == 'o'
            else:
                set1 == 'o'
      except  RecursionError:
           print('they is a recursionError')   
      except  NameError:
          print('name error also')
      except EOFError :
          pass
         
    
    board(save_data)

def text1():
    while True:
        print('enter a text in numbers')
        name = input()
        if name.isdecimal():
            break
        elif name.isalnum():
            print('it contains number and strings')
        


