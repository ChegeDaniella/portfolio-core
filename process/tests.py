from django.test import TestCase
from .models import Project

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):
        self.new_project = Project(name="portfolio",description="this is a test", repository="https://github.com/ChegeDaniella/Resort_Website")

    def tearDown(self):
        Project.objects.all().delete()

    def test_save_project(self):
        self.new_project.save_project()        

