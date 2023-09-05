from django.contrib import admin

# Register your models here.
import blog.models
from blog.models import Artikel

class PubArtikel(admin.ModelAdmin):
    def save_model(self, request, obj, form, change) :
        if self.model._meta.model_name == 'category' :
            exclue = ('penulis')
        elif not obj.penulis:
            obj.penulis = request.user
        obj.save()
     
    def get_readonly_fields(self, request, obj=None):
        current_user = request.user
        
        readonly_fields = []

        if isinstance(obj, Artikel):
            readonly_fields.extend(['date_create', 'date_edit'])
            if current_user.has_perm('blog.terbitkan'):
                readonly_fields.extend(['penulis', 'slug'])
            elif current_user.has_perm('blog.add_artikel'):              
                if obj.publish:
                    return [data.name for data in self.model._meta.fields]
                else:
                    readonly_fields.extend(['slug', 'publish', 'penulis'])
        return readonly_fields

for model_name in dir(blog.models):
    model = getattr(blog.models, model_name)
    if isinstance(model, type) :
        admin.site.register(model, PubArtikel)