_`Functional programming in Python`
===================================

_`Abstraction for behaviors`
----------------------------

Object-oriented programming (OOP) is the abstraction for things that have *noun* attribute. Just like biological
classification, scientists use the context *Domain*, *Kingdom*, *Phylum*, *Class*, *Order*, *Family*, and *Genus*
to describe creatures. It is scientifically rigorous, comprehensive, but not such flexible to deal with open set.
(for example to describe a totally new specie which can not been interpreted in this system indeed).

Functional programming (FP) is the abstraction for things that have *verb* attribute. We describe the data without
modification *raw*; we define the process steps for data as *preprocessing*; we called the behaviors of extracting
informative things from data *feature engineering*; we *train* to find the pattern possibly underlying the data.
No matter what investigation in what field we are struggling, we repeat those behaviors step by step, always.

_`Using functions`
------------------

Like many other programming languages, python is also supports multi-paradigm well. The function can be used
as value to pass in, the modified function can be return as a value as well, after which the
:ref:`currying <function currying>` occurs.

.. note::

   The term _`function currying` refers the changes of calling for function with form of :code:`f1(a, b, c)`, into
   the form as :code:`f2(a)(b)(c)`. In modern programming, this architecture is helpful to decoupling our operation
   logic on data. In the last form, :code:`f2(a)` return a function that the behavior :code:`a` is determined; then
   :code:`f2(a)(b)` return the behavior :code:`b` is determined as well; assume the :code:`c` is the data, it is
   clear that data :code:`c` can be processed, if and only if the pre-processes :code:`a` and :code:`b` are pre
   defined.

For building the function with high reusability, here shows some advice:

* make arguments concise when parameterization
* variable-length arguments will make function easy to be extended
* design for call back in where calculation method might vary
* for one-time manipulating, use lambda

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Jun 16, 2023
