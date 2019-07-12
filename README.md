## boke项目
---
### 目标实现简易博客系统

>今日任务目标:
- 1.结构设计
- 2.MVC设计
- 3.静态页面返回

目录设计
* model.py
* route.py
* handlers.py
* configs
* status
 * css
 * js
* main.py

```python
    """
    PS:
        用户自动登陆在中间件处理
        通过判断cookies,request[__user__]=json_response
        在具体的接口内判断user
        在中间件处理

    """
```
