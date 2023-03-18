from django.contrib import admin
from .models import Category, Article, UserArticle, MyUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

################## Category Admin ##################
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Category, CategoryAdmin)

################## Article Admin ##################
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'statuse', 'created', 'category_to_str')
    list_filter = ('statuse',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['statuse']

    def category_to_str(self, obj):
        return ", ".join([category.title for category in obj.category.all()])

    category_to_str.short_description = "category"

# Register your models here.
admin.site.register(Article, ArticleAdmin)

################## MyUser Admin ##################
class MyUserAdmin(BaseUserAdmin):

    list_display = ('first_name', 'last_name', 'age', 'gender', 'user_name', 'email', 'mobile_number')
    list_filter = ('user_name',)

    fieldsets = (
        (None, {'fields': ('email',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', )}),
    )

    add_fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name', 'age', 'gender', 'mobile_number')}),
        ('Account info', {'fields': ('user_name', 'email', 'password1', 'password2')}),
    )

    search_fields = ('user_name', 'email', 'mobile_number')
    ordering = ('first_name',)

admin.site.register(MyUser, MyUserAdmin)
