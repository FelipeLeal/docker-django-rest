"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from drugstore import views

urlpatterns = [
    # =====================REST API Spec - Drug=====================
    #
    # [GET] Array with all the drugs
    path('drugs', views.DrugList.as_view(), name='drugs_list'),
    # [GET] Return a drug by its id. Returns status 404 if drug is not found.
    path('drugs/<int:pk>', views.DrugDetail.as_view()),
    # [POST] Create a drug based on json payload. Returns status 201 with a json
    # body on success. Returns status 400 on validation error or when “Content-Type”
    # header is not set as “application/json”. Returns status 500 on every other error.
    path('drug', views.DrugDetail.as_view()),
    # [PUT] Updates a drug based on its id and a json payload. Returns status
    # 200 on success. Return status 404 if drug is not found. Returns status 400 on
    # validation error or when “Content-Type” header is not set as “application/json”.
    # Returns status 500 on every other error.
    path('drug/<int:pk>', views.DrugDetail.as_view()),
    # [DELETE] Deletes a drug based on its id. Returns status 204 on success.
    # Return status 404 when drug is not found. If this drug has vaccinations associated,
    # it returns status 400.
    path('drug/<int:pk>', views.DrugDetail.as_view()),

    # =====================REST API Spec - Vaccination=====================
    #
    # [GET] Array with all the vaccinations
    # [POST] Create a vaccination based on json payload. Returns status
    # 201 with a json body on success. Returns status 400 on validation error or when
    # “Content-Type” header is not set as “application/json”. Returns status 500 on
    # every other error.
    path('vaccinations', views.VaccinationList.as_view(), name='vaccination_list'),

    # [GET] return a vaccination by its id. Returns status 404 if
    # vaccination is not found.
    # [PUT] Updates a vaccination based on its id and a json payload.
    # Returns status 200 on success. Return status 404 if vaccination is not found.
    # Returns status 400 on validation error or when “Content-Type” header is not set as
    # “application/json”. Returns status 500 on every other error.
    path('vaccinations/<int:pk>', views.VaccinationDetail.as_view()),

    # JWT Auth
    path('token/', views.ValidationView.as_view(), name='token_obtain'),
]
