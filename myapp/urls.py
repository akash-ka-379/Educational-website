from django.urls import path
from.import views
urlpatterns=[
    path('about/',views.about,name="about"),
    path('boots/',views.boots,name="boots"),
    path('django/',views.django,name="django"),
    path('edu/',views.edu,name="edu"),
    path('flask/',views.flask,name="flask"),
    path('java/',views.java,name="java"),
    path('python/',views.python,name="python"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('logout/',views.logout,name="logout")

]