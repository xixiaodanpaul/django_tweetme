from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserTweetMixin

class TweetDetailView(DetailView):
	model = Tweet
	template_name = "tweets/detail_view.html"


class TweetListView(ListView):
	model = Tweet
	template_name = "tweets/list_view.html"

	def get_queryset(self):
		qs = Tweet.objects.all()
		print(self.request.GET)
		return qs


class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = "tweets/create_view.html"
	login_url = "/admin"


class TweetUpdateView(LoginRequiredMixin, UserTweetMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = "tweets/update_view.html"


class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	success_url = reverse_lazy("tweets:delete")
