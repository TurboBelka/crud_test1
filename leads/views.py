from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from . import forms, models


class LeadsList(generic.TemplateView):
    template_name = 'leads/list.html'


class TourLeadCreateView(generic.CreateView):
    template_name = 'leads/create.html'
    form_class = forms.TourLeadCreateForm
    success_url = reverse_lazy('leads:tours')


class TourLeadListView(generic.ListView):
    template_name = 'leads/all_tours.html'
    model = models.TourLeads
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(TourLeadListView, self).get_context_data(**kwargs)
        tours = models.TourLeads.objects.all()
        paginator = Paginator(tours, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            tours_pages = paginator.page(page)
        except PageNotAnInteger:
            tours_pages = paginator.page(1)
        except EmptyPage:
            tours_pages = paginator.page(paginator.num_pages)

        context['tours'] = tours_pages
        return context


class TourLeadEditView(generic.UpdateView):
    template_name = 'leads/edit_tour.html'
    context_object_name = 'tour'
    form_class = forms.TourLeadCreateForm
    model = models.TourLeads
    success_url = reverse_lazy('leads:tours')

    # def get_context_data(self, **kwargs):
    #     context = super(TourLeadEditView, self).get_context_data(**kwargs)
    #     cur_tour = models.TourLeads.objects.get(pk=self.kwargs.get('pk'))
    #     context['form'] = forms.TourLeadCreateForm(instance=cur_tour)
    #     context['language_form'] = forms.LanguagesFormSet
    #     return context


class TourLeadDeleteView(generic.DeleteView):
    model = models.TourLeads
    success_url = reverse_lazy('leads:tours')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class TourLeadDetailView(generic.DetailView):
    template_name = 'leads/tour.html'
    model = models.TourLeads
    context_object_name = 'tour'
