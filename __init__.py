'''
一个包下，必须有此方法 在别的地方才可以导入这个包，即便此方法是空的，但是也仅仅是允许导入包，它下面的模块却是不能用的；
若是想用，那么就要用到 __all__ = ['模块名']；或者 from . import 模块名---这两有点麻烦；
发布模块，作用相当于系统内置模块 是在所有地方都可用，不用再用all啥的写明，见setup文件内容
'''
"""__all__ = []
from . import caiquan"""

