# UMR_Mirror-Flipper
Micropython Code for an ESP32


This Code drives a DRV8825 stepper-motor-driver.
It rotates the motor (200 steps/rev) 90° after 30 seconds and back after another 30 seconds. Then repeats.


setMicroSteps() method takes 1,2,4,8,16,32 as an argument and sets the microstep configuration of the driver.
qurter-step-mode is the default


moveStep(direction) method moves one (micro)step in the given direction, direction argument accepts 0 or 1


driverSlp() method disables the driver, caution: no more holding torque is available then.
the driver is awake by default


driverWake() mathod wakes the driver back up


flipMirror() is a method to rotate the motor 90° in alternating directions
a "direction" variable can be declared globally if the starting direction should not be 0 but 1


getFreq() method reads a "freq.txt" file in the same directory as the "boot.py" file.
it expects an integer to set the time between the motor turning in seconds and returns that integer
if that file is not existing or its contents cannot be converted to an integer, the method will return the default value 30


then a timer is declared and initialized, it calls the flipMirror() method every by getFreq() given seconds.



uploading new code:

install rshell with >pip install rshell

connect to board with >rshell -p PORT

upload code with >cp /PATH/boot.py /pyboard/boot.py

to enter python prompt enter >repl

reset the board after uploading new code



troubleshooting:

if board is bricked and connecting via rshell is not possible
connect to board using serial tool and
rename the boot.py file with the following commands:

uos.rename("boot.py", "temp_boot.py")

or delete the file entirely

uos.rm("boot.py")

then reset the board and upload new code


