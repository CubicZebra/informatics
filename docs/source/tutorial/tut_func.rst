_`Framework in a nutshell`
==========================

.. currentmodule:: info.docfunc

Works in research always want fast verification for some experimental ideas. Nevertheless, those ideas are usually
too prototypical to be implemented in practice. This framework can be deemed as a language intersection between
researcher and engineer: for researchers, it affords abundant enough utilities assisting building their processing
and algorithm flow, while for engineers, it is standardized wrapper for algorithm implementation. As showed in
:numref:`Figure %s <framework objective>`, it contributes to accelerate forming the practicable data processing flow,
from the scientific prototype to engineering practice.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/framework_objective.jpg
   :name: framework objective
   :width: 600
   :align: center

   the bridge between research and practice

_`Featured syntax`
------------------

Framework is featured for relatively unambiguous parameterization design on data processing. Furthermore, type hint
and check, lambda calculus is enhanced in this system in order to fast implement customized computing steps.

_`Arguments predefine and type system`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parameter passing in Python includes positional arguments, optional arguments with default values, var-positional and
`var-keyword <https://docs.python.org/3/glossary.html#term-function>`_ arguments where var means the variable length.
As the illustration in :numref:`dataflow function scripting style`, those passing mechanisms can be equivalently
replaced by var-keyword exclusively. The wrapping function, is the main body of a pipeline in the
:numref:`Figure %s <framework objective>`, while the var-keyword instance, can be deemed as the corresponding config
to change the operational behavior of that pipe.

Pre-definition of default values and type check of argument can refer the example implementation in
:numref:`decorator for parameter setting`. Activating the entry or return type checking controlling can see the
:numref:`decorator to attach documents or execute type checking`.

Design language of function here is mapping: data will be calculated from a certain form to the another.  This
framework separates executing body of function, parameters, and type checking system, for presenting a clear
feeling on this mapping logic.

_`Function based scripting`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In coding practice, a junior implementor might extend lots of branches to satisfy different constraint conditions.
This habit will make the code block difficult to be maintained in the future. Following example shows a pseudo code
with a mass of that indented branches for numeric calculating, type conversion, output control:

.. code-block:: python
   :caption: indentation style in python
   :name: indentation style in python

   res = ...

   if cond1:
       res = res + 2

   if cond2:
       res = int(res)
   elif cond3:
       res = float(res)
   else:
       res = str(res)

   if cond4:
       print(f'Type of current result is {type(res)}.')

Fortunately, applying ternary expression in Python can considerably simplify :numref:`indentation style in python`,
using non-indentation style as:

.. code-block:: python
   :caption: non-indentation style in python
   :name: non-indentation style in python

   res = res + 2 if cond1 else res
   res = int(res) if cond2 else float(res) if cond3 else str(res)
   _ = print(f'Type of current result is {type(res)}.') if cond4 else ...

The magic of non-indentation style is not only compacting code, if use the operator ``:=`` to replace the assigning
operator ``=``, each line in :numref:`non-indentation style in python` will be a hashable object, which can be
included into a mutable object (e.g. list). Therefore, equivalent script on basis of lambda calculus is realizable
as:

.. code-block:: python
   :caption: lambda style of python
   :name: lambda style of python

   f = (lambda x, cond1, cond2, cond3, cond4: [res := x + 2 if cond1 else x,
                                               res := int(res) if cond2 else float(res) if cond3 else str(res),
                                               _ := print(f'Type of current result is {type(res)}.') if cond4 else ...,
                                               res][-1])

The lambda calculus using :py:func:`~info.docfunc.F` is the practice of var-keyword only function superpositioned
with non-indentation style. This programming paradigm is preferred for designing customized processing flow for tasks.

_`Unit of data processing`
--------------------------

The purpose of class :py:func:`~info.docfunc.Unit` using as data processing unit, is four-fold.

_`Packaging units`
~~~~~~~~~~~~~~~~~~

Code styles of plain Python script may vary individually, especially in scientific computation where test and
trials are usually exists. For most researches, people spend amount time, on code construction for data preprocessing.
Therefore, a well-organized form of code should make the previous works (related code implementation) be of high
reusability, then time saving.

Following code shows a workflow for cropping, normalization, and edge sharpening sequentially for 3D images:

.. code-block:: python
   :caption: plain scripting
   :name: plain scripting

    from info.me import tensorn as tsn

    container = []
    for image in images:  # ndarray each case
        res = tsn.cropper(data=image, crop_range=[(.25, .25, .25), (.75, .75, .75)])
        res = tsn.normalization(data=res)
        res = tsn.prewitt_sharpen(data=res, sharp_alpha=0.9)
        container.append(res)

However, plain scripting in that processing flow in ``for`` loop is unstructured. For more compact organization via
dataflow pipeline, it can be implemented as:

.. code-block:: python
   :caption: pipeline scripting
   :name: pipeline scripting

    from info.me import Unit
    from info.me import tensorn as tsn

    processing = Unit(mappings=[tsn.cropper, tsn.normalization, tsn.prewitt_sharpen],
                      crop_range=[(.25, .25, .25), (.75, .75, .75)], sharp_alpha=0.9)
    container = [processing(data=image) for image in images]  # ndarray each case

_`Function wrapper`
~~~~~~~~~~~~~~~~~~~

It is also the wrapper for existed functions (or methods, scripts), after which can either be called as common
function, or a specific step inside data processing pipeline:

.. code-block:: python
   :caption: wrap common function into dataflow function
   :name: wrap common function into dataflow function

    from numpy import ndarray
    from info.me import Unit, F

    def common_function(x: ndarray) -> ndarray:
        ...
        return processed_ndarray

    info_function = F(lambda **kw: common_function(kw.get('data')))  # function wrapper
    info_function_u = Unit(mappings=[info_function])  # unit wrapper

    info_function(data=image)  # either can be called as common function
    info_function_u(data=image)
    p = Unit(mappings=[..., info_function_u, ...])  # or reused in other pipelines

:ref:`Dataflow function <Dataflow function>` is of the form with var-keyword arguments only, which can theoretically
wrap any callable object in Python.

_`Integrate implemented unit or pipeline`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If there's already a dataflow function or unit implemented by someone, it is also handy to integrate that works
into your personal task:

.. code-block:: python
   :caption: use implemented function or unit in your task
   :name: use implemented function or unit in your task

    from implemented_module import data_load_function, data_export_unit  # implemented by others
    from info.me import Unit

    predictor = Unit(mappings=[...])
    task_pipeline = Unit(mappings=[data_load_function, predictor, data_export_unit])

    for image in images:
        task_pipeline(data=image)

Therefore the big significance of the framework is, data can flow seamlessly among functions, in spite of varying
individuals or teams, meanwhile each team can be more focused on the function(s) they are building up.

_`Pipe style code`
~~~~~~~~~~~~~~~~~~

With unit instances, dataflow support pipe coding style, whose form is even as readily comprehensible as plain
description. For instance, image processing steps from cropping, de-noising, resampling, then using two different
method to make augmentation, compare their results, and finally save the compared result can be implemented as:

.. code-block:: python
   :caption: pipe coding style
   :name: pipe coding style

   from info.me import Unit, F, archive
   from info.me import tensorn as tsn

   crop, denoise, resample = [Unit(mappings=_) for _ in [tsn.cropper, tsn.gaussian_filter, tsn.resize]]
   prewitt, canny = [Unit(mappings=_) for _ in [tsn.prewitt_filter, tsn.canny_filter]]
   compare, save = Unit(mappings=[F(lambda **kw: ...)]), Unit(mappings=[archive])

   p = crop >> denoise >> resample >> (prewitt | canny) >> compare >> save  # pipe coding style

The operator :code:`>>` intuitively prompt the data processing units, of before and after steps, while operator
:code:`|` connects the paralleled processing units. When it involved more steps, factors that can affect final result
will increase exponentially. Trial on all possible options using manual configuration sometimes intelligible, but
always make the result mess. However, with this, data processing can be of ease for disassembly or integrating, just
like building lego.

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Feb 8, 2024