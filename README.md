# ECE 4984 Final Project

A facility location game-based simulation tool to optimally deploy base stations in a cellular network

### Requirements

This program requires Python 3.6 or newer to run. Any prior versions are not guaranteed to work properly. In order to run the program, download the `main.py` file, and run it with `python3 main.py`. By default, the program is set to run on user input, but it can be switched to a debug mode with hardcoded values by changing line 3 to `DEBUGVALS = True`.

You will be prompted to enter the minimum and maximum ranges of the small cells that you wish to deploy, and then you are given the option to add facilities and customers to the system. For facilities, the parameters are the x-location, the y-location, the range, and the operational cost, all in arbitrary units. For customers, the parameters are the x-location and the y-location, both in arbitrary units as well.

Currently, the program only supports finding a location or locations for small cells covering one or two customers that are not in range of a current facility. Attempting to add more customers that are not in range of a current facility may cause undefined behavior.
