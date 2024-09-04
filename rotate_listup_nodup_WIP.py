# Still debugging. It doesn't work well.
# I am trying to reduce duplication.

import rhinoscriptsyntax as rs
import itertools
import hashlib

y_angle = [0, 90, 180, 270]
x_angle = [0, 45, 90, 135, 225, 270, 315]

def generate_rotations():
    return list(itertools.product(y_angle, x_angle))

def get_geometry_hash(geometry):
    bbox = rs.BoundingBox(geometry)
    if bbox:
        bbox_points = [(point.X, point.Y, point.Z) for point in bbox]
        bbox_points = sorted(bbox_points)
        hash_value = hashlib.md5(str(bbox_points).encode()).hexdigest()
        return hash_value
    return None

def get_unique_rotations(rotations, module):
    unique_rotations = []
    seen_hashes = set()

    for y_angle, x_angle in rotations:
        module_instance = rs.CopyObject(module)
        if not module_instance:
            continue

        centroid = rs.SurfaceAreaCentroid(module_instance)[0]
        rs.RotateObject(module_instance, centroid, y_angle, axis=(0,1,0))
        rs.RotateObject(module_instance, centroid, x_angle, axis=(1,0,0))

        geom_hash = get_geometry_hash(module_instance)
        if geom_hash:
            print("Checking hash: {}".format(geom_hash)) 
            if geom_hash not in seen_hashes:
                unique_rotations.append((y_angle, x_angle))
                seen_hashes.add(geom_hash)
                print("Added unique rotation: {}".format((y_angle, x_angle))) 
        else:
            print("Failed to get geometry hash")

        rs.DeleteObject(module_instance)

    return unique_rotations

def place_modules_grid(rotations, grid_size):
    module = get_existing_module()
    if not module:
        print("No module selected")
        return
    
    spacing = 5

    for i, (y_angle, x_angle) in enumerate(rotations):
        module_instance = rs.CopyObject(module)
        if not module_instance:
            continue
        
        row = i // grid_size
        col = i % grid_size
        x = col * spacing
        y = row * spacing
        z = 0

        rs.MoveObject(module_instance, (x, y, z))
        centroid = rs.SurfaceAreaCentroid(module_instance)[0]
        rs.RotateObject(module_instance, centroid, y_angle, axis=(0,1,0))
        rs.RotateObject(module_instance, centroid, x_angle, axis=(1,0,0))

def get_existing_module():
    return rs.GetObject("Select the existing module")

module = get_existing_module()

if module:
    rotations = generate_rotations()
    unique_rotations = get_unique_rotations(rotations, module)

    grid_size = int(len(unique_rotations) ** 0.5) + 1
    place_modules_grid(unique_rotations, grid_size)
else:
    print("No module selected")