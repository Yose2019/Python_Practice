'''
🗂️ Week 3 – Final Project
File Explorer Utility
Objective

Create a console-based File Explorer that allows a user to inspect, analyze, and search files inside a directory.

Functional Requirements
1. Directory Validation
Accept a directory path from the user.
Verify that the path exists.
Verify that the path is a directory.
Display an appropriate error if invalid.
2. File Listing

Display every file in the directory.

Ignore subdirectories.
Handle empty directories gracefully.
3. File Information

For every file, display:

File name
File extension
File size (bytes)
4. Directory Statistics

Generate a report containing:

Total number of files
Total size of all files
Largest file (name and size)
Smallest file (name and size)
Count of files by extension

Example:

Directory Report

Total Files : 14
Total Size  : 245831 Bytes

Largest File
-------------
movie.mp4
185423 Bytes

Smallest File
--------------
todo.txt
52 Bytes

Extension Summary
-----------------
py   : 5
txt  : 4
pdf  : 2
jpg  : 3
5. Search & Filter

Implement the following searches:

Search by extension

Example:

py

↓

Display all Python files.

Search by partial filename

Example:

report

↓

Matches:

report.pdf
report_final.docx
monthly_report.xlsx
Search by minimum size

Example:

5000

↓

Display every file whose size is at least 5000 bytes.
'''