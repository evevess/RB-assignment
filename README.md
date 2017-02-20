# RB-assignment
An assessment of RB company for their candidate of junior software developer

Usage instruction: 
easyversion.py is the easy version that point different sorting to different route without GUI
Checkbox.py include a regular user interface : first a checkbox will popup and you could choose your way of sorting,  then the sorted data will show up accordingly when you make a call to your localhost.
importdata.py linked the webpage with checkbox, however, i have not find a way of reading the checkbox input value on web.

Difficulties:

a.In checkbox.py line 105 i have to assign a specific port, and change it every time when i run the code. Otherwise it shows error.

b. I couldn't find a way to show the data with requested sorting when a call to localhost is made. Mine currently works as: first showing the requested sorting and then show the localhost address, when a call is made the sorted data will be shown. Any suggestion how can I fix this?

d. Need further research: 
What does assumptions, configuration, consistency, PEP8 specifically imply here?
For example, is 'user can only choose one way of sorting at one time' an assumption or not and if it is, how can I justify it?

Time usage:
Start with reading some documentation of bottle and watch youtube video of bottle web framework from PythonBytes. Then downloading python and pycharm. It took some time to install and setup everything.
First start coding without bottle and that take approximately 1 hour to: first print the raw data, then user interface popup with sorting request(5 ways), then print the sorted data accordingly. 
Afterwards, the real task starts, took me about two hours to find a nice way to print the data on webpage by using the template 'display_table' and the easy version is created accordingly.
It tooks 2-3 hours to link the webpage to the checkbox by creating templates.
Then it took me almost almost a whole day to try to find a way to show the user interface when making a call to localhost, and to automatically refresh/reload the webpage when the sorting request is sent, and read the input from web checkbutton. unfortunately i did not succeed on these parts. 

I do not think I did it well due to my limited knowledge of web deveopment, but I did really enjoy doing it. It is a lot of fun and thank you for the assignment! 
