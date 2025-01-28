
import openpyscad as ops
import numpy as np

def make_array(unit, x, y, z, repetitions):
    new_union = ops.Union()
    centers = []
    for i in range(repetitions):
        for j in range(repetitions):
            for k in range(repetitions):
                translated_unit = unit.translate([i * x, j * y, k * z])
                new_union.append(translated_unit)
                # Calculating the center of each unit
                center = np.array([i*x+x/2,j*y+y/2,k*z+z/2])
                centers.append(center)
    return new_union, centers

def make_squares(params):
    squares = ops.Union()
    for w, h in params:
        square = ops.Cube([w, w, h])
        squares.append(square)
    return squares

def get_bounding_box(centers):
    min_corner = np.min(centers, axis=0)
    max_corner = np.max(centers, axis=0)
    return min_corner, max_corner

def center_at_origin(union, centers, params):
    min_corner, max_corner = get_bounding_box(centers)
    center = (min_corner + max_corner) / 2
    translation_vector = np.asarray([params[0][0]/4,params[0][0]/4,0]) ### [width/4, width/4, 0]
    centered_union = union.translate(translation_vector.tolist())
    return centered_union, (centers + translation_vector).tolist()

def stack_objects(union_1, union_2, z_offset):
    stacked_union = ops.Union()
    stacked_union.append(union_1)
    stacked_union.append(union_2.translate([0, 0, z_offset]))
    return stacked_union

def match_center(union_1, union_2, centers_1, centers_2):
    matched_union = ops.Union()
    for obj, center_1, center_2 in zip(union_2.children, centers_1, centers_2):
        translation_vector = np.array(center_1) - np.array(center_2)
        new_obj = obj.translate(translation_vector.tolist())
        matched_union.append(new_obj)
    return matched_union

if __name__ == "__main__":
    params = [(50, 0.5), (50, 0.5)]  ### (width, height)
    
    ### Create first layer
    first_layer = make_squares(params)
    x = 200; y = 200; z = 0.5
    repetitions = 2
    first_layer, centers_1 = make_array(first_layer, x, y, z, repetitions)
    
    ### Centering the first layer at the origin
    centered_first_layer, centered_centers_1 = center_at_origin(first_layer, np.array(centers_1))
    
    ### Define parameters for the second layer
    params = [(100, 0.5), (100, 0.5)]
    
    ### Create second layer
    second_layer = make_squares(params)
    second_layer, centers_2 = make_array(second_layer, x, y, z, repetitions)

    ### Center the second layer at the origin
    centered_second_layer, centered_centers_2 = center_at_origin(second_layer, np.array(centers_2), params)

    ### Match centers of the second layer to the first layer
    matched_second_layer = match_center(centered_first_layer, centered_second_layer, centered_centers_1, centered_centers_2)
    
    ### Stack layers
    z_offset = 1  # Adjusted z_offset to match the height of one layer of squares = adding all heights :)
    stacked_layers = stack_objects(centered_first_layer, matched_second_layer, z_offset)

    with open("stacked_layers.scad", "w") as f:
        f.write(stacked_layers.dumps())
