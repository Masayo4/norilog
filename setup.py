from setuptools import setup, find_packages

setup(
    name='norilog',#プロジェクトnameと同じにする
    version = '1.0.0',#文字列
    packages = find_packages(),#パッケージを全て取ってきてくれる関数
    include_package_data = True,#templatesとstaticをパッケージとしてインストールする
    install_requires =[
        'Flask',
    ],
    entry_points="""
        [console_scripts]
        norilog = norilog:main
    """,
    )
