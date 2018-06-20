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
    
    考虑到特殊情况，如果用户输入了不符合要求的数据，系统会提示重新输入，并且可以随时退出：
![image](https://github.com/weiyue0307/SECourse-PJ-Simulator/raw/master/Results_Picture/错误输入值&退出游戏.png)
