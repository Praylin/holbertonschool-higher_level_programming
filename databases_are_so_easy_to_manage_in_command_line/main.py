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

    #If the first argument is 'print', print the records of the corresponding tables
    elif(sys.argv[1] == 'print'):
        if(sys.argv[2] == "school"):
            for data in School.select():
                print data
        elif(sys.argv[2] == "batch"):
            for data in Batch.select():
                print data
        elif(sys.argv[2] == "user"):
            for data in User.select():
                print data
        elif(sys.argv[2] == "student"):
            for data in Student.select():
                print data

    #If the first argument is insert, insert data into corresponding tables
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

    #If the first argument is delete, delete the record from the corresponding table
    elif(sys.argv[1] == 'delete'):
        if (sys.argv[2] == "school"):
            try:
                school = School.get(School.id == sys.argv[3])
                print "Delete" + str(school)
                school.delete_instance()
            except:
                print "Nothing to delete"

        elif (sys.argv[2] == "batch"):
            try:
                batch = Batch.get(Batch.id == sys.argv[3])
                print "Delete" + str(batch)
                batch.delete_instance()
            except:
                print "Nothing to delete"

        elif (sys.argv[2] == "user"):
            try:
                user = User.get(User.id == sys.argv[3])
                print "Delete" + str(user)
                user.delete_instance()
            except:
                print "Nothing to delete"

        elif (sys.argv[2] == "student"):
            try:
                student = Student.get(Student.id == sys.argv[3])
                print "Delete: " + str(student)
                student.delete_instance()
            except:
                print "Nothing to delete"

        else:
            print "Enter a valid model/table name"

    #If first argument is print_batch_by_school, print the batches in a school corresponding to the school_id
    elif (sys.argv[1] == "print_batch_by_school"):
        try:
            print Batch.get(school = sys.argv[2])
        except:
            print "School not found"

    #If the first argument is print_student_by_batch,
    elif (sys.argv[1] == "print_student_by_batch"):
        try:
            for data in Student.select():
                data = Student.get(batch = sys.argv[2])
                print data

        except:
            print "Batch not found"

    elif (sys.argv[1] == "print_student_by_school"):
        try:
            for data in Student.select():
                data = Student.get(id = sys.argv[2])
                print data
        except:
            print "School not found"
    #if the first argument is not part of this list,
    else:
        print "Undefined action", sys.argv[1]
