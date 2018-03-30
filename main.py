from spy_details import spy #importing spy_name,spy_age,spy_rating from spy_details
print"Hello Buddy"
print"What's up?"
Status_Message=["Every morning is a ray of hope","Workhard to make your dreams come true","Never work for satisfy others"]#displaying menu of old status listed
friends=[{'name':'sushant','age':24,'rating':3.5,'is_online':True},{'name':'aman','age':29,'rating':4,'is_online':True}]
def add_status(c_status): #defining function add_status
    if c_status != None: #if there is nothing mentioned or choosed in or from status
        print"Your current status is " + c_status
    else:
        print "You don't have any status currently."
        existing_status=raw_input("You want to select from old status? Y/N ") #asking options which option you want to select either old status or not
        if existing_status.upper()=="N":
            new_status=raw_input("Enter your status: ")
            if len(new_status)>0: #checking length of status
                Status_Message.append(new_status)
        elif existing_status.upper()=="Y":
            serial_number=1
            for old_status in Status_Message: #traversing in list Status_Message
                print str(serial_number) +". "+ old_status
                serial_number=serial_number + 1
            user_choice=input("Enter your choice: ")
            new_status=Status_Message[user_choice-1]
        updated_status=new_status
        return updated_status
def add_friend():
    frnd={
        'name':'',
        'age':0,
        'rating':0.0
    }
    frnd['name']=raw_input('What is your name? ')
    frnd['age']=input('What is your age ? ')
    frnd['rating']=input('What is your rating ?')
    if len (frnd['name'])>2 and 12<frnd['age']<50 and frnd['rating'>spy['rating'] :
         friends.append(frnd)
    else:
        print "Friend cannot be added."
    return len(friends)
def select_frnd():
    serial_no=1
    for frnd in friends:
        print serial_no + ".  " + frnd['name']
        serial_no=serial_no+1
    user_selected_frnd=input("Enter your choice: ")
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index
def send_message():
    selected_frnd=select_frnd()
    print selected_frnd
def read_message():
    selected_frnd=select_frnd()
def spy_chat(spy['name'],spy['age'],spy['rating']):
    print "Here are you're options " + spy['name']
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input("What do you want to do \n 1. Add a status \n 2. Add a friend \n 3.Send a secret message. \n 4.Read a secret message \n 5.Read chats from user \n 6.Exit ") #asked to choose the option
        if spy_choice==1:
            c_status=add_status(current_status)
            print "Updated status is  " + c_status
        elif spy_choice==2:
            no_of_friends=add_friend()
            print "You have " + str(no_of_friends) + " friends."
        elif spy_choice==3:
            send_message()
        elif spy_choice==4:
            print "Read a secret message."
        elif spy_choice==5:
            print "Read chats from user."
        elif spy_choice==6:
            show_menu=False
        else:
            print "Invalid options"
spy_exist=raw_input("Are you a new user (Y/N)? ") #asking spy whether you are new or not.
if spy_exist.upper()=="N": # when spy is an old one
    print "Welcome back" + spy['name'] + " age : " + str(spy['age']) + " having rating of " + str(spy['rating'])
    spy_chat(spy['name'],spy['age'],spy['rating']) #calling functions
elif spy_exist.upper()=="Y":
    spy={
        'name':'',
        'age':0,
        'rating':0.0
    }
    spy['name']=raw_input("What is your spy name? ")
    print spy['name']
    if len(spy['name'])>2: #setting length of the name
        print "Welcome " + spy['name'] + "." # concatinating welcome with spy_name
        spy_salutation=raw_input('What should we call you (Mr. or Ms.)? ')
        if spy_salutation=="Mr." or spy_salutation=="Ms." or spy_salutation=="ms." or spy_salutation=="mr.": # applying salutation to the name
            spy['name'] = spy_salutation + spy['name'] #concatinating name with salutation
            print  "Welcome " + spy['name'] + ".Glad to see you back."
            print "Alright " + spy['name'] + " I'd like to know little bit more about you before you proceed."
            spy['age']=input("What is your age? ") #taking age from user
            if 50>spy['age']>12: #fixing age of user from 12 to 50
                print "Welcome to the team. "
                spy['rating']=input('What is your rating ? ') # taking rating from user
                if spy['rating']>5: #fixing the rating greater than 5
                    print "Welldone. "
                elif 3<spy['rating']<=5: # fixing the rating greater than 3 and less than equal to 5
                    print "Average"
                elif 2<spy['rating']<=3.5: # fixing the rating less than 2 and greater than equal to 3.5
                    print "Need to work"
                else: #worst rating
                    print "Worst."
                spy_is_online=True #checking if spy is online
                print "Authentication is completed.Welcome " + spy['name'] + " age: "+ str(spy['age']) + " rating: " + str(spy['rating']) # typecasting integer to string
                spy_chat(spy['name'],spy['age'],spy['rating']) #callinf functions spy_chat
            else:
                 print "You are not eligible for spy."
        else: #when salutation is incorrect
             print "Invalid salutation"
    else:
        print "OOpss you are not permitted."
else:
    print "Invalid entry."







