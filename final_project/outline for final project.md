outline for final project
- needs to import some file with information about each exercise 
    - parsing through the file to find appropriate workout information will be the most difficult 
    - could export the program into a txt file for the user 
- creation of file could be included as part of final project  

possible imports throughout:
- regex
- random 
- sys
- argparse

parse_args() function:
    - takes arguments from user 
    - maybe one property is level (l) and another is body group
        - beginner, intermediate, advanced
        - push, pull, legs
    - arguments are used to parse info and create a program 

what if i made a class object that held the instance of the user's preferences? 
- need class that will: 
    - take user arguments 
    - read through file
    - write/format appropriate program
        - 4-8 workouts depending on difficulty level (no supersets because i'm lazy)
    - return said program 
- calling the class would look like:
    User(level, body_group)

what about said file? how do we create a file that has all this information?
- pandas maybe?
- parses through a webpage for specific workouts
    - usage of web 
- need tags to be added 
- exported as csv 
- so how to parse through the information? 
    - 

how this will use all modules
- web scraping / parsing? 
    - will be the most difficult to pull off 
    - transfer info from website into database
- git - can review everything on my github for hte presentation
- obviously will use basics and data container types (and classes for module 7)
- usage of pandas