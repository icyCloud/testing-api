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

## HTMLTestRunnerCN安装过程
github地址：https://github.com/findyou/HTMLTestRunnerCN
```
cp ../HTMLTestRunnerCN/python2x/HTMLTestRunnerCN.py common/
```
