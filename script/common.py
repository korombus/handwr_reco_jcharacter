# -*- coding: utf-8 -*-
##################################
#
# Common function script
#
# author: korombus
# date: 2020-03-03
##################################

import platform

def get_directory_reference_char():
    pf = platform.system()
    dir_ref_char = '/'

    if pf == 'Windows':
        dir_ref_char = '\\'
    
    return dir_ref_char