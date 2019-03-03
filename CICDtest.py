#!/usr/bin/python

import logging


logging.basicConfig(filename = 'C:/Users/SBijlan/Documents/Automation/DIY/PracticeCICD/cicdPractice.log', filemode = 'a', level = logging.INFO, format = '%(asctime)s  %(levelname)-10s %(message)s')

logging.info("Practice run - test auto-build in Jenkins based on changes in SCM")
