## 关键词提取

POST:  /analysis/text/keywords

#### >>>接口数据格式：

JSON

#### >>>HTTP请求方式

POST

#### >>>传入参数:

```json
{
	'content': string,
    'top_num': Integer
}
```

##### >>参数说明

| 字段名称 | 字段类型 | 是否必须 | 说明描述                                                     |
| -------- | -------- | -------- | ------------------------------------------------------------ |
| content  | string   | 是       | 可以为中文，不支持英文，编码utf-8                            |
| top_num  | Integer  | 是       | 正整数，不能为其他类型（若是小数、负数、字符串则返回异常信息），数字应大于等于0，小于等于100 |

#### >>>成功返回:

json：

```json
{
	'status': 0,
    'keywords':list<string>		
}
```

##### >>参数说明

| 字段名称 | 字段类型     | 是否必须 | 说明描述                                                     |
| -------- | ------------ | -------- | :----------------------------------------------------------- |
| status   | int          | 是       | 返回状态，成功返回值为0                                      |
| keywords | list<string> | 是       | 返回list<string>格式，包含top_num个关键词（当top_num大于content实际的关键词个数时返回实际的关键词列表），编码utf-8 |

#### >>>失败返回:

json：

```json
{
	'status': 1，
    'message':string
		
}
```

##### >>参数说明

| 字段名称 | 字段类型 | 是否必须 | 说明描述                |
| -------- | -------- | -------- | ----------------------- |
| status   | int      | 是       | 返回状态，失败返回值为1 |
| message  | string   | 是       | 返回失败的信息          |



#### >>>实例:

##### >>正确传入参数：

```json
{
	'content': '深蓝的天空中挂着一轮金黄的圆月，下面是海边的沙地，都种着一望无际的碧绿的西瓜。其间有一个十一二岁的少年，项带银圈，手捏一柄钢叉，向一匹猹尽力地刺去。那猹却将身一扭，反从他的胯下逃走了。这少年便是闰土。我认识他时，也不过十多岁，离现在将有三十年了；那时我的父亲还在世，家景也好，我正是一个少爷。他便对父亲说，可以叫他的儿子闰土来管祭器的。我的父亲允许了；我也很高兴，因为我早听到闰土这名字，而且知道他和我仿佛年纪，闰月生的，五行缺土，所以他的父亲叫他闰土',
    'top_num': 5, 
}
```

##### >>正确返回内容：

```json
{
	'status': 0，
    'keywords':[闰土, 父亲, 便, 知道, 猹]
		
}
```



##### >>错误传入参数：

```json
{
	'content': '深蓝的天空中挂着一轮金黄的圆月，下面是海边的沙地，都种着一望无际的碧绿的西瓜。其间有一个十一二岁的少年，项带银圈，手捏一柄钢叉，向一匹猹尽力地刺去。那猹却将身一扭，反从他的胯下逃走了。这少年便是闰土。我认识他时，也不过十多岁，离现在将有三十年了；那时我的父亲还在世，家景也好，我正是一个少爷。他便对父亲说，可以叫他的儿子闰土来管祭器的。我的父亲允许了；我也很高兴，因为我早听到闰土这名字，而且知道他和我仿佛年纪，闰月生的，五行缺土，所以他的父亲叫他闰土',
    'top_num':-5, 
}
```

##### >>错误返回内容：

json：

```json
{
	'status': 1，
    'message':<异常信息>   
		
}
```

##### 



