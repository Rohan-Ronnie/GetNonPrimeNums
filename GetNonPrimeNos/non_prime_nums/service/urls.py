from django.conf.urls import include, url
from tastypie.api import Api
from non_prime_nums.service.non_prime_nums_service import GetNonPrimeNumsResource

v1_non_prime_nums_api = Api(api_name='v1')
v1_non_prime_nums_api.register(GetNonPrimeNumsResource())
urlpatterns = [
    url(r'^', include(v1_non_prime_nums_api.urls))
]