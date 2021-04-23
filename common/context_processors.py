from .models import Contact


def pages(request):
    contacts_dict = get_contacts_dict(list(Contact.objects.all()))
    return {'contacts': contacts_dict}


def get_contacts_dict(contacts_list) -> dict:
    contacts_dict = dict()
    for contact in contacts_list:
        if contact.tag == 'Расписание':
            value = contact.value.split('|')
        else:
            value = contact.value
        contacts_dict[contact.tag] = value

    return contacts_dict

