#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#
#  This file is part of the `bioigraph` python module
#
#  Copyright (c) 2014-2015 - EMBL-EBI
#
#  File author(s): Dénes Türei (denes@ebi.ac.uk)
#
#  Distributed under the GNU GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  Website: http://www.ebi.ac.uk/~denes
#

import codecs

__all__ = ['MysqlMapping','FileMapping','ReferenceList',
           'PickleMapping','ReadSettings','ReadList']

class MysqlMapping(object):
        
    def __init__(self,tableName,fieldOne,fieldTwo,db=None,tax=None,bi=False):
        self.tableName = tableName
        self.fieldOne = fieldOne
        self.fieldTwo = fieldTwo
        self.tax = tax
        self.db = db
        self.bi = bi

class FileMapping(object):
        
    def __init__(self,textFile,oneCol,twoCol,separator,header=0,bi=False,tax=9606):
        self.textFile = textFile
        self.oneCol = oneCol
        self.twoCol = twoCol
        self.separator = separator
        self.header = header
        self.bi = bi

class ReferenceList(object):
    
    def __init__(self,nameType,typ,tax,inFile):
        self.infile = inFile
        self.nameType = nameType
        self.typ = typ
        self.tax = tax
    
    def load(self):
        f = codecs.open(self.infile,encoding='utf-8',mode='r')
        lst = []
        for l in f:
            lst.append(l.strip())
        f.close()
        self.lst = set(lst)

class PickleMapping(object):
        
    def __init__(self,pickleFile):
        self.pickleFile = pickleFile

class ReadSettings:
    
    def __init__(self, name = "unknown", separator = None, nameColA = 0, nameColB = 1, 
            nameTypeA = "uniprot", nameTypeB = "uniprot", typeA = "protein", 
            typeB = "protein", isDirected = False, sign = False, inFile = None, 
            references = False, extraEdgeAttrs = {}, extraNodeAttrsA = {}, 
            extraNodeAttrsB = {}, header = False, taxonA = False, taxonB = False, 
            ncbiTaxId = False, interactionType = 'PPI', inputArgs = {}):
        self.typeA = typeA
        self.typeB = typeB
        self.nameColA = nameColA
        self.nameColB = nameColB
        self.nameTypeA = nameTypeA
        self.nameTypeB = nameTypeB
        self.isDirected = isDirected
        self.inFile = inFile
        self.extraEdgeAttrs = extraEdgeAttrs
        self.extraNodeAttrsA = extraNodeAttrsA
        self.extraNodeAttrsB = extraNodeAttrsB
        self.name = name
        self.separator = separator
        self.header = header
        self.refs = references
        self.sign = sign
        self.taxonA = taxonA
        self.taxonB = taxonB
        self.ncbiTaxId = ncbiTaxId
        self.intType = interactionType
        self.inputArgs = inputArgs

class ReadList:
    
    def __init__(self,name="unknown",separator=None,nameCol=0,
            nameType="uniprot",typ="protein",inFile=None,extraAttrs={},header=False):
        self.typ = typ
        self.nameCol = nameCol
        self.nameType = nameType
        self.inFile = inFile
        self.extraAttrs = extraAttrs
        self.name = name
        self.separator = separator
        self.header = header