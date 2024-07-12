_`Misc modules and functions`
=============================

.. currentmodule:: info.docfunc

_`Kernel related utilities`
---------------------------

Description
~~~~~~~~~~~

Kernel generator using for multipurpose such as de-noising, filtering, local feature capturing, and etc. Advanced
constructor tool applied for highly customized numerical computing. Or kernel related utilities.

Tensor kernel generator module in informatics. Location in ``info.toolbox.libs._basic``. Also can import through
``from info.me import kernel_utils``.

.. autosummary::
   :nosignatures:

   KernelGen
   averaging_kernel
   gaussian_kernel
   laplacian_of_gaussian_kernel
   gabor_kernel

Docstrings
~~~~~~~~~~

.. autoclass:: KernelGen

.. autodata:: averaging_kernel
   :no-value:

.. autodata:: gaussian_kernel
   :no-value:

.. autodata:: laplacian_of_gaussian_kernel
   :no-value:

.. autodata:: gabor_kernel
   :no-value:

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Jun 28, 2023
