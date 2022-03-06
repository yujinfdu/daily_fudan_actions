from git_base import *
from sys import exit as sys_exit
import time
import random

t = 90*random.randint(0,20)
time.sleep(t)

daily_fudan_core = r'https://github.com/Limour-dev/daily_fudan_core.git'
daily_fudan_actions = r'https://github.com/Limour-dev/daily_fudan_actions.git'

try_call(git_add_upstream, daily_fudan_core)

git_c2upstream()

arg = get_arg()

if arg:
    ret = pip_install()
    if ret:
        sys_exit(ret)
    ret = run_pythonfile_arg('dailyFudan.py', arg)
    if ret:
        sys_exit(ret)
