import time
time.time()
localtime = time.asctime( time.localtime(time.time()))
print "Local current time :", localtime 

epochtime = time.localtime(time.time())
print "Time since EPOCH! :", epochtime