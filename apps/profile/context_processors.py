from django.conf import settings


def settings_to_context(request):
    """ Context processor for settings """
    var_list = list(var for var in dir(settings) if var[:2]!="__")
    var_dict = {}
    for var in var_list:
       var_dict[var] = settings.__getattr__(var)
    return var_dict

