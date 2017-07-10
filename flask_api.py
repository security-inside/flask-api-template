##########################################################################################
#
# File: flask_api.py
# Author: Cristobal Espinosa
# Web: http://www.securityinside.info 
#
##########################################################################################

# Imports ################################################################################
from flask import Flask, redirect, request, Response
from flask_cors import CORS

import jwt
import json
import flask_api_functions
##########################################################################################

# Initial values #########################################################################
application = Flask(__name__)
CORS(application)

API_VERSION = 'v1'
DEBUG = True
##########################################################################################

##########################################################################################
# This function makes initial tasks.
##########################################################################################
@application.before_first_request
def _run_on_start():

    if not DEBUG:
        print "Flask started!"
        
        # Here you can do some initial tasks

##########################################################################################    

##########################################################################################
# This function returns happy 404.
##########################################################################################
@application.errorhandler(404)
def page_not_found(e):
    
    return redirect("https://goo.gl/LuKygx", code=302)

##########################################################################################

##########################################################################################
# This function returns happy 405.
##########################################################################################
@application.errorhandler(405)
def method_not_allowed(e):
    
    ret_html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"/>'
    ret_html = ret_html + '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es">'
    ret_html = ret_html + '<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
    ret_html = ret_html + '<title>Flask API SecurityInside.info Template</title>'
    ret_html = ret_html + '<style type="text/css" media="screen">'
    ret_html = ret_html + 'h1 {text-align:left; color: #444;}'
    ret_html = ret_html + '</style></head><body>'
    ret_html = ret_html + '<h1>Flask API <a href="http://www.securityinside.info" target="blank">SecurityInside.info</a> Template</h1>'
    ret_html = ret_html + 'Method not allowed or missing params, check API doc to solve the problem.'
    ret_html = ret_html + '</body></html>'

    return flask_api_functions.ret_content_type(ret_html, 'html', 405) 

##########################################################################################

##########################################################################################
# This function shows API index info.
##########################################################################################
@application.route('/', methods=['GET'])
def main():

    return index()

@application.route('/' + API_VERSION, methods=['GET'])
def index():
    
    ret_html = '<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"/>'
    ret_html = ret_html + '<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es">'
    ret_html = ret_html + '<head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />'
    ret_html = ret_html + '<title>Flask API SecurityInside.info Template</title>'
    ret_html = ret_html + '<style type="text/css" media="screen">'
    ret_html = ret_html + 'h1 {text-align:center; color: #444;}'
    ret_html = ret_html + '</style></head><body>'
    ret_html = ret_html + '<h1>Flask API <a href="http://www.securityinside.info" target="blank">SecurityInside.info</a> Template</h1>'
    ret_html = ret_html + '</body></html>'

    return flask_api_functions.ret_content_type(ret_html, 'html', 200)    

##########################################################################################

##########################################################################################
# This function shows API alive info. 
##########################################################################################
@application.route('/' + API_VERSION + '/ping', methods=['GET'])
def ping():
    
    response = {'code': 200, 'message': 'pong'}    
    return flask_api_functions.ret_content_type(response, 'json', 200)

##########################################################################################

##########################################################################################
# This function checks auth user and return JWT.
##########################################################################################
@application.route('/' + API_VERSION + '/login', methods=['POST'])
def login():
    
    # Check preconditions
    ##################################################################################
    response = flask_api_functions.check_preconditions(request, False)
    
    if (response['code'] != 200):
        return flask_api_functions.ret_content_type(response, 'json', response['code'])
    ##################################################################################
    
    # Check for user credentials
    ##################################################################################
    response = flask_api_functions.check_auth(request)
    return flask_api_functions.ret_content_type(response, 'json', response['code'])
    ##################################################################################

########################################################################################## 

##########################################################################################
# This function returns user profile.
##########################################################################################
@application.route('/' + API_VERSION + '/profile', methods=['GET'])
def get_profile():

    # Check preconditions
    ##################################################################################
    response = flask_api_functions.check_preconditions(request, True)
    
    if (response['code'] != 200):
        return flask_api_functions.ret_content_type(response, 'json', response['code'])
    ##################################################################################
    
    # Return user profile
    ##################################################################################
    code = 200
    response = {'code': code, 'message': None, 'jwt_data': flask_api_functions.get_jwt_info(request)}
    return flask_api_functions.ret_content_type(response, 'json', code)      
    ##################################################################################

########################################################################################## 

##########################################################################################
# API Main.
##########################################################################################
if __name__ == '__main__':

    try:        
        application.run(debug=DEBUG, host='0.0.0.0', port=16381)
    except Exception as e:
        print(e.message)

##########################################################################################
