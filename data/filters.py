from unicodedata import category
import django_filters 
from django_filters import DateFilter
from .forms import *
from .models import *
from django.contrib.auth import get_user_model,login,authenticate
from django.views.generic import (CreateView,DeleteView,ListView,TemplateView, DetailView,UpdateView)

#User=settings.AUTH_USER_MODEL
User = get_user_model()


class InterviewFilter(django_filters.FilterSet):
    #start_date=DateFilter(field_name="upload_date",lookup_expr='gte')
    #end_date=DateFilter(field_name="upload_date",lookup_expr='lte')
    class Meta:
        model=Interviews
        fields='__all__'
        exclude=['upload_date','doc','link','is_active','featured']



class BitrainingFilter(django_filters.FilterSet):
    #start_date=DateFilter(field_name="upload_date",lookup_expr='gte')
    #end_date=DateFilter(field_name="upload_date",lookup_expr='lte')
    class Meta:
        model=FeaturedCategory
        fields='__all__'
        exclude=['updated_at','description','created_at','is_active','created_by']



'''
class InterviewFilter(django_filters.FilterSet):
     class Meta:
         model = Interview
         fields = ['first_name', 'upload_date']
         #fields='__all__'
         filter_overrides = {
             models.CharField: {
                 'filter_class': django_filters.CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
             models.BooleanField: {
                 'filter_class': django_filters.BooleanFilter,
                 'extra': lambda f: {
                     'widget': forms.CheckboxInput,
                 },
             },
        }
''' 