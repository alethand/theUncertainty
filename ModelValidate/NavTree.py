# -*- coding: utf-8 -*-

import comnTree
import Sql

#左侧导航栏
class NavTree(comnTree.ComnTree):
    
    def __init__(self, parent = None):
        
        comnTree.ComnTree.__init__(self, parent)
        