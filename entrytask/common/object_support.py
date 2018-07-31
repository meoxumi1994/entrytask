import string, random


def assign(md, body, list_att):
    for att in list_att :
        if att in body :
            setattr(md, att, body[att])

def require(body, list_att):
    for att in list_att:
        if not att in body:
            return "missing " + att + " field"
    return False

def get_params(request):
    body = {}
    for key in request.GET.iterkeys():
        body[key] = request.GET.get(key)
    return body

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

__All__ = []