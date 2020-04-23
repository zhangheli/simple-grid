# 简单网格策略

## 策略说明

均值：（当前最新买盘最高 + 当前最新卖盘最低）/ 2

开仓：在盘口挂出买1和卖1，当你的买单或卖单完成后，再重新开启相应的仓位，保持你始终有买1和卖1的订单

**请注意，该策略是帮你在kumex盘口挂出买1和卖1订单，请不要在实际环境直接使用，否则，你必然会亏钱！**

## 如何使用

* 克隆该策略项目至本地后，安装依赖：
  ```shell script
  pip install python-kumex
  ```

* 复制config.json.example，并重命名为config.json，然后完善相关的配置信息

  ```json
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

  

* 让你的策略运行起来：

  ```shell
  ./simple_grid.py
  ```

  

