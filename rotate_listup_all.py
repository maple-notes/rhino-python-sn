import rhinoscriptsyntax as rs
import itertools

# List of angles for rotations
y_angle = [0, 90, 180, 270]
x_angle = [0, 45, 90, 135, 225, 270, 315]

# Generate all possible rotations
def generate_rotations():
    return list(itertools.product(y_angle, x_angle))

# Filter out unique rotations to avoid duplicates
def get_unique_rotations(rotations):
    unique_rotations = []
    seen_rotations = set()
    
    for rotation in rotations:
        normalized = tuple(rotation)
        if normalized not in seen_rotations:
            unique_rotations.append(rotation)
            seen_rotations.add(normalized)
    return unique_rotations

# Place modules in a grid with specified rotations
def place_modules_grid(rotations, grid_size):
    # Get the existing module to be used
    module = get_existing_module()
    if not module:
        return
    
    spacing = 5  # Distance between each module

    for i, (y_angle, x_angle) in enumerate(rotations):
        # Copy the module to place in the grid
        module_instance = rs.CopyObject(module)
        if not module_instance:
            continue
        
        # Determine the position in the grid
        row = i // grid_size
        col = i % grid_size
        x = col * spacing
        y = row * spacing
        z = 0

        # Move and rotate the module
        rs.MoveObject(module_instance, (x, y, z))
        centroid = rs.SurfaceAreaCentroid(module_instance)[0]
        rs.RotateObject(module_instance, centroid, y_angle, axis=(0,1,0))
        rs.RotateObject(module_instance, centroid, x_angle, axis=(1,0,0))

# Prompt user to select the existing module in Rhino
def get_existing_module():
    return rs.GetObject("Select the existing module")

# Generate all rotations and filter out unique ones
rotations = generate_rotations()
unique_rotations = get_unique_rotations(rotations)

# Determine the grid size based on the number of unique rotations
grid_size = int(len(unique_rotations) ** 0.5) + 1

# Place the unique modules in the grid
place_modules_grid(unique_rotations, grid_size)
