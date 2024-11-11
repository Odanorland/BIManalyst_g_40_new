# Tutorial blabla 

## Issue 
* For part A3, we developed a script to extract door quantities from an IFC model and calculate the associated costs. One issue we encountered was that, when extracting door types based on their IFC type name, the script retrieved the door name along with a unique identifier (e.g., ...). This required the user to input a price for each individual door, defeating the purpose of the script, which is to save time. 

## Description
* This tutorial aim to show one way to modify the extracted name of an element type (ex. door-type)e so that we get the type but not consider the uniqe code assigned in the property sets in the model. 
* The point of doing this is so that we can sort the information based on element type. 

```python
base_name = re.split(r":\d+$", door_name)[0]
```



