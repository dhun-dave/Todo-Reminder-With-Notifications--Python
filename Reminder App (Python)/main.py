import time
from plyer import notification


if __name__ == "__main__":

    notification.notify(
        title="Take a break?",
        message=" Taking breaks every 25 minutes are good for you (as per the Pomodoro Technique) ",


        timeout=10
    )

    time.sleep(1500)