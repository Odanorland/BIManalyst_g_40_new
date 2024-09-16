# BIManalyst group 40
Focus area : BUILD

A1 Submission: 

In the structural report "CES_BLD_24_06_STR" p. 12 they claim that the coulumns are within the following dimensions: 360x360mm, 420x420mm, 480x480mm, 600x600. We are verifying that this is the case in the model using the provided script. 

The script is defining the valid dimensions of the columns, from the report. Then it loops thhrough all objects in the model, and all objects that contains "IfcColumns" in the name are identified as a column. For each column it finds their bounding box to determine width and depth, and checks if it`s within the valid demensions. In the end it output the number of columns that are NOT within the requirements. For the model provided zero columns were outside the valid dimensions.  
