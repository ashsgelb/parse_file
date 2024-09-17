Name: 
    Ashley Gelber

Date: 
    9/17/2024

Task: 
    Go through the agenda and put it into a spreadsheet with catagroies for Day, Time, Title, and Details

Idea: 
    Instead of tediously copy and pasting, write a python script that can generate this spreadsheet. Use the formatting given on the website (https://www.p3highereducation.com/agenda/)

Implementation: 
    1. Parse the code based off of formatting given on the website (https://www.p3highereducation.com/agenda/)
    2. Have it print to prettytables (easy way to debug while coding)
    3. Create another file using same code basis that uses pandas to allow export to an excel file

Example Files (took text from website):
    1. sunday.txt
    2. monday.txt
    3. tuesday.txt

Pretty Table Output:
    1. Sunday_table -- showing only events on Sunday
    2. Monday_table -- showing only events on Monday
    3. Tuesday_table -- showing only events on Tuesday
    4. All_table -- show events for all three days

Excel Output:
    1. Sunday_excel -- showing only events on Sunday
    2. Monday_excel -- showing only events on Monday
    3. Tuesday_excel -- showing only events on Tuesday
    4. All_excel -- show events for all three days


**Pretty Table**

*Prerequisites*

Before running the script, ensue you have the following installed:
    1. Python 3.x
    2. Required Python Library: prettytable

You can intall the necessary libraries using pip:
    pip isntall prettytable


*Usage*
    
To run the script, use the following command in your terminal:
    python3 parse.py <input_file_1>.txt <input_file_2>.txt ... <input_file_n>.txt

Arguments
    <input_1>.txt and <input_2>.txt: Text files containing the event data to be processed. You can specify multiple input files.

**Excel Table**

*Prerequisites*

Before running the script, ensue you have the following installed:
    1. Python 3.x
    2. Required Python Library: openpyxl

You can intall the necessary libraries using pip:
    pip isntall prettytable


*Usage*
    
To run the script, use the following command in your terminal:
    python3 parse_excel.py <input_file_1>.txt <input_file_2>.txt ... <input_file_n>.txt

Arguments
    <input_1>.txt and <input_2>.txt: Text files containing the event data to be processed. You can specify multiple input files.

