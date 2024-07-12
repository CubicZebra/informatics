_`Operations on file search and mapping`
========================================

Most of the analysis occurs on data stored in the file system. The ability to accurately manipulate (primarily loading)
these files is an essential skill. Accurately loading and manipulating files improves the overall efficiency of the
process, as it ensures that the correct data is being used for analysis, reducing the risk of errors and
inconsistencies.

Engineering implementation of file operations requires good understanding of the file structure and format, as well as
size and complexity of the files being analyzed. Large or complex files can pose challenges in terms of processing
power, memory usage, and time required for analysis.

_`Applying generator function`
------------------------------

For persistent inflow data, the cost of memory consuming should be under consideration. :numref:`generator function`
demonstrates the logic to return a iterable container via two different implemented methods. Compare to the case of
:code:`iter2`, :code:`iter1` will increasingly occupy the cache until release after return, which readily results in
memory leak if the scale of :code:`cases` is large enough.

.. code-block:: python
   :caption: generator function
   :name: generator function

   def iter1():
       res = []
       for case in cases:
           res.append(case)
       return res

   def iter2():
       for case in cases:
           yield case

   def iter3():
       return (_ for _ in cases)

   print(all([id(v1) == id(v2) for v1, v2 in zip(iter1(), iter2())]))  # True
   print(all([id(v1) == id(v2) for v1, v2 in zip(iter1(), iter3())]))  # True

Notably, the tuple comprehension in Python will trigger lazy evaluation. In that case a generator object will be
return. From example above, :code:`iter3` can be seem as an another equivalent implementation for :code:`iter2`.

_`File searcher and folder relocation`
--------------------------------------

For universality, interfaces of search or filtering are designed in form of high-order function. Example of
:numref:`file searcher` shows two different pipelines for searching image files with `jpg` or `jpeg` suffix, and
for finding empty files.

.. code-block:: python
   :caption: file searcher
   :name: file searcher

   from info.me import io, Unit
   import os
   p = Unit(mappings=[io.search_from_root])
   p1 = p.shadow(search_condition=lambda x: x[-3:] == 'jpg' or x[-4:] == 'jpeg')
   p2 = p.shadow(search_condition=lambda x: os.stat(x).st_size == 0)

.. sidebar::
   :name: file structure for JPG and BMP

   .. code-block:: none

      --- root
       |--- JPG
       | | --- img_1.jpg
       | | --- ...
       | | --- img_n.jpeg
       |--- BMP
         | --- img_1.bmp
         | --- ...
         | --- img_m.bmp

Occasionally files in identical folder needs some kind of uniformed treatment (like using labels as folder names
for data with different attributes). Under this circumstance, folder relocation can escape redundant operation on
files. Following the :code:`p1` in :numref:`file searcher`, the example implementation in :numref:`folder relocation`
shows an operation of reading images located in different file folders named using file format suffix (as shown in
:ref:`example right side <file structure for JPG and BMP>`).

Those two searchers can both be run, in desktop or hadoop distributed file systems. Refer their documentations
for details.

.. code-block:: python
   :caption: folder relocation
   :name: folder relocation

   p3 = p.shadow(search_condition=lambda x: x[-3:] == 'bmp')
   for f in io.leaf_folders(data='root_path'):
       imgs = p1(data=f) if f[-3:] == 'JPG' else p3(data=f) if f[-3:] == 'BMP' else []

_`Universal data loader`
------------------------

The charm of :ref:`functional programming <Abstraction for behaviors>` is using function to define behaviors. It is of
greater scalability to deal with different dataset. Simple combination and definition can make pipeline be capable for
loading any type of data:

.. code-block:: python
   :caption: meta data loader
   :name: meta data loader

   from info.me import io, Unit
   from PIL import Image
   import nibabel as nib
   import numpy as np
   p = Unit(mappings=[io.search_from_root, io.generic_filter])
   bmp_loader = p.shadow(search_condition=lambda x: x[-3:] == 'bmp', apply_map=lambda x: np.array(Image.open(x)))
   jpg_loader = p.shadow(search_condition=lambda x: x[-3:] == 'jpg', apply_map=lambda x: np.array(Image.open(x)))
   nii_array = p.shadow(search_condition=lambda x: x[-3:] == 'nii' or x[-6:] == 'nii.gz',
                        apply_map=lambda x: nib.load(x).get_fdata().transpose((2, 0, 1)))

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Feb 18, 2024