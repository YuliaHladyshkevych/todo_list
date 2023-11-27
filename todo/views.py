from django.shortcuts import render
from django.views import generic

from todo.models import Tag, Task


# def index(request):
#
#     num_tags = Tag.objects.count()
#     num_tasks = Task.objects.count()
#
#     num_visits = request.session.get("num_visits", 0)
#     request.session["num_visits"] = num_visits + 1
#
#     context = {
#         "num_tags": num_tags,
#         "num_tasks": num_tasks,
#         "num_visits": num_visits + 1,
#     }
#
#     return render(request, "todo/index.html", context=context)

class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(TaskListView, self).get_context_data(**kwargs)
    #     name = self.request.GET.get("name", "")
    #     context["search_form"] = TaskSearchForm(initial={
    #         "name": name
    #     })
    #
    #     return context
    #
    # def get_queryset(self):
    #     queryset = Task.objects.all()
    #     form = TaskSearchForm(self.request.GET)
    #
    #     if form.is_valid():
    #         return queryset.filter(name__icontains=form.cleaned_data["name"])
    #
    #     return queryset


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 5

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super(TaskTypeListView, self).get_context_data(**kwargs)
    #     name = self.request.GET.get("name", "")
    #     context["search_form"] = TaskTypeSearchForm(initial={
    #         "name": name
    #     })
    #
    #     return context
    #
    # def get_queryset(self):
    #     queryset = TaskType.objects.all()
    #     form = TaskTypeSearchForm(self.request.GET)
    #
    #     if form.is_valid():
    #         return queryset.filter(name__icontains=form.cleaned_data["name"])
    #
    #     return queryset
