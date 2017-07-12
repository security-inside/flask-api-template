##########################################################################################
#
# File: flask_api_functions.py
# Author: Cristobal Espinosa
# Web: http://www.securityinside.info 
#
##########################################################################################

# Imports ################################################################################
from flask import Flask, redirect, request, redirect, Response

import base64
import json
import datetime
import time
import jwt
import os
##########################################################################################

# Initial values #########################################################################
SECRET = 'here_you_have_to_set_jwt_secret'
##########################################################################################

##########################################################################################
# This function checks call preconditions.
#
# @param request - User request data.
# @param has_to_check_token - If has or not to check request jwt.
#
# @return Formatted response.
# 
##########################################################################################
def check_preconditions(request, has_to_check_token):
    
    # Check for authorization header
    ##################################################################################
    aut_header = check_request_header(request)
    if (aut_header['code'] != 200):
        return aut_header
    ##################################################################################

    # Check for JWT
    ##################################################################################
    if has_to_check_token:
        jwt_response = check_jwt(request)
        if (jwt_response['code'] != 200):
            return jwt_response
    ##################################################################################

    response = {'code': 200, 'message': None}
    return response

##########################################################################################

##########################################################################################
# This function checks user authorization header param.
#
# @param request - User request data.
#
# @return Formatted response.
# 
##########################################################################################
def check_request_header(request):

    if 'Authorization' in request.headers:
        response = {'code': 200, 'message': 'Authorization header received correctly.'}
        return response                           
    
    else:
        response = {'code': 401, 'message': 'Authorization header not received.'}
        return response

##########################################################################################

##########################################################################################
# This function checks jwt.
#
# @param request - User request data.
#
# @return Formatted response.
# 
##########################################################################################
def check_jwt(request):

    try:
        token = request.headers['Authorization'].split()[1]

        msg = jwt.decode(token, SECRET)

        response = {'code': 200, 'message': msg}
        return response                

    except jwt.ExpiredSignatureError:
        response = {'code': 401, 'message': 'Your token has expired. Log in again to continue using resources.'}
        return response
        
    except Exception as e:
        print(e.message)

        response = {'code': 401, 'message': 'Your token is not valid. Log in again to continue using resources.'}
        return response

##########################################################################################

##########################################################################################
# This function checks jwt.
#
# @param request - User request data.
#
# @return Formatted response.
# 
##########################################################################################
def get_jwt_info(request):

    try:
        token = request.headers['Authorization'].split()[1]

        return jwt.decode(token, SECRET)

    except Exception as e:
        print(e.message)

        return None

##########################################################################################

##########################################################################################
# This function checks user authorization header request.
#
# @param request - User request data.
#
# @return Formatted response.
# 
##########################################################################################
def check_auth(request):
    
    try:
        auth = base64.b64decode(request.headers['Authorization'].split()[1])
    
    except:
        response = {'code': 401, 'message': 'Invalid basic authorization header.'}
        return response

    if len(auth.split(':')) != 2:
        response = {'code': 401, 'message': 'Invalid basic authorization header.'}
        return response
    else:
        """
        Here you have to check user credentials and optional totp value.
        """

        # If user credentials is ok, then generate jwt
        if(True): 
            
            # User with valid credentials
            token = jwt.encode({
                'user_id': '<insert_here_user_id>',
                'user_name': '<insert_here_user_name>',
                'user_roles': '<insert_here_user_roles>',
                'other_fields': '<insert_here_other_fields>',
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, 
                SECRET)
                                
            response = {'code': 200, 'message': None, 'token': token}
            return response

        # If user credentials is not ok, then return error message
        else:
            response = {'code': 401, 'message': '(d\'oh!) Wrong user, password, totp value or maybe user is not active.'}
            return response

##########################################################################################

##########################################################################################
# This function sets return headers.
#
# @param response - Message to response.
# @param type - Content-type to return.
# @param code - Server status code to show.
#   
# @return Formatted response.
# 
##########################################################################################
def ret_content_type(response, type, code):    

    if (type == 'json'):
        del response['code']
        
        return json.dumps(response), code, {'Server': 'Always look on the bright side of life','Content-Type': 'application/json', 'Need-help': 'info@securityinside.info', 'Strict-Transport-Security': 'max-age=31536000', 'Cache-control': 'no-store', 'Pragma': 'no-cache', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'deny'}
    
    if (type == 'html'):
        return response, code, {'Server': 'Always look on the bright side of life', 'Need-help': 'info@securityinside.info', 'Strict-Transport-Security': 'max-age=31536000', 'Cache-control': 'no-store', 'Pragma': 'no-cache', 'X-XSS-Protection': '1; mode=block', 'X-Content-Type-Options': 'nosniff', 'X-Frame-Options': 'deny'}

##########################################################################################        
