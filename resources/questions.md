# Deep RL 训练所需的元素 #
- 动作：参数的修改
- 状态：参数值、力场曲线，或者计算出的属性等
- 回报：误差等
# 需求 #
- 读明白并且解析ReaxFF力场文件（\*.ff），可以使用程序读写
- 可以使用分子动力学软件计算在该力场参数下的各种性质（杨氏模量等）
- 如何更好地描述当前状态
# 需要问的内容 #
- 具体地力场文件参数是什么，哪些比较有价值需要用来参数调节，哪些不需要调节
- 如何构建分子动力学输入文件（所有需要算的属性，如何计算，如何构建，怎么用这些文件）
- 直接提供相关输入文件并且教给我们怎么用更好