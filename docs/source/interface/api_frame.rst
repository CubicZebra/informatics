_`Framework utilities`
======================

.. currentmodule:: info.docfunc

Description
-----------

Utility set of informatics framework for agile development. Functions cover attribute registering, document attaching,
runtime type checking, unit testing, workflow design, building and interface wrapping. For easy importing, all
classes and functions listed here have been integrated into the main entry ``info.me``.

.. autosummary::
   :nosignatures:

   T
   F
   FuncTools
   Unit
   TrialDict
   ExeDict
   SingleMap
   traversal_on_params
   experiments
   functest

And also some meta implementation frameworks for data loading, processing, visualization, analyzing, and exporting,
as well as some code block wrapper for easy develop. Function here mainly in namespace ``info.toolbox.libs.operations``.
All those function are integrated into ``info.me`` as well.

.. autosummary::
   :nosignatures:

   generic_printer
   generic_logger
   exception_logger
   default_param
   diagnosing_tests

Docstrings
----------

.. autoclass:: T

.. autoclass:: F

.. autoclass:: FuncTools

.. autoclass:: Unit

.. autoclass:: TrialDict

.. autoclass:: ExeDict

.. autoclass:: SingleMap

.. autodata:: traversal_on_params
   :no-value:

.. autodata:: experiments
   :no-value:

.. autodata:: functest
   :no-value:

.. autodata:: generic_printer
   :no-value:

.. autodata:: generic_logger
   :no-value:

.. autodata:: exception_logger
   :no-value:

.. autodata:: default_param
   :no-value:

.. autodata:: diagnosing_tests
   :no-value:

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Jun 29, 2023
