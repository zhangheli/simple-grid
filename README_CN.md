# 简单网格策略

## 策略说明

均值：（当前最新买盘最高 + 当前最新卖盘最低）/ 2

开仓：在盘口挂出买1和卖1，当你的买单或卖单完成后，再重新开启相应的仓位，保持你始终有买1和卖1的订单

**请注意，该策略是在KuMEX盘口挂出买1和卖1订单**。  

**此外，KuCoin拥有level3级别的交易数据、极优的撮合引擎，以及对api用户提供特别的手续费折扣，极大程度的减少了你在策略实施时的劣势，同时提供sandbox环境作为数据测试支撑，帮助你规避风险**。  

**这里仅提供一个简单且不完备的交易策略，所以在使用时请注意规避风险，当然，我们不希望你出现较多的亏损，所以在未经自己亲手测试之前，请千万不要直接在实际环境使用，我们也不想你成为一个慈善家！！！**

**如果你想在实际环境中利用策略获得稳定的盈利，我们希望你能够在sandbox环境配合其他参数或是策略进行测试调整，以使你能够达到目的，我们也非常期待你能分享你的测试数据以及独到的见解。**

**当然，如果这个过程中，你遇到任何问题需要帮助亦或是有赚钱的策略想要分享，请在ISSUE中反映，我们会努力及时响应。**

## 如何使用

* 克隆该策略项目至本地后，安装依赖：

  ```shell script
  pip install python-kumex
  ```

* 复制config.json.example，并重命名为config.json，然后完善相关的配置信息

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

  

* 让你的策略运行起来：

  ```shell
  ./simple_grid.py
  ```

  