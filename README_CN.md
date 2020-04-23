# 简单网格策略

## 策略说明

均值：（当前最新买盘最高 + 当前最新卖盘最低）/ 2

开仓：基于均值挂出买盘最高以及卖盘最低，平仓后再重新开仓

## 如何使用

* 克隆该策略项目至本地后，安装依赖：
  ```shell script
  pip install python-kumex
  ```

* 复制config.json.example，并重命名为config.json，然后完善相关的配置信息

* 让你的策略运行起来：

  ```shell
  ./simple_grid.py
  ```

  