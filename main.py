"""Demonstrates the use of the Smiley class and its subclasses.
If you have access to a SenseHAT (either via a Raspberry Pi or a SenseHAT emulator), you can use the real SenseHAT class instead of the mock SenseHAT class.
That is, delete the sense_hat.py file that is included in this bundle."""

import time
from sad import Sad
from happy import Happy
from angry import Angry

def main():
    smiley = Happy()
    smiley.show()

    time.sleep(1)
    smiley.blink()


    smiley = Sad()
    smiley.show()

    time.sleep(1)
    smiley.blink()

    smiley = Angry()
    smiley.show()

    time.sleep(1)


if __name__ == '__main__':
    ############################################################
    # Uncomment the lines below only if you have multi-processing issues
    # from multiprocessing import freeze_support
    # freeze_support()
    ############################################################
    main()

