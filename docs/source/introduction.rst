_`Introduction`
===============

_`Installation`
---------------

_`Platforms and options`
~~~~~~~~~~~~~~~~~~~~~~~~

.. |ge| unicode:: U+2265

:code:`informatics` is officially support the following desktop platforms:

* Windows

* Linux

* MacOS

Ensure Python (|ge| 3.9) is installed. Install :code:`informatics` via pip-based installer as appropriate:

.. tab:: Basic

   Install :code:`informatics` with basic dependent components.

   .. code-block:: console

      (.venv) $ pip install informatics

.. tab:: Instances

   Install basic :code:`informatics` with instance data.

   .. code-block:: console

      (.venv) $ pip install informatics[ins]

.. tab:: Visualization

   Install basic :code:`informatics` with visualization dependencies. Backend of visualization utilities requires at
   least one of `PySide2 <https://pypi.org/project/PySide2/>`_, `PySide6 <https://pypi.org/project/PySide6/>`_,
   `PyQt5 <https://pypi.org/project/PyQt5/>`_, `PyQt6 <https://pypi.org/project/PyQt6/>`_.
   `PySide6 <https://pypi.org/project/PySide6/>`_ is suggested. For functions who using spatial rendering,
   `PyOpenGL <https://pypi.org/project/PyOpenGL/>`_ is necessary as well.

   .. code-block:: console

      (.venv) $ pip install informatics[vis]

.. tab:: Medical

   Install basic :code:`informatics` with medical image related dependencies.

   .. code-block:: console

      (.venv) $ pip install informatics[med]

.. tab:: Networks

   Install basic :code:`informatics` with configurable neural network with dynamic architecture. For normal use,
   :code:`torch` is required.

   .. code-block:: console

      (.venv) $ pip install informatics[net]

_`Check installation`
~~~~~~~~~~~~~~~~~~~~~

To check whether :code:`informatics` was installed, run following code in Python or command line shell:

.. tab:: Python

   .. code-block:: python

      import info
      print(info.__version__)

.. tab:: Terminal

   .. code-block:: console

      (.venv) $ python -c "import info; print(info.__version__)"

Version number will in the prompt if :code:`informatics` has been properly installed, otherwise error message.

_`Upgrade for options`
~~~~~~~~~~~~~~~~~~~~~~

Default installation only consist of basic component. If optional dependencies are required to be activated, re do
the pip installer with its `identifier <https://peps.python.org/pep-0685/>`_ (e.g.
:code:`pip install informatics[ins] informatics[vis]` for integrating instance data and visualization tools, whether
basic :code:`informatics` was installed already or not). Notably, the local version must keep the identical as one
of remote.

Or alternatively, using pip installer to install missing module(s) when :code:`ImportError` raised in the prompt.

_`Overview`
-----------

Informatics is designed to enable users to solve complex problems in science, engineering, and other domains
efficiently and accurately. Its powerful capabilities are achieved through a combination of cutting-edge software
engineering techniques and the elegance of Python's functional programming paradigm. The strength of highly modular
and extensible architecture allows users to quickly assemble and customize data processing pipelines to meet their
specific needs. Whether it's data cleaning, transformation, analysis, or visualization, informatics provides a rich
set of tools and functions to facilitate these tasks.

It is in active development, in order to satisfy increasing requests in scientific computation.

_`Featured as`
~~~~~~~~~~~~~~

Informatics is currently featured:

* Powerful integration capability for various utilities (e.g. functions, frames, packages, and etc.) in Python
  ecosystem.

* Universal processing interface designed in high dimensionality to guarantee consistency of calling for different
  types of data.

* Scripting on basis of functional programming paradigm, with properties of robust performance, and easy decoupling
  for extension.

* Intuitive combination of data processing units, for fast experiments, validation, or building for upper
  applications.

* Documentation in details for not only basic functions, but the tutorials, interpretation for essential concepts,
  examples of applications, and such like.

_`Simple examples`
~~~~~~~~~~~~~~~~~~

Critical structure called :py:func:`~info.docfunc.Unit` can wrap any of the callable object in Python. Data processing
can be implemented via :ref:`functional programming scripting <Function based scripting>`. Therefore with various
units (e.g. :code:`u1`, :code:`u2` with different arguments), it is able to combine them as desired:

.. code-block:: python
   :caption: example of unit combination
   :name: example of unit combination

   p = u1 >> u2

Auto test the pipe :code:`p` for determining its optimal argument combination:

.. code-block:: python
   :caption: example of auto test
   :name: example of auto test

   param_options = {
       'u1_arg1': [...],
       'u1_arg2': [...],
       ...,
       'u2_arg4': [...],
       'u2_arg5': [...],
   }

   functest(data=p, params_pool=param_options)

Or apply that pipe, as well as its optimal argument configuration from (or to) others' works:

.. code-block:: python
   :caption: example of reuse pipe
   :name: example of reuse pipe

   from other_libs import pipe, opt_config
   my_unit = ...
   my_pipe = pipe.shadow(**opt_config) >> my_unit

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Apr 25, 2023