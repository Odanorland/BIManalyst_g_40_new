# Tutorial on modifying the extracted ifc type name from model

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

