from django.urls import path
from tasks import views
 
urlpatterns = [
    path('',views.home, name="home"),
    path('singup/', views.signup, name="signup"),
    path('tasks/', views.tasks, name="tasks"),
    path('logout/',views.signout, name="logout"),
    path('signin/',views.signin,name="signin"),
    path('tasks/create', views.createTask,name="create-task"),
    path('task/<int:task_id>', views.task_detail, name="task-detail"),
    path('tasks/completed', views.completed_tasks, name="tasks_completed"),
    path('task/<int:task_id>/complete', views.complete_task, name="complete_task"),
    path('task/<int:task_id>/delete', views.delete_task, name="delete_task")

]