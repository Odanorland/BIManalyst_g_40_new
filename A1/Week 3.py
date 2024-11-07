import bpy

# Dimensions to verify
valid_dimensions = {(0.360, 0.360), (0.420, 0.420), (0.480, 0.480), (0.600, 0.600)}

# Initialize counters
total_columns = 0
invalid_columns = 0

# Loop through all objects in the Blender scene
for obj in bpy.context.scene.objects:
    # Check if the object is a column based on its name
    if "IfcColumn" in obj.name:
        total_columns += 1

        # Switch to object mode to ensure we can access mesh data
        bpy.context.view_layer.objects.active = obj
        bpy.ops.object.mode_set(mode='OBJECT')

        # Get the object's mesh data (bounding box)
        mesh = obj.data

        # Calculate the dimensions from the bounding box (in meters)
        bbox_corners = [obj.matrix_world @ v.co for v in mesh.vertices]
        min_corner = bbox_corners[0]
        max_corner = bbox_corners[0]
        
        for corner in bbox_corners:
            min_corner = [min(min_corner[i], corner[i]) for i in range(3)]
            max_corner = [max(max_corner[i], corner[i]) for i in range(3)]

        # Get width and depth from bounding box (assuming width and depth are in the X and Y axes)
        width = abs(max_corner[0] - min_corner[0])
        depth = abs(max_corner[1] - min_corner[1])

        # Round dimensions to avoid floating-point precision issues
        width_rounded = round(width, 3)
        depth_rounded = round(depth, 3)

        # Check if dimensions match one of the valid sizes
        if (width_rounded, depth_rounded) not in valid_dimensions:
            invalid_columns += 1

# Output the results
print(f"Columns outside the given dimensions: {invalid_columns}")

