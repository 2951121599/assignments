## 基于Text-CNN的中文新闻分类
使用[**Keras**](https://keras.io/)和[**TensorFlow**](https://www.tensorflow.org/)搭建中文的新闻分类模型，并在GPU上训练和测试。  
准确率(micro avg)为94.29%，较baseline提升了5.89%。

[dataprep.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/dataprep.py) 原始数据文件的读取、整理和持久化  
[preprocess.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/preprocess.py) 数据预处理  
[models.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/models.py) 模型定义  
[train.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/train.py) 训练模型  
[predict.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/predict.py) 模型推理  
[flask_server.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/flask_server.py) 通过Flask封装API接口进行调用  
[flask_client.py](https://github.com/yang-zhou-x/assignments/blob/master/textCNN_text_classification/flask_client.py) 调用示例，也可以用postman等软件。  
对于新闻文本的预处理包括分词、移除停用词、移除标点符号、移除英文和数字、序列对齐等。  

模型结构：
![textCNN_summary.PNG](https://github.com/yang-zhou-x/assignments/blob/master/others/textCNN_summary2.PNG)

## 数据来源
[THUCNews中文文本数据集](http://thuctc.thunlp.org/#%E4%B8%AD%E6%96%87%E6%96%87%E6%9C%AC%E5%88%86%E7%B1%BB%E6%95%B0%E6%8D%AE%E9%9B%86THUCNews)  
THUCTC(THU Chinese Text Classification)是由清华大学自然语言处理实验室推出的中文文本分类工具包。THUCNews是其根据新浪新闻RSS订阅频道2005~2011年间的历史数据筛选过滤生成，包含74万篇新闻文档（2.19 GB），均为UTF-8纯文本格式。THUCNews包含14个类别：财经、彩票、房产、股票、家居、教育、科技、社会、时尚、时政、体育、星座、游戏、娱乐。[THUCTC工具包](http://thuctc.thunlp.org/)在此数据集上的评测结果为准确率(micro avg)88.4%。

各类别文本长度的均值、最大值、中位数和最小值：  
![seq_len.png](https://github.com/yang-zhou-x/assignments/blob/master/others/THUCNews_len2.PNG)

## 结果对比
THUCTC工具包在THUCNews数据集上的[测试结果](http://thuctc.thunlp.org/#%E6%B5%8B%E8%AF%95%E7%BB%93%E6%9E%9C)(baseline)为：  
![THUCTC_baseline.PNG](https://github.com/yang-zhou-x/assignments/blob/master/others/THUCTC_baseline.PNG)  

本文Text-CNN模型的测试结果（测试集比例为0.2）：  
![clf_report.PNG](https://github.com/yang-zhou-x/assignments/blob/master/others/THUCNews_clf_report2.PNG)

可以看出，本文模型在绝大多数类别上的precision、recall和F1分数都高于THUCTC工具包的结果。综合准确率达到了94.29%（micro avg），提升了5.89%。

预测结果的混淆矩阵如下所示：
![confusion_matrix.png](https://github.com/yang-zhou-x/assignments/blob/master/others/THUCNews_confusion_matrix2.PNG)  

## 环境配置
CUDA==9.2  
cuDNN==7.3.1  
tensorflow-gpu==1.13.1  
keras-gpu==2.2.4  

## 作者
周扬，中国人民大学  
yzhou0000@gmail.com
