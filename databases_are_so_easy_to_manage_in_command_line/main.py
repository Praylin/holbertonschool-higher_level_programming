#script should be executed with arguments
from models import *
import sys

#If the user doesn't enter any argument
if (len(sys.argv) < 2):
    print "Please enter an action"
#First argument should be an action:
else:
    #If the argument is 'create', create the following tables
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

    #If the first argument is 'print'
    elif(sys.argv[1] == 'print'):
        if(sys.argv[2] == "school"):
            school_data = School.select(School.name, School.id)
            for s in school_data:
                print "School: %s (%d)" %(s.name, s.id)
        elif(sys.argv[2] == "batch"):
            batch_data = Batch.select(Batch.name, Batch.id)
            for s in batch_data:
                print "Batch: %s (%d)" %(s.name, s.id)
        elif(sys.argv[2] == "user"):
            user_data = User.select(User.first_name, User.last_name, User.age, User.id)
            for s in user_data:
                print "User: %s %s %d (%d)" %(s.first_name, s.last_name, s.age, s.id)
        elif(sys.argv[2] == "student"):

                student_data = Student.select().join(Batch)
            #batch_data = Batch.select(Batch.name, Batch.id)
                print student_data
                for s in student_data:
                    print "Student: %s %s (%d) part of the batch: Batch: " %(s.first_name, s.last_name, s.id)

    #If the first argument is insert
    elif(sys.argv[1] == 'insert'):
        if (sys.argv[2] == "school"): #Insert data in school table
            school_data = School.create(name = sys.argv[3])
            print "New school: " + str(school_data)
        elif (sys.argv[2] == "batch"): #Insert data in batch table
            batch_data = Batch.create(school = sys.argv[3], name = sys.argv[4])
            print "New Batch: " + str(batch_data)
        elif (sys.argv[2] == "user"): #Insert data in user table
            user_data = sys.argv[2].create(first_name = sys.argv[3], last_name = sys.argv[4], age = sys.argv[5])
            data = __str__()
            print data
        elif (sys.argv[2] == "student"): #Insert data in student table
            if(len(sys.argv) == 6): #If user enters on last_name
                student_data = Student.create(batch = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5])
            elif(len(sys.argv) == 7): #If user enters both last_name and first_name
                student_data = Student.create(batch = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5], first_name =sys.argv[6])
            else:
                print "Not enough arguments"
            print "New student: " + str(student_data)
        else:
            print "No table with that name"

    #If the first argument is delete
    elif(sys.argv[1] == 'delete'):
        if (sys.argv[2] == "school"):
            school = School.get(School.id == sys.argv[3])
            if school.exists():
                school.delete_instance()
            else:
                print "Nothing to delete"
        elif (sys.argv[2] == "batch"):
            batch = Batch.get(Batch.id == sys.argv[3])
            if batch.exists():
                batch.delete_instance()
            else:
                print "Nothing to delete"
        elif (sys.argv[2] == "user"):
            user = User.get(User.id == sys.argv[3])
            if user.exists():
                user.delete_instance()
            else:
                print "Nothing to delete"
        elif (sys.argv[2] == "student"):
            student = Student.get(Student.id == sys.argv[3])
            if student.exists():
                student.delete_instance()
            else:
                print "Nothing to delete"
        else:
            print "Enter a valid model/table name"
    #if the first argument is not part of this list,
    else:
        print "Undefined action", sys.argv[1]
