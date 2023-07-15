"""
    Better way to avoid complexity

    When there are many class-models of an app, 
    it is better to use this way to avoid complexity.
"""

"""
    Create models directory

    In this way, we delete the models.py file in the app 
    and create a directory called models, 
    then we create the models class in separate files, 
    finally we create a file named __init__ in that directory 
    and all class-model We call it.
"""


"""
    # for example :: App Directories 

    + myapp
        - ...
        + models
            - __init__.py
            - office.py
            - library.py
"""

###############
# __init__.py #
###############

from .office import Person
from .library import Category, Book



#############
# office.py #
#############

class Person(models.Model):
    pass


##############
# library.py #
##############

class Category(models.Model):
    pass

class Book(models.Model):
    pass