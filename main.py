spy_name=raw_input("What is your spy name? ")
print spy_name
if len(spy_name)>2:
    print "Welcome " + spy_name + "."
    spy_salutation=raw_input('What should we call you (Mr. or Ms.)? ')
    if spy_salutation=="Mr." or spy_salutation=="Ms.":
         spy_name = spy_salutation + spy_name
         print  "Welcome " + spy_name + ".Glad to see you back."
         print "Alright " + spy_name + " I'd like to know little bit more about you before you proceed."
         spy_age=input("What is your age? ")
         if 50>spy_age>12:
            print "Welcome to the team. "
            spy_rating=input('What is your rating ? ')
            if spy_rating>5:
                 print "Welldone. "
            elif 3<spy_rating<=5:
                     print "Average"
            elif 2<spy_rating<=3.5:
                print "Need to work"
            else:
                print "Worst"

            spy_is_online=True
            print "Authentication is completed.Welcome " + spy_name + " age: "+ str(spy_age) + " rating: " + str(spy_rating)






         else:
            print "Rejected. "

    else:
         print "Invalid salutation."

else:
    print "Ooopss you are not permitted. "

