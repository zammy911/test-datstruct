from compat.decorators import render_to
from profile.models import * 
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
@render_to('base.html')
def show_contact(request):
    """
    Displays contacts
    """
    return ({
       'contact': Contact.objects.all(),
       })

