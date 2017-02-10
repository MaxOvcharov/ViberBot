from simpleViberBot import app, set_webhook
import time
import sched
import threading

if __name__ == "__main__":
    scheduler = sched.scheduler(time.time(), time.sleep)
    scheduler.enter(5, 1, set_webhook, (viber,))
    t = threading.Thread(target=scheduler.run)
    t.start()
    app.run()
