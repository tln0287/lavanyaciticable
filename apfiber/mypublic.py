from Company.models import Agents,Companys
from UserManage.models import Menu


def callmenu(db, id):
    menu = Menu.objects.using(db).filter(type=id, status=1).all()
    return menu


def menuidwise(db, id):
    menu = Menu.objects.using(db).filter(id=id, status=1).all().order_by(order='ASC')
    return menu


def menuall(db):
    menu = Menu.objects.using(db).filter(status=1).all()
    return menu


def menumadulewise(db, id):
    menu = Menu.objects.using(db).filter(module_id=id, status=1).all()
    return menu


