"""
The actual pymputator
"""

# Stantard library imports
import calendar
from datetime import datetime
import getpass
try:
    from HTMLParser import HTMLParser
except ImportError:
    # python 3 compatible
    from html.parser import HTMLParser
import logging
import pprint

# Third parties
import requests


def setup_logging(level=logging.DEBUG, formatter=logging.Formatter('%(asctime)s %(levelname)s : %(message)s - (%(module)s, line %(lineno)s)')):
    """
    Setups a logger with a `StreamHandler` that prints to  `stdout` with `debug` logging
    level and the following formatter

    %(asctime)s %(levelname)s : %(message)s - (%(module)s, line %(lineno)s')

    @return logger: The previously formatted logger
    """

    # First the logger
    logger = logging.getLogger('')
    logger.setLevel(level)

    # Then the handler
    stdout_handler = logging.StreamHandler()
    stdout_handler.setLevel(level)
    stdout_handler.setFormatter(formatter)

    # We add the handler to the logger
    logger.addHandler(stdout_handler)

    return logger

log = setup_logging()
now = datetime.now()

class InputHTMLParser(HTMLParser):

    def add_template(self):
        self.template = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'input' or tag == 'select':
            if tag == 'select':
                log.info(attrs)
            for attr in attrs:
                if attr[0] == 'name':
                    name = attr[1]
                if attr[0] == 'value':
                    value = attr[1]
            try:
                self.template[name] = value
            except UnboundLocalError:
                self.template[name] = ''

def _input(input_string):
    """
    An input / raw_input wrapper, used to be compatible with both python 2 and 3
    :param input_string: The argument to input / raw_input

    :return response: The response given by the user
    :rtype: string
    """
    try:
        response = raw_input(input_string)
    except NameError:
        response = input(input_string)
    return response


def days(month=now.month):
    """
    Generator to give the days of a month. If no month is specified, it uses current month
    :param month: month to iterate

    :return day: Generator of days, as `datetime` objects
    """
    year = now.year
    weeks = calendar.monthcalendar(year, month)

    for week in weeks:
        for day in week:
            if day != 0:
                # week is a list such as [0,0,0,1,2,3,4] or [5,6,7,8,9,10,11]
                # as a default, 0 index in the list correspond to a Monday and so forth
                # The entries with a value of 0 are only there to complete the list
                yield datetime(year, month, day)

def _is_weekend(day):
    """
    Check if the given day is weekend

    :param day: The day to look if is weekend or not, as a datetime.datetime object

    :rtype: Boolean
    """
    if day.isoweekday() > 5:
        return True

def is_work_day(day):
    if not _is_weekend(day):
        return True

if __name__ == '__main__':

    log.info('Starting execution ...')
    user = _input('Please enter your username: ')
    pwd = getpass.getpass('Please enter your password: ')

    # FIXME: This need to be asked by command line or something
    EXAMPLE_DAY = '19/03/2015'

    input_html_parser = InputHTMLParser()
    input_html_parser.add_template()

    with requests.Session() as s:
        s.auth = (user, pwd)
        response = s.get('http://www.morse.es/gsp/asp/Maqueta2.asp', data={'p_data':EXAMPLE_DAY})
        # FIXME: Check response.status_code

        # Feed the parser with the response to prepare the data to be sent with the post
        input_html_parser.feed(response.content)
        post_data = input_html_parser.template

        for day in days():
            if is_work_day(day):
                day_str = day.strftime('%d/%m/%Y')
                    log.info('Imputing day {day}'.format(day=day_str))
                    post_data['p_data'] = day_str
                    # FIXME: Selects are not correctly parsed, here are hardcoded and only work with one line
                    post_data['c_client1'] = post_data['p_Client1']
                    post_data['c_exe1'] = post_data['p_exe1']

                    s.post('http://www.morse.es/gsp/asp/Maqueta2.asp', data=post_data)
