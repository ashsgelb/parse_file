#parse and print using pretty print

import sys
import re
from prettytable import PrettyTable

class Event:
    def __init__(self):
        self.day = ""
        self.time = ""
        self.title = ""
        self.description = ""

def read_file():
    
    #check that a file name is given in the command line
    if len(sys.argv) < 2:
        print("Error: Enter a file name")
        sys.exit(1)

    all_events = []

    for filename in sys.argv[1:]:
        #open the file (or attempt to)
        try:
            with open(filename, 'r') as file:
                events = process(file)
                all_events += events
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    #make a table with proper names
    table = PrettyTable()
    table.field_names = ["Day", "Time", "Title", "Description"]

    #iterate through and print the events
    for event in all_events:
        table.add_row([event.day, event.time, event.title, event.description])
    
    #print out the table
    print(table)

def process(file):
    
    #make a list for all of the events
    events = []

    #set the current event to none
    current_event = None

    #read the first line for the day and remove the comma
    first_line = file.readline().strip()
    day = first_line.split()[0][:-1]  #remove the comma
    
    #regular expression to detect time entries (had AI help for this one)
    time_regex = re.compile(r'\d{1,2}:\d{2} (am|pm) — \d{1,2}:\d{2} (am|pm)')

    #iterate over the remaining lines
    for line in file:

        #clear out any white space that will mess it up
        line = line.strip()
        
        #every new time indicates a new event -- use regex function
        #if it is a time line
        if time_regex.match(line):

            #if there is a previous event make sure it is saved
            if current_event:
                events.append(current_event)
            
            # Start a new event
            current_event = Event()
            current_event.day = day #set to the day got earlier
            current_event.time = line #time is the first line in each one
            current_event.title = "" #don't have yet
            current_event.description = "" #don't have yet
        
        #if it is not a time line
        elif line:

            #if there is a current event -- otherwise end of page
            if current_event:

                #if there is no title add a title
                if not current_event.title:
                    current_event.title = line
                
                #otherwise the rest of it is description
                else:   
                    if current_event.description:
                        current_event.description += " "
                    current_event.description += line

    #make sure to add the last event, since no more lines to go through
    if current_event:
        events.append(current_event)

    return events
   

if __name__ == "__main__":
    read_file()

