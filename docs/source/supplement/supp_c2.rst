_`Informatics primer`
=====================

_`Informatics function`
-----------------------

Informatics function is a derived Python function featured:

* Use keyword arguments exclusively.
* Use :code:`data` as reserved keyword, to accept the data to be processed

In a nutshell, informatics function can theoretically wrap any type of python function. Here shows the examples:

.. code-block:: python
   :caption: informatics function scripting style
   :name: informatics function scripting style

   from info.me import T, F, Null, FuncTools

   def plain_func(a, b=1, *c, **d):  # function define in plain python:
        return a + b + len(c) + len(d)  # a is for data to be processed

   # to wrap plain_func in informatics version
   @FuncTools.attach_attr(info_func=True, entry_tp=..., return_tp=...)  # err here if wrong data inflow and outflow
   def info_func1(**params):
       a, b, c, d = params.get('data'), params.get('b', 1), params.get('c', ()), params.get('d', {})
       return plain_func(a, b, *c, **d)

   # more rigorous, applying type checking and default value assignment
   @FuncTools.params_setting(data=T[Null: ...], b=T[1: int], c=T[(): tuple], d=T[{}: dict])  # err here if wrong args
   @FuncTools.attach_attr(info_func=True, entry_tp=..., return_tp=...)
   def info_func2(**params):
       a, b, c, d = params.get('data'), params.get('b'), params.get('c'), params.get('d')
       return plain_func(a, b, *c, **d)

   # or use lambda for fast wrapping:
   info_func3 = F(lambda **kw: plain_func(kw.get('data'), kw.get('b', 1), *kw.get('c', ()), **kw.get('d', {})))

_`Unit and pipeline`
--------------------

The glue for informatics functions, as well as for unit instance self. With registered informatics function, except
for auto type checking, you can attach it anywhere embedded in your data processing pipeline. Following the example in
:numref:`informatics function scripting style`:

.. code-block:: python
   :caption: use informatics function in unit
   :name: use informatics function in unit

   from info.me import Unit
   u1 = Unit(mappings=[..., plain_func, ...])  # error here due to plain_func
   u2 = Unit(mappings=[info_func1, Unit([info_func2, info_func3], structure='parallel')])  # OK

Unit is an elementary pipeline which cannot be disassembled further. More complicated pipelines can be implemented
based on those elementary units, or on the existing pipelines themselves.

.. code-block:: python
   :caption: combine units into pipeline
   :name: combine units into pipeline

   p1 = u1 >> u2
   p2 = u1 | u2
   p3 = p1 >> (p2 | u1)

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: May 8, 2023