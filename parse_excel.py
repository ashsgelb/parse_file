# import sys
# import re
# from prettytable import PrettyTable


# class Event:
#     def __init__(self):
#         self.day = ""
#         self.time = ""
#         self.title = ""
#         self.description = ""

# def read_file():
    
#     #check that a file name is given in the command line
#     if len(sys.argv) != 2:
#         print("Error: Enter a file name")
#         sys.exit(1)

#     #get the filename from command line arguments
#     filename = sys.argv[1]

#     #open the file (or attempt to)
#     try:
#         with open(filename, 'r') as file:
#             process(file)
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# def process(file):
    
#     #make a list for all of the events
#     events = []

#     #set the current event to none
#     current_event = None

#     #read the first line for the day and remove the comma
#     first_line = file.readline().strip()
#     day = first_line.split()[0][:-1]  #remove the comma
    
#     #regular expression to detect time entries (had AI help for this one)
#     time_regex = re.compile(r'\d{1,2}:\d{2} (am|pm) — \d{1,2}:\d{2} (am|pm)')

#     #iterate over the remaining lines
#     for line in file:

#         #clear out any white space that will mess it up
#         line = line.strip()
        
#         #every new time indicates a new event -- use regex function
#         #if it is a time line
#         if time_regex.match(line):

#             #if there is a previous event make sure it is saved
#             if current_event:
#                 events.append(current_event)
            
#             # Start a new event
#             current_event = Event()
#             current_event.day = day #set to the day got earlier
#             current_event.time = line #time is the first line in each one
#             current_event.title = "" #don't have yet
#             current_event.description = "" #don't have yet
        
#         #if it is not a time line
#         elif line:

#             #if there is a current event -- otherwise end of page
#             if current_event:

#                 #if there is no title add a title
#                 if not current_event.title:
#                     current_event.title = line
                
#                 #otherwise the rest of it is description
#                 else:   
#                     if current_event.description:
#                         current_event.description += " "
#                     current_event.description += line

#     #make sure to add the last event, since no more lines to go through
#     if current_event:
#         events.append(current_event)

#     #need to create a data frame for mysefl
#     data  = {
#         "Day": [event.day for event in events],
#         "Time": [event.time for event in events],
#         "Title": [event.title for event in events],
#         "Description": [event.description for event in events]
#     }

#     my_excel = panda.DataFrame(data)

#     # Save the DataFrame to an Excel file
#     excel_filename = 'events.xlsx'
#     my_excel.to_excel(excel_filename, index=False, engine='openpyxl')

#     print(f"Data has been exported to {excel_filename}")


   

# if __name__ == "__main__":
#     read_file()



import sys
import re
from prettytable import PrettyTable
import pandas as panda

class Event:
    def __init__(self):
        self.day = ""
        self.time = ""
        self.title = ""
        self.description = ""

def read_file():
    
    #check that at least one file name is given in the command line
    if len(sys.argv) < 2:
        print("Error: Enter a file name")
        sys.exit(1)

    #init list for all of the events
    all_events = []

    #iterate though all  diff input files
    for filename in sys.argv[1:]:
        
        #open the file (or attempt to)
        try:
            with open(filename, 'r') as file:
                events = process(file)
                all_events.extend(events)
        
        #print an error if can't open or just have problems
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    # print(table)

    #need to create a data frame for mysefl
    data  = {
        "Day": [all_events.day for all_events in all_events],
        "Time": [all_events.time for all_events in all_events],
        "Title": [all_events.title for all_events in events],
        "Description": [all_events.description for all_events in all_events]
    }

    my_excel = panda.DataFrame(data)

    # Save the DataFrame to an Excel file
    excel_filename = 'events.xlsx'
    my_excel.to_excel(excel_filename, index=False, engine='openpyxl')

    print(f"Data has been exported to {excel_filename}")

def process(file):
    
    #make a list for all of the events
    events = []

    #set the current event to none
    current_event = None

    #read the first line for the day and remove the comma
    first_line = file.readline().strip()
    day = first_line.split()[0][:-1]  #remove the comma
    
    #regular expression to detect time entries
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
            current_event.description = "" #don't have ye
        
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
    if current_event:
            events.append(current_event)

    return events

if __name__ == "__main__":
    read_file()

