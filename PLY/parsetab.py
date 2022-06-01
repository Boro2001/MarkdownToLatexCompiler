
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALPHANUMERIC BACKTICK BULLET CELLTEXT CLOSE_FENCE DIGIT EOF ESCAPEDCHAR ESCAPEDPIPE FENCED_IGNORE_WS FENCED_NEWLINE FROM GT HASH IGNORE_WS IMPORT INITIALPARACHAR INITIALTEXTCHAR LINECHAR LINENUMBER LISTNUMBER LITERALCHAR NEWLINE OPEN_FENCE PIPE PUNCTUATION QUOTE TEXTCHAR TEXTLINE TO WORDCHAR WSdocument : block EOF\n                | document block EOFblock : heading\n    | paragraph\n    | list\n    | blockquote\n    | fencedcodeblock\n    | table\n    | NEWLINEheading : HEADINGLINE NEWLINE\n        | NEWLINE HEADINGLINE NEWLINE paragraph : paragraphline\n        | NEWLINE paragraphlineparagraphline : PARAGRAPHLINE NEWLINE\n        | PARAGRAPHLINE EOFlist : NEWLINE listline\n        | listline\n        | listline listline\n        | NEWLINE listline listlinelistline : LISTLINE NEWLINE\n        | LISTLINE EOFblockquote : NEWLINE quoteline\n        | quoteline\n        | quoteline quoteline\n        | NEWLINE quoteline quotelinequoteline : QUOTELINE NEWLINE\n        | QUOTELINE EOFfencedcodeblock : OPEN_FENCE infostring FENCED_IGNORE_WS importspec FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE FENCED_IGNORE_WS importspec FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE infostring importspec FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE infostring FENCED_IGNORE_WS FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE importspec FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE infostring FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE FENCED_IGNORE_WS FENCED_NEWLINE textline CLOSE_FENCE\n        | OPEN_FENCE infostring FENCED_IGNORE_WS importspec FENCED_NEWLINE  textline textline CLOSE_FENCE\n        | OPEN_FENCE FENCED_IGNORE_WS importspec FENCED_NEWLINE textline textline CLOSE_FENCE\n        | OPEN_FENCE infostring importspec FENCED_NEWLINE textline textline CLOSE_FENCE\n        | OPEN_FENCE infostring FENCED_IGNORE_WS FENCED_NEWLINE textline textline CLOSE_FENCE\n        | OPEN_FENCE importspec FENCED_NEWLINE textline textline CLOSE_FENCE\n        | OPEN_FENCE infostring FENCED_NEWLINE textline textline CLOSE_FENCE\n        | OPEN_FENCE FENCED_IGNORE_WS FENCED_NEWLINE textline textline CLOSE_FENCEtextline : TEXTLINEinfostring : WORDimportspec : IMPORT FENCED_IGNORE_WS path FENCED_IGNORE_WS start FENCED_IGNORE_WS endpath : WORD\n        | STRINGstart : FROM FENCED_IGNORE_WS location\n        | FENCED_IGNORE_WS location\n        | FROM location\n        | locationend : TO FENCED_IGNORE_WS location\n        | TO locationlocation : LINENUMBER\n    | STRINGtable : tableheading tabledelimiterrow tablerow\n        | tableheading tabledelimiterrow tablerow tablerow\n        | NEWLINE tableheading tabledelimiterrow tablerow\n        | NEWLINE NEWLINE tableheading tabledelimiterrow tablerow\n        | NEWLINE NEWLINE tableheading tabledelimiterrow tablerow tablerow\n    tableheading : tablerowtablerow : cell PIPE NEWLINE\n        | cell cell PIPE NEWLINE\n        | cell NEWLINE\n        | cell cell NEWLINE\n        | cell PIPE EOF\n        | cell cell PIPE EOF\n        | cell EOF\n        | cell cell EOF\n        cell : CELLTEXTtabledelimiterrow : TABLEDELIMINATORCELL PIPE NEWLINE\n        | TABLEDELIMINATORCELL  NEWLINE\n        | TABLEDELIMINATORCELL TABLEDELIMINATORCELL PIPE NEWLINE\n        | TABLEDELIMINATORCELL TABLEDELIMINATORCELL  NEWLINEHEADINGLINE : HASH LINECHAR\n        | HASH  HASH LINECHAR\n        | HASH WS LINECHAR\n        | HASH  HASH WS LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        | HASH  HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR\n        \n    QUOTELINE : LINECHAR LITERAL\n        | GT LINECHAR LITERAL\n        | GT LINECHAR LINECHAR LITERAL LITERAL\n        | GT LINECHAR LINECHAR LINECHAR LINECHAR LITERAL\n        | GT LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL\n        | GT LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL\n        | GT LINECHAR LITERAL LITERAL\n        | GT LINECHAR LINECHAR LITERAL LITERAL LITERAL\n        | GT LINECHAR LINECHAR LINECHAR LINECHAR LITERAL LINECHAR LITERAL\n        | GT LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL LITERAL LINECHAR\n        | GT LINECHAR LINECHAR LITERAL\n        | GT LINECHAR LINECHAR LITERAL LINECHAR LITERAL\n        | GT LINECHAR LINECHAR LITERAL LINECHAR LITERAL LITERAL\n        | GT LINECHAR LINECHAR LITERAL LINECHAR LINECHAR LITERAL\n    \n    LITERAL : BACKTICK LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n        | BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK\n\n    WORD : WORDCHAR\n    | WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    | WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR\n    \n    LISTLINE : BULLET WS\n    | WS BULLET WS\n    | WS BULLET WS LINECHAR\n    | WS BULLET WS LINECHAR LINECHAR LINECHAR\n    | WS BULLET WS LINECHAR LINECHAR LINECHAR LINECHAR\n    | WS WS BULLET WS LINECHAR LINECHAR LINECHAR LINECHAR\n    | WS WS BULLET WS WS LINECHAR LINECHAR LINECHAR LINECHAR\n    \n    PARAGRAPHLINE : INITIALPARACHAR LINECHAR LITERAL\n    | INITIALPARACHAR LINECHAR LINECHAR LINECHAR\n    | INITIALPARACHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL\n    | INITIALPARACHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL\n    | INITIALPARACHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL\n    \n    STRING : QUOTE LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    | QUOTE LINECHAR  LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE\n    \n    TABLEDELIMINATORCELL : PIPE\n    \n    CELLCHAR : ESCAPEDCHAR\n    | ESCAPEDPIPE\n    | WS\n    | ALPHANUMERIC\n    | PUNCTUATION\n    '
    
_lr_action_items = {'NEWLINE':([0,1,9,10,20,21,22,26,27,29,31,46,47,49,51,62,64,65,68,83,84,86,88,91,93,95,96,117,120,121,122,125,126,128,129,147,148,149,157,178,179,180,184,186,188,190,191,204,205,206,210,212,214,216,217,225,226,227,230,231,232,234,240,241,242,244,245,250,251,252,257,258,259,264,265,266,269,],[9,9,30,36,55,57,59,66,-69,-1,70,85,-154,-74,-96,-130,97,99,-2,118,119,-75,-76,-131,-137,-97,130,146,-87,-77,-110,-132,-138,-106,-102,-88,-78,-111,-98,-89,-79,-112,-133,-139,-99,-107,-103,-90,-80,-113,-134,-140,-100,-109,-108,-91,-81,-114,-135,-141,-101,-104,-92,-82,-115,-136,-105,-93,-83,-116,-94,-84,-117,-95,-85,-118,-86,]),'OPEN_FENCE':([0,1,29,68,],[14,14,-1,-2,]),'HASH':([0,1,9,17,29,68,],[17,17,17,48,-1,-2,]),'INITIALPARACHAR':([0,1,9,29,68,],[23,23,23,-1,-2,]),'BULLET':([0,1,9,12,19,29,33,53,57,58,68,],[24,24,24,24,54,-1,24,90,-20,-21,-2,]),'WS':([0,1,9,12,17,19,24,29,33,48,54,57,58,68,90,124,],[19,19,19,19,50,53,62,-1,19,87,91,-20,-21,-2,124,151,]),'LINECHAR':([0,1,9,13,17,23,25,29,34,48,50,59,60,61,63,68,86,87,91,92,94,114,120,121,122,124,125,126,127,128,144,147,148,149,151,152,153,154,155,156,176,178,179,180,182,183,184,185,187,188,202,204,205,206,208,209,223,225,226,227,229,233,238,240,241,242,248,250,251,252,255,257,258,259,262,265,266,268,271,273,],[18,18,18,18,49,61,63,-1,18,86,88,-26,-27,92,94,-2,120,121,125,126,127,144,147,148,-110,152,153,154,155,156,176,178,179,-111,182,183,184,185,187,189,202,204,205,-112,208,209,210,211,213,215,223,225,226,-113,229,230,238,240,241,-114,244,245,248,250,251,-115,255,257,258,-116,262,264,265,-117,268,269,-118,271,273,275,]),'GT':([0,1,9,13,29,34,59,60,68,],[25,25,25,25,-1,25,-26,-27,-2,]),'CELLTEXT':([0,1,9,26,27,29,30,45,66,67,68,73,82,85,97,98,99,100,101,118,119,130,131,132,146,],[27,27,27,27,-69,-1,27,27,-63,-67,-2,27,27,-71,-64,-68,-61,-65,27,-73,-70,-62,-66,27,-72,]),'$end':([1,29,68,],[0,-1,-2,]),'EOF':([2,3,4,5,6,7,8,9,11,12,13,20,21,22,26,27,28,32,33,34,36,37,38,51,55,56,57,58,59,60,62,64,65,66,67,70,71,72,82,91,93,95,96,97,98,99,100,102,116,122,125,126,128,129,130,131,132,137,140,142,149,157,158,161,163,164,166,167,168,180,184,186,188,190,191,193,194,195,196,206,210,212,214,216,217,218,227,230,231,232,234,242,244,245,252,259,266,],[29,-3,-4,-5,-6,-7,-8,-9,-12,-17,-23,56,58,60,67,-69,68,-13,-16,-22,-10,-18,-24,-96,-14,-15,-20,-21,-26,-27,-130,98,100,-63,-67,-11,-19,-25,-55,-131,-137,-97,131,-64,-68,-61,-65,-57,-56,-110,-132,-138,-106,-102,-62,-66,-58,-33,-34,-32,-111,-98,-59,-31,-30,-40,-29,-41,-39,-112,-133,-139,-99,-107,-103,-28,-38,-37,-36,-113,-134,-140,-100,-109,-108,-35,-114,-135,-141,-101,-104,-115,-136,-105,-116,-117,-118,]),'FENCED_IGNORE_WS':([14,39,42,43,44,81,111,112,113,115,143,145,170,171,172,173,174,175,177,197,200,201,203,220,221,222,224,237,239,247,249,254,256,261,263,267,270,272,274,276,],[40,74,-43,80,-119,-120,143,-45,-46,-121,169,-122,198,199,-50,-53,-54,-142,-123,-48,-49,-143,-124,235,-47,-144,-125,-145,-126,-146,-127,-147,-128,-148,-129,-149,-150,-151,-152,-153,]),'IMPORT':([14,39,40,42,44,74,81,115,145,177,203,224,239,249,256,263,],[43,43,43,-43,-119,43,-120,-121,-122,-123,-124,-125,-126,-127,-128,-129,]),'WORDCHAR':([14,44,80,81,115,145,177,203,224,239,249,256,],[44,81,44,115,145,177,203,224,239,249,256,263,]),'PIPE':([15,16,26,27,35,46,47,64,66,67,69,83,84,97,98,99,100,130,131,],[47,-60,65,-69,47,84,-154,96,-63,-67,47,117,-154,-64,-68,-61,-65,-62,-66,]),'BACKTICK':([18,61,63,89,94,95,122,123,128,149,150,154,155,156,157,180,181,185,187,189,190,206,207,211,213,214,215,227,228,242,243,252,253,259,260,266,],[52,52,52,122,52,52,-110,149,52,-111,180,52,52,52,52,-112,206,52,52,52,52,-113,227,52,52,52,52,-114,242,-115,252,-116,259,-117,266,-118,]),'FENCED_NEWLINE':([39,40,41,42,44,74,75,77,81,103,115,145,173,174,175,177,201,203,219,222,224,236,237,239,246,247,249,254,256,261,263,267,270,272,274,276,],[76,78,79,-43,-119,104,105,108,-120,133,-121,-122,-53,-54,-142,-123,-143,-124,-44,-144,-125,-52,-145,-126,-51,-146,-127,-147,-128,-148,-129,-149,-150,-151,-152,-153,]),'LITERALCHAR':([52,89,123,150,181,207,228,243,253,],[89,123,150,181,207,228,243,253,260,]),'TEXTLINE':([76,78,79,104,105,106,107,108,109,110,133,134,135,138,159,],[107,107,107,107,107,107,-42,107,107,107,107,107,107,107,107,]),'QUOTE':([80,143,144,169,171,176,199,202,220,223,235,238,248,255,262,268,271,273,275,],[114,114,175,114,114,201,114,222,114,237,114,247,254,261,267,270,272,274,276,]),'CLOSE_FENCE':([106,107,109,110,134,135,136,138,139,141,159,160,162,165,192,],[137,-42,140,142,161,163,164,166,167,168,193,194,195,196,218,]),'FROM':([143,],[171,]),'LINENUMBER':([143,169,171,199,220,235,],[173,173,173,173,173,173,]),'TO':([198,],[220,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'document':([0,],[1,]),'block':([0,1,],[2,28,]),'heading':([0,1,],[3,3,]),'paragraph':([0,1,],[4,4,]),'list':([0,1,],[5,5,]),'blockquote':([0,1,],[6,6,]),'fencedcodeblock':([0,1,],[7,7,]),'table':([0,1,],[8,8,]),'HEADINGLINE':([0,1,9,],[10,10,31,]),'paragraphline':([0,1,9,],[11,11,32,]),'listline':([0,1,9,12,33,],[12,12,33,37,71,]),'quoteline':([0,1,9,13,34,],[13,13,34,38,72,]),'tableheading':([0,1,9,30,],[15,15,35,69,]),'tablerow':([0,1,9,30,45,73,82,101,132,],[16,16,16,16,82,102,116,132,158,]),'PARAGRAPHLINE':([0,1,9,],[20,20,20,]),'LISTLINE':([0,1,9,12,33,],[21,21,21,21,21,]),'QUOTELINE':([0,1,9,13,34,],[22,22,22,22,22,]),'cell':([0,1,9,26,30,45,73,82,101,132,],[26,26,26,64,26,26,26,26,26,26,]),'infostring':([14,],[39,]),'importspec':([14,39,40,74,],[41,75,77,103,]),'WORD':([14,80,],[42,112,]),'tabledelimiterrow':([15,35,69,],[45,73,101,]),'TABLEDELIMINATORCELL':([15,35,46,69,],[46,46,83,46,]),'LITERAL':([18,61,63,94,95,128,154,155,156,157,185,187,189,190,211,213,214,215,],[51,93,95,128,129,157,186,188,190,191,212,214,216,217,231,232,233,234,]),'textline':([76,78,79,104,105,106,108,109,110,133,134,135,138,159,],[106,109,110,134,135,136,138,139,141,159,160,162,165,192,]),'path':([80,],[111,]),'STRING':([80,143,169,171,199,220,235,],[113,174,174,174,174,174,174,]),'start':([143,],[170,]),'location':([143,169,171,199,220,235,],[172,197,200,221,236,246,]),'end':([198,],[219,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> block EOF','document',2,'p_document','grammar.py',6),
  ('document -> document block EOF','document',3,'p_document','grammar.py',7),
  ('block -> heading','block',1,'p_block','grammar.py',12),
  ('block -> paragraph','block',1,'p_block','grammar.py',13),
  ('block -> list','block',1,'p_block','grammar.py',14),
  ('block -> blockquote','block',1,'p_block','grammar.py',15),
  ('block -> fencedcodeblock','block',1,'p_block','grammar.py',16),
  ('block -> table','block',1,'p_block','grammar.py',17),
  ('block -> NEWLINE','block',1,'p_block','grammar.py',18),
  ('heading -> HEADINGLINE NEWLINE','heading',2,'p_heading','grammar.py',23),
  ('heading -> NEWLINE HEADINGLINE NEWLINE','heading',3,'p_heading','grammar.py',24),
  ('paragraph -> paragraphline','paragraph',1,'p_paragraph','grammar.py',30),
  ('paragraph -> NEWLINE paragraphline','paragraph',2,'p_paragraph','grammar.py',31),
  ('paragraphline -> PARAGRAPHLINE NEWLINE','paragraphline',2,'p_paragraphline','grammar.py',37),
  ('paragraphline -> PARAGRAPHLINE EOF','paragraphline',2,'p_paragraphline','grammar.py',38),
  ('list -> NEWLINE listline','list',2,'p_list','grammar.py',43),
  ('list -> listline','list',1,'p_list','grammar.py',44),
  ('list -> listline listline','list',2,'p_list','grammar.py',45),
  ('list -> NEWLINE listline listline','list',3,'p_list','grammar.py',46),
  ('listline -> LISTLINE NEWLINE','listline',2,'p_listline','grammar.py',51),
  ('listline -> LISTLINE EOF','listline',2,'p_listline','grammar.py',52),
  ('blockquote -> NEWLINE quoteline','blockquote',2,'p_blockquote','grammar.py',57),
  ('blockquote -> quoteline','blockquote',1,'p_blockquote','grammar.py',58),
  ('blockquote -> quoteline quoteline','blockquote',2,'p_blockquote','grammar.py',59),
  ('blockquote -> NEWLINE quoteline quoteline','blockquote',3,'p_blockquote','grammar.py',60),
  ('quoteline -> QUOTELINE NEWLINE','quoteline',2,'p_quoteline','grammar.py',65),
  ('quoteline -> QUOTELINE EOF','quoteline',2,'p_quoteline','grammar.py',66),
  ('fencedcodeblock -> OPEN_FENCE infostring FENCED_IGNORE_WS importspec FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',7,'p_fencedcodeblock','grammar.py',71),
  ('fencedcodeblock -> OPEN_FENCE FENCED_IGNORE_WS importspec FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',6,'p_fencedcodeblock','grammar.py',72),
  ('fencedcodeblock -> OPEN_FENCE infostring importspec FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',6,'p_fencedcodeblock','grammar.py',73),
  ('fencedcodeblock -> OPEN_FENCE infostring FENCED_IGNORE_WS FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',6,'p_fencedcodeblock','grammar.py',74),
  ('fencedcodeblock -> OPEN_FENCE importspec FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',5,'p_fencedcodeblock','grammar.py',75),
  ('fencedcodeblock -> OPEN_FENCE infostring FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',5,'p_fencedcodeblock','grammar.py',76),
  ('fencedcodeblock -> OPEN_FENCE FENCED_IGNORE_WS FENCED_NEWLINE textline CLOSE_FENCE','fencedcodeblock',5,'p_fencedcodeblock','grammar.py',77),
  ('fencedcodeblock -> OPEN_FENCE infostring FENCED_IGNORE_WS importspec FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',8,'p_fencedcodeblock','grammar.py',78),
  ('fencedcodeblock -> OPEN_FENCE FENCED_IGNORE_WS importspec FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',7,'p_fencedcodeblock','grammar.py',79),
  ('fencedcodeblock -> OPEN_FENCE infostring importspec FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',7,'p_fencedcodeblock','grammar.py',80),
  ('fencedcodeblock -> OPEN_FENCE infostring FENCED_IGNORE_WS FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',7,'p_fencedcodeblock','grammar.py',81),
  ('fencedcodeblock -> OPEN_FENCE importspec FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',6,'p_fencedcodeblock','grammar.py',82),
  ('fencedcodeblock -> OPEN_FENCE infostring FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',6,'p_fencedcodeblock','grammar.py',83),
  ('fencedcodeblock -> OPEN_FENCE FENCED_IGNORE_WS FENCED_NEWLINE textline textline CLOSE_FENCE','fencedcodeblock',6,'p_fencedcodeblock','grammar.py',84),
  ('textline -> TEXTLINE','textline',1,'p_textline','grammar.py',88),
  ('infostring -> WORD','infostring',1,'p_infostring','grammar.py',92),
  ('importspec -> IMPORT FENCED_IGNORE_WS path FENCED_IGNORE_WS start FENCED_IGNORE_WS end','importspec',7,'p_importspec','grammar.py',96),
  ('path -> WORD','path',1,'p_path','grammar.py',100),
  ('path -> STRING','path',1,'p_path','grammar.py',101),
  ('start -> FROM FENCED_IGNORE_WS location','start',3,'p_start','grammar.py',105),
  ('start -> FENCED_IGNORE_WS location','start',2,'p_start','grammar.py',106),
  ('start -> FROM location','start',2,'p_start','grammar.py',107),
  ('start -> location','start',1,'p_start','grammar.py',108),
  ('end -> TO FENCED_IGNORE_WS location','end',3,'p_end','grammar.py',111),
  ('end -> TO location','end',2,'p_end','grammar.py',112),
  ('location -> LINENUMBER','location',1,'p_location','grammar.py',117),
  ('location -> STRING','location',1,'p_location','grammar.py',118),
  ('table -> tableheading tabledelimiterrow tablerow','table',3,'p_table','grammar.py',123),
  ('table -> tableheading tabledelimiterrow tablerow tablerow','table',4,'p_table','grammar.py',124),
  ('table -> NEWLINE tableheading tabledelimiterrow tablerow','table',4,'p_table','grammar.py',125),
  ('table -> NEWLINE NEWLINE tableheading tabledelimiterrow tablerow','table',5,'p_table','grammar.py',126),
  ('table -> NEWLINE NEWLINE tableheading tabledelimiterrow tablerow tablerow','table',6,'p_table','grammar.py',127),
  ('tableheading -> tablerow','tableheading',1,'p_tableheading','grammar.py',132),
  ('tablerow -> cell PIPE NEWLINE','tablerow',3,'p_tablerow','grammar.py',136),
  ('tablerow -> cell cell PIPE NEWLINE','tablerow',4,'p_tablerow','grammar.py',137),
  ('tablerow -> cell NEWLINE','tablerow',2,'p_tablerow','grammar.py',138),
  ('tablerow -> cell cell NEWLINE','tablerow',3,'p_tablerow','grammar.py',139),
  ('tablerow -> cell PIPE EOF','tablerow',3,'p_tablerow','grammar.py',140),
  ('tablerow -> cell cell PIPE EOF','tablerow',4,'p_tablerow','grammar.py',141),
  ('tablerow -> cell EOF','tablerow',2,'p_tablerow','grammar.py',142),
  ('tablerow -> cell cell EOF','tablerow',3,'p_tablerow','grammar.py',143),
  ('cell -> CELLTEXT','cell',1,'p_cell','grammar.py',148),
  ('tabledelimiterrow -> TABLEDELIMINATORCELL PIPE NEWLINE','tabledelimiterrow',3,'p_tabledelimiterrow','grammar.py',155),
  ('tabledelimiterrow -> TABLEDELIMINATORCELL NEWLINE','tabledelimiterrow',2,'p_tabledelimiterrow','grammar.py',156),
  ('tabledelimiterrow -> TABLEDELIMINATORCELL TABLEDELIMINATORCELL PIPE NEWLINE','tabledelimiterrow',4,'p_tabledelimiterrow','grammar.py',157),
  ('tabledelimiterrow -> TABLEDELIMINATORCELL TABLEDELIMINATORCELL NEWLINE','tabledelimiterrow',3,'p_tabledelimiterrow','grammar.py',158),
  ('HEADINGLINE -> HASH LINECHAR','HEADINGLINE',2,'p_HEADINGLINE','grammar.py',162),
  ('HEADINGLINE -> HASH HASH LINECHAR','HEADINGLINE',3,'p_HEADINGLINE','grammar.py',163),
  ('HEADINGLINE -> HASH WS LINECHAR','HEADINGLINE',3,'p_HEADINGLINE','grammar.py',164),
  ('HEADINGLINE -> HASH HASH WS LINECHAR','HEADINGLINE',4,'p_HEADINGLINE','grammar.py',165),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR','HEADINGLINE',5,'p_HEADINGLINE','grammar.py',166),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR','HEADINGLINE',6,'p_HEADINGLINE','grammar.py',167),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',7,'p_HEADINGLINE','grammar.py',168),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',8,'p_HEADINGLINE','grammar.py',169),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',9,'p_HEADINGLINE','grammar.py',170),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',10,'p_HEADINGLINE','grammar.py',171),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',11,'p_HEADINGLINE','grammar.py',172),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',12,'p_HEADINGLINE','grammar.py',173),
  ('HEADINGLINE -> HASH HASH WS LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',13,'p_HEADINGLINE','grammar.py',174),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR','HEADINGLINE',4,'p_HEADINGLINE','grammar.py',175),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR','HEADINGLINE',5,'p_HEADINGLINE','grammar.py',176),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',6,'p_HEADINGLINE','grammar.py',177),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',7,'p_HEADINGLINE','grammar.py',178),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',8,'p_HEADINGLINE','grammar.py',179),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',9,'p_HEADINGLINE','grammar.py',180),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',10,'p_HEADINGLINE','grammar.py',181),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',11,'p_HEADINGLINE','grammar.py',182),
  ('HEADINGLINE -> HASH HASH LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR','HEADINGLINE',12,'p_HEADINGLINE','grammar.py',183),
  ('QUOTELINE -> LINECHAR LITERAL','QUOTELINE',2,'p_QUOTELINE','grammar.py',190),
  ('QUOTELINE -> GT LINECHAR LITERAL','QUOTELINE',3,'p_QUOTELINE','grammar.py',191),
  ('QUOTELINE -> GT LINECHAR LINECHAR LITERAL LITERAL','QUOTELINE',5,'p_QUOTELINE','grammar.py',192),
  ('QUOTELINE -> GT LINECHAR LINECHAR LINECHAR LINECHAR LITERAL','QUOTELINE',6,'p_QUOTELINE','grammar.py',193),
  ('QUOTELINE -> GT LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL','QUOTELINE',7,'p_QUOTELINE','grammar.py',194),
  ('QUOTELINE -> GT LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL','QUOTELINE',8,'p_QUOTELINE','grammar.py',195),
  ('QUOTELINE -> GT LINECHAR LITERAL LITERAL','QUOTELINE',4,'p_QUOTELINE','grammar.py',196),
  ('QUOTELINE -> GT LINECHAR LINECHAR LITERAL LITERAL LITERAL','QUOTELINE',6,'p_QUOTELINE','grammar.py',197),
  ('QUOTELINE -> GT LINECHAR LINECHAR LINECHAR LINECHAR LITERAL LINECHAR LITERAL','QUOTELINE',8,'p_QUOTELINE','grammar.py',198),
  ('QUOTELINE -> GT LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL LITERAL LINECHAR','QUOTELINE',9,'p_QUOTELINE','grammar.py',199),
  ('QUOTELINE -> GT LINECHAR LINECHAR LITERAL','QUOTELINE',4,'p_QUOTELINE','grammar.py',200),
  ('QUOTELINE -> GT LINECHAR LINECHAR LITERAL LINECHAR LITERAL','QUOTELINE',6,'p_QUOTELINE','grammar.py',201),
  ('QUOTELINE -> GT LINECHAR LINECHAR LITERAL LINECHAR LITERAL LITERAL','QUOTELINE',7,'p_QUOTELINE','grammar.py',202),
  ('QUOTELINE -> GT LINECHAR LINECHAR LITERAL LINECHAR LINECHAR LITERAL','QUOTELINE',7,'p_QUOTELINE','grammar.py',203),
  ('LITERAL -> BACKTICK LITERALCHAR BACKTICK','LITERAL',3,'p_LITERAL','grammar.py',210),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR BACKTICK','LITERAL',4,'p_LITERAL','grammar.py',211),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',5,'p_LITERAL','grammar.py',212),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',6,'p_LITERAL','grammar.py',213),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',7,'p_LITERAL','grammar.py',214),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',8,'p_LITERAL','grammar.py',215),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',9,'p_LITERAL','grammar.py',216),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',10,'p_LITERAL','grammar.py',217),
  ('LITERAL -> BACKTICK LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR LITERALCHAR BACKTICK','LITERAL',11,'p_LITERAL','grammar.py',218),
  ('WORD -> WORDCHAR','WORD',1,'p_WORD','grammar.py',224),
  ('WORD -> WORDCHAR WORDCHAR','WORD',2,'p_WORD','grammar.py',225),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR','WORD',3,'p_WORD','grammar.py',226),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',4,'p_WORD','grammar.py',227),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',5,'p_WORD','grammar.py',228),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',6,'p_WORD','grammar.py',229),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',7,'p_WORD','grammar.py',230),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',8,'p_WORD','grammar.py',231),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',9,'p_WORD','grammar.py',232),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',10,'p_WORD','grammar.py',233),
  ('WORD -> WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR WORDCHAR','WORD',11,'p_WORD','grammar.py',234),
  ('LISTLINE -> BULLET WS','LISTLINE',2,'p_LISTLINE','grammar.py',241),
  ('LISTLINE -> WS BULLET WS','LISTLINE',3,'p_LISTLINE','grammar.py',242),
  ('LISTLINE -> WS BULLET WS LINECHAR','LISTLINE',4,'p_LISTLINE','grammar.py',243),
  ('LISTLINE -> WS BULLET WS LINECHAR LINECHAR LINECHAR','LISTLINE',6,'p_LISTLINE','grammar.py',244),
  ('LISTLINE -> WS BULLET WS LINECHAR LINECHAR LINECHAR LINECHAR','LISTLINE',7,'p_LISTLINE','grammar.py',245),
  ('LISTLINE -> WS WS BULLET WS LINECHAR LINECHAR LINECHAR LINECHAR','LISTLINE',8,'p_LISTLINE','grammar.py',246),
  ('LISTLINE -> WS WS BULLET WS WS LINECHAR LINECHAR LINECHAR LINECHAR','LISTLINE',9,'p_LISTLINE','grammar.py',247),
  ('PARAGRAPHLINE -> INITIALPARACHAR LINECHAR LITERAL','PARAGRAPHLINE',3,'p_PARAGRAPHLINE','grammar.py',253),
  ('PARAGRAPHLINE -> INITIALPARACHAR LINECHAR LINECHAR LINECHAR','PARAGRAPHLINE',4,'p_PARAGRAPHLINE','grammar.py',254),
  ('PARAGRAPHLINE -> INITIALPARACHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL','PARAGRAPHLINE',6,'p_PARAGRAPHLINE','grammar.py',255),
  ('PARAGRAPHLINE -> INITIALPARACHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL','PARAGRAPHLINE',7,'p_PARAGRAPHLINE','grammar.py',256),
  ('PARAGRAPHLINE -> INITIALPARACHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LITERAL','PARAGRAPHLINE',8,'p_PARAGRAPHLINE','grammar.py',257),
  ('STRING -> QUOTE LINECHAR QUOTE','STRING',3,'p_STRING','grammar.py',263),
  ('STRING -> QUOTE LINECHAR LINECHAR QUOTE','STRING',4,'p_STRING','grammar.py',264),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR QUOTE','STRING',5,'p_STRING','grammar.py',265),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',6,'p_STRING','grammar.py',266),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',7,'p_STRING','grammar.py',267),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',8,'p_STRING','grammar.py',268),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',9,'p_STRING','grammar.py',269),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',10,'p_STRING','grammar.py',270),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',11,'p_STRING','grammar.py',271),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',12,'p_STRING','grammar.py',272),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',13,'p_STRING','grammar.py',273),
  ('STRING -> QUOTE LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR LINECHAR QUOTE','STRING',14,'p_STRING','grammar.py',274),
  ('TABLEDELIMINATORCELL -> PIPE','TABLEDELIMINATORCELL',1,'p_TABLEDELIMINATORCELL','grammar.py',280),
  ('CELLCHAR -> ESCAPEDCHAR','CELLCHAR',1,'p_CELLCHAR','grammar.py',295),
  ('CELLCHAR -> ESCAPEDPIPE','CELLCHAR',1,'p_CELLCHAR','grammar.py',296),
  ('CELLCHAR -> WS','CELLCHAR',1,'p_CELLCHAR','grammar.py',297),
  ('CELLCHAR -> ALPHANUMERIC','CELLCHAR',1,'p_CELLCHAR','grammar.py',298),
  ('CELLCHAR -> PUNCTUATION','CELLCHAR',1,'p_CELLCHAR','grammar.py',299),
]