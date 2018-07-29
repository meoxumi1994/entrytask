from django.http import HttpResponse, JsonResponse
from common.auth import auth_admin, auth_visitor
from common.error_support import Error
import traceback, sys

import time
import logging

logger = logging.getLogger('django')

def handle_json_response(f):
    def wrapper(request):
        response = f(request)
        if not response :
            return JsonResponse({ 'error' : Error.REQUEST_NOT_VALID }, safe=False)
        return JsonResponse(response, safe=False)
    return wrapper

def handle_error(f):
    def wrapper(request):
        try:
            start_time = time.time()
            response = f(request)
            logger.info("handle time excution : %s seconds" % (time.time() - start_time))
        except ValueError :
            return JsonResponse({ 'error': Error.VALUE }, safe=False)
        except OSError :
            return JsonResponse({ 'error': Error.OS }, safe=False)
        except :
            print(traceback.print_exc(file=sys.stdout))
            return JsonResponse({ 'error': Error.CANNT_HANDLE }, safe=False)
        return response
    return wrapper

def handle_auth_admin(f):
    def wrapper(request):
        try:
            admin_id = auth_admin(request)
            if not admin_id:
                return {'error': Error.AUTH_FAILED }
        except:
            return {'error': Error.AUTH_FAILED }
        return f(request, admin_id)
    return wrapper

def handle_auth_visitor(f):
    def wrapper(request):
        try:
            user_id = auth_visitor(request)
            if not user_id:
                return {'error': Error.AUTH_FAILED }
        except:
            return {'error': Error.AUTH_FAILED }
        return f(request, user_id)
    return wrapper

def handle_time(f):
    def wrapper(request):
        start_time = time.time()
        response = f(request)
        print("--- %s seconds ---" % (time.time() - start_time))
        return response
    return wrapper

__All__ = []