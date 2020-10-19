import time
from chronometer import Chronometer

def main():
    long_running_task = lambda: time.sleep(1.)

    with Chronometer() as t:
        long_running_task()  # that will take a few seconds.
    print('Phew, that took me {:.3f} seconds!'.format(float(t)))

if __name__ == "__main__":
        main()