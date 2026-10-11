#封装:就是把数据和操作数据的方法放在一起,并对外隐藏内部实现细节,只提供必要的访问方式
"""
私有属性,方法与公共的有什么区别?
私有的只能在类的内部访问,在外部是无法访问的;
而公共的属性,方法在类的内部,外部都是可以访问的.
私有的属性和方法在命名的时候,均以__开头.(python中没有真正的私有机制)
"""


class Car:   #定义一个汽车类
    def __init__(self,name,color,owner):  #初始化品牌,颜色,拥有者
        self.name = name        #品牌(公共属性)
        self.color = color      #颜色(公共属性)
        self.__owner = owner    #拥有者(私有属性)

    def start(self):            #开始(公共方法)
        print(f"一辆{self.color}的{self.name}开始启动")
    def running(self):          #行驶(公共方法)
        print(f"一辆{self.color}的{self.name}正在高速上行驶...")
    def stop(self):             #停止(公共方法)
        print(f"一辆{self.color}的{self.name}开始停止")
    def __control(self):        #控制(私有方法)
        print("发动机启动")
    def get_owner(self):        #获取拥有者信息
        print(f"{self.__owner}")
if __name__ == "__main__":
    c1 = Car("奥迪","白色","张三")
    print(c1.name)
    print(c1.color)
    print(c1._Car__owner)

    c1.start()
    c1.running()
    c1.stop()
    c1._Car__control()
    c1.get_owner()