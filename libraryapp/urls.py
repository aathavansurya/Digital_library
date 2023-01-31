from django.urls import path

from libraryapp import views

urlpatterns=[
    path('',views.login,name='login'),  #  it will take to login page
    path('log',views.readlog),          #  it will check login credentials and take to home page

    path('adminhome',views.adhome,name='adhome'),

    path('adminreg',views.adminreg),   # it will redirect to admin registration page
    path('adred',views.adminred),   # it will read the admin page details and store in the User table

    path('studentregone',views.stdregred),  # it will take to the student registration page
    path('studentreg',views.studentred),   # it will read the student data and store in the student table

    path('addbk',views.addbk_fun,name='addbk'),  # it will take to add book page
    path('redbook',views.redbk_fun),    # it will read the book data and store into the book table

    path('display',views.display,name='dis'),      # it will take to book details display page..
    path('delete/<int:id>', views.delete, name='del'),   # it will delete the Book table book details
    path('update/<int:id>',views.update,name='up'),   # it will take to update page of the book tables

    path('logout',views.logout,name='out'),    # it will take to login page

    path('assign',views.assign,name='assign'),       # it will take to assign book page
    path('sc',views.redassign),                     # it is used to get a student name and book name data..as per the semester and course details
    path("assignred",views.assignbook,name='assg'),       # it will assign the book to the  student

    path('display2',views.issubk,name="issuebk"),      # it will display the assigned book details
    path('delete1/<int:id>',views.delete1,name='del1'),     # it will delete the assign book details
    path('vanish/<int:id>',views.update2,name='update'), #it will update the record
    path('stddisplay',views.call,name='std_dis'), # it will send perticular student data
                                                  # to that same student  home page
    path('stdhome',views.stdhome,name='std_home'),

    path('dispro',views.disprofile,name='profile'),
    path('edit',views.edit,name='edit'),


]