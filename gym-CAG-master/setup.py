from setuptools import setup
from setuptools import find_packages

setup(name='gym_CAG',
      version='1.0.0',
      author='HengJie Zhang',
      author_email='707481877@qq.com',
      description='Crazy Arcade game environment for openai/gym',
      packages=find_packages(),
      #url='https://github.com/gpldecha/gym-leftright',
      #license='MIT',
      install_requires=['gym']
)


#package_dir={'gym_leftright' : 'gym_leftright/envs'},
