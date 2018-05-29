from setuptools import setup,find_packages

setup(
    name='PD_FC',
    version='1.0',
    description='Data Format Change',
    author='Kwon Hyeoknae & Park Duri',
    author_email='nhk321@naver.com  & twooo.park@gmail.com',
    url='https://github.com/kwonhyucknae/Public_Data_FormatChange',
    download_url='https://github.com/kwonhyucknae/Public_Data_FormatChange/archive/1.0.tar.gz',
    install_requires=[],
    packages=find_packages(exclude = ['docs','tests*']),
    keywords=['Public_Data','Format_Change'],
    python_requires='>=3',
    package_data={
        ''
    },
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6.5'
    ]
    
)
