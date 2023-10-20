from .models import SiteContacts

def site_contacts(request):
    site_contacts = SiteContacts.objects.first()

    context = {
        "site_contacts": site_contacts
    }

    return context