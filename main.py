from spy_details import spy_name,spy_age,spy_rating #importing spy_name,spy_age,spy_rating from spy_details
print"Hello Buddy"
print"What's up?"
Status_Message=["Every morning is a ray of hope","Workhard to make your dreams come true","Never work for satisfy others"]#displaying menu of old status listed
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
def spy_chat(spy_name,spy_age,spy_rating): #defining the function
    print "Here are you're options " + spy_name
    current_status=None
    show_menu=True
    while show_menu:
        spy_choice=input("What do you want to do \n 1. Add a status \n 2. Add a friend \n 3.Send a secret message. \n 4.Read a secret message \n 5.Read chats from user \n 6.Exit ") #asked to choose the option
        if spy_choice==1:
            current_status=add_status(current_status)
            print "Updated status is  " + current_status
        elif spy_choice==2:
            print "Add a friend"
        elif spy_choice==3:
            print "Send a secret message."
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
    print "Welcome back" + spy_name + " age : " + str(spy_age) + " having rating of " + str(spy_rating)
    spy_chat(spy_name,spy_age,spy_rating) #calling functions
elif spy_exist.upper()=="Y":
    spy_name=raw_input("What is your spy name? ")
    print spy_name
    if len(spy_name)>2: #setting length of the name
        print "Welcome " + spy_name + "." # concatinating welcome with spy_name
        spy_salutation=raw_input('What should we call you (Mr. or Ms.)? ')
        if spy_salutation=="Mr." or spy_salutation=="Ms." or spy_salutation=="ms." or spy_salutation=="mr.": # applying salutation to the name
            spy_name = spy_salutation + spy_name #concatinating name with salutation
            print  "Welcome " + spy_name + ".Glad to see you back."
            print "Alright " + spy_name + " I'd like to know little bit more about you before you proceed."
            spy_age=input("What is your age? ") #taking age from user
            if 50>spy_age>12: #fixing age of user from 12 to 50
                print "Welcome to the team. "
                spy_rating=input('What is your rating ? ') # taking rating from user
                if spy_rating>5: #fixing the rating greater than 5
                    print "Welldone. "
                elif 3<spy_rating<=5: # fixing the rating greater than 3 and less than equal to 5
                    print "Average"
                elif 2<spy_rating<=3.5: # fixing the rating less than 2 and greater than equal to 3.5
                    print "Need to work"
                else: #worst rating
                    print "Worst."
                spy_is_online=True #checking if spy is online
                print "Authentication is completed.Welcome " + spy_name + " age: "+ str(spy_age) + " rating: " + str(spy_rating) # typecasting integer to string
                spy_chat(spy_name,spy_age,spy_rating) #callinf functions spy_chat
            else:
                 print "You are not eligible for spy."
        else: #when salutation is incorrect
             print "Invalid salutation"
    else:
        print "OOpss you are not permitted."
else:
    print "Invalid entry."







