import peewee
#creating instance of instance of peewee.SqliteDatabase
my_models_db = peewee.SqliteDatabase("my_models.db", pragmas = (('foreign_keys', True), ))

#Class BaseModel inherited from peewee.Model
class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique = True)
    class Meta:
        database = my_models_db
        order_by = ('id', )

'''class School inherited from BaseModel:
    has a 'name' variable and a function which
    returns the data in the table School'''
class School(BaseModel):
    name = peewee.CharField(128, null = False)
    def __str__(self):
        return "School: " + self.name + " (" + str(self.id) + ")"

'''class Batch inherited from BaseModel: has a
    foreign_key of the table School, a name variable
    and a function which returns all the data of the
    table Batch'''
class Batch(BaseModel):
    school = peewee.ForeignKeyField(School, related_name = "batches", on_delete = "CASCADE")
    name = peewee.CharField(128, null = False)
    def __str__(self):
        return "Batch: " + self.name + " (" + str(self.id) + ")"

'''class User inherited from BaseModel: has variables
    first_name, last_name and age and a function which
    returns all the data of the table User'''
class User(BaseModel):
    first_name = peewee.CharField(128, default = "")
    last_name = peewee.CharField(128, null = False)
    age = peewee.IntegerField(null = False)
    def __str__(self):
        return "User: " + self.first_name + self.last_name + " (" + str(self.id) + ")"

'''class Student inherited from User: has a foreign_key
    from table Batch and a function which returns all the
    data of the table Student'''
class Student(User):
    batch = peewee.ForeignKeyField(Batch, related_name = "students", on_delete = "CASCADE")
    def __str__(self):
        return "Student: " + self.first_name + " " + self.last_name + " (" + str(self.id) + ")" + " part of the batch: " + str(self.batch)

'''class Exercise inherited from BaseModel: has a foreign key from
 Student table and variables subject, note and an array variable
 subjetcs and a function which returns all the data of the table'''
class Exercise(BaseModel):
    subjects = [('math', "Math"), ('english', "English"), ('history', "History"), ('c_prog', "C prog"), ('swift_prog', "Swift prog")]
    student = peewee.ForeignKeyField(Student, related_name = "exercises", on_delete = "CASCADE")
    subject = peewee.CharField(128, choices = "SUBJECTS")
    note = peewee.IntegerField(default = 0)
    def __str__(self):
        return "Exercise: " + str(self.student) + " has " + str(self.note) + " in " + str(self.subject) + "(" + str(self.id) + ")"
