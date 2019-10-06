from django.test import TestCase
from .models import Uploader, Uploads, tags
import datetime as dt
# Create your tests here.



# Create your tests here.
class UploaderTestClass(TestCase):

    #Set up method
    def setUp(self):
        self.sam= Uploader(first_name = 'Sam', last_name ='Nujoma', email ='sam@gmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sam,Uploader))


    #Testing save method
    def test_save_method(self):
        self.sam.save_uploader()
        uploaders = Uploader.objects.all()
        self.assertTrue(len(uploaders) > 0)


class UploadstestClass(TestCase):

    def setUp(self):
        #Creating a new editor and saving it
        self.sam= Uploader(first_name = 'James', last_name = 'Nujoma', email = 'sam@gmail.com')
        self.sam.save_uploader()

        #Creating a  new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Uploads(title = 'Test Article', post = 'This is a random test Post',editor = self.sam)
        self.new_uploads.save()

        self.new_uploads.tags.add(self.new_tag)

    def tearDown(self):
        Uploader.objects.all().delete()
        tags.objects.all.delete()
        Uploads.objects.all.delete()

    
    def test_get_news_today(self):
        today_photos = Uploads.todays_photos()
        self.assertTrue(len(today_photos)>0)

    def test_get_photos_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()

