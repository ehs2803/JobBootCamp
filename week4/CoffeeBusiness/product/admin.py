from django.contrib import admin

from product.models import Product, Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title_en', 'title_kr', 'detail']
    search_fields = ['title_kr']

    def __str__(self):
        return self.title_kr

class CommentAdmin(admin.ModelAdmin):
    list_display = ['content_list', 'content', 'author', 'create_date', 'modify_date']
    search_fields = ['author']


admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)