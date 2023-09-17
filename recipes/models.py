from PIL import Image

from io import BytesIO

from django.db import models

from django.core.files.uploadedfile import SimpleUploadedFile

from django.contrib.auth.models import User



# Define the updated compress_and_optimize_image function


class Book(models.Model):

    title = models.CharField(max_length=200)

    year = models.PositiveSmallIntegerField()

    cover_photo = models.ImageField(upload_to='book_covers/')



    



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.cover_photo)
    
    def compress_and_optimize_image(self, image_field):
        img = Image.open(image_field.path)

        image_io = BytesIO()



        # Save the compressed image to the BytesIO object

        img.save(image_io, format='JPEG', quality=20, optimize=True)



        # Save the compressed image back to the same image field

        image_field.file = SimpleUploadedFile(

            image_field.name, image_io.getvalue(), content_type='image/jpeg')



        # Save the changes to the image field

        image_field.save(image_field.name, image_field.file, save=False)
    def __str__(self):

        return self.title
    



class BookPage(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')

    keywords = models.CharField(max_length=800)

    page_photo = models.ImageField(upload_to='book_pages/')




    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.page_photo)
    def compress_and_optimize_image(self, image_field):
        img = Image.open(image_field.path)
        img.save(image_field.path, quality=20, optimize=True)

    def __str__(self):

        return f"Page {self.pk} of {self.book.title}"

class Post(models.Model):

    title = models.CharField(max_length=255)

    video_file = models.FileField(upload_to='blog_videos/')

    thumbnail = models.ImageField(upload_to='thumbnails/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    body = models.TextField()

    date = models.DateField()



    



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.thumbnail)

    def compress_and_optimize_image(self, image_field):
        img = Image.open(image_field.path)
        img.save(image_field.path, quality=20, optimize=True)

    def __str__(self):

        return self.title + '|' + str(self.author)

class WebImgs(models.Model):

    title = models.CharField(max_length=25)

    thumbnail = models.ImageField(upload_to='web_imgs/')



    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)

        self.compress_and_optimize_image(self.thumbnail)

    def compress_and_optimize_image(self, image_field):
        img = Image.open(image_field.path)
        img.save(image_field.path, quality=20, optimize=True)