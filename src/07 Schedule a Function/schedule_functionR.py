import time
from datetime import datetime
import sched

def schedule_function_R(*args):
    secondsToWait = (args[0] - time.time())
    timeToSchedule = datetime.fromtimestamp(args[0])
    functionToRun = args[1].__name__

    print(f"{functionToRun}() scheduled for {timeToSchedule.strftime('%a %b %d %H:%M:%S %Y')}")
    print(secondsToWait)
    time.sleep(secondsToWait)
    print(args[2])
    if len(args)>3:
        print(args[3])

def schedule_function(timeToSchedule, function, *args):
    s = sched.scheduler(time.time, time.sleep)
    s.enterabs(timeToSchedule, 1, function, argument=args )
    print(f"{function.__name__}() scheduled for {time.asctime(time.localtime(timeToSchedule))}")
    s.run()
    
        

if __name__ == '__main__':
    schedule_function(time.time() + 1, print, 'Howdy!')
    schedule_function(time.time() + 1, print, 'Howdy!', 'How are you?')
