from django.contrib import admin
from .models import Post, Affiliate
from .forms import PostForm


class AffiliateInlineContent(admin.StackedInline):
    model = Affiliate
    exclude = ['when']
    extra = 1


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [AffiliateInlineContent ]
    list_filter = ('category','sub_category','feature')
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
                'tags',
                'feature',
                'promoted',
                'deactivate',
            ),
        }),
    )


    def changelist_view(self, request, extra_context=None):    
        if not request.user.is_superuser:
            self.list_display_links = ('id','title')
            self.list_display = ('id','title','pub_date','category','sub_category','feature','promoted')
        else:
            self.list_display_links = ('id','title')
            self.list_display = ('id','title','pub_date','category','sub_category','feature','promoted','author')
        return super(PostAdmin, self).changelist_view(request, extra_context)


    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)
    

    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)