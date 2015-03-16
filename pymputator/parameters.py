"""
Command line parsing 
"""

import argparse
import calendar

months = calendar.month_name[1:]
parser = argparse.ArgumentParser()
parser.add_argument('--month', choices=months)
args = parser.parse_args()
print args
             
