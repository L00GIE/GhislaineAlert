# GhislaineAlert
A small python script that queries the B.O.P. information for Ghislaine Maxwell to notify of any (further) changes to this horrible woman's sentence or location.

About this script:
This script uses the same form data / backend utilized by the official site (bop.gov/inmateloc/)
This script queries the B.O.P. information for a single inmate: Ghislaine Maxwell (IRN: 02879-509)
The script checks the current information from the B.O.P. against hard-coded information gathered on August 20th 2025, and will create an alert window (if changes are found) providing the changes to said information.
The script performs these queries on an hourly basis and will add a message with a date/timestamp (local time) to the terminal output each time it performs the query.

Instructions:
1. Download and extract main.py
2. Run using CMD or Terminal by navigating to the file's directory and execute command: "python main.py"
3. Leave running in the background and hope you don't get an alert.
