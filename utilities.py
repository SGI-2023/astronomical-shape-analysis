import numpy as np
   
def read_obj(file_path):
    # Function that read an obj file and return a list of tuples with information of each cell
    # Output:
    #   meshes .- [(vertices: np.array(n x 3) , faces: list(np.array))]

    # init list to store meshes
    meshes = []

    # Init vertices list
    vertices = []
    # Init faces list
    faces = []

    # Open file
    file = open(file_path, "r")

    # Set prev line read as "v" for initialization
    prev_line = "v"

    # Faces indices corrector
    corr_f = 0

    for line in file:
        # Split line
        split_line = line.split()    

        # Get type of data {v, f}
        actual_line = split_line[0]

        # If actual line is v and pref is f, means we started with a new cell
        if actual_line == "v" and prev_line == "f":

            # Store previous mesh 
            meshes.append((vertices, faces))

            # Update faces indices corrector
            corr_f += len(vertices)

            # Clean vertices and faces
            vertices = []
            faces = []

        # Read vertices
        if actual_line == 'v':
            
            v = np.array(split_line[1:], dtype=float)

            # Update vertices
            vertices.append(v)

            # Update prev state
            prev_line = "v"

        # Read faces
        elif actual_line == 'f':
            
            
            f = np.array(split_line[1:], dtype=int ) - np.ones(len(split_line[1:]), dtype = int)

            # Correct faces indices
            f -= corr_f

            # Update faces
            faces.append(f)

            # Update prev state
            prev_line = "f"

    # Append last set of vertices and faces
    meshes.append((vertices, faces))

    return meshes


def intertia_tensor(points):
    # Compute the inertia tensor for a point cloud
    # for this code we assume that the mass of each point is 1
    # Formulas from: http://www.kwon3d.com/theory/moi/iten.html
    
    # Get x, y, z coordinates for all points
    x, y, z = points[:,0], points[:, 1], points[:, 2]
    
    # Diagonal terms of Inertia tensor
    Ixx = np.sum(x^2 + y^2, axis=0)
    Iyy = np.sum(z^2 + x^2, axis=0)
    Izz = np.sum(x^2 + y^2, axis=0)
    # Off diagonal terms
    Ixy = -np.sum(x*y, axis=0)
    Ixz = -np.sum(x*y, axis=0)
    Iyz = -np.sum(y*z, axis=0)

    # Intertia matrix
    I = np.array([
        [ Ixx, Ixy, Ixz ], 
        [ Ixy, Iyy, Iyz ],
        [ Ixz, Iyz, Izz ] 
        ]   
    )
    
    return I