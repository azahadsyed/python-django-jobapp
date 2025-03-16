from django.contrib import admin

from app.models import Author, JobPost, Location, Skill

# class JobAdmin (admin.ModelAdmin):
#     pass


    
class JobAdmin (admin.ModelAdmin):
#    list_display= ('title',)
#    list_display= ('title','date','salary')
#    list_display= ('title','salary','date')
     list_display= ('__str__','title','salary','date')
    #  list_filter=('date',)
     list_filter=('date','salary','expiry',)
     search_fields= ['title','description']
     search_help_text ="Write in your query and hit enter"
    #  fields=(('title','description'),'expiry')
    #  exclude = ('title',)
     fieldsets = ( 
                 
        ('Basic Information', {"fields": ( 'title','description'),}),
        ('More Information',{'classes': ('collapse',),"fields": (('salary','expiry'),'slug')}),
    )
    
# Register your models here.
# admin.site.register(JobPost,JobAdmin)
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skill)