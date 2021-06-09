from datetime import datetime, timezone

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from blogging.models import Post
from blogging.forms import PostForm


class BlogListView(ListView):
    model = Post
    template_name = "blogging/list.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


class BlogDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__exact=None)


class BlogAddPostView(FormView):
    model = Post
    template_name = "blogging/add.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.published_date = datetime.now(timezone.utc)
        self.object.save()
        return super().form_valid(form)
