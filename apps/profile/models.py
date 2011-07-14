from django.db import models


class Contact(models.Model):
    """  Contacts model for ticket #1
         shows contact
    """
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    bio = models.TextField()
    contacts = models.CharField(max_length=50)
    email = models.EmailField()
    jabber = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    other_contacts = models.TextField()

    def __unicode__(self):
        return u"%s %s" % (self.name, self.lastname)



