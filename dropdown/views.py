from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Person, Country, State, City, District
from .forms import PersonForm

# Create your views here.
class ProfileListView(ListView): 
    model = Person
    form_class = PersonForm
    template_name = 'dropdown/profile_list.html'
    context_object_name = 'profile'

class ProfileCreateView(CreateView):
    model = Person
    template_name = 'dropdown/profile_form.html'
    form_class = PersonForm
    success_url = reverse_lazy('profile_changelist')


class ProfileUpdateView(UpdateView):
    model = Person
    template_name = 'dropdown/profile_form.html'
    form_class = PersonForm  
    success_url = reverse_lazy('profile_changelist')



def load_state(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id) 
    return render(request, 'dropdown/state_dropdown_list_options.html', {'states': states})

def load_district(request):
    state_id = request.GET.get('state_id')
    districts = District.objects.filter(state_id=state_id)
    return render(request, 'dropdown/district_dropdown_list_options.html', {'districts': districts})

def load_city(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id) 
    return render(request, 'dropdown/city_dropdown_list_options.html', {'cities': cities})



