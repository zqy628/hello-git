#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
写一个hotdog方法
'''
class Hotdog(object):
    def __init__(self):
        self.condiments = ['bread']
        self.cooked_string = 'raw'
        self.cooked_level = 0

    def __str__(self):
        msg = 'the hotdog has ' + ''.join(self.condiments) + ',and the status is ' + self.cooked_string
        return msg

    def add_condiment(self,add_condiment):
        self.condiments.append(add_condiment)

    def cook(self):
        self.cooked_level += 3
        if self.cooked_level <= 3:
            self.cooked_string = 'raw'
        elif self.cooked_level <= 5:
            self.cooked_string = 'half cooked'
        elif self.cooked_level <= 8:
            self.cooked_string = 'cooked'
        else:
            self.cooked_string = 'over cooked'

hd = Hotdog()
hd.add_condiment('fanqie')
hd.add_condiment('vegatable')
hd.cook()
hd.cook()
print hd