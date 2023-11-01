# 北京114预约挂号平台实时刷新工具

### 1. 自主登陆114获取cookie信息

* 114网址：https://www.114yygh.com/

登陆到114之后，自主进行授权操作，登陆后，点击F12进入开发者工具。

![](images/F9D7620F-E6D6-430C-A419-9700181294CC.png)

找到Application选项卡，然后找到cookie为`cmi-user-ticket`的`cookie`，将`Key`和`Value`通过等于号(`=`)拼装起来拼，用于后续操作赋值。

![](images/5DB58EC7-A7AB-4471-9604-D6BD8E718806.png)

### 2. 选择要实时检测的门诊网址

选择自己希望查询的门诊科室，然后复制URL即可，例如：

* https://www.114yygh.com/hospital/126/c1df24b5f98d8dc660112aa1f81f24e4/200000264/source
* https://www.114yygh.com/hospital/122/d3bbb5cb1ac8a26829dd4e23b88f839a/200044316/source
* https://www.114yygh.com/hospital/3/57c6654fe6c60748d71f02ffacfadd1e/200047992/source

必须点击到最细的科室级别，然后复制URL，否则无发进行解析。

![](images/6D65B0A1-8980-4AEF-8596-C4AEB7FB87E4.png)

### 3. 运行py文件

目前分为两种运行模式，用于不同场景：

* (默认) default：静默
* rich：Terminal 高亮

#### 3.1 default 静默模式

![](images/3f1da64e-9a5a-47f5-8ae7-217662fefe79.jpeg)

#### 3.2 rich 高亮模式

![](images/68b47553-99af-47e4-a721-905180ce05e4.jpeg)

### 4. 实时门诊预约状态

![](images/CBB685EF-CAD3-4D94-9EB7-76B0254BB781.png)

### 5. 渠道通知

通过录入钉钉、飞书webhook地址，程序自动发送有号通知提醒。

![](images/img.png)

# 免责声明

此软件程序用于替代人工耗时的检索过程，请勿修改代码中的网站保护策略。知法懂法，请参考[破坏计算机信息系统罪](https://www.66law.cn/zuiming/276.aspx)。
