"""
    * an initial value can be set for the arguments sent from the url to the view,
    in which case that argument can receive or not receive a value from the url.

    * arguments with initial value must be written from the end in the input of the views function:

"""

"""

## urls file ##

path('hello/<int:a>/<int:b>/<int:c>/', index2, name='index2'),


## views file ##

def index2(request, a , b , c=10 ):
	pass

"""