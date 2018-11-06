# 比赛网站搭建


## 解决django form 使用cleaned_data字段消失的问题  
**重写clean函数**
```python
def clean(self):
        cleaned_data = super(CheckLoginForm,self).clean()

        return cleaned_data
```