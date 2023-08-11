import numpy as np
import vedo as vd

# Installation: https://vedo.embl.es/docs/vedo.html#install-and-test

# Template for visualization
# Link to tutorials: https://vedo.embl.es/#quick_start

# How to define a mesh in Vedo

# create a mesh from vertices and faces: 
#   mesh = vd.Mesh([vertices, faces ] ,   c= (color name or RGB (0-1) ), alpha = (opacity 0 - 1)  )
# Read a mesh from obj file:
#   mesh = vd.Mesh( file_path ,  c= (color), alpha = (opacity 0 - 1)  )
# https://vedo.embl.es/docs/vedo/mesh.html#Mesh


# You can also define point clouds 
#   point_cloud = vs.Points( points , r = (point radius in pixels))
# more info: https://vedo.embl.es/docs/vedo/pointcloud.html

# When you want to show into scene you use vd.show( all objects that you defined  )
#  vd.show(mesh, point_cloud)



# Example

# Define the vertices of the cube
vertices = np.array([
    [0, 0, 0],  # Vertex 0
    [1, 0, 0],  # Vertex 1
    [1, 1, 0],  # Vertex 2
    [0, 1, 0],  # Vertex 3
    [0, 0, 1],  # Vertex 4
    [1, 0, 1],  # Vertex 5
    [1, 1, 1],  # Vertex 6
    [0, 1, 1]   # Vertex 7
])

# Define the faces of the cube 
faces = np.array([
    [0, 1, 2, 3],  # Face 0 (bottom)
    [4, 5, 6, 7],  # Face 1 (top)
    [0, 1, 5, 4],  # Face 2 (front)
    [2, 3, 7, 6],  # Face 3 (back)
    [0, 3, 7, 4],  # Face 4 (left)
    [1, 2, 6, 5]   # Face 5 (right)
])

# Random point cloud inside cube
points = np.random.rand(20,3)

# Define cube
cube = vd.Mesh([vertices, faces], c = [0, 0.5, 1], alpha = 0.5)

# Define point cloud
point_cloud = vd.Points(points, c ='red', r = 11)

vd.show(cube, point_cloud)

