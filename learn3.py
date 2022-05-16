score = {'scor':'0', 'val':'12', 'time' : 'slow'}

if score['time'] == 'medium':

    varibe = 1
elif score['time'] == 'slow':
    varibe = 2
else:
    print("end")

output = score['time']+str(varibe)

print("time of moveing" +str(output) )

for key_n, var_n in score.items():
    print(key_n + var_n)

box = []

for bi in  range(10):
    box2 = {'fox' : 1, 'cat' : 2, 'monkey' : 3}
    box2['work'] = 10
    box.append(box2)
    print(box)
    print(box2['fox'])

text1 = "what is this"
text2 = "where is the world"
text3 = "where this enegry comes"

text_list = [text1, text2, text3]

for word in text_list:
    print(word)

score2 = {'this' : 'word', 'text' : 'text', 'when' :'where'}

list_score = [score, score2]

for man in list_score:
    print(man )

#for oka in score2[]:
#    if score2['text'] == text :
#        for b , c in score2.items():

user_details = {'name_user' : 
        {'id': '78327', 
            'passwd' : '#@%^', 
            'fb_id':'sun@mail.com',  },
        'name_user2' :  {'id': '78327', 
            'passwd' : '#@%^', 
            'fb_id':'sun@mail.com',  },   }
        for dell, info in user_details.items():
            print ("your name" +dell)
            user_id = info['id']
            user_passwd = info['passwd']
            user_fb = info['fb_id']

            print ("your user id" + user_id)
            print ("your paswwd" + user_passwd)
            print ("your fb" + user_fb)

