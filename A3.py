import ifcopenshell
import ifcopenshell.util.element

# Load the IFC file
ifc_path = r"C:\Users\ASUS\Downloads\CES_BLD_24_10_ARC.ifc"  # Replace with your actual IFC file path
model = ifcopenshell.open(ifc_path)

# Lists to store glass facades and their properties
glass_facades = []

# Function to check if a material is glass
def is_glass(material):
    if material and material.is_a("IfcMaterial"):
        return material.Name and "glass" in material.Name.lower()
    return False

# Check for curtain walls
curtain_walls = model.by_type("IfcCurtainWall")
for curtain_wall in curtain_walls:
    materials = curtain_wall.HasAssociations
    if any(is_glass(mat) for mat in materials if mat.is_a("IfcRelAssociatesMaterial")):
        glass_facades.append({
            "Type": "Curtain Wall",
            "GlobalId": curtain_wall.GlobalId,
            "Name": curtain_wall.Name,
        })

# Check for windows
windows = model.by_type("IfcWindow")
for window in windows:
    materials = window.HasAssociations
    if any(is_glass(mat) for mat in materials if mat.is_a("IfcRelAssociatesMaterial")):
        glass_facades.append({
            "Type": "Window",
            "GlobalId": window.GlobalId,
            "Name": window.Name,
        })

# Print results
if glass_facades:
    print("Glass Facades Found:")
    for facade in glass_facades:
        print(f"Type: {facade['Type']}, Name: {facade['Name']}, GlobalId: {facade['GlobalId']}")
else:
    print("No glass facades found in the IFC model.")
