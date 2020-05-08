# Simple_grid_strategy

[![Logo](https://img.shields.io/badge/KuCoin-KuMex-yellowgreen?style=flat-square)](https://github.com/Kucoin-academy/Guide)
[![GitHub stars](https://img.shields.io/github/stars/Kucoin-academy/simple-grid.svg?label=Stars&style=flat-square)](https://github.com/Kucoin-academy/simple-grid)
[![GitHub forks](https://img.shields.io/github/forks/Kucoin-academy/simple-grid.svg?label=Fork&style=flat-square)](https://github.com/Kucoin-academy/simple-grid)
[![GitHub issues](https://img.shields.io/github/issues/Kucoin-academy/simple-grid.svg?label=Issue&style=flat-square)](https://github.com/Kucoin-academy/simple-grid/issues)

[![](https://img.shields.io/badge/lang-English-informational.svg?longCache=true&style=flat-square)](README.md)
[![](https://img.shields.io/badge/lang-Chinese-red.svg?longCache=true&style=flat-square)](README_CN.md)

## Strategy description

Average value: (current bid + current ask) / 2  

Open position: place bid and ask position, if your order has been taken, open the new position and keep the bid_ask position.  

Notice: This strategy runs in KuMex.  

**KuCoin** provides **the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers**. At the same time, we offer the **sandbox environment** as the data testing support to avoid the risks.

Only a simple and incomplete trading strategy is provided here, so please pay attention to **avoiding risks** when using it. We hope that you can **make test adjustments in the sandbox environment with other parameters or strategies,  as we do not want you to become a philanthropist! ! !**

Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in **ISSUE**, we will try to respond in a timely manner. 

:point_right: If you are interested in this strategy, please click **the star in the upper right corner**, we will  measure **the popularity of this strategy and subsequent optimization prioritie**s based on the amounts of stars. You can also click **watching in the upper right corner** to continue to follow this project by receiving update notifications.  

## How to use

* Download [Python](https://www.python.org/)

  * For MAC OS

    * Download [Homebrew](http://brew.sh/)：

      
      ```shell
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
      ```

    * Download [Python3](https://www.python.org/)：

    ```shell
    brew install python
    ```

    * Confirm if you download successfully:

    ```shell
    python --version
    ```

    ​	   if the return code is **3.7...or newer version** means you have already downloaded successfully.

  * Please download python in [Python](https://www.python.org/) official website for other system requirement.

* Confirm that you have already downloaded [git](https://git-scm.com/), open command terminal or git GUIs, clone this project to your local:

  ```shell
  git clone https://github.com/Kucoin-academy/simple-grid.git
  ```

  ![git_clone](./img/git_clone.gif)

* Install the dependency:

  ```shell script
  pip install python-kumex
  ```

  ![pip_install](./img/pip_install.gif)
  
* Open the project you have cloned, paste config.json.example,  rename as config.json

* Using text editor to open config.json, then add the relevant configuration information: 

  ```
  {
   "api_key": "api key",
    "api_secret": "api secret",
    "api_passphrase": "api pass phrase",
    // if sandbox  
    "is_sandbox": true,
    // contract name, e.g.:XBTUSDTM 
    "symbol": "contract name",
    // leverage, e.g.:5
    "leverage": "Leverage of the order",
    // order size, e.g.:1
    "size": "Order size. Must be a positive number"
  }
  ```

* Run your strategy:

  ```shell
  cd simple_grid
  ./simple_grid.py
  ```

