# Helpers

## 左右对齐

- Align

在`incantation.Module.CSS.Helpers`里，暂时只有关于对齐的API。

```python
from incantation.Module.CSS.Helpers import left_align, right_align, center_align
left_align(obj)  # 将对象设置为右对齐
right_align(obj) # 将对象设置为左对齐
```

- Hover

为对象的class添加`hoverable`可以使其悬浮。

```python
obj.cons_class('hoverable')
```