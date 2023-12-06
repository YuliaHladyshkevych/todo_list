from django.http import Http404
from django.test import TestCase
from django.urls import reverse
from todo.models import Task, Tag


class TaskViewsTestCase(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Home")
        self.task = Task.objects.create(content="Finish the report", is_done=False)
        self.task.tags.add(self.tag1, self.tag2)

    def test_task_list_view(self):
        response = self.client.get(reverse("todo:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/task_list.html")

    def test_task_complete_view(self):
        response = self.client.get(
            reverse("todo:task-complete", kwargs={"pk": self.task.pk})
        )
        self.assertEqual(response.status_code, 302)
        completed_task = Task.objects.get(pk=self.task.pk)
        self.assertTrue(completed_task.is_done)


class TagViewsTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Work")

    def test_tag_list_view(self):
        response = self.client.get(reverse("todo:tag-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, "todo/tag_list.html"
        )
