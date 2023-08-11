import pandas as pd
from sklearn.decomposition import PCA
import plotly.graph_objects as go
import numpy as np

def PlotWithAxis(id, filename, fig = go.Figure(), Pcolor = 'blue', AColors = ["red", "orange", "pink"]):
        if isinstance(filename, str):
               #   Read File
                df = pd.read_csv(filename, sep= " ", names=['id', 'x', 'y', 'z'])
                df = df.loc[df['id'] == id]
                df = df.drop(['id'], axis=1)
                df

                P = df.to_numpy()
        else:
                P = filename    


        #   Fit PCA components
        pca = PCA(n_components=3)
        pca.fit(P)

        # get center of mass
        mean = np.array(  [np.mean(P[:,0]), np.mean(P[:,1]), np.mean(P[:,2]) ]) 

        #   Compute e-vals and e-vecs, then reescale e-vectors
        evecs = pca.components_
        evals = pca.explained_variance_
        evecs[0] = evals[0] * evecs[0]
        evecs[1] = evals[1] * evecs[1]
        evecs[2] = evals[2] * evecs[2]
    

        #   Plot
        fig.add_trace(  
                go.Scatter3d(x = P[:,0], y = P[:,1],  z = P[:,2],
                mode = 'markers',
                marker_color = Pcolor,
                marker_size = 1.4,
                name = f'Id = {id}') )

        for j in range(3):
                vec = pca.components_[j]
                a, b, c = vec + mean
                x_, y_, z_ = mean        
                fig.add_trace(  
                go.Scatter3d(x = [x_, a], y = [y_, b], z = [z_, c],
                            mode= 'lines', 
                            marker_color = AColors[j],
                            marker_size = 6.0, 
                            name= f'eigenvector {j+1}')  ) 


        fig.update_layout(title= f'Halo Id = {id}')

        return pca.components_, pca.explained_variance_, mean, fig
