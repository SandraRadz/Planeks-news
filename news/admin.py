from django.contrib import admin

from news.models import Comment, New


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'date_created')
    list_filter = ('date_created',)
    exclude = ['pub_date']
    inlines = [CommentInline]


admin.site.register(New, NewAdmin)