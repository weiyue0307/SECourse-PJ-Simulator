# SECourse-PJ-Simulator
少数派博弈模拟器
    
	这是一个少数派博弈--酒吧问题模拟器

本项目使用面向对象方法完成，语言为python3.6

项目中分为3个对象/类（存放于三个py文件中），分别为：
	
	·环境（play.py）
	
	·参与者（agent.py）
	
	·策略（strategy.py）
	
    主运行程序在play.py文件中，运行之后，命令行串口提示用户输入  总的迭代次数T、参与者的人数n、记忆的长度m、单个策略者的策略个数s：
![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/输入初始值.png)	
    
    考虑到特殊情况，如果用户输入了不符合要求的数据，系统会提示重新输入，并且可以随时退出（后续凡是有输入的地方都会有这些提示和操作）：
![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/错误输入值&退出游戏.png)

    给予初始值之后，用户就可以参与玩耍游戏啦！系统每次会提示让用户选择去还是不去酒吧（输入数字1表示去，数字-1表示不去），用户做出选择之后，系统会给予“Bad Choice！”还是“Good Choice！”的评价，也相当于是对酒吧状态的表明（如：如果用户输入数字1，显示Good Choice！说明酒吧现在为愉悦的）。用户做出几次选择之后，可以选择暂停游戏的进行（输入数字0为暂停游戏），查看相关信息：过去每次选择应选的最佳策略、各个参与者得分情况等，并且同时系统会生成两张图片：每个用户每次的得分情况，酒吧每次的人数。
    
![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/运行.png)

    用户分数（每轮每个人的分数）

![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/用户分数.png)

    酒吧情况（每次的人数）  

![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/酒吧情况.png)

    查看之后可以选择返回游戏（输入数字-2），随时可以输入‘quit’返回游戏。
    
![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/返回游戏&退出游戏.png)
