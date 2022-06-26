import types

def list_modules(module_name):
    try:
        module = __import__(module_name, globals(), locals(), [module_name.split('.')[-1]])
    except ImportError:
	print("Didn't work")
        return
    print(module_name)
    for name in dir(module):
        if type(getattr(module, name)) == types.ModuleType:
            list_modules('.'.join([module_name, name]))
