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
    for door_name, data in cost_data.items():
        print(f"{door_name:<60} {data['quantity']:<10} {data['cost_per_unit']:<20.2f} {data['total_cost']:<15.2f}")

def main():
    # Path to your IFC file
    ifc_file_path = "C:\\Users\\ASUS\\Downloads\\CES_BLD_24_10_ARC.ifc"

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