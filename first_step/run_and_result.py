from tasks import add
import time

result = add.delay(3,7)
while result.ready() == False:
    print 'waiting for result'
    time.sleep(1)
print 'result is ' + str(result.get())
