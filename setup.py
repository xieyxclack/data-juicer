import logging
import os.path
import re

import setuptools


def get_package_dir():
    pkg_dir = {
        'data_juicer.tools': 'tools',
    }
    return pkg_dir


def get_install_requirements(require_f_paths, env_dir='environments'):
    reqs = []
    for path in require_f_paths:
        target_f = os.path.join(env_dir, path)
        if not os.path.exists(target_f):
            logging.warning(f'target file does not exist: {target_f}')
        else:
            with open(target_f, 'r', encoding='utf-8') as fin:
                reqs += [x.strip() for x in fin.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith('#')]
    return reqs


# allowing selective installment based on users' needs
# TODO: The specific taxonomy and dependencies will be determined
#  after implementing some preliminary operators and detailed discussions
min_requires = get_install_requirements(
    ['minimal_requires.txt', 'science_requires.txt'])
extra_requires = {
    'mini':
    min_requires,
    'dev':
    get_install_requirements(['dev_requires.txt']),
    'tools':
    get_install_requirements(
        ['preprocess_requires.txt', 'quality_classifier_requires.txt']),
}
extra_requires['all'] = [v for v in extra_requires.values()]

with open('data_juicer/__init__.py', 'r') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(),
                        re.MULTILINE).group(1)

with open('README.md', encoding='utf-8') as f:
    readme_md = f.read()

setuptools.setup(
    name='data_juicer',
    version=version,
    author='SysML team of Alibaba DAMO Academy',
    description='A Data-Centric Text Processing System for Large Language '
    'Models.',
    long_description=readme_md,
    long_description_content_type='text/markdown',
    license='Apache License 2.0',
    packages=setuptools.find_packages(),
    package_dir=get_package_dir(),
    install_requires=min_requires,
    extras_require=extra_requires,
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
)
