from spy_details import spy,Spy,ChatMessage#importing spy_name,spy_age,spy_rating from spy_details
from steganography.steganography import Steganography #importing Steganography module from steganography class of steganography library
from datetime import datetime #importing datetime module from datetime class
from colorama import Fore,Style #importing colorama module
import csv
time=datetime.now()  #.now() function which will return current date and time
print time #printing returned current date and time
print "Hello Buddy."
print "What's up?"
Status_Message=["Every morning is a ray of hope","Workhard to make your dreams come true","Never work to satisfy others"]#displaying menu of old status listed
friend1=Spy('Naman','Mr.',23,4)
friend2=Spy('Niti','Ms.',26,3)
friends=[friend1,friend2]
def load_frnds(): #load friends in friends list from fnds.csv file
    with open ('frnds.csv','rb') as friends_data:
        reader =list(csv.reader(friends_data))
        for row in reader[1:]:
            spy=Spy(name=row[0],salutation=row[1],age=row[2],rating=row[3])
            friends.append(spy)
load_frnds()
def load_chats(): #loading chat of sender and receiver
    with open ('chat.csv','rb') as chats_data:
        reader =list(csv.reader(chats_data))
        for message,date,sent_by_me,receiver_name in reader[1:]:
            print Fore.BLACK+message,Fore.BLUE+date,Fore.RED+sent_by_me,Fore.CYAN+receiver_name
            print (Style.RESET_ALL)
def selected_chat(): #function to see chat of special friend
    s_name=raw_input("Enter the name of friend whose name chat you want to see.")
    with open ('chat.csv','rb') as chats_data:
        reader =list(csv.reader(chats_data))
        for message,date,sent_by_me,receiver_name in reader[1:]:
            if s_name==receiver_name:
                print Fore.BLUE+date,Fore.RED+sent_by_me,Fore.BLACK+message
                print (Style.RESET_ALL)
            else:
                print "No,chat is available."
def add_status(c_status): #defining function add_status.
    if c_status != None: #if there is nothing mentioned or choosed in or from status.
        print"Your current status is " + c_status
    else:
        print "You don't have any status currently."
    existing_status=raw_input("You want to select from old status? Y/N ") #asking options which option you want to select either old status or not
    if existing_status.upper()=="N": #if user dont want to choose from existing status
        new_status=raw_input("Enter your status: ") #asking new status from user
        if len(new_status)>0: #checking length of status
            with open('sts.csv','a') as friend_status:
                writer = csv.writer(friend_status)
                writer.writerow([new_status])
                updated_status = new_status
    elif existing_status.upper()=="Y": #option when user want to choose from existing status
        serial_number=1
        for old_status in Status_Message: #traversing in list Status_Message
            print str(serial_number) +". "+ old_status #concatinating serial number with choosed status
            serial_number=serial_number + 1
        user_choice=input("Enter your choice: ") #asking choice of user to choose options
        new_status=Status_Message[user_choice-1] #deducting by 1 from user choice so that it can point correct index os Status_message list.
    updated_status=new_status #the data stored in new_status will be now stored to updated_status
    return updated_status #will return to the function add_status
def add_friend(): #defining function add_friend()
    frnd=Spy('','',0,0.0)#write from import sys to print frnd
    frnd.name=raw_input('What is your friend name? ')
    frnd.salutation=raw_input('What should we call you (Mr. or Ms.)?')
    frnd.age=input('What is your friend age ? ')
    frnd.rating=input('What is your friend rating ?')
    if len(frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating: #conditons for adding new friend
        with open ('frnds.csv','a') as friends_data: #will append to fnds.csv file the name of friend
            writer=csv.writer(friends_data)
            writer.writerow([frnd.name,frnd.salutation,frnd.rating,frnd.age,frnd.is_online])
    else:
        print "Friend cannot be added."
    return len(friends) #will return to add_friend()
def select_a_friend(): # defining a function
    serial_no=1
    for frnd in friends:
        print str(serial_no) + ".  " + frnd.name
        serial_no=serial_no+1
    user_selected_frnd=input("Enter your choice: ") #asking user choice to which friend to select
    user_selected_frnd_index=user_selected_frnd-1
    return user_selected_frnd_index #returning data to select_a_friend()
def send_a_message(): #definig function
    selected_frnd=select_a_friend()
    original_image=raw_input("What is the name of your image? ") #asking user about the name of image
    secret_text=raw_input("What is your secret text? ")#asking about what secret text you need to save in image
    list=['HELP ME','SOS','SAVE ME','EMERGENCY'] #listing the special message
    if secret_text.upper() in list:
        print Fore.RED +" Inappropriate message."
        print (Style.RESET_ALL)
    else:
        output_path = "output.png"
        Steganography.encode(original_image,output_path,secret_text) #encoding the image with secret text.
        print "Your secret text has been successfully encoded."
        with open ('chat.csv','a') as chats_data:
            writer=csv.writer(chats_data)
            writer.writerow([secret_text,time,spy.name,friends[selected_frnd].name])
def read_a_message():
    selected_frnd=select_a_friend()
    output_path=raw_input("Which image you want to decode? ") #asking about which image user need to decode
    secret_text=Steganography.decode(output_path) #decoding the text from image
    print "Secret text is " + secret_text
    new_chat =ChatMessage(secret_text,False)
    friends[selected_frnd].chats.append(new_chat) #appending
    print "Your secret message has been saved. "
def spy_chat(spy_name,spy_age,spy_rating): # defining function
    print "Here are you're options " + spy.name
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input("What do you want to do \n 1. Add a status \n 2. Add a friend \n 3.Send a secret message. \n 4.Read a secret message \n 5. Read all chats \n 6.Read chats from selected friends\n 0.Exit ") #asked to choose the option
        if spy_choice==1: #will display the status
            current_status=add_status(current_status)
            print "Updated status is  " + current_status
        elif spy_choice==2: #will display numbers of friend user have.
            no_of_friends=add_friend()
            print "You have " + str(no_of_friends) + " friends."
        elif spy_choice==3:# will send encoded messsage
            send_a_message()
        elif spy_choice==4: #will display the decoded message
            read_a_message()
        elif spy_choice==5:
            load_chats()
        elif spy_choice==6:
            selected_chat()
        elif spy_choice==0: #will come out of show_menu option
            show_menu=False
        else:
            print "Invalid options"
spy_login = raw_input("Enter your username/email. ")  # creating login option asking username
spy_password = raw_input("Enter the password")
if spy_login == 'Ayushi' and spy_password == 'loginadmin':
    print "You are logged in."
    spy_exist=raw_input("Are you a new user (Y/N)? ") #asking spy whether you are new or not.
    if spy_exist.upper()=="N": # when spy is an old one
         print "Welcome back" + spy.name + " age : " + str(spy.age) + " having rating of " + str(spy.rating)
         spy_chat(spy.name,spy.age,spy.rating) #calling functions
    elif spy_exist.upper()=="Y":
        spy=Spy("","",0,0.0) #spy class
        spy.name=raw_input("What is your spy name? ")
        print spy.name
        if len(spy.name)>2: #setting length of the name
            print "Welcome " + spy.name + "." # concatinating welcome with spy_name
            spy.salutation=raw_input('What should we call you (Mr. or Ms.)? ')
            if spy.salutation=="Mr." or spy.salutation=="Ms." or spy.salutation=="ms." or spy.salutation=="mr.": # applying salutation to the name
                spy.name = spy.salutation + spy.name #concatinating name with salutation
                print  "Welcome " + spy.name + ".Glad to see you back."
                print "Alright " + spy.name + " I'd like to know little bit more about you before you proceed."
                spy.age=input("What is your age? ") #taking age from user
                if 50>spy.age>12: #fixing age of user from 12 to 50
                    print "Welcome to the team. "
                    spy.rating=input('What is your rating ? ') # taking rating from user
                    if spy.rating>5: #fixing the rating greater than 5
                        print "Welldone. "
                    elif 3<spy.rating<=5: # fixing the rating greater than 3 and less than equal to 5
                        print "Average"
                    elif 2<spy.rating<=3.5: # fixing the rating less than 2 and greater than equal to 3.
                        print "Need to work"
                    else: #worst rating
                        print "Worst."
                    spy_is_online=True #checking if spy is online
                    print "Authentication is completed.Welcome " + spy['name'] + " age: "+ str(spy['age']) + " rating: " + str(spy['rating']) # typecasting integer to string
                    spy_chat(spy.name,spy.age,spy.rating) #callinf functions spy_chat
                else:
                     print "You are not eligible for spy."
            else: #when salutation is incorrect
                 print "Invalid salutation"
        else:
            print "OOpss you are not permitted."
    else:
        print "Invalid entry."
else:
    print "You can't log in."


