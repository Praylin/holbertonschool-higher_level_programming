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

        try:
            Exercise.create_table()
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
        elif(sys.argv[3] == "exercise"):
            for data in Exercise.select():
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
            user_data = User.create(first_name = sys.argv[3], last_name = sys.argv[4], age = sys.argv[5])
            data = __str__()
            print data
        elif (sys.argv[2] == "student"): #Insert data in student table
            if(len(sys.argv) == 6): #If user enters only last_name
                student_data = Student.create(batch = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5])
            elif(len(sys.argv) == 7): #If user enters both last_name and first_name
                student_data = Student.create(batch = sys.argv[3], age = sys.argv[4], last_name = sys.argv[5], first_name =sys.argv[6])
            else:
                print "Not enough arguments"
            print "New student: " + str(student_data)
        elif (sys.argv[2] == "exercise"): #Insert data in Exercise table
            exercise_data = Exercise.create(student = sys.argv[3], subject = sys.argv[4], note = sys.argv[5])
            print "New exercise: " + str(exercise_data)
        else:
            print "No table with that name"

    #If the first argument is delete, delete the record from the corresponding table
    elif(sys.argv[1] == 'delete'):
        if (sys.argv[2] == "school"):
            try:
                school = School.get(School.id == sys.argv[3])
                print "Delete: " + str(school)
                school.delete_instance()
            except:
                print "Nothing to delete"

        elif (sys.argv[2] == "batch"):
            try:
                batch = Batch.get(Batch.id == sys.argv[3])
                print "Delete: " + str(batch)
                batch.delete_instance()
            except:
                print "Nothing to delete"

        elif (sys.argv[2] == "user"):
            try:
                user = User.get(User.id == sys.argv[3])
                print "Delete: " + str(user)
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

        elif (sys.argv[2] == "exercise"):
            try:
                exercise = Exercise.get(Exercise.id == sys.argv[3])
                print "Delete: " + str(exercise)
                exercise.delete_instance()
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

    #If the first argument is print_student_by_batch, print all the student details corresponding to the batch_id
    elif (sys.argv[1] == "print_student_by_batch"):
        try:
            for data in Student.select().where(Student.batch == sys.argv[2]):
                print data
        except:
            print "Batch not found"

    #If the first argument is print_student_by_school, print all the student details corresponding to the school_id
    elif (sys.argv[1] == "print_student_by_school"):
        try:
            for student in Student.select().join(Batch).where(Batch.school_id == sys.argv[2]):
                print student, Batch.get(id = sys.argv[2])
        except:
            print "School not found"

    #If the first argument is print_family, print all the student details with corresponding last_name
    elif (sys.argv[1] == "print_family"):
            for data in Student.select().where(Student.last_name == sys.argv[2]):
                print data

    #If the first argument is age_average, print the average of all the student ages
    elif (sys.argv[1] == "age_average"):
        ages = []
        age_sum = 0
        if (len(sys.argv) == 3): #age_average if batch_id is provided
            data = Student.select(Student.age).where(Student.batch == sys.argv[2])
        else:
            data = Student.select(Student.age)
        for i in data:
            ages.append(i.age)
            age_sum = age_sum + i.age
        length = len(ages)
        print age_sum/length

    #If the first argument is change_batch, get the corresponding student_data and batch_data based on arguments 2 and 3
    elif (sys.argv[1] == "change_batch"):
        student_data = Student.get(Student.id == sys.argv[2])
        batch_data = Batch.get(Batch.id == sys.argv[3])
        if (student_data.batch == batch_data): #If the student already present in the batch
            print "%s already in %s" % (student_data, batch_data)
        else: #If the student not present in the batch, save the particular student data in the corresponding batch
            print "%s has been moved to %s" % (student_data, batch_data)
            student_data.batch = sys.argv[3]
            student_data.save()

    #If the first argument is print_all , print all the data in hierarchy model
    elif (sys.argv[1] == "print_all"):
        for school_data in School.select():
            print school_data
            for batch_data in Batch.select().where(Batch.school == school_data):
                print "\t" + str(batch_data)
                for student_data in Student.select().where(Student.batch == batch_data):
                    print "\t \t" + str(student_data)
                    for exercise_data in Exercise.select().where(Exercise.student == student_data):
                        print "\t \t \t" + str(exercise_data)

    #If the first argument is note_average_by_student
    elif (sys.argv[1] == "note_average_by_student"):
        try:
            for exercise_data in Exercise.select().where(Exercise.student == sys.argv[2]):
                print str(exercise_data.subject) + ":"  + str(exercise_data.note)
        except:
            print "Student not found"

    #If the first argument is note_average_by_batch
    elif (sys.argv[1] == "note_average_by_batch"): #Not correct
        try:
            note_avg = []
            note_sum = 0
            for exercise_data in Exercise.select().join(Student).where(Student.batch == sys.argv[2]):
                note_avg.append(exercise_data.note)
                note_sum = note_sum + exercise_data.note
            print note_sum/len(note_avg)

        except:
            print "Batch not found"
    # #If the first argument is note_average_by_school
    # elif (sys.argv[1] == "note_average_by_school"):

    #If the first argument is top_batch
    # elif (sys.argv[1] == "top_batch"):



    #if the first argument is not part of this list,
    else:
        print "Undefined action", sys.argv[1]
