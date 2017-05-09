#!/usr/bin/env python

import time
import sys
import syslog
import requests
from qhue import Bridge

# Variables for each Dash button MAC address
kleenex_dash = 'ac:63:be:16:7b:89'

last_action_file = '/tmp/tcl-lametric'

def main(argv):

  syslog.syslog(str(argv))

  action = argv[1]
  mac = argv[2]

  if action not in ['add', 'old']:
    sys.exit(0)

  if mac != kleenex_dash:
    sys.exit(0)

  syslog.syslog('Dash button action detected')

  try:
    h = open(last_action_file, 'r')
    lastseen = int(float(h.read().rstrip('\n')))
    h.close()
    if not lastseen:
      lastseen = 0
  except Exception:
    syslog.syslog("Can't load state file, setting last seen at 0")
    lastseen = 0

  now = time.time()
  syslog.syslog("Last seen: %i" % int(lastseen))
  delta = int(now) - lastseen
  syslog.syslog("Last seen: %i ago" % delta)

  h = open(last_action_file, 'w')
  h.write(str(now))
  h.close()

  if delta < 10:
    syslog.syslog("No triggering action (double request?)")
    sys.exit(0)

  syslog.syslog("Triggering action")

  requests.get('http://tcl-api.service.dc1.consul:5000/push-lametric')
  syslog.syslog('Notification sent to LaMetric')


if __name__ == '__main__':
  main(sys.argv)