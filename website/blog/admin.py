from django.contrib import admin
from .models import Post
admin.site.register(Post)

# Procedure for registering the Modular Form
from .models import EnqDB
from .form import EnqDBForm

class EnqDBAdmin(admin.ModelAdmin):
    list_display = ['name','mail','mno','messege']
admin.site.register(EnqDB,EnqDBAdmin)


from .models import Postlu
from .form import Postform

class PostAdmin(admin.ModelAdmin):
    list_display = ['author','title','text','created_date']
admin.site.register(Postlu,PostAdmin)











