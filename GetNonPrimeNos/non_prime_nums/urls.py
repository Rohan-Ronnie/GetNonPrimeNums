from django.conf.urls import include, url

urlpatterns = [

                       url(r'^service/', include('non_prime_nums.service.urls')),

]