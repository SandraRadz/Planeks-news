from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from news.models import Comment, New


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class NewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'status', 'date_created')
    list_filter = ('date_created',)
    exclude = ['pub_date']
    inlines = [CommentInline]
    summernote_fields = ('text',)


admin.site.register(New, NewAdmin)