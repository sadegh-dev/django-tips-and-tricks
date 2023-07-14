"""
    After making changes in the fields of the model class, 
    we must apply these changes in the db with the makemigrations command 
    and then the migrate command, 
    of course, after creating or making changes in the class methods, 
    there is no need to execute the migrate commands.
"""


"""
    According to a slogan,
    
    It is better to have bigger models and a smaller view.
    It means that as much as possible, data settings,
    including checking their conditions, setting fields and filtering,
    and other things, should be done in the models section.


"""