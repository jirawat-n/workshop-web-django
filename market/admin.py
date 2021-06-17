from django.contrib import admin
from .models import bookshop, PostImage,Category,Contact
# from .models import bookshop,Category,author,PostImage
# Register your models here.


admin.site.register(Category)
admin.site.register(Contact)

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(bookshop)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['book_id','book_name']
    list_filter = ['book_category','book_recommend','book_active']
    inlines = [PostImageAdmin]

    class Meta:
       model = bookshop

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


# class ItemAdmin(admin.ModelAdmin):
    

