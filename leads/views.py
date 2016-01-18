from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from . import forms, models


class LeadsList(generic.TemplateView):
    template_name = 'leads/list.html'


class AddEditViexMixin(object):
    title = ''

    def get_context_data(self, **kwargs):
        context = super(AddEditViexMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        if pk:
            self.object = self.get_object()
            form = self.form_class(request.POST, instance=self.object)
            languages_formset = forms.LanguagesFormSet(request.POST,
                                                       instance=self.object)
        else:
            form = self.form_class(request.POST)
            languages_formset = forms.LanguagesFormSet(request.POST)

        if form.is_valid() and languages_formset.is_valid():
            return self.form_valid(form, languages_formset)
        else:
            return self.form_invalid(form, languages_formset)

    def form_valid(self, form, formset):
        if not hasattr(self, 'object'):
            self.object = formset.instance = form.save()
        else:
            form.save()
        formset.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                languages_formset=formset,
            )
        )


class TourLeadCreateView(AddEditViexMixin, generic.CreateView):
    form_class = forms.TourLeadCreateForm
    template_name = 'leads/create.html'
    success_url = reverse_lazy('leads:tours')
    model = models.TourLeads
    title = 'Add'

    def get_context_data(self, **kwargs):
        context = super(TourLeadCreateView, self).get_context_data(**kwargs)
        if not context.get('languages_formset'):
            context['languages_formset'] = forms.LanguagesFormSet(instance=models.TourLeads())
        return context


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
        context['title'] = 'Tour Leads'
        return context


class TourLeadEditView(AddEditViexMixin, generic.UpdateView):
    template_name = 'leads/create.html'
    context_object_name = 'tour'
    form_class = forms.TourLeadCreateForm
    model = models.TourLeads
    title = 'Update'
    success_url = reverse_lazy('leads:tours')

    def get_context_data(self, **kwargs):
        context = super(TourLeadEditView, self).get_context_data(**kwargs)
        cur_tour = models.TourLeads.objects.get(pk=self.kwargs.get('pk'))
        context['form'] = forms.TourLeadCreateForm(instance=cur_tour)
        context['languages_formset'] = forms.LanguagesFormSet(instance=self.object)
        return context


class TourLeadDeleteView(generic.DeleteView):
    model = models.TourLeads
    success_url = reverse_lazy('leads:tours')


class TourLeadAllDeleteView(generic.View):

    def post(self):
        tours_for_delete = self.request.POST.values()[1:]
        models.TourLeads.objects.filter(id__in=tours_for_delete).delete()
        return JsonResponse({'url': str(reverse_lazy('leads:tours'))})


class TourLeadDetailView(generic.DetailView):
    template_name = 'leads/tour.html'
    model = models.TourLeads
    context_object_name = 'tour'
