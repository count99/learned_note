# css初學筆記
## 三種變更樣式方式
1. css文件引用

		如 <link rel='stylesheet' href='common.css'/>

2. 	&lt;head&gt;中加上&lt;style&gt;編寫

		<style>
			.logo{
			background-color:red;
			}
		</style>

3.  &lt;div&gt;中直接編寫

		如 <div style='background-color:red;'>123</div>
	
## 選擇器
1. class選擇器

		.logo{
		background-color:red;
		}

2. id選擇器
	
		\#logo{
		background-color:red;
		}
		
3. 關聯選擇器

		a div{
		background-color:red;
		}
		
4. 組合選擇器

		a, div{
		background-color:red;
		}
		
5. 屬性選擇器

		input[type='text']{
		background-color:red;
		}
## CSS Box Model

網路上找到的圖

![來自PJCHENder愛分享](https://lh4.googleusercontent.com/proxy/0uOlkHl59TV2fJGKFh_kMh-HaMtceACXzG-U65sRpFA4brHPHyB4YpCwYw_2iLOKnI4JKGBMXvF8A9Qg3fg=s0-d)

> Margin 邊界
> Border 邊框
> Padding 留白

### background

+ background-color
+ background-image
+ background-repeat
+ background-attachment
+ background-position

### display

+ nono 
+ block
+ inline

### cursor
  
> 滑鼠樣式

### float

> 浮動

在網頁顯示原來的子&lt;div>可能在加上float樣式後，蓋過父&lt;div>，可用兩方法解。

1. 加ㄧ新 `<div style='clear:both;></div>`
2. 原父加一class='clearfix'的css樣式

```
.clearfix: after{
	content:" . ";
	display: block;
	height: 0;
	clear: both;
	visibility: hidden;
	}
```
### position

+ fixed
+ absoluate
+ relative

### cpactiy

> 透明度
> 