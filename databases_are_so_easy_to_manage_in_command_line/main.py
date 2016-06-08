#script should be executed with arguments
from models import *
import sys

if (len(sys.argv) < 2):
    print "Please enter an action"
#First argument should be an action:
else:
    if (sys.argv[1] == 'create'):
        try:
            School.create_table()
        except peewee.OperationalError:
            pass

        try:
            Batch.create_table()
        except peewee.OperationalError:
            pass

        try:
            User.create_table()
        except peewee.OperationalError:
            pass

        try:
            Student.create_table()
        except peewee.OperationalError:
            pass

    elif(sys.argv[1] == 'print'):
        print "print"
    elif(sys.argv[1] == 'insert'):
        if (sys.argv[2] == "school"):
            school_data = School.create(name = sys.argv[3])
            # data = __str__()
            print "New school " + "School" +": " + sys.argv[3] + "(" + str(school_data) + ")"
        # elif (sys.argv[2] == "Batch"):
        #     batch_data = Batch.create(school = insert_data, name = sys.argv[3])
        #     #data = __str__()
        #     print
        # elif (sys.argv[2] == "User"):
        #     user_data = sys.argv[2].create(first_name = sys.argv[3], last_name = sys.argv[4], age = sys.argv[5])
        #     data = __str__()
        #     print data
        # elif (sys.argv[2] == "Student"):
        #     student_data = sys.argv[2].create(batch = batch_data, age = sys.argv[3] last_name = sys.argv[4], first_name =sys.argv[5])
        #     data = __str__()
        #     print data
        else:
            print "No table with that name"
    elif(sys.argv[1] == 'delete'):
        print "delete"
    #if the first argument is not part of this list,
    else:
        print "Undefined action", sys.argv[1]
