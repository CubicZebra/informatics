_`Modules for learning`
=======================

.. currentmodule:: info.docfunc

_`Module Bayes`
---------------

Description
-----------

For infrastructure used for Bayesian statistical inference and further constructional components of online or self
adaption featured algorithms, utilize the functions in namespace ``info.toolbox.libs.bayes._frame``, or
alternatively import ``bayes`` from the main entry ``info.me``.

.. autosummary::
   :nosignatures:

   Bayes
   GaussianWishart
   bernoulli
   categorical
   binomial
   multinomial
   poisson
   gaussian

Docstrings
----------

.. autoclass:: Bayes

.. autoclass:: GaussianWishart

.. autodata:: bernoulli
   :no-value:

.. autodata:: categorical
   :no-value:

.. autodata:: binomial
   :no-value:

.. autodata:: multinomial
   :no-value:

.. autodata:: poisson
   :no-value:

.. autodata:: gaussian
   :no-value:

_`Module anomaly`
------------------

Description
-----------

Utilities used for training models for anomaly and change detection. Functions and classes here mainly in
namespace ``info.toolbox.libs.anomaly``. All those objects are also integrated into ``info.me`` as well.

.. autosummary::
   :nosignatures:

   Hotelling
   NaiveBayes
   Neighbors
   VonMisesFisher

Docstrings
----------

.. autoclass:: Hotelling

.. autoclass:: NaiveBayes

.. autoclass:: Neighbors

.. autoclass:: VonMisesFisher

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Apr 23, 2024
