# Tool: Extracting amount of doors and determining cost

* Group 40 - Analyst 
* Focus area: Built
* Analyst Level 2: Analyse the property sets of an IFC file in the BlenderBIM GUI and develop a simple Python Script in BlenderBIM using ifcOpenShell.

## State the problem / claim that your tool is solving.
*  Quickly determine quantity and cost of elements (ex.doors) in a model 
## State where you found that problem.
* In our experience with the 'Advanced Building Design' course, we spent a significant amount of time extracting quantities for tasks like cost calculations and LCA analysis. A tool to streamline this process would be very useful.  

## Description of the tool
 * The tool first identifies the number of doors in the IFC model. Then, it calculates the total cost for each door type based on user-input. Finally, a table displaying each door type, unit price, and total cost is generated, making the data clear and easy for the user to interpret.  

## Instructions to run the tool.
* Open the script in visual studio code or similar, and view the terminal.  
* The terminal shows "PS" and the location, and then you should type "python" and you filename (ex.01Script.py).  
* Run the script from the terminal.  
* Give the input that the program asks for. 
* The first thing the program will ask for is the file path. Insert then the file path to where the model is stored on your computer. (It could for example look like this: C:\Users\xxxxx\Documents\DTU\41934 Advanced BIM\A3\CES_BLD_24_11_ARC.ifc). 
* You should get the data presented in a table.

```python
import ifcopenshell
import re

def count_doors_by_name(ifc_file):
    # Dictionary to hold counts of doors by name
    door_count = {}

    # Get all door elements
    doors = ifc_file.by_type("IfcDoor")
    print(f"Found {len(doors)} doors in the IFC file.")  # Debugging line

    if len(doors) == 0:
        print("No doors were found in the IFC file. Check if the file contains doors.")
        return door_count  # Return early if no doors are found

    # Iterate over each door and group by base name (without unique IDs)
    for door in doors:
        # Check if door has a name attribute, if not assign "Unknown Door"
        door_name = door.Name if hasattr(door, "Name") and door.Name else "Unknown Door"

        # Use regex to remove anything after a colon and the unique ID number
        base_name = re.split(r":\d+$", door_name)[0]

        # Increment the count for this base name
        if base_name in door_count:
            door_count[base_name] += 1
        else:
            door_count[base_name] = 1

    return door_count

def input_costs(door_count):
    # Dictionary to hold cost information for each door type
    cost_data = {}

    # Prompt user for cost input for each type of door
    for door_name, count in door_count.items():
        while True:
            try:
                cost_per_unit = float(input(f"Enter cost per unit for '{door_name}' (Quantity: {count}): "))
                break  # Exit the loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        # Calculate total cost for this door type
        total_cost = count * cost_per_unit

        # Store cost per unit and total cost in the dictionary
        cost_data[door_name] = {
            "quantity": count,
            "cost_per_unit": cost_per_unit,
            "total_cost": total_cost
        }

    return cost_data

def display_cost_summary(cost_data):
    # Print a summary table
    print("\nCost Summary for Doors:")
    print(f"{'Door Name':<60} {'Quantity':<10} {'Cost per Unit ($)':<20} {'Total Cost ($)':<15}")
    print("-" * 105)

    total_quantity = 0
    total_cost = 0

    for door_name, data in cost_data.items():
        quantity = data['quantity']
        cost_per_unit = data['cost_per_unit']
        total_cost_door = data['total_cost']

        print(f"{door_name:<60} {quantity:<10} {cost_per_unit:<20.2f} {total_cost_door:<15.2f}")
        
        # Update totals
        total_quantity += quantity
        total_cost += total_cost_door

    # Calculate average cost per door if total_quantity is greater than 0
    average_cost_per_door = total_cost / total_quantity if total_quantity > 0 else 0

    # Print summary line for totals
    print("-" * 105)
    print(f"{'TOTAL':<60} {total_quantity:<10} {'-':<20} {total_cost:<15.2f}")

def main():
    # Prompt the user to enter the path to the IFC file
    ifc_file_path = input("Please enter the path to your IFC file: ")

    # Open the IFC file
    try:
        ifc_file = ifcopenshell.open(ifc_file_path)
        print("Successfully opened IFC file:", ifc_file_path)
    except Exception as e:
        print("Error opening IFC file:", e)
        return

    # Count doors only by the base name (without unique identifiers)
    door_count = count_doors_by_name(ifc_file)

    if not door_count:
        print("No doors found or no detailed information was identified.")
        return

    # Input cost for each door type and calculate total costs
    cost_data = input_costs(door_count)

    # Display the cost summary
    display_cost_summary(cost_data)

if __name__ == "__main__":
    main()
```


## What Advanced Building Design Stage (A,B,C or D) would your tool be usefuL?
* For the different phases; Plan, Design, Build and Use, this tool is most useful in the cost estimation during the planning phase. 

## Which subjects might use it?
* Project managers mainly. 

## What information is required in the model for your tool to work?
* The model must contain doors
* All doors must be classified as IfcDoor

# Tutorial: Modifying the extracted ifc type name from model

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

