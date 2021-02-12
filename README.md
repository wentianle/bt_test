# KeepAccounts_v2.0
KeepAccounts.exe和其配套表格能够实现微信、支付宝官方导出账单的读取合并，为每笔帐标记类型，并按月份和类型生成可视化图表。再也不用消费一笔记一笔，每月仅需10分钟，记好所有的帐。

作者：	MickLife

Bilibili:	https://space.bilibili.com/38626658

Github:  https://github.com/MickLife/KeepAccounts_v2.0

程序和表格下载链接：https://pan.baidu.com/s/1trgfNS6RuXJwy_NWVSo74Q 提取码：84d3

### v2.0更新内容

1. 利用python脚本编写程序，自动合并微信、支付宝账单，节省了操作时间。
2. 更新记账分类方法，使记账有助于改善你的消费习惯
3. 更新Excel明细页和可视化页，增加数据透视表和数据透视图。
***
# 如何使用

### 第一步 下载账单

**微信账单**    

1. 进入手机版微信，选择 “我”，进入用户中心界面，然后点击 “支付” 选项；
2. 点击 “钱包”，进入钱包界面后，点击右上角的 “账单” 按钮；
3. 点击右上角“常见问题”，点击“下载账单”->“用于个人对账”；
4. 自定义账单时间，然后点击 “下一步”；
5. 填写要导出的邮箱（微信会把账单发送到你填写的邮箱），点击 “下一步”；
6. 输入支付密码，提示申请已提交，微信官方会给你发送一条消息，里面有账单的解压码；
8. 前往你的邮箱下载得到压缩包，用解压码解压得到 .csv 格式微信账单，导出成功。

**支付宝账单**
1. 电脑浏览器中打开支付宝官网 https://www.alipay.com/
2. 点击右上角“客户服务”->“自助服务”；
3. 在“交易服务”中点击“交易记录”一项；
4. 扫码登录；
5. 选择交易时间，并选择下载 excel 格式，得到 .zip 压缩包（其实是 .csv 格式，这是一种更轻便的文本格式）；
6. 解压压缩包得到 .csv 格式的支付宝账单，导出成功。

**备注：**
商家用户请勿从商家中心导出，否则数据格式不同无法使用本程序导入账单。请按以上步骤或切换至个人版页面导出。

### 第二步 运行程序合并账单
1. 将 KeepAccounts_v2.0.zip 解压，推荐解压至 D:\Program Files\；
2. 运行 KeepAccounts_v2.0 目录下的 **KeepAccounts.exe**；
3. 根据提示，依次选择微信 csv 账单、支付宝 csv 账单和账本文件（自动记账2.0_源数据.xlsx）；
4. 程序会自动将微信和支付宝账单合并到你选择的账本文件。
5. 运行成功后按任意键退出。

**备注：**
* 程序会将账单中大部分中性支出、收入（如提现、退款）删除。
* 小部分中性支出、收入会被程序识别，并在逻辑 2 标注 0，乘后金额会显示 0。
* 由于算法的编写由个人完成，不能做到识别所有情况，如果一些中性支出、收入没能自动识别，请手动在源数据表格中将乘后金额改为 0 即可。

### 第三步 补充数据、标记类别
1. 打开“自动记账2.0_源数据.xlsx”；
2. 打开“明细”sheet页，在最后一行追加其他收入和支出数据（如现金、银行卡、校园卡、余额宝等消费情况）；
3. 在最后两列的下拉列表中选择类别；
4. 填写时注意，“月份、乘后金额、类别标记1、类别标记2”为必填项，其他可视情况填写。
5. 追加数据后一定要保存

### 第四步 查看可视化图表
1. 打开“自动记账2.0_可视化.xlsx”前，最好不要关闭源数据表格；
2. 打开“自动记账2.0_可视化.xlsx”；（如果提示各种安全警告和更新链接询问，请点击“允许更新、启用内容”之类的选项）
3. **如果你是第一次打开这个表格，需要更新数据源连接属性。**
    更新步骤：
    
    a. 请选择任意数据透视表中的任意一个单元格，点击“数据透视表工具-分析”选项卡，点击“更新数据源”处的下拉菜单，点击“连接属性”

    b. 在“连接属性”对话框中，点击“定义”选项卡

    c. 点击连接文件路径右侧的“浏览”，定位到表格文件的路径，选择“自动记账2.0_数据源.xlsx”文件，点击确定

    d. 在选择表格的弹窗中选择“明细$”，点击确定；

    e. 点击确定，看到数据自动更新。

4. 查看可视化图表，退出时记得保存。

**备注：**
所有数据透视表、数据透视图中的筛选按钮均可点击，可以根据需求自定义。

***

# Q&A

#### 如何自定义消费类型？
1. 在“自动记账2.0_源数据.xlsx”文件的“消费类型2.0”sheet页修改类别；
2. 消费类别会同步出现在明细页的下拉列表、可视化的数据透视图和透视表中；
3. 第二行编辑后需在“公式”选项卡 - “名称管理器”中同步修改，否则二级下拉列表将失效。

备注：
* 类别名称中勿包含空格、划线、标点符号等特殊字符，会导致bug
* 如果不清楚背后的原理，请在B2:O12区域内编辑，不要新增行列
* 请勿修改明细页的数据有效性公式，因为不使用INDIRECT公式改用直接引用会导致bug，下拉列表消失。
* 如果修改后出现问题，请自行检索关键词，学习有关知识：数据有效性、二级下拉、INDIRECT函数、名称管理器。

#### 打开可视化表格，数据没有更新怎么办？
答：第一次打开这个表格，需要更新数据源连接属性。后续打开时不必每次这样操作。如果你已经更新过连接属性，但数据仍没有更新，请右键数据透视表的任意单元格，点击“更新”。如果这样还是不行，请在数据透视表工具-分析选项卡中，点击刷新下面的小三角，点击“全部刷新”。

#### 追加其他明细内容需要填写所有项吗？
答：“月份、乘后金额、类别标记1、类别标记2”为必填项，其他可视情况填写。

#### 每月导入前需要删除上个月的明细吗？
答：不需要。程序会直接在明细页最后一行后附加新的数据。

#### 第二年可以接着导入吗？
答：不可以，暂时还不支持筛选年份，因为不想增加工作量ㄒ_ㄒ。第二年就把表格copy一份，数据清空当作新表来记录吧！如果你有好的表格设计想法，欢迎私信与我交流呀。

#### 怎么反馈bug或改进意见？
答：欢迎在B站私信 MickLife 反馈，一起携手改变世界！

***
附：Excel自动记账v1.0链接： 【Mick小课堂3】Excel自动化个人记账方案 表格分享
https://www.bilibili.com/video/BV145411Y7Bj 
# bt_test
