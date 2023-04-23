# Importing the Modules
import keyboard, time, argparse
from pynput.keyboard import Controller, Key

# main Function
def DiscoKeyboard(run:int=10, hold:float=0.25):
     """# DiscoKeyboard
     ---------------------
     Set the Value of Parameter (Optional).
     - `run` How many times Run
     - `hold` How much sec delay

     Simple and easy program. run it and enjoy the light of keyboard.

     -----------
     ### To see the loading progress in Keyboard.
     - Disable the locks.
     """

     kbd =  Controller()
     N, C, S = False, False, False
     nl, cl, sl =Key.num_lock, Key.caps_lock, Key.scroll_lock

     # Change Light with value.
     def changeBool(key, bool, timer:float=0.0) -> bool:
          time.sleep(timer)
          kbd.tap(key)
          return False if bool else True

     # Set as Default lock value.
     def qut():
          if N: changeBool(nl, N)
          if C: changeBool(cl, C)
          if S: changeBool(sl, S)

     # Times to run lighting Keyboard.
     for _ in range(run):
          if keyboard.is_pressed('esc') or keyboard.is_pressed('tab') or keyboard.is_pressed('enter'): return qut()
          N, C, S = changeBool(nl, N, hold), changeBool(cl, C, hold), changeBool(sl, S, hold)
     qut() # Set Default after run.

# Parser the Arguments

parser = argparse.ArgumentParser(prog='DiscoKeyboard', description='You will get to see the look like disco lights in the keyboard')

# adding arguments value
parser.add_argument('--t', type=int, help="It will work till input time. [default: 10] Time.", default=10)
parser.add_argument('--s', type=float, help="Will stop till the input value, keep the value between (0.1 - 1.0) for best visualization. [default: 0.25]", default=0.25)
parser.add_argument('--v', action='version', version=f'%(prog)s 0.1.1', help='See the Version of program.')

try: 
     # Run the function with argument.
     args = parser.parse_args()
     DiscoKeyboard(args.t, args.s)
except Exception as e: print(e)