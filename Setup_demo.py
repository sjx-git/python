''' 1. 编辑setup.py文件  py_modules需指明所需包含的py文件'''
from distutils.core import setup

setup(name="jiaxing", version="1.0", description="jiaxing's module", author="jiaxing", py_modules=['Hello_python.caiquan','*'])

'2.构建模块 python3 Setup_demo.py build'

'3.生成发布压缩包 python setup.py sdist  打包后,生成最终发布压缩包jiaxing-1.0.tar.gz '

'4.安装的方式:' \
'   找到模块的压缩包 ' \
'   解压 ' \
'   进入文件夹 执行命令python setup.py install ' \
'   注意：如果在install的时候，执行目录安装，可以使用python setup.py install --prefix=安装路径'

