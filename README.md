# JEE Alerter

Reloads the JEE Main webpage to check if there are any updates (NTA doesn't 
release the time at which the results will be released lol).
Update frequency is passed via command line parameters.

## Requirements
- Requests
- BeautifulSoup
- playsound 

## Usage
Use with Caffeinate
```
caffeinate ./jeealerter.py <update duration in seconds>
```

Example:
```
caffeinate ./jeealerter.py 60
```
checks every 60 seconds for an update.
