from django.urls import path
from .views import (
    IssueListView,
    IssueDetailView,
    IssueCreateView,
    IssueDeleteView,
    IssueUpdateView,
    # DraftIssueListView,
    # ArchivedIssueListView,
    # PublishedIssueListView
)

# The 'name' is the name of the HTML name in Templates
urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    # path('drafts/', DraftIssueListView.as_view(), name='draft_list'),
    # path('archived/', ArchivedIssueListView.as_view(), name='archived_list'),
    # path('published/', PublishedIssueListView.as_view(), name='published_list'),
    path('<int:pk>', IssueDetailView.as_view(), name='detail'),
    path('new/', IssueCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='confirm_delete'),
]