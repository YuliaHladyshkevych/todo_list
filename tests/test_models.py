from django.test import TestCase
from todo.models import Tag, Task
from django.utils import timezone


class TagModelTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Work")

    def test_tag_str_representation(self):
        self.assertEqual(str(self.tag), "Work")

    def test_tag_unique_name(self):
        with self.assertRaises(Exception):
            Tag.objects.create(name="Work")


class TaskModelTestCase(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Work")
        self.tag2 = Tag.objects.create(name="Personal")
        self.task = Task.objects.create(
            content="Finish the report",
            deadline=timezone.now() + timezone.timedelta(days=3),
            is_done=False,
        )
        self.task.tags.add(self.tag1, self.tag2)

    def test_task_str_representation(self):
        self.assertEqual(str(self.task), "Finish the report")

    def test_task_default_values(self):
        task = Task.objects.create(content="Test task")
        self.assertFalse(task.is_done)
        self.assertIsNone(task.deadline)

    def test_task_tags(self):
        self.assertEqual(self.task.tags.count(), 2)

    def test_task_ordering(self):
        Task.objects.create(content="Task 1", is_done=True)
        Task.objects.create(content="Task 2")

        tasks = Task.objects.all()
        self.assertEqual(tasks[0].content, "Task 2")
        self.assertEqual(tasks[1].content, "Finish the report")
        self.assertEqual(tasks[2].content, "Task 1")
