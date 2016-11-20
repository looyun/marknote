# from django.shortcuts import render
from django.views.generic import DetailView, CreateView, TemplateView, UpdateView, DeleteView


from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect, get_object_or_404


from . import forms, models


# Create your views here.


class NoteDetailView(DetailView):
    template_name = "notes/note.html"
    model = models.Note

    pk_url_kwarg = "pk"

    def get_object(self, queryset=None):
        obj = super(NoteDetailView, self).get_object()
        return obj


class AddView(CreateView):
    template_name = "notes/add.html"
    model = models.Note
    form_class = forms.PostForm

    @csrf_exempt
    def form_valid(self, form):

        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return redirect("/")


class EditView(UpdateView):
    template_name = "notes/edit.html"
    model = models.Note
    pk_url_kwarg = "pk"
    fields = [
        'title',
        'content',
    ]
    success_url = "/"


class IndexView(TemplateView):
    template_name = "notes/index.html"

    def get_context_data(self, **kwargs):

        # note = get_object_or_404(models.Note)

        kwargs['notes'] = models.Note.objects.all()

        return super(IndexView, self).get_context_data(**kwargs)


class CateView(TemplateView):
    template_name = "notes/category.html"

    def get_context_data(self, **kwargs):

        # note = get_object_or_404(models.Note)

        kwargs['notes'] = models.Note.objects.all()

        return super(CateView, self).get_context_data(**kwargs)


class NoteDeleteView(DeleteView):

    model = models.Note
    success_url = "/"
