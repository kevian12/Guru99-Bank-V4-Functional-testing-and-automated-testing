# Guru99 Bank V4 - 功能测试与自动化测试项目

## 项目概述
对在线银行系统（Guru99 Bank V4）进行系统性功能测试，设计测试用例并基于 Selenium + pytest 实现自动化测试框架。

## 项目成果
- **测试用例**：设计 **136条** 功能测试用例，覆盖 16 个功能模块
- **自动化脚本**：实现 **77条** 自动化测试用例（15个模块），采用 Page Object Model 设计模式
- **测试框架**：基于 Selenium WebDriver + pytest + webdriver-manager，支持 Edge 浏览器

## 覆盖的模块
| 模块 | 测试用例数 | 自动化数 | 说明 |
|------|-----------|---------|------|
| 登录模块 | 10 | 10 | 正常/异常登录、输入验证、SQL注入 |
| 新建客户 | 20 | 7 | 客户注册、字段级校验（名称/地址/PIN/手机号/邮箱） |
| 编辑/删除客户 | 18 | 9 | 客户信息维护、确认弹窗处理 |
| 账户管理 | 22 | 13 | 开户（储蓄/活期）、账户编辑、删除 |
| 交易模块 | 30 | 20 | 存款、取款、转账、余额校验 |
| 查询模块 | 20 | 9 | 余额查询、Mini Statement、定制化报表 |
| 密码管理 | 10 | 6 | 密码修改、新旧密码校验 |
| 其他 | 6 | 3 | 导航菜单、页面跳转 |

## 技术栈
- Python 3.12
- Selenium WebDriver 4.46
- pytest 9.1
- webdriver-manager（自动管理浏览器驱动）
- Page Object Model 设计模式
- openpyxl（测试用例管理）

## 快速开始
```bash
pip install selenium pytest webdriver-manager openpyxl
cd root/A_selenium_test
python -m pytest tests/ -v
```
