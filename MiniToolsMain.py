import random
import time
import psutil
import os
import platform
import keyboard

# Additional welcome string just for start up.
# Sets the 0 easter egg to be able to be found.
print("Welcome to MiniTools!")
ZeroFound = False

# Tool selection. Checks for user input and sets tool value to said input.
# This is also defined as the function "ToolScreen"
def ToolScreen():
    print("=============================- Please select a tool below. -============================")
    print("1: RNG, 2: Time Ticker, 3: CPU Tool, 4: Memory Tool, 5: Network Tool, 6: Keyboard Tester")
    print("Please only put the number EG 1! Press ESC to exit tool. (You may need to hold for some)")
    print("----------------------------------------------------------------------------------------")
    return int(input("Select what tool you want to use: "))

# Puts the tools in a while loop so they can be exited properly
while True:

    # Sets tool to ToolScreen function's return. It took me a good 5 minutes to figure
    # out how that one worked.. And apparently also calls the function.
    tool = ToolScreen()

    # Little easter egg for if someone tries to be funny.
    if tool == 0 and ZeroFound == False:
        print("Ha ha, very funny..")
        ZeroFound = True
        ToolScreen()

    # If user typed 1 for tool, will initiate the RGN tool. Asks for minimum and 
    # maximum numbers and generates floats once per second corresponding to input.
    elif tool == 1:
        while True:
            print("Random Number Generater selected.")
            MinVal = float(input("Minimum number: "))
            MaxVal = float(input("Maximum number: "))
            while True:
                RandNum = random.uniform(MinVal, MaxVal)
                print(RandNum)
                time.sleep(.5)
                if keyboard.is_pressed("esc"):
                                break

    # If user typed 2 for tool, will initiate the Time Tick tool. Simply
    # adds 1 to current time tick and shows it, counting +1 per second.
    elif tool == 2:
        print("Time Ticker selected.")
        TimeTick = 0
        while True:
            TimeTick = TimeTick + 1
            print(TimeTick)
            time.sleep(1)
            if keyboard.is_pressed("esc"):
                            break
            
    # If user typed 3 for tool, will initiate the CPU tool.
    # CPU tool has 2 options that the user can select.
    elif tool == 3:
        print("==Pick a CPU stat==")
        print("1: CPU specs, 2: CPU usage")
        CpuStat = int(input("Stat: "))

    # CPU Specs checker subtool. Checks the CPU name and cores.
        if CpuStat == 1:
            print("CPU Specs selected.")
            print(f"CPU: {platform.processor()}")
            print(f"Cores: {os.cpu_count()}")
            while True:
                  if keyboard.is_pressed("esc"):
                                  break
                  
    # CPU Usage checker subtool. Checks CPU usage
    # and CPU clock speed (MHz)
        elif CpuStat == 2:
            print("CPU Usage selected.")
            while True:
                print("CPU Usage: ", psutil.cpu_percent(interval=1))
                print("CPU Speed: ", psutil.cpu_freq().current,"MHz")
                if keyboard.is_pressed("esc"):
                                break

    # Memory tool. Checks total RAM, RAM usage, and RAM usage %
    # and displays it every second.
    elif tool == 4:
        print("Memory Tool selected!")
        while True:
            mem = psutil.virtual_memory()
            print(f"Total Memory: {mem.total / (1024**3):.2f} GBs")
            print(f"Used Memory: {mem.used / (1024**3):.2f} GBs")
            print(f"Percent: {mem.percent}%")
            time.sleep(1)
            if keyboard.is_pressed("esc"):
                            break
            
    # Network tool. Checks network usage and a bunch of random network
    # stats and prints them once per second.
    elif tool == 5:
        print("Network Tool selected.")
        print("I couldn't add more without flooding the logs..")
        time.sleep(3)
        while True:
            print(f"Network usage: {psutil.net_io_counters()}")
            print(f"Network stats: {psutil.net_if_stats()}")
            time.sleep(1)
            if keyboard.is_pressed("esc"):
                            break

    # Keyboard input checker. Simply takes the keyboard input,
    # prints it, and pauses for a tiny little bit to prevent
    # spam on release of key.
    elif tool == 6:
        while True:
            key = keyboard.read_key()
            print(f"Key: {key}")
            time.sleep(.25)
            if keyboard.is_pressed("esc"):
                            break

    # If the selected tool doesn't exist, re-open the select menu.
    else:
        print("That tool does not exist!")
        ToolScreen()

# And that's all! Next project is a better UI based one.
