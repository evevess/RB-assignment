# RB-assignment
An assessment of RB company for their candidate of junior software developer

Usage instruction: 
Checkbox.py is the main file, simply run this file. 
It works as follows: first a checkbox will popup and you could choose your way of sorting,  then the sorted data will show up accordingly when you make a call to your localhost.

Difficulties:
a.In checkbox.py line 105 i have to assign a specific port, and change it every time when i run the code. Otherwise it shows error.

b.I created a regular checkbox that is not linked to the webpage and I am wondering if there is a specific bottle web framework user interface available? or if there is a way to link the checkbox to bottle webpage?

c. I couldn't find a way to show the data with requested sorting when a call to localhost is made. Mine currently works as: first showing the requested sorting and then show the localhost address, when a call is made the sorted data will be shown. Any suggestion how can I fix this?

d. Need further research: 
What does assumptions, configuration, consistency, PEP8 specifically imply here?
For example, is 'user can only choose one way of sorting at one time' an assumption or not and if it is, how can I justify it?

Time usage:
Start with reading some documentation of bottle and watch youtube video of bottle web framework from PythonBytes. Then downloading python and pycharm. It took some time to install and setup everything.
First start coding without bottle and that take approximately 1 hour to: first print the raw data, then user interface popup with sorting request(5 ways), then print the sorted data accordingly. 
Afterwards, the real task starts, took me about two hours to find a nice way to print the data on webpage by using the template 'display_table'.
Then it took me almost half day to try to find a way to show the user interface when making a call to localhost, and to automatically refresh/reload the webpage when the sorting request is sent. unfortunately i did not succeed on both parts. 

I do not think I did it well due to my limited knowledge of web deveopment, but I did really enjoy doing it. It is a lot of fun and thank you for the assignment! 
