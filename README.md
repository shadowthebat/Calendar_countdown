Simple countdown calendar.
- create calendar by adding dates or 'events'
-   create list of datetime objects
-   set with CURRENT YEAR and desired day/month
-   the year will automatically update
-   create corresponding list of labels in same order as datetime objects

- example:
-   from datetime import datetime as d
-   from convertdate import holidays

-   canada = d(d.now().year, 7, 1)
-   ny = d(d.now().year, 1, 1)

-   passover = holidays.passover(d.now().year) # extract from convertdate
-   passover = d(passover[0], passover[1], passover[2]) # set as datetime object

-   key = [canada, new years]
-   labels = ['canada day', 'new years day']

- display number of days and weeks until event
- optional arguments include: head, tail, len
- example:
- 	python calendar_fresh.py (displays all countdown events chronologically)
-	python calendar_fresh.py head (displays closest 5 results)
-	python calendar_fresh.py tail (displays furthest 5 results)
-	python calendar_fresh.py len (displays total number of events)
