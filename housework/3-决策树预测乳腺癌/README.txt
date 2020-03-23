乳腺癌数据集下载于：https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data。

决策数-乳腺癌 代码执行后会生成一个cancertree.dot文件。需要主动将其生成图片。

生成图片方法：
   1.安装graphviz，pip install graphviz，其官网介绍为https://blog.csdn.net/lanchunhui/article/details/49472949。
   2.在cmd中切换到dot文件所在的目录。
   3.生成图片，输入dot -Tpng cancertree.dot -o cancertree.png 。

