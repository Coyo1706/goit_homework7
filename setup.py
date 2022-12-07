from setuptools import setup, find_namespace_packages

setup(
    name='clean-folder',
    version='0.9.1',
    description='Files sorter by category',
    author='Artem Pryshva',
    author_email='artemprishva@gmail.com',
    url='https://github.com/Coyo1706/sorted_files.py.git',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean-folder=clean_folder.clean:sort']}

)