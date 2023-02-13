#!/home/local/Anaconda3-2020.02/envs/py3.9/bin/python

from datetime import datetime
import subprocess
import pdb
import copy
import argparse
import numpy as np
from argparse import RawTextHelpFormatter

def send(tsvfile,ndays=7,broadcast=None,individual=False,
             header='astro-ph this week:') :
    """ Go through tsvfile and send mail if day is within ndays from today

        tsvfile (str) : file to read date (1st column, format includes Month 
                         and ends with day, e.g.  Thursday, May 10), plus
                         other columns to include in reminder (col 4 for
                         individual email)
        ndays (int) : send message if date is within ndays from today
        broadcast (str) : if not None, send message to this address
        individual (bool) : if True, send to address in column 3
        header (str) : string to prepend before spreadsheet line(s)
    """

    print('ndays: ', ndays)
    print('broadcast: ', broadcast)
    print('individual: ', individual)

    # download the current version of google sheet
    fp=open('astroph','w')
    output=subprocess.run(['curl','-L',addr],stdout=fp)
    fp.close()

    # setup for dates, get current day number
    months=['January','February','March','April','May','June',
            'July','August','September','October','November','December']
    year=2023
    daynow=datetime.now().timetuple().tm_yday

    # start to construct the email message
    fout=open('message','w')
    for h in header.split('\\n') :
        fout.write(h+'\n')

    # read through the file, getting event dates
    m=0
    oldout=''
    fp=open(tsvfile)
    send = False
    for line in fp:
        date=line.split('\t')[0]
        for imonth,month in enumerate(months) :
            if month in date : 
                m = imonth+1
                d=date.split(' ')[-1]
        if m < 1 : continue

        # get day number of event
        date=datetime(year=year,month=m,day=int(d))
        dayno=date.timetuple().tm_yday
        if dayno < daynow : continue
  
        # if event is within ndays from now, add event to message 
        if dayno-daynow < ndays and oldout != None: 
            out=line.split('\t')
            if len(out[0]) == 0 : out[0] = oldout[0]
            if out[1] != '' : 
                fout.write('  {:<24s} {:10s} {:s}\n'.format(out[0],out[1],out[2]))
                send = True
            oldout=copy.copy(out)

    fout.close()

    # send message to requested recipients
    if send :
        fin = open('message')
        if individual :
            print('mail sent to: ', out[3])
            subprocess.run(['mail','-s','astroph reminder',out[3]],
                           stdin=fin)

        if broadcast != None :
            print('mail sent to: ', broadcast)
            subprocess.run(['mail','-s','astroph reminder',broadcast],
                           stdin=fin)
