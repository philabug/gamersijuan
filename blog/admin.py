from django.contrib import admin
from .models import Post, Affiliate
from .forms import PostForm

class AffiliateInlineContent(admin.StackedInline):
    model = Affiliate
    extra = 1

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [AffiliateInlineContent]
    list_display = ('id','title','pub_date','author')
    list_display_links = ('id','title')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            "fields": (
                'title',
                'banner',
                'content',
                'feature',
                'pub_date',
                'tags',
                'slug',
            ),
        }),
    )
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)