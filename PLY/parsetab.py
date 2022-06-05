
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALPHANUMERIC BACKTICK BULLET GT HASH LITERALCHAR NEWLINE PIPE PUNCTUATION SLASH WSdocument : block\n                | block document\n    block : heading\n    | quote\n    | bulletitem\n    | code\n    \n    heading : HASH sentence NEWLINE\n    \n    bulletitem : BULLET sentence NEWLINE\n    \n    quote : GT sentence NEWLINE\n    \n        word : ALPHANUMERIC\n            | ALPHANUMERIC word\n    \n    sentence : word\n    | word WS sentence\n    \n    code : BACKTICK BACKTICK BACKTICK sentence BACKTICK BACKTICK BACKTICK\n    '
    
_lr_action_items = {'HASH':([0,2,3,4,5,6,18,21,22,28,],[7,7,-3,-4,-5,-6,-7,-9,-8,-14,]),'GT':([0,2,3,4,5,6,18,21,22,28,],[8,8,-3,-4,-5,-6,-7,-9,-8,-14,]),'BULLET':([0,2,3,4,5,6,18,21,22,28,],[9,9,-3,-4,-5,-6,-7,-9,-8,-14,]),'BACKTICK':([0,2,3,4,5,6,10,13,14,17,18,20,21,22,24,25,26,27,28,],[10,10,-3,-4,-5,-6,17,-12,-10,23,-7,-11,-9,-8,-13,26,27,28,-14,]),'$end':([1,2,3,4,5,6,11,18,21,22,28,],[0,-1,-3,-4,-5,-6,-2,-7,-9,-8,-14,]),'ALPHANUMERIC':([7,8,9,14,19,23,],[14,14,14,14,14,14,]),'NEWLINE':([12,13,14,15,16,20,24,],[18,-12,-10,21,22,-11,-13,]),'WS':([13,14,20,],[19,-10,-11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'document':([0,2,],[1,11,]),'block':([0,2,],[2,2,]),'heading':([0,2,],[3,3,]),'quote':([0,2,],[4,4,]),'bulletitem':([0,2,],[5,5,]),'code':([0,2,],[6,6,]),'sentence':([7,8,9,19,23,],[12,15,16,24,25,]),'word':([7,8,9,14,19,23,],[13,13,13,20,13,13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> block','document',1,'p_document','grammar.py',34),
  ('document -> block document','document',2,'p_document','grammar.py',35),
  ('block -> heading','block',1,'p_block','grammar.py',45),
  ('block -> quote','block',1,'p_block','grammar.py',46),
  ('block -> bulletitem','block',1,'p_block','grammar.py',47),
  ('block -> code','block',1,'p_block','grammar.py',48),
  ('heading -> HASH sentence NEWLINE','heading',3,'p_heading','grammar.py',54),
  ('bulletitem -> BULLET sentence NEWLINE','bulletitem',3,'p_bulletitem','grammar.py',60),
  ('quote -> GT sentence NEWLINE','quote',3,'p_quote','grammar.py',66),
  ('word -> ALPHANUMERIC','word',1,'p_word','grammar.py',72),
  ('word -> ALPHANUMERIC word','word',2,'p_word','grammar.py',73),
  ('sentence -> word','sentence',1,'p_sentence','grammar.py',82),
  ('sentence -> word WS sentence','sentence',3,'p_sentence','grammar.py',83),
  ('code -> BACKTICK BACKTICK BACKTICK sentence BACKTICK BACKTICK BACKTICK','code',7,'p_code','grammar.py',94),
]
