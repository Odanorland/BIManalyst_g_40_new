# About the tool 

## State the problem / claim that your tool is solving.
*  Quickly determine quantity and cost of elements (ex.doors) in a model 
## State where you found that problem.
* In our experience with the 'Advanced Building Design' course, we spent a significant amount of time extracting quantities for tasks like cost calculations and LCA analysis. A tool to streamline this process would be very useful.  

## Description of the tool
 * The tool first identifies the number of doors in the IFC model. Then, it calculates the total cost for each door type based on user-input. Finally, a table displaying each door type, unit price, and total cost is generated, making the data clear and easy for the user to interpret.  

## instructions to run the tool.
* Open the script in visual studio code or similar, and view the terminal.  
* The terminal shows "PS" and the location, and then you should type "python" and you filename (ex.01Script.py).  
* Run the script from the terminal.  
* Give the input that the program asks for. 
* The first thing the program will ask for is the file path. Insert then the file path to where the model is stored on your computer. (It could for example look like this: C:\Users\xxxxx\Documents\DTU\41934 Advanced BIM\A3\CES_BLD_24_11_ARC.ifc). 
* You should get the data presented in a table.   

# About the tool 
## What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?
* For the different phases; Plan, Design, Build and Use, this tool is most useful in the cost estimation during the planning phase. 

## Which subjects might use it?
* Project managers mainly. 

## What information is required in the model for your tool to work?
* The model must contain doors
* All doors must be classified as IfcDoor 
* Doors must have a value for height and width in the property sets. 




# Tutorial on modifying the extracted ifc type name from model

* Group 40 - Analyst 
* Focus area: Built
* Analyst Level 2: Analyse the property sets of an IFC file in the BlenderBIM GUI and develop a simple Python Script in BlenderBIM using ifcOpenShell.


## Issue 
* For part A3, we developed a script to extract door quantities from an IFC model and calculate the associated costs. One issue we encountered was that, when extracting door types based on their IFC type name, the script retrieved the door name along with a unique identifier (e.g., Ext. Double-Flush out - Glass: Ext. Double-Flush out Glass: 1648394). This required the user to input a price for each individual door, defeating the purpose of the script, which is to save time. 

## Description
* This tutorial aim to show one way to modify the extracted name of an element type (ex. door-type) so that we get the type but not consider the uniqe code assigned in the property sets in the model. 
* The point of doing this is so that we can sort the information based on element type. 

```python
# This gives the door name including an unique identifyer
door_name = door.Name if hasattr(door, "Name") and door.Name else "Unknown Door"

# this splits the name in two parts based on regex pattern, and accesses the first of them
base_name = re.split(r":\d+$", door_name)[0]
```

## Result 
Door type name "Ext. Double-Flush out - Glass: Ext. Double-Flush out Glass:1648394" would be converted to "Ext. Double-Flush out - Glass: Ext. Double-Flush out Glass". 

Result from running the script, after modifying the type name: 
![alt text](https://github.com/Odanorland/BIManalyst_g_40_new/blob/main/Skjermbilde18.11.PNG "Result")

