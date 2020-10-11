from django.contrib import admin
from .models import Post, Affiliate
from .forms import PostForm

class AffiliateInlineContent(admin.StackedInline):
    model = Affiliate
    extra = 1

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [AffiliateInlineContent]
    list_display = ('id','title','pub_date','category','sub_category','feature','deactivate')
    list_display_links = ('id','title')
    list_filter = ('category','sub_category','feature','deactivate')
    search_fields = ('title',)
    ordering = ['id']
    fieldsets = (
        (None, {
            "fields": (
                'title',
                'short_description',
                'banner',
                'category',
                'sub_category',
                'content',
                'feature',
                'pub_date',
                'tags',
                'deactivate'
            ),
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)