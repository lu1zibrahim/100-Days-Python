def hello(name="World"):
    return f"Hello, {name[0].upper()+name[1::].lower()}!" if name != "" else "Hello, World!"


#Better way
#def hello(name=''):
#    return f"Hello, {name.title() or 'World'}!"


#Another way
#def hello(name=""):
#    return f"Hello, {name.capitalize() if name else 'World'}!"