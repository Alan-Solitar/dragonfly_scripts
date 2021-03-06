from dragonfly import (Grammar, AppContext, MappingRule, 
Dictation, Key, Text, Integer, Mimic,Function,BringApp,
IntegerRef, Choice)
#javascript = AppContext(title="python")
grammar = Grammar("python")

noSpaceNoCaps = Mimic("\\no-caps-on") + Mimic("\\no-space-on")

def snake(variable):
  var = str(variable).replace(' ','_')
  return var
def snake_case(variable):
  Text(snake(variable)).execute()

def camel_case(variable):
  words = str(variable).split(' ')
  #words = [word.capitalize() for index,word in enumerate(words) if index > 0 else word]
  words = [w.capitalize() if i>0 else w for i,w in enumerate(words)]
  camel_version = ''.join(words)
  Text(camel_version).execute()

def pascal_case(variable):
  words = str(variable).split(' ')
  words = [w.capitalize() for w in words]
  pascal_version = ''.join(words)
  Text(pascal_version).execute()
def kebab_case(variable):
  var = str(variable).replace(' ','-')
  Text(var).execute()
def lower_case(variable):
  Text(str(variable).replace(' ','').lower()).execute()
def include(variable):
  Text(str(variable).replace(' ',',')).execute()
def import_function(variable,text):
  a,b = str(variable).lower(), str(text).lower()
  output_string = 'import {} as {}'.format(a,b)
  Text(output_string).execute()
def method_call(variable): 
  Text('.{}()'.format(str(variable))).execute() 
  Key('left').execute().upper()
def call(variable):
  var = snake(variable)
  Text('{}()'.format(var)).execute()
  Key('left').execute()
def function(variable):
  var = snake(variable)
  command = Text('def {}():'.format(var)) + Key('left') + Key('left')
  command.execute()
def string(variable):
  var = snake(variable)
  Text("'{}'".format(var)).execute()


class PythonMapping(MappingRule):
  name = "my_rules"
  #mappings
  mapping = {
    #programming language case formatting
    "snake <variable>": Function(snake_case),
    "camel <variable>": Function(camel_case),
    "pascal <variable>": Function(pascal_case),
    "kebab <variable>": Function(kebab_case),
    "pascal <variable>": Function(pascal_case),
    "lower <variable>":Function(lower_case),
    #python specific
    "fun <variable>":Function(function),
    "import <variable> as <text>":Function(import_function),
    "dot <variable>":Function(method_call),
    "call <variable>":Function(call),
    #general stuff
    "begin":Key('home'),
    "end":Key('end'),
    "next":Key('end')+Key('enter'),
    "code": BringApp('C:\Program Files (x86)\Microsoft VS Code'),
    "fox":BringApp('C:\Program Files\Mozilla Firefox'),
    "box":BringApp('C:\Program Files\Oracle\VirtualBox'),
    "string <variable>":Function(string),
    "string literal <text>"         :Text("'%(text)s'"),
    "is list": Text(" = []") + Key('left'),
    "is tuple"             : Text(" = ()") + Key('left'),
    "is dictionary"        : Text(" = {}") + Key('left')
  }
  extras = [ Dictation("variable"),Dictation("text") ]
  #defaults = {"variable": None,"text":None}
 
grammar.add_rule(PythonMapping())
grammar.load()
# Unload function which will be called by natlink at unload time.
def unload():
    global grammar
    if grammar:
        grammar.unload()
        grammar = None
