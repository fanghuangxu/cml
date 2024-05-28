# setup.py

from setuptools import setup, find_packages

setup(
    name='china_minecraft_launcher',
    version='0.1.0',
    author='fanghuangxu',
    author_email='fanghuangxu@163.com',
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    url='https://github.com/fanghuangxu/china-minecraft-launcher',
    license='LICENSE.txt',
    description='This is a library to launch minecraft',
    long_description=\
'''
zh:这是一个启动minecraft的库
en:This is a library to launch minecraft
''',
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.7',
)
