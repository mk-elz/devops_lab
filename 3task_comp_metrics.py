#!/usr/bin/env python

import psutil
import datetime
import json
import configparser
import time


class CompMetrics:
    """Common base class for all comp metrics"""

    def get_cpu(self):
        return str(psutil.getloadavg())

    def get_mem(self):
        mem = str(psutil.virtual_memory().active / (1024 * 1024))
        vmem = str(psutil.virtual_memory().used / (1024 * 1024))
        return mem, vmem

    def get_d_io(self):
        return str(psutil.disk_io_counters().write_bytes / (1024 * 1024))

    def get_n_io(self):
        return str(psutil.net_io_counters().bytes_sent / (1024 * 1024))

    def get_setting(self):
        """Get settings from ini"""

        config = configparser.RawConfigParser()
        config.read('conf.ini')
        time_sleep = float(config.get('common', 'interval'))
        output_type = config.get('common', 'output')
        return time_sleep, output_type


my = CompMetrics()
timeSleep, outputType = my.get_setting()
i = 1
"""timeStamp= ('TIMESTAMP: {:%Y-%m-%d %H:%M:%S}'\
            .format(datetime.datetime.now()))"""
if outputType == 'json':
    while True:
        timeStamp = ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        mem, vmem = my.get_mem()
        snapshotStr = json.dumps({
            'SNAPSHOT': str(i),
            'TIMESTAMP': timeStamp,
            'CPU': my.get_cpu(),
            'MEM': my.get_mem()[0] + 'Mb',
            'VMEM': my.get_mem()[1] + 'Mb',
            'IO INFO': my.get_d_io() + 'Mb',
            'NET INFO': my.get_n_io() + 'Mb'
        }, indent=4) + '\n'
        file = open('metrics-log.json', 'a')
        file.write(snapshotStr)
        #        file.write('\n')
        file.close()
        time.sleep(timeSleep * 60)
        #   time.sleep(timeSleep)
        i += 1

elif outputType == 'txt':
    while True:
        timeStamp = ('{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now()))
        snapshotStr = 'SNAPSHOT: ' + str(i) + ' | ' + \
                      'TIMESTAMP: ' + timeStamp + ' | ' + \
                      'CPU: ' + my.get_cpu() + ' | ' + \
                      'MEM: ' + my.get_mem()[0] + 'Mb' + ' | ' + \
                      'VMEM: ' + my.get_mem()[1] + 'Mb' + ' | ' + \
                      'IO INFO: ' + my.get_d_io() + 'Mb' + ' | ' + \
                      'NET INFO: ' + my.get_n_io() + 'Mb' + '\n'
        file = open('metrics-log.txt', 'a')
        file.write(snapshotStr)
        # file.write('\n')
        file.close()
        time.sleep(timeSleep * 60)
        #        time.sleep(timeSleep)
        i += 1
