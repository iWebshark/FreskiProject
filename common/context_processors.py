from .models import Contact


def pages(request):
    contacts_dict = get_contacts_dict(list(Contact.objects.all()))
    return {'contacts': contacts_dict}


def get_contacts_dict(contacts_list) -> dict:
    contacts_dict = dict()
    for contact in contacts_list:
        contacts_dict[contact.tag] = contact.value
    return contacts_dict
