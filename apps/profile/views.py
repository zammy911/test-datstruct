from compat.decorators import render_to
from profile.models import * 
from django.shortcuts import get_object_or_404


@render_to('app.html')
def show_contact(request):
    """
    Displays contacts
    """
    return ({
       'contact': Contact.objects.all(),
       })

