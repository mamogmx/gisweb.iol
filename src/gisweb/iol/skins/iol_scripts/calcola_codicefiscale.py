## Script (Python) "codicefiscale"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=fisica_cognome, fisica_nome, fisica_data_nato, fisica_sesso, fisica_cod_cat_nato
##title=
##
from gisweb.utils import json_dumps, Type, cf_build
from Products.CMFPlomino.PlominoUtils import StringToDate
result={'success': 0}

nascita = StringToDate(fisica_data_nato, format=None)
giorno = nascita.day()
mese = nascita.month()
anno = nascita.year()

data = (fisica_cognome, fisica_nome, anno, mese, giorno, fisica_sesso, fisica_cod_cat_nato)

try:
    result['value'] = cf_build(*data)
except Exception as err:
    result['err_type'] = Type(err)
    result['err_msg'] = str(err)
else:
    result['success'] = 1

return json_dumps(result)
