from dragonfly import (Grammar, AppContext, MappingRule, 
Dictation, Key, Text, Integer, Mimic,Function,BringApp,
IntegerRef, Choice)
#javascript = AppContext(title="python")
grammar = Grammar("bash")

class BashMapping(MappingRule):
  name = "bash_rules"
  #mappings
  mapping = {
    #programming language case formatting
    "ls": Text('ls')+ Key('enter'),
    'bash': Text('bash')+ Key('enter'),
    'cd <variable>': Text('cd %(variable)s') +Key('enter')
    
  }
  extras = [ Dictation("variable"),Dictation("text") ]
  #defaults = {"variable": None,"text":None}


grammar.add_rule(BashMapping())
grammar.load()
# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar:
        grammar.unload()
        grammar = None