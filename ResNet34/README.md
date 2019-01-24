
# 基于残差网络ResNet34的多角度人脸识别

本文通过建立残差网络ResNet34，对114人的多角度人像进行分类预测，即输入测试图片后返回人物的对应标签。

数据来源：niversity of Ljubljana的Peter Peer。
每个人包含7张照片：左侧脸照、45°照、正面照、135°照、右侧脸照、正面照（不露齿笑）和正面照（露齿笑），极少数存在不足7张或超过7张的情况。

每人随机抽取2张照片进行测试，预测准确率为82.28%。
  
本文的难点在于预测时人像角度的不确定性，如根据正面照来识别侧面照，或是根据侧面照来识别正面照。因此，需要在识别时满足不变性（invariance），包括位置不变性（translation invariance）、选择不变性（rotation invariance）、视角不变性（viewpoint invariance）和大小不变性（size invariance）等。本文使用ResNet34中所包含的大量卷积层（convolution layer）来满足不变性的要求。