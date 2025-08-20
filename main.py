"""
Ghislaine (IRN: 02879-509) Locator
by: Logan Ketelaars

This python script will request public B.O.P. information on an hourly basis to
alert to any (further) changes regarding that bitch Maxwell's B.O.P. situation.
"""

import time, json, requests
from tkinter import messagebox

running = True # Determines whether for main loop is running
messageshown = False # Prevents messages from being shown every hour after change is detected.

def performPost():
    global running
    global messageshown

    # Current B.O.P. information for that bitch as of Aug. 20th 2025
    facilityCode = "BRY"
    projReleaseDate = "07/17/2037"
    actualReleaseDate = ""

    # Setup POST information
    url = "https://www.bop.gov/PublicInfo/execute/inmateloc"
    forminfo = {
        "todo": "query",
        "output": "json",
        "inmateNumType": "IRN", 
        "inmateNum": "02879-509"
    }

    # Send post request to B.O.P. inmate locator backend and get response json
    resp = requests.post(url, forminfo)
    respData = json.loads(resp.content)

    # Check for response code
    if resp.status_code != 200:
        print("There was an error retrieving the B.O.P. data")
        running = False
        return

    try:
        # Deserialize json response
        data = respData["InmateLocator"][0]
    except(IndexError):
        # Error if expected key is not found in Json array
        print("There was an error parsing the B.O.P. returned data")
        running = False
        return

    # Get relevant information from B.O.P. response
    loc = data["faclCode"]
    projRelDate = data["projRelDate"]
    actuRelDate = data["actRelDate"]
    print(f"Facility Code: {loc}\nProjected Release Date: {projRelDate}\nActual Release Date: {actuRelDate}\n")

    # Check for changes and make changes human readable
    changesString = ""

    if loc != facilityCode:
        changesString += f"Facility changed from {facilityCode} to {loc}\n"
    if projRelDate != projReleaseDate:
        changesString += f"Projected Release Date changed from {projReleaseDate} to {projRelDate}\n"
    if actuRelDate != actualReleaseDate:
        changesString += f"Release Date changed from {actualReleaseDate} to {actuRelDate}"

    # If changes are found show message box.
    if changesString != "" and not messageshown:
        messagebox.showwarning("Ghislaine Alert!", f"Information for Inmate 02879-509 (That Maxwell bitch) has changed! Changes: '{changesString}'")
        messageshown = True
    else:
        print("No changes to alert.\n\n")


# Helper function to generate local system timestamps in specific format (DD/MM/YYYY @ hh:mm MD)
def get_ts():
    t = time.localtime()
    h = t.tm_hour
    ap = "AM"
    if h > 12:
        h -= 12
        ap = "PM"
    return str(t.tm_mday) + "/" + str(t.tm_mon) + "/" + str(t.tm_year) + " @ " + str(h) + ":" + str(t.tm_min) + ap


# Main loop function
def run():
    ts = get_ts() # Time stamp for terminal information
    print(f"{ts}: Checking for B.O.P. changes to inmate 02879-509 (Ghislaine \"that cunt\" Maxwell)") # Output request info to terminal
    performPost() # Check B.O.P. info for changes
    time.sleep(3600) # Wait an hour before next check


# Main loop
while running:
    run()
