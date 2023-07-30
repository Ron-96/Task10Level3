from django import forms
from .models import AlbumTitleSuggestion

class AlbumTitleSuggestionForm(forms.ModelForm):
    """
    A Django ModelForm class for handling album title suggestions.

    This form is used to capture user-provided album title suggestions and store them
    in the corresponding model, `AlbumTitleSuggestion`. It inherits from the base
    ModelForm class provided by Django, which makes it easier to work with models.

    :param model: The model associated with this form.
    :type model: django.db.models.Model
    :param fields: The list of fields from the associated model that should be included
                   in the form.
    :type fields: list

    Attributes:
        model (django.db.models.Model): The model associated with this form. In this case,
            it is set to `AlbumTitleSuggestion`, indicating that this form is used to create
            or update instances of the `AlbumTitleSuggestion` model.

        fields (list): The list of fields from the associated model that should be included
            in the form. In this case, the form includes only the 'title' field from the
            `AlbumTitleSuggestion` model, as it represents the user's suggested album title.

    :Note:
        This form should be used to handle album title suggestions in the application.
        Make sure to link this form with a view and template to handle user input.
    """
    class Meta:
        model = AlbumTitleSuggestion
        fields = ['title']