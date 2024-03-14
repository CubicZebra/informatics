_`Introduction`
===============

_`Installation`
---------------

_`Platforms and options`
~~~~~~~~~~~~~~~~~~~~~~~~

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

.. |ge| unicode:: U+2265

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Apr 25, 2023