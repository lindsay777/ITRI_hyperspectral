def returnAPI():
    ori_shape = "(6047048, 272)"
    pca_shape = "(6047048, 3)"
    pca_num = 3
    clus_num = 6
    dtype = "float32"
    exp_var = [0.16969464, 0.01304162, 0.00392883]
    exp_var_ratio = [0.91719973, 0.07048996, 0.02123532]
    kmeans_cluster_center_sum = [ 0.06168981, -0.9825819, 0.42780823, 0.02801337, 0.13503368, 1.1408762]

    result_pca_kmeans = "result_pca_kmeans.jpg"
    result_kmeans = "result_kmeans.jpg"

    labels_pca_kmeans = [807805,1601100,1561091,1234069,731236,111747]
    labels_kmeans = [807805,1598537,1560782,1237208,731091,111625]

    x = [64,32,16]
    y_64 = [807805,1594335,1558548,1243220,731304,111836]
    y_32 = [807805,1601100,1561091,1234069,731236,111747]
    y_16 = [807805,1599172,1560464,1236428,731365,111814]

    return ori_shape,pca_shape,pca_num,clus_num,result_pca_kmeans,result_kmeans,labels_pca_kmeans,labels_kmeans
    