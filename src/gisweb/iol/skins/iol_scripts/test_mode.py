## Script (Python) "test_modec"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=default=False
##title=Is app in test mode?
##


"""
Returns True or False

Ti dice se la applicazione di cui fa parte il documento o il form è in test.
La funzione interroga la proprietà del plominodb <tipo_app>_is_in_test.
Se la variabile non è settata restituisce il valore di default.
"""

tipo_app = context.naming('tipo_app')

if tipo_app:
    test_prop = '%s_is_in_test' % tipo_app
else:
    test_prop = 'app_in_test'

try:
    test = getattr(context.getParentDatabase(), test_prop)
except AttributeError, err:
    test = default

return test
