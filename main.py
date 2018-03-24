spy_name=raw_input("What is your spy name? ")
print spy_name
if len(spy_name)>2: #setting length of the string
    print "Welcome " + spy_name + "." # concating welcome with spy_name
    spy_salutation=raw_input('What should we call you (Mr. or Ms.)? ')
    if spy_salutation=="Mr." or spy_salutation=="Ms.": # apping salutation to name
         spy_name = spy_salutation + spy_name #concating name with salutation
         print  "Welcome " + spy_name + ".Glad to see you back."
         print "Alright " + spy_name + " I'd like to know little bit more about you before you proceed."
         spy_age=input("What is your age? ") #taking age from user
         if 50>spy_age>12: #fixing age of user from 12 to 50
            print "Welcome to the team. "
            spy_rating=input('What is your rating ? ') # taking rating from user
            if spy_rating>5: #fixing rating greater than 5
                 print "Welldone. "
            elif 3<spy_rating<=5: # fixing rating greater than 3 and less than equal to 5
                     print "Average"
            elif 2<spy_rating<=3.5: # fixing rating less than 2 and greater than equal to 3.5
                print "Need to work"
            else: #worst rating
                print "Worst"

            spy_is_online=True #checking if spy is online
            print "Authentication is completed.Welcome " + spy_name + " age: "+ str(spy_age) + " rating: " + str(spy_rating) # typecasting integer to string






         else: #age less than required
            print "Rejected. "

    else: #when salutation is incorrect
         print "Invalid salutation."

else: #when name is invalid
    print "Ooopss you are not permitted. "

