import random
import logging
import sys, time
from daemon import Daemon

class MyDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(3)
			logging.info("->")


def init_log():
	logging.basicConfig(filename='/var/log/amir.log',level=logging.INFO,
	 format="[%(asctime)s][%(levelname)s] %(message)s",
	 datefmt="%Y-%m-%d %H:%M:%S")


def test(s):
	ch = 2
	assert s > ch
	logging.info("%s is greater than %s" %(s,ch))


init_log()

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/amir.pid')

	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			logging.info("starting service")
			daemon.start()
		elif 'stop' == sys.argv[1]:
			logging.info("stopping service")
			daemon.stop()


a = random.randint(1,5)

"""
try:
	test(a)
except AssertionError:
	logging.error("Assert! for %s" %a)
except Exception:
	print "Exception!"

"""