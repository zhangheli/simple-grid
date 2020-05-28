# 简单网格策略

[![Logo](https://img.shields.io/badge/KuCoin-KuMex-yellowgreen?style=flat-square)](https://github.com/Kucoin-academy/Guide)
[![GitHub stars](https://img.shields.io/github/stars/Kucoin-academy/simple-grid.svg?label=Stars&style=flat-square)](https://github.com/Kucoin-academy/simple-grid)
[![GitHub forks](https://img.shields.io/github/forks/Kucoin-academy/simple-grid.svg?label=Fork&style=flat-square)](https://github.com/Kucoin-academy/simple-grid)
[![GitHub issues](https://img.shields.io/github/issues/Kucoin-academy/simple-grid.svg?label=Issue&style=flat-square)](https://github.com/Kucoin-academy/simple-grid/issues)

[![](https://img.shields.io/badge/lang-English-informational.svg?longCache=true&style=flat-square)](README_EN.md)
[![](https://img.shields.io/badge/lang-Chinese-red.svg?longCache=true&style=flat-square)](README_CN.md)

## 策略说明

均值：（当前最新买盘最高 + 当前最新卖盘最低）/ 2

开仓：在盘口挂出买1和卖1，当你的买单或卖单完成后，再重新开启相应的仓位，保持你始终有买1和卖1的订单

请注意，该策略是在KuMEX盘口挂出买1和卖1订单。  

**KuCoin**拥有**level3交易数据、强大的撮合引擎、针对api用户提供的手续费折扣**，同时提供**sandbox环境**作为数据测试支撑，帮助你规避风险。

我们仅提供一个简单且不完备的交易策略，使用时**请注意规避风险**，我们希望你能够**在sandbox环境配合其他参数或是策略进行测试调整，我们也不想你成为一个慈善家！！！**

当然，如果这个过程中，你遇到任何问题或是有赚钱的策略想要分享，请在**ISSUE**中反映，我们会努力及时响应。

:point_right: 如果你对该策略有兴趣，请点击**右上角star**，我们会根据star数来衡量策略的**受欢迎程度和后续优化优先级**，你也可以点击**右上角watching**通过接收更新通知来持续关注该项目。

## 如何使用

* 安装Python

  * Windows系统请前往[Python](https://www.python.org/downloads/windows/)官网自行安装，64位请选择1，32位请选择2。

    <img src="./img/python_download.png" style="zoom:50%" />

    * 在开始安装时请注意将以下选项勾选：

      <img src="./img/python_win.png" style="zoom:40%" />

  * MAC OS X安装

    * 打开命令终端，输入以下命令安装Homebrew（安装过程中需要输入**电脑密码**）：

      ```shell
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    * 在命令终端输入以下命令，安装Python3：

      ```shell
      brew install python
      ```

    * 在命令终端输入以下命令，确认是否安装成功：

      ```shell
      python3 --version
      ```

      ![](./img/python_version.gif)

* 确保你已经安装git (mac 自带该软件,终端输入`which git`，查看安装位置)，未安装者请前往官网[git](https://git-scm.com/)安装。

* 在命令终端输入以下命令，安装项目依赖：

  ```shell script
  pip3 install python-kumex
  ```

  ![pip_install](./img/pip_install.gif)
  
* 在你需要跑策略的位置新建文件夹（例如桌面），**右键**点击新建的文件夹选择**“新建位于文件夹位置的终端窗口”**（**windows系统**：在右键点击文件夹点击**git Bash here**），在弹出的窗口中输入以下命令，克隆项目至本地，完成后本地会新增文件夹**simple-grid**：
  
  ```shell
  git clone https://github.com/Kucoin-academy/simple-grid.git
  ```
  
  ![git_clone](./img/git_clone.gif)
  
* 打开克隆好的项目（**simple-grid**）文件夹，将**config.json.example**文件重命名为**config.json**，并用文本编辑器（比如**记事本**）打开**config.json**，然后完善相关的配置信息：

  ```
  {
    "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // 是否是沙盒环境  
    "is_sandbox": true,
    // 合约名称，比如：XBTUSDTM 
    "symbol": "contract name",
    // 杠杆倍数，比如：5
    "leverage": "Leverage of the order",
    // 开仓数量，比如：1
    "size": "Order size. Must be a positive number"
  }
  ```

* Mac/Linux **在项目目录下**打开命令终端：

  ```shell
  cd simple-grid
  ```
  * 用以下命令让你的策略运行起来：
  
    ```shell
    ./simple_grid.py
    ```
  
* Windows **在项目目录下**打开命令终端：

  ```shell
  cd simple-grid
  ```
  * 用以下命令让你的策略运行起来：
  
    ```shell
    py simple_grid.py
    ```
  
  

