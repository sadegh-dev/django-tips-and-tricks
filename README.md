# django-tips-and-tricks


# launch [complete]
	- config settings for launch
	- delete static settings from main urls.py
	- upload django project on server


# general [complete]
	- general points
	- running multiple Django projects through different ports 
	- run command on shell
	- Meta class


# install [complete]
	- create project
	- rename project


# settings [complete]
	- general config
	- general variables
	- connect to email-service [like gmail]


# HttpRequest


# templates
	- default template structure
	- center template structure
	- template structure connect react
	- send data from views to template
	- access to HTTP-method
	- initialize the variable by with
	- create link
	- * partitioning HTML files
	- pagination
	- list tags
	- built-in template filter
	- create html page 404


# static/media
	- static files
	- media files
	- media and statc files structures
	- run collectstatic command
	- use jquery


# views
	- points of views
	- decoratores
	- structure views function
	- direct use HTML-tag in function-views
	- redirect in views
	+ CBV : class base view [https://ccbv.co.uk/]
		- View class
		- TemplateView class
		- RedirectView class
		- ListView class
		- DetailView class
		- MonthArchiveView class

		- FormView class
		- CreateView class
		- DeleteView class
		- UpdateView class

		- mixin
		- FormMixin

	- manager types [like: get, all, filter]
	- custom decorator for computing querySet time
	- optimization QuerySet for get data in relation-class
	- list field-lookups of querySet
	- F-experssions
	- union several querySet
	- create-update-delete-add
	- create search
	- complex lookup – Q function
	- Full text search
	- create custom manager
	- Http 404


# messages
	- points of message
	- create message


# signals
	- points of signals
	- practical examples of signals
	- basic signal settings
	- pre_save - post_save
	- way of call the signals method
	- pre_delete - post_delete


# urls
	- points of urls *
	- Error handling
	- create url by parameters
	- Initial value for passed arguments *
	- path function *
	- re_path function
	- set url-name *
	- cancellation of famous url-name *
	- set namespace for app *
	- create unique url-slug *
	- send parameters by url to views *
	- persian url *
	- set slug in admin panel *
	- reverse, reverse_lazy methods
	- difference in methods of reverse - reverse_lazy
	- grouping urlpatterns
	- Subset creation for addresses with a common pattern
    - send additional data to path ans include


# admin
	- points of admin
	- default admin-panel
	- custom admin-panel for the class
	- admin action
	- admin title
	- custom style admin-panel
	- creating computational field in admin-panel
	- set validation-field in admin-panel


# app [complete]
	- points of app
	- create new app
	- create app inside main directory


# models
	- * points of models
	- * create package model
	- * ORM : object relational mapping
	- * naming model
	- * field types
	- * field options
	+ related methods 
		- create method
		- save method
		- delete method
		- add method
		- remove method
		- clear method
		- set method
		- update method
	+ * override default methods
		- override save method
		- override delete method
	- * creating proccessing functions on field
	- * create custom validation of field
	- * __str__ method in model-class
	- * get_absolute_url method in model-class
	- * Meta class in model-class
	+ abstract - inheritance
		- abstract base classes
		- multi-table inheritance
		- proxy models
	+ relation between classes
		- one to many [ForeignKey]
		- one to one
		- many to many
		- intermediate model
		- backward relation
		- on_delete attribute
		- limit_choices_to attribute
	- migrations
	- content types


# middleware


# db
	- points of database
	- sqlite3
	- postgreSQL
	- mySQL
	- mongoDB
	- use several databases


# forms [complete]
	- * strategy
	- * points of forms
	- * normal form structure
	- * list of fields-form
	- * list of widgets
	- * create date-time field
	- create shamsi date-time field
	- * create form by forms.ModelForm
	- * help_desk - widget - error_messages in forms.ModelForm
	- * create edit-form by forms.ModelForm
	- ** edit 2 model-class by 1 form
	- * create delete-button by forms.ModelForm
	- * initialization fields-form
	- set reCAPTCHA in form
	- * create form by forms.Form
	- create 2 form in 1 page
	- ** different ways of displayeing form in html-page
	- * default validation and form errors
	- ** create custom validation form
	- ** set persian form-errors
	- deactive validation-fom [not recommended]
	- * management forms.ValidationError


# Authentication
	- * points of auth
	- [NOT USE] use default User-model-class
	- [NOT USE] relation one-to-one with default User-model-class
	- ** custom User-model-class
	- * different AbstractUser and AbstractBaseUser
	- use CBV in authentication Views
	- ** change authentication password
	- [check] oauth
	- reset password by CBV for send email
	- *signup new-user by create_user method in default User-model-class
	- ** default login method
	- [NOT USE] use authentication-backend for get Email and use comparison username and email
	- ** default logout method
	- ** access user-data in views after login
	- ** access user-data in template-file after login
	- block out run function-views for user not logged
	- block out run class-views for user not logged
	- [NOT USE] default register method [with more fields]
	- [NOT USE] create one-to-one User-class with profile-class
	- [NOT USE]	create password and confirm password fields
	- determining the user path after logout
	- allow access to own page, not others
	- login by phone number


# security
	- security topics
	- protected admin-panel-url
	- security of period upload project
	- cross site scripting (XSS)
	- python-decouple
	- points of security


# permission


# debugging


# celery
	- points of celery
	- use celery in python code
	- flower
	- management comman-line utilities
	- signatures in celery
	- use celery in django project
	- example of django-celery project
	- celery beat
	- example2 of dajngo-celery project
	- worker running in background by supervisor



# caching
	- plan
	- cache levels
	- caching by redis
	- caching by memcached
	- cache arguments
	- cache full webiste page
	- cache views
	- cache template
	- delete old cache when new data is added
	- The low-level cache API
	- downstream caches


# sessions


# testing
	- points of testing
	- testing plan
	- testing directory
	- run tests
	- test inheritance
	- assertions
	- testing tools
	- testing urls
	- testing forms
	- testing models
	- testing views
	+ pytest module for django project
		- pytest mark functions
		- custom mark functions
		- fixture method


# aggregation


# annotate
	- aggregating annotations



# gunicorn

# dockerize



# modules
	- custom module
	- Markdown module
	- RegEx module
	- ckeditor module
	- pillow module
	- timezone module
	- sorl-thumbnail module
	- django-filter module

