from setuptools import setup
from setuptools.command.build_ext import build_ext
import shutil
import glob
import os
import re
sep = os.path.sep
cythonize = __import__('Cython.Build', fromlist=['cythonize']).cythonize


_archive_src = '.' + sep + 'docs'
_build_src = '.' + sep + 'build'
_package_src = '.' + sep + 'info'


def clean_build_folders():
    """clean build and *.egg-info folders before compiling"""
    path = os.getcwd()
    _ = os.listdir(path)
    rm_src = ['build', '*.egg-info', 'docs'+sep+'build']
    _exists = [glob.glob(os.path.join(path, _)) for _ in rm_src]
    exists = [item[0] for item in _exists if len(item) > 0]
    for rm_item in exists:
        shutil.rmtree(rm_item)


def include_documents(source_root, interactive=False):
    res = []
    if 'build' in os.listdir(source_root):
        if 'html' in os.listdir(source_root + sep + 'build'):
            response = input(f"include docs in '{source_root}{sep}build{sep}html' ? [y/n]\n> ") if interactive else 'Y'
            if re.compile(r'\b[y|Y]').match(response) is not None:
                shutil.make_archive(source_root + sep + 'build' + sep + '~doc', 'zip',
                                    source_root + sep + 'build' + sep + 'html')
                res = [source_root + sep + 'build' + sep + '~doc.zip']
    return res


def _cleanup(x):
    for f in x:
        if os.path.exists(f):
            os.remove(f)


def files_searcher(root: str, match_condition: callable):
    for item in os.listdir(root):
        _ = os.path.join(root, item)
        if not os.path.isdir(_):
            if match_condition(_):
                yield _
        else:
            yield from files_searcher(_, match_condition)


def _cythonize(x, call=None, configs=None):
    configs = configs if configs else {'language_level': 3, 'always_allow_keywords': True}
    res = cythonize(x, exclude=['**/__init__.py'], compiler_directives=configs)
    if call:
        call()
    return res


cleanup = (lambda src: [_ext := ('pyd', 3) if os.name == 'nt' else ('so', 2),
                        ext := [_ for _ in files_searcher(src, lambda x: x[-_ext[1]:] == _ext[0])],
                        py := ['.'.join(_.split('.')[:-2])+'.py' for _ in ext], _cleanup(py)])
cleanup_c = (lambda src: [c := [_ for _ in files_searcher(src, lambda x: x[-2:] == '.c')], _cleanup(c)])


class CleanBuildExt(build_ext):
    def run(self):
        super().run()
        cleanup(_build_src)
        cleanup_c(_package_src)


clean_build_folders()
setup(
    requires=['numpy', 'scipy', 'dill', 'tensorly', 'pydicom', 'SimpleITK', 'pyqtgraph', 'pyradiomics', 'pandas'],
    ext_modules=_cythonize(['info/basic/**/*.py']),
    data_files=[('~info', include_documents(_archive_src))],
    cmdclass={'build_ext': CleanBuildExt},
)
_cleanup([_archive_src + '/build/~doc.zip'])


if __name__ == '__main__':
    pass
