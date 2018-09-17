# testing-api
基于unittest + HTMLTestRunner的API自动化测试报告

## 启动
```
vim config.ini
[runner]
RUNNER_URL=http://api.com
RUNNER_PTAH=./reports/testing-api.html
RUNNER_TITLE=API自动化测试报告
RUNNER_DESCRIPTION=详细测试用例结果
RUNNER_TESTER=demo

python start.py
```

## HTMLTestRunnerCN
#### 安装
```
git clone https://github.com/ganodermaking/testing-api.git
git clone https://github.com/findyou/HTMLTestRunnerCN
cd testing-api/common/
cp ../HTMLTestRunnerCN/python2x/HTMLTestRunnerCN.py common/
```

#### setUpClass方法
测试用例们被执行前执行的方法

#### setUp方法
在执行每个测试用例之前被执行，任何异常（除了unittest.SkipTest和AssertionError异常以外）都会当做是error而不是failure，且会终止当前测试用例的执行。

#### tearDown方法
执行了setUp()方法后，不论测试用例执行是否成功，都执行tearDown()方法。如果tearDown()的代码有异常(除了unittest.SkipTest和AssertionError异常以外)，会多算一个error。

#### tearDownClass方法
测试用例被执行后执行的方法
