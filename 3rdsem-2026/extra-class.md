# class and objects
# database
# pandas


# Data - anything that gets generate on your electronics parts
# Anything getting written on your hard drive is called data.
# data - different types - structured data - csv, excel, xml  file.
# unstructured - pdf, images and videos.
# semi structured - json - javascript object notation - dict 
# dict vs json - dict - key - immutable datatype. 
# json-key - string.


# structure data -  datatypes 
# primitives datatype and non-primitives data.
# primitives - int, float, string, char and complex number
# non-primitives - (user-defined datatypes) - class and struct. 

# class - blueprint of your data. How the data will look like.

class classname:
    variable
    functions

# variable - space where we store the data. - glass - we store the water
# function - behaviour 

# variable types - instance variable, class variable and static variable
# function types - instance function, class function and static function 

# instance - class in the memory. instance of class can be infinite.
# memory - ram of your pc. 

# instance of class is called as object.

abc = classname()


e.g. user class

class User:
    # class variable
    id = 0
    
    # constructor
    # self reference
    # instance function
    def __init__(self, name:str = "default", mobile="123131231"):
        # instance variable
        # self.variable_name
        self.name = name
        self.mobile = mobile
        self.user_id = User.id + 1 
        User.id += 1

    def get_user_info(self):
        print(f"user_id: {user_id} user_name: {self.name}")

    # class function
    @classmethod
    def employee_count(cls):
        print(User.id)

    @staticmethod
    def static_user():
        count = 0
        return "user"

User.employee_count
obj = User() 
obj = User("prashant") # constructor - automatically gets called.
obj.get_user_info() # explicitly  calling the function.

# class - properties - oops
# object oriented programming system
# major pillars
# minor pillars

# major - abstraction, encapsulation, polymorphism and hierarcy
# minor - concurrency and modularity.

# abstraction - hidding the implementation and giving an access to an feature.
# encapsulation - binding of data with function.
# polymophirsm - different forms (functions) # different behaviour.
# ek function - different forms hum usse polymorphirsm
# poly - compiletime poly and runtime poly
# hierarch - composition and inheritence
# inheritence - parent - child behaviour

class department:
    self.name = dept_name

class Employee(User):

    def __init__(self, name, mobile, dept_name):
        self.__super__(self, name, mobile)
        self.dept = Department(dept_name) # composition

    def get_user_info(self):  # runtime poly
        print(f"user_id: {user_id} user_name: {self.name} dept_name: {dept_name}")


# abstract class and interface
# abstract class - can't object of it.
# partial incomplete methods 
# class - all function are incomplete methods - interface 
# force to apply the certain behaviour

# MRO - method resolution order
# python supports multiple inheritence
# class bird(flyable, aquatic) # left hand side class will pripority
# flyable and aquatic - function pqr - function of flyable will get called.

abc import ABC, abstractmethod

# abstract class and interface
# all interface class are abstract class but not a vice-versa
class flyable(ABC):

    @abstractmethod
    def fly(self):
        pass

# abstract class
class flyable(ABC):

    @abstractmethod
    def fly(self):
        pass

    # instance method / concentrate method
    def get_bird_name(self):
        return self.bird_name

++++++++++++++++++++++++++++++++++++++++++

# try - exeception
# file operation
# Database
# pandas
# numpy

# ------------

# ---------
# Object - predefined function magic method 
# __str__()
# __init__()
# __dict__()
# __new__()

# singleton - class which as only one object.
# singleton - 1. private method to check the instance count
# 2. inherit the method __new__() - if class variable doesn't contain the instance count then create a new object.
# 3. in java - constructor ko private 
# 3. in python - constructor return instance of the class


# self - reference of the current object
# self.variable_name - represent instance variable

class User(object):
    def __init__(self, name):
        self.name = name
        # User.name = name - class variable
    
class employee(User):
    def __init__(self, name, salary):
        self.__super__.__init__(name) # parent class constructor calling.
        self.salary = salary

    def valid_salary(self):
        # adasdad - input - can't convert it into the float
        # to handle such situation or inputs we use try exception
        flag = 0
        try:
            # abcd
            salary = float(self.salary)
            if salary > 0:
                flag = 1
        except ValueError as e:
            print("conversion failed: ", e)
        except Exception as e:
            print("conversion failed: ", e)
        finally:
            # it will always run
            if flag:
                print("valid salary")
            else:
                print("invalid salary")
        return flag

## file operations
class FileOperations(object):
# operation ---> read, write and append.
# combination of operations ---> read - write, read - append
# file mode - binary and ascii

    # absolute and relative
    # absoulte - complete path c:\user\prashant\demo\abc.txt
    # relative - path from current folder - ..\demo\abc.txt

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        # context manager - with
        # concept called as closeable - java
        
        # memory management  - java and python - gc - garbage collector
        # garbage collector - object memory  ko free karna - 
        # expiry - when count of the reference become zero
        # a = User()
        # a = Employee() # user - 0 and employee - 1
        # a = None # employee - 0
        # gc.collect()
        # import gc
        # c and c++ - free memory - karna bhul  - memory error.
        # gc 

        # file - close - updated data can't be access. 
        # linux - 
        # resource management - file, db and memory (gc) - developer 
        # with - open and close - closable in java
        # class - closeable - resouce management - open and close get called automatically - like gc.
        #
        with resouce_name.open() as ref_name:
            ref_name
        # ref_name X
        try:
            # file operations - r, w, a, rb, wb, ab, w+, r+, a+, wb+, rb+, ab+

            with open(self.file_path, "r") as fp:
                content = fp.read()
        exception exception as e:
            print(e)
    
        with open(self.file_path, "w") as fp:
            # fp - 0 
            fp.seek(100) - 
            fp.write("adea")
        


# data - structure, semistructured and unstructed 
# data - structured  - use DB or excel - grid formatted - 
# table format - row and column data - then we can use the database - rdbms
# relationship database management system
# data - connection establishment within the data 
# e.g. employee - department - rdbms 
# data - will be reperesent - column value 

id | name | salary | department
1 | pra | 100| technical
2 | pra | 40 | technical
3 | pra | 100 | technical 
100's rows - 

# to identify each row - we have a candidate key  - combination of single column or muliple column of that individual row.
# name - candidate key
# name, dept and salary - candidate key - no limit 
# excel - serial number, column - alphabets 
# database - primary key, column - column_name
# primary key - minimum key is called as primary key - 
# primary key - the key that represents the unique row.
# DDL, DML and DQL - commands 
# used to represent the data













