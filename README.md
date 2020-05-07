# Simple_grid_strategy

## Strategy description

Average value: (current bid + current ask) / 2  

Open position: place bid and ask position, if your order has been taken, open the new position and keep the bid_ask position.  

**Notice: This strategy runs in KuMex.** 

**Moreover, KuCoin provides the transaction data of level 3, great matching engine, and the commission discount specially offers to the API customers, which could greatly reduce the disadvantages of the trading operations. At the same time, we offer the sandbox environment as the data testing support to avoid the risks.**

**Only a simple and incomplete trading strategy is provided here, so please pay attention to avoiding risks when using it. Of course, we do not want you to suffer more losses, so please do not directly run it in the actual environment before you have tested it yourself. We do not want you to become a philanthropist! ! !**

**If you want to use the strategy in the actual environment to earn stable profits, we hope that you can make test adjustments in the sandbox environment with other parameters or strategies to enable you to achieve your goals. We also look forward to sharing your test data and Insights.**

**Surely, if you encounter any problems in this process, or you have a profitable strategy to share, please reflect in ISSUE, we will try to respond in a timely manner.**. 

**If you are interested in this strategy, please click the star in the upper right corner, we will  measure the popularity of this strategy and subsequent optimization priorities based on the amounts of stars. You can also click watching in the upper right corner to continue to follow this project by receiving update notifications**.  

## How to use

* After clone this project to your local, install the dependency:

  ```shell script
  pip install python-kumex
  ```

* Paste config.json.example,  rename as config.json, then add the relevant configuration information: 

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
  ./simple_grid.py
  ```

  
