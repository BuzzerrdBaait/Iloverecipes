from django.contrib import admin

from .models import Book, BookPage, Post, WebImgs,UserBook, UserBookPage, UserProfile, DefaultUserProfilePicture

from django.forms import Textarea

from OCR import perform_ocr

from django.db import models

from django.contrib import admin


class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'year','cover_photo')

    search_fields = ('title', 'year')

    prepopulated_fields = {'title': ('title',)}

    actions = ['compress_cover_photos']


admin.site.register(Book, BookAdmin)

class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'date')

    list_filter = ('author', 'date')

    search_fields = ('title', 'author__username')

    date_hierarchy = 'date'

    actions = ['compress_thumbnails']

admin.site.register(Post, PostAdmin)

class WebImgsAdmin(admin.ModelAdmin):

    list_display = ('title',)

    search_fields = ('title',)

    actions = ['compress_images']

admin.site.register(WebImgs, WebImgsAdmin)

class BookPageAdmin(admin.ModelAdmin):

    list_display=('book','keywords','page_photo')

    def save_model(self, request, obj, form, change):

        custom_keywords = form.cleaned_data.get('keywords')  # Replace with the actual field name from your form

        print(custom_keywords)

    
        image_field = form.cleaned_data.get('page_photo')  


        if image_field:


            try:

                path = image_field.path
                print("file name", path)


                ocrtext = perform_ocr(path)

                print(ocrtext)

                length=len(obj.keywords)

                if length > 1000:
                    obj.keywords=(ocrtext,custom_keywords)
                else:
                    obj.keywords += f"{ocrtext}"
            except:
                obj.keywords = custom_keywords



        super().save_model(request, obj, form, change)


admin.site.register(BookPage, BookPageAdmin,)

admin.site.register(UserBook,)

admin.site.register(UserProfile,)

admin.site.register(UserBookPage,)

admin.site.register(DefaultUserProfilePicture)










