import json
from xml.dom.minidom import Document

class Car():

    '''Constructor'''
    def __init__(self, *args, **kwargs):
        #Assigning values for the keys
        if len(args) > 0 and isinstance(args[0], dict):
            hash = args[0]
            name = hash.get('name')
            brand = hash.get('brand')
            nb_doors = hash.get('nb_doors')
        else:
            name = kwargs.get('name')
            brand = kwargs.get('brand')
            nb_doors = kwargs.get('nb_doors')

        if name == None or not isinstance(name, str):
            raise Exception("name is not a string")
        if brand == None or not isinstance(brand, str):
            raise Exception("brand is not a string")
        if (nb_doors <= 0) and (isinstance(nb_doors, int)):
            raise Exception("nb_doors is not > 0")
        self.__name = name
        self.__brand = brand
        self.__nb_doors = nb_doors

    '''Destructor'''
    def __del__(self):
        pass

    '''Getters'''
    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_nb_doors(self):
        return self.__nb_doors

    '''Setters'''
    def set_name(self, name):
        self.__name = name

    def set_brand(self, brand):
        self.__brand = brand

    def set_nb_doors(self,nb_doors):
        self.__nb_doors = nb_doors

    '''methods'''
    #Returns a dictionary data structure which describes a car
    def to_hash(self):
        return {'name': self.__name, 'brand': self.__brand, 'nb_doors': self.__nb_doors}

    #Returns a string with all information
    def __str__(self):
        info = self.__name + " " + self.__brand + " " + "(" + str(self.__nb_doors) + ")"
        return info

    #Update the private attribute nb_doors
    def set_nb_doors(self, number):
        self.__nb_doors = number

    #Returns a string in json format
    def to_json_string(self):
        json_string = json.dumps(self.to_hash()) #Dumps the directory which is returned by to_hash()
        return json_string

    #Returns the DOM element
    '''Required XML is:
        <car nb_doors = "5">
            <name>
                <![CDATA[Rogue]]>
            </name>
            <brand>
                Nissan
            </brand>
        </car>'''
    def to_xml_node(self, doc):
        car = doc.createElement('car')
        car.setAttribute('nb_doors', str(self.__nb_doors))
        doc.appendChild(car)
        name = doc.createElement('name')
        name_content = doc.createCDATASection(self.__name)
        name.appendChild(name_content)
        car.appendChild(name)
        brand = doc.createElement('brand')
        brand_content = doc.createTextNode(self.__brand)
        brand.appendChild(brand_content)
        car.appendChild(brand)
        return car
