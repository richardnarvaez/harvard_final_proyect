from django.contrib import admin
from django.urls import path
from ejob_app import views
from ejob_app.views import UserController
# from  django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", UserController.show_home_page, name='index'),
    path("login", UserController.login, name='login'),
    path("job_details/<int:job_id>",views.ApplicationController.job_details, name="job_details"),
    path("apply/<int:job_id>", views.ApplicationController.apply, name='apply'),
    path("see_applications", views.ApplicationController.my_applications, name="my_applications"),
    path("seeker_register",views.UserController.seekerRegister, name='seeker_register'),
    path("recruiter_register", views.UserController.recruiterRegister, name='recruiter_register'),
    path("search/", views.SearchController.search_for_jobs, name="search_list"),
    path("seekerprofile",views.UserController.seekerProfile, name= 'seeker_profile'),
    path("recruiterprofile",views.UserController.recruiterProfile, name='recruiter_profile'),
    path("skills",views.UserController.add_skills, name='skills'),
    path("add_jobs", views.JobController.add_job, name='add_job'),
    path("manage_jobs", views.JobController.manage_jobs, name='manage_jobs'),
    path('job_edit/<int:job_id>', views.JobController.edit_job, name='job_edit'),
    path('applications/<int:application_id>',views.JobController.applications, name='applications'),
    path('applicant_details/<int:job_id>/<int:seeker_profile_id>',
         views.JobController.applicant_details, name='applicant_details'),
    path('accept_applicant/<int:application_id>',views.JobController.accept_applicant, name='accept_applicant'),
    path('reject_applicant/<int:application_id>',views.JobController.reject_applicant, name='reject_applicant'),
    path('logout', views.UserController.logout_user, name='logout'),
    path('ajax/load_subcategory',views.AjaxRequestController.subcategory, name='subcategory'),
    path('interview_call/<int:application_id>', views.JobController.interview_call, name='send_interview_call'),
    path('accept_final_applicant/<int:application_id>', views.JobController.accept_final_applicant, name='accept_final_applicant'),
    path('ajax/load_category', views.AjaxRequestController.category, name='category')
]
