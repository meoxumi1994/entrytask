class Error(object):
    VALUE = 'Value Error'
    OS = 'Operation System Error'
    AUTH_FAILED = 'You are missing access_token or access_token is not valid'
    CANNT_HANDLE = 'cann\'t handle this error, please see error in log'
    USER_NAME_OR_PASSWORD = 'missing user_name or password'
    REQUEST_NOT_VALID = 'request is not valid'
    USER_NAME_USED = 'user_name has been used'
    WRONG_PASSWORD = 'wrong password'
    MISSING_EVENT_TIME = 'missing event time'
    MISSING_USER_NAME = 'missing user name'

__All__ = ['Error']