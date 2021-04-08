from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/book_list.html'
    login_url = 'account_login'

    def get_queryset(self):  # new
        return Book.objects.filter(Q(title__icontains='beginners') | Q(title__icontains='api'))


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):  # new
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = 'account_login'  # new
    permission_required = 'books.special_status'  # new


class SearchResultsView(ListView): # new
    model = Book
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):  # new
        query = self.request.GET.get('q')

        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )