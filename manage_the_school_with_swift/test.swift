class Person{
    var first_name: String = ""
    var last_name: String = ""
    var age: Int = 0
    init (first_name: String, last_name: String, age: Int){
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    }
    func fullName() -> String{
        let full_name = first_name + " " + last_name
        return full_name
    }
