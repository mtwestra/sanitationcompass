from django.contrib import admin
from django.apps import apps
from django.forms import ModelForm
from django.utils.translation import ugettext, ugettext_lazy as _
from comp.models import Technology, TechGroup

class AnswerAdmin(admin.ModelAdmin):
    model = apps.get_model('comp', 'Answer')

admin.site.register(apps.get_model('comp', 'Answer'), AnswerAdmin)


class CriterionInLine(admin.TabularInline):
    model = apps.get_model('comp', 'Criterion')
    extra = 3

class FactorAdmin(admin.ModelAdmin):
    model = apps.get_model('comp', 'Factor')
    list_display = ('factor', 'order', 'display_criteria',)
    inlines = [CriterionInLine, ]

admin.site.register(apps.get_model('comp', 'Factor'), FactorAdmin)


class RelevancyInLine(admin.TabularInline):
    model = apps.get_model('comp', 'Relevancy')
    extra = 0

class TechnologyAdminForm(ModelForm):

    class Meta:
        model = Technology
        fields = '__all__' # Or a list of the fields that you want to include in your form

    # def __init__(self, *args, **kwargs):
    #    super(TechnologyAdminForm, self).__init__(*args, **kwargs)
    #    try:
    #        output_groups = TechGroup.objects.filter(order__gt=self.instance.group.order)
    #    except TechGroup.DoesNotExist:
    #        output_groups = []
    #    if len(output_groups):
    #        self.fields['output'].queryset = Technology.objects.filter(group__order__exact=output_groups[0].order)
    #    else:
    #        self.fields['output'].queryset = Technology.objects.filter(pk=0) #Empty QS

class TechnologyAdmin(admin.ModelAdmin):
    model = apps.get_model('comp', 'Technology')
    list_display = ('__str__', 'group', 'display_output',  'display_input', 'display_image', )
    ordering = ['group__order']
    inlines = [RelevancyInLine, ]
    form = TechnologyAdminForm

admin.site.register(apps.get_model('comp', 'Technology'), TechnologyAdmin)

class NoteAdmin(admin.ModelAdmin):
    model = apps.get_model('comp', 'Note')

admin.site.register(apps.get_model('comp', 'Note'), NoteAdmin)

class TechGroupAdmin(admin.ModelAdmin):
    model = apps.get_model('comp', 'TechGroup')

admin.site.register(apps.get_model('comp', 'TechGroup'), TechGroupAdmin)
