"""Wrapper module for sceptremods.templates.vpc"""

from sceptremods.templates import vpc
def sceptre_handler(sceptre_user_data):
    return vpc.sceptre_handler(sceptre_user_data)
