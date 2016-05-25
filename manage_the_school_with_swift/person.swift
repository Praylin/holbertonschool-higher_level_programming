//Describe a class named Person

class Person {
  var first_name: String
  var last_name: String
  var age: Int

  init(first_name: String, last_name: String, age: Int) {
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
  }

  func fullName() -> String {
    var full_name: String
    full_name = first_name + " " + last_name
    return full_name
  }
}

//Class Mentor inherited from class Person and implemented from protocol Classify

class Mentor : Person, Classify {
  let subject : Subject?
  init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
    self.subject = subject
    super.init(first_name: first_name, last_name: last_name, age: age)
  }
  func isStudent() -> Bool {
    return false
  }
  func stringSubject() -> String {
    /*if subject = Subject.Math {
      return "Math"
    } else if subject = Subject.English {
      return "English"
    } else if subject = Subject.French {
      return "French"
    } else if subject = Subject.History {
      return "History"
    } else {*/
    return String("\(self.subject!)")

  }
}

//Class Student inherited from class Person and implemented from protocol Classify

class Student : Person, Classify {
  func isStudent() -> Bool {
    return true
  }
}

//Protocol Classify

protocol Classify {
  func isStudent() -> Bool
}

//Enum Subject

enum Subject {
  case Math
  case English
  case French
  case History
}
