
def success(data):
    return {
        'status': 'success',
        'data': data
    }

def error(error_message):
    return {
        'status': 'error',
        'error_func': error_message
    }

__All__ = []