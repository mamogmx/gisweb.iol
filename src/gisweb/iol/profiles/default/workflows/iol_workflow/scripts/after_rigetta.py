## Script (Python) "after_rigetta"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=state_change
##title=
##
doc = state_change.object

#Aggiornamento dello stato su plominoDocument
doc.updateStatus()

#INVIO MAIL RIGETTO
doc.sendThisMail('rigetto')