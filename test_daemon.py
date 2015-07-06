import random
import logging
import sys, time
from daemon import Daemon

class MyDaemon(Daemon):
	def run(self):
		while True:
			time.sleep(3)
			logging.info("->")


def init_log(log_file):
	logging.basicConfig(filename='/var/log/%s'%(log_file),level=logging.INFO,
	 format="[%(asctime)s][%(levelname)s] %(message)s",
	 datefmt="%Y-%m-%d %H:%M:%S")


def test(s):
	ch = 2
	assert s > ch
	logging.info("%s is greater than %s" %(s,ch))


init_log('%s.log' %sys.argv[0])

if __name__ == "__main__":
	daemon = MyDaemon('/tmp/%s.pid'% sys.argv[0])

	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			logging.info("starting service")
			try:
				daemon.start()
			except Exception, e:
				logging.error('Shutting down ! %s' %e)

		elif 'stop' == sys.argv[1]:
			logging.info("stopping service")
			try:
				daemon.stop()
			except Exception, e:
				logging.error('Could not stop! %s' %e)

		elif 'restart' == sys.argv[1]:
			logging.info("restarting service")
			try:
				daemon.restart()
			except Exception, e:
				logging.error('Could not restart! %s' %e)

		elif 'status' == sys.argv[1]:
			pid = daemon.status()
			if pid:
				print "Service is running [pid:%s]" %pid
			else:
				print "Service is stopped!"

		else:
			print "Unknown command!"
			sys.exit(2)

		sys.exit(0)
	else:
		print "usage: %s start|stop|restart|status" % sys.argv[0]
		sys.exit(2)



a = random.randint(1,5)

"""
try:
	test(a)
except AssertionError:
	logging.error("Assert! for %s" %a)
except Exception:
	print "Exception!"

"""