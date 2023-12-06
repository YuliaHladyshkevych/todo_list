from django.test import TestCase
from todo.forms import TaskForm
from todo.models import Tag, Task


class TaskFormTestCase(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")

    def test_task_form_valid_data(self):
        form = TaskForm(
            data={
                "content": "Finish the report",
                "datetime_created": "2023-11-27 08:00:00",
                "deadline": "2023-11-30 17:00:00",
                "is_done": False,
                "tags": [self.tag1.id, self.tag2.id],
            }
        )

        self.assertTrue(form.is_valid())

    def test_task_form_invalid_data(self):
        form = TaskForm(
            data={
                "content": "",  # Content is required
                "datetime_created": "2023-11-27 08:00:00",
                "deadline": "2023-11-30 17:00:00",
                "is_done": False,
                "tags": [self.tag1.id, self.tag2.id],
            }
        )

        self.assertFalse(form.is_valid())

    def test_task_form_save(self):
        form = TaskForm(
            data={
                "content": "Finish the report",
                "datetime_created": "2023-11-27 08:00:00",
                "deadline": "2023-11-30 17:00:00",
                "is_done": False,
                "tags": [self.tag1.id, self.tag2.id],
            }
        )

        self.assertTrue(form.is_valid())

        task = form.save()

        self.assertIsInstance(task, Task)
        self.assertEqual(task.content, "Finish the report")
        self.assertEqual(task.tags.count(), 2)
