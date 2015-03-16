from datetime import datetime
import calendar
import json

import requests

from pymputator import settings

_now = datetime.now()

def days(month=_now.month):
    """
    Generator to give the days of a month. If no month is specified, it uses current month
    :param month: month to iterate
    """

    year = _now.year
    weeks = calendar.monthcalendar(year, month)

    for week in weeks:
        for day in week:
            if day != 0:
                # week is a list such as [0,0,0,1,2,3,4] or [5,6,7,8,9,10,11]
                # as a default, 0 index in the list correspond to a Monday and so forth
                # The entries with a value of 0 are only there to complete the list
                yield datetime(year, month, day)

def is_weekend(day):
    """
    Check if the given day is weekend or not.
    :param day: The day to look if is weekend or not, as a datetime.datetime object

    :rtype: True if the day is weekend, False otherwise
    """
    if day.isoweekday() > 5:
        return True

def load_user_configuration_file():
    with open(settings.LOCAL_CONFIGURATION_FILE) as cfg:
        pass

USER = None
PWD = None


TEMPLATE = {
    'INSERIR': 'Y',
    'BORRAR': 'N',
    'FL_VALIDAR': 'N',
    'SEL_CLIENT': 'N',
    'p_data': None,
    'p_inicials': USER,
    'p_inicials_original': USER,
    'p_nom': '',
    'setmana': None,
    'ann': None,
    'alhacerblur': '',
    'sortir': '4',
    'b_fila': '',
    'NumMinHores': '8',
    'c_txtExe1': 'Q140042',
    'c_client1': '2401',
    'p_Client1': '2401',
    'c_exe1': 'Q140042',
    'p_exe1': 'Q140042',
    'tarea1': '',
    'c_tarea1': '0',
    'p_tarea1': '',
    'c_parte1': '',
    'p_parte1': '',
    'ubicacion1': '1',
    'c_ubicacion1': '1',
    'p_ubicacion1': '1',
    'c_inicio1': '08:30',
    'p_inicio1': '08:30',
    'c_final1': '16:30',
    'p_final1': '16:30',
    'c_total1': '08:00',
    'p_total1': '08:00',
    'c_descripcion1': '',
    'p_descripcion1': '',
    'p_fact1': '0',
    'c_fact1': '0',
    'filestotal': '8',
    'c_txtExe2': '',
    'c_client2': '',
    'p_client2': '',
    'c_exe2': '',
    'p_exe2': '',
    'tarea2': '',
    'c_tarea2': '',
    'p_tarea2': '',
    'c_parte2': '',
    'p_parte2': '',
    'ubicacion2': '1',
    'c_ubicacion2': '1',
    'p_ubicacion2': '',
    'c_inicio2': '00:00',
    'p_inicio2': '',
    'c_final2': '00:00',
    'p_final2': '',
    'c_total2': '00:00',
    'p_total2': '',
    'c_descripcion2': '',
    'p_descripcion2': '',
    'p_fact2': '',
    'c_fact2': '0',
    'c_txtExe3': '',
    'c_client3': '',
    'p_client3': '',
    'c_exe3': '',
    'p_exe3': '',
    'tarea3': '',
    'c_tarea3': '',
    'p_tarea3': '',
    'c_parte3': '',
    'p_parte3': '',
    'ubicacion3': '1',
    'c_ubicacion3': '1',
    'p_ubicacion3': '',
    'c_inicio3': '00:00',
    'p_inicio3': '',
    'c_final3': '00:00',
    'p_final3': '',
    'c_total3': '00:00',
    'p_total3': '',
    'c_descripcion3': '',
    'p_descripcion3': '',
    'p_fact3': '',
    'c_fact3': '0',
    'c_txtExe4': '',
    'c_client4': '',
    'p_client4': '',
    'c_exe4': '',
    'p_exe4': '',
    'tarea4': '',
    'c_tarea4': '',
    'p_tarea4': '',
    'c_parte4': '',
    'p_parte4': '',
    'ubicacion4': '1',
    'c_ubicacion4': '1',
    'p_ubicacion4': '',
    'c_inicio4': '00:00',
    'p_inicio4': '',
    'c_final4': '00:00',
    'p_final4': '',
    'c_total4': '00:00',
    'p_total4': '',
    'c_descripcion4': '',
    'p_descripcion4': '',
    'p_fact4': '',
    'c_fact4': '0',
    'c_txtExe5': '',
    'c_client5': '',
    'p_client5': '',
    'c_exe5': '',
    'p_exe5': '',
    'tarea5': '',
    'c_tarea5': '',
    'p_tarea5': '',
    'c_parte5': '',
    'p_parte5': '',
    'ubicacion5': '1',
    'c_ubicacion5': '1',
    'p_ubicacion5': '',
    'c_inicio5': '00:00',
    'p_inicio5': '',
    'c_final5': '00:00',
    'p_final5': '',
    'c_total5': '00:00',
    'p_total5': '',
    'c_descripcion5': '',
    'p_descripcion5': '',
    'p_fact5': '',
    'c_fact5': '0',
    'c_txtExe6': '',
    'c_client6': '',
    'p_client6': '',
    'c_exe6': '',
    'p_exe6': '',
    'tarea6': '',
    'c_tarea6': '',
    'p_tarea6': '',
    'c_parte6': '',
    'p_parte6': '',
    'ubicacion6': '1',
    'c_ubicacion6': '1',
    'p_ubicacion6': '',
    'c_inicio6': '00:00',
    'p_inicio6': '',
    'c_final6': '00:00',
    'p_final6': '',
    'c_total6': '00:00',
    'p_total6': '',
    'c_descripcion6': '',
    'p_descripcion6': '',
    'p_fact6': '',
    'c_fact6': '0',
    'c_txtExe7': '',
    'c_client7': '',
    'p_client7': '',
    'c_exe7': '',
    'p_exe7': '',
    'tarea7': '',
    'c_tarea7': '',
    'p_tarea7': '',
    'c_parte7': '',
    'p_parte7': '',
    'ubicacion7': '1',
    'c_ubicacion7': '1',
    'p_ubicacion7': '',
    'c_inicio7': '00:00',
    'p_inicio7': '',
    'c_final7': '00:00',
    'p_final7': '',
    'c_total7': '00:00',
    'p_total7': '',
    'c_descripcion7': '',
    'p_descripcion7': '',
    'p_fact7': '',
    'c_fact7': '0',
    'c_txtExe8': '',
    'c_client8': '',
    'p_client8': '',
    'c_exe8': '',
    'p_exe8': '',
    'tarea8': '',
    'c_tarea8': '',
    'p_tarea8': '',
    'c_parte8': '',
    'p_parte8': '',
    'ubicacion8': '1',
    'c_ubicacion8': '1',
    'p_ubicacion8': '',
    'c_inicio8': '00:00',
    'p_inicio8': '',
    'c_final8': '00:00',
    'p_final8': '',
    'c_total8': '00:00',
    'p_total8': '',
    'c_descripcion8': '',
    'p_descripcion8': '',
    'p_fact8': '',
    'c_fact8': '0',
    'numitems': '9',
    'c_acumulado': '08:00',
    'p_acumulado': ''
}



if __name__ == '__main__':

    with requests.Session() as s:
        s.auth = (USER, PWD)
        for day in MONTH:
            if (is_weekend(day) or is_not_working(day, NOT_WORKING_DAYS)):
                continue
            #print(dir(day))
            day_str = day.strftime('%d/%m/%Y')
            week_str = day.week
            print('Imputing {day} '.format(day=day_str))
            TEMPLATE['p_data'] = day_str
            TEMPLATE['setmana'] = week_str
            TEMPLATE['ann'] = day.year
            s.post('http://www.morse.es/gsp/asp/Maqueta2.asp', data=TEMPLATE)

