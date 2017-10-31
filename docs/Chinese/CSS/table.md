# Table

在[grid](./grid.md)章节我们已经写过一些table了。  
比如，这是一行内嵌入两个table。
[![4-8 Split](./Grid48.PNG)](./Grid48.PNG)
其中的每一个`table`对象，都是
```python
from incantation.Module.CSS.Table import table

table_example = table(["A","B","C"],
                          [[1,2,3],
                           [2,3,4],
                           [5,6,7]
                          ]).cons_class('striped')
```

`cons_class`这个方法表示，为对象的`class`属性在首部添加一些值。
根据所添加的`class`属性的不同, 表格将呈现不同的效果。
请直接查看materialize-css的文档[Table](http://materializecss.com/table.html)


