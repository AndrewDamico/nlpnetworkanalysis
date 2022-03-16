from sklearn.decomposition import PCA


def PCA3D(centroids, k, meta, n=1):
    labels = range(k)
    pca_results = PCA(n_components=3).fit_transform(centroids)
    df = pd.DataFrame()
    df['pca-one'] = pca_results[:,0]
    df['pca-two'] = pca_results[:,1] 
    df['pca-three'] = pca_results[:,2]
    
    
    ax = plt.figure(figsize=(16,10)).gca(projection='3d')
    labels = range(0,k)
    #color = list(labels_color_map)[:k]
    x = df["pca-one"]
    y = df["pca-two"]
    z = df["pca-three"]

    ax.scatter(
        xs = x, 
        ys = y,
        zs = z,
        #c = color,
        s = 500
        #cmap='tab10',
        #hue = labels_color_map
    )
    ax.set_xlabel('pca-one')
    ax.set_ylabel('pca-two')
    ax.set_zlabel('pca-three')

    plt.title(f"NYT Headline k={k} 3 Dimensional PCA Reduction\n{meta}", fontdict=None, loc='center', pad=None, fontsize=18)
    #plt.title(meta, horizontalalignment='right', verticalalignment='bottom', transform=ax.transAxes, fontsize=18)
    plt.savefig(f'images/3d/{n}.png')    
    #return plt.show()
    plt.close('all')
    return

def PCA2D(centroids, k, meta, n=1):
    pca_result = PCA(n_components=2).fit_transform(centroids)
    df = pd.DataFrame()
    df['pca-one'] = pca_result[:,0]
    df['pca-two'] = pca_result[:,1]
    
    
    ax = plt.figure(figsize=(16,10)).gca()
    labels = range(0,k)
    #color = list(labels_color_map)[:k]
    x = df["pca-one"]
    y = df["pca-two"]

    ax.scatter(
        x = x, 
        y = y,
        #c = color,
        s = 500
        #cmap='tab10',
        #hue = labels_color_map
    )
    ax.set_xlabel('pca-one')
    ax.set_ylabel('pca-two')
    ax.triplot(tri.Triangulation(x, y), 'bo-', lw=1)
    plt.title(f"NYT Headline k={k} 2 Dimensional PCA Reduction", fontdict=None, loc='center', pad=None, fontsize=18)
    plt.text(1, 0, meta, horizontalalignment='right', verticalalignment='bottom', transform=ax.transAxes, fontsize=18)
    #plt.plot([1,7,9])
    plt.savefig(f'images/2d/{n}.png')    
    plt.close('all')
    return