from django.contrib import admin
from .models import Post, Affiliate
from .forms import PostForm


class AffiliateInlineContent(admin.StackedInline):
    model = Affiliate
    extra = 1


class PostAdmin(admin.ModelAdmin):
    form = PostForm
    inlines = [AffiliateInlineContent ]
    list_display = ('id','title','pub_date','category','sub_category','feature','deactivate','author')
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
                'deactivate',
            ),
        }),
    )

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