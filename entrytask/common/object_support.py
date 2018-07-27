
def assign(md, body, list_att):
    for att in list_att :
        if att in body :
            setattr(md, att, body[att])

__All__ = []