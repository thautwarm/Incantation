#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 17:20:58 2017

@author: misakawa
"""
ICON_URL = 'http://materializecss.com/icons.html'

def icon(name, loc = ''):
    return f'<i class="material-icons {loc}" >{name}</i>'

mode_edit      = icon('mode_edit')
add            = icon('add')
access_alarm   = icon('access_alarm')
account_box    = icon('account_box')
account_circle = icon('account_circle')
all_inclusive  = icon('all_inclusive')
android        = icon('android')
arrow_upward   = icon('arrow_upward')
arrow_downward = icon('arrow_downward')
attach_file    = icon('attach_file')
cloud          = icon('cloud')