_`Anomaly and change`
=====================

In the realm of data analysis, anomaly and change detection play pivotal roles in understanding the behavior of
complex systems. Particularly in dynamic environments, where data patterns and distributions constantly shift,
effective anomaly and change detection becomes crucial techniques and methodologies employed for identifying unusual
patterns and significant variations in datasets.

Anomaly detection aims to identify observations that significantly deviate from the expected patterns or the main
distribution of the data. By employing statistical algorithms, detected outliers can be indicative of errors,
novelties, or can provide valuable insight into the underlying system. Change detection, on the other hand, focuses
on identifying significant changes in the statistical properties or patterns of data over time. Such changes might
indicate system failures, external disturbances, or natural evolution of the system. Change detection techniques
range from simple threshold-based approaches to complex statistical tests and machine learning models, depending
on the nature and complexity of the data.

_`Anomaly detection`
--------------------

The application scopes of anomaly detection, is usually confused from that of binary classification. In fact, many
failures of algorithm in practical tasks are results from the lack of comprehension for the data self, as well as
oversimplification for feature engineering. We mentioned what does :ref:`pattern <Pattern in high dimensional data>`
means in data, in aspect of binary classification task, its precondition for using is that we supposes two groups of
datasets have their respective patterns, and their representations are possibly clustered in high dimension space
individually.

To concrete this abstract concept, imagine two though experiments: training classifiers for distinguishing images of
cat and dog, and for distinguishing images of cat and no cat. For the former, obviously you know what those two
species look like, but for the later, can you image a precise definition for the class *no cat*? A dog can be no cat,
however a book, a pen, a cup can also be *no cat*. Either cat or dog, is narrow concept with explicit definition,
abstraction for these narrow concepts is also the suggested scope for practice of current :ref:`AI <AI>` approaches.
But for *no cat*, it is a comparatively broader concept more than a clear definition.

Thus, for summary using the following :numref:`Figure %s <classification and anomaly>`, the most difference between
binary classification and anomaly determination, is that for binary classification, it actually calculates the most
possible margin between two clusters, however for anomaly determination, it only hypotheses the existence of one
cluster, then using certain approaches to determine tis boundary of this cluster.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/classification_and_anomaly_diff.jpg
   :name: classification and anomaly
   :width: 600
   :align: center

   difference between binary classification and anomaly determination

Make confusion on those two types of tasks seems ridiculous, but take places over and over for many junior data
analysts. They uses classification algorithm frames to train models expected to make distinguishing on *stable*
and *unstable* signals, on *healthy* and *unhealthy* cases, or such like. They integrated expertise, struggled in
dealing with data cleaning and labeling, trained and validated the models. Nevertheless, once observations, with
new patterns in comparison to the ones in their training data, appear, the performance of the models decline, hence
new model is in urgent. All things happen just like an infinite loop.

Therefore, the correct understanding and definition of the problem is a prerequisite and crucial step in
problem-solving. If our analytical task tends to establish patterns on one side, various methods of anomaly
detection will excel in such tasks.

_`Hotelling T-squared`
~~~~~~~~~~~~~~~~~~~~~~

The Hotelling T\ :sup:`2` statistic is a multivariate extension of the :ref:`t-test <Student's T test>`. It is derived
by Harold Hotelling in 1931 to deal with evaluating significance of mean differences between two or more groups of
datasets containing multiple variables (:ref:`[Ramirez1991,<[Ramirez1991]>` :ref:`Holst2011] <[Holst2011]>`).

Criterion distribution is established using multivariate gaussian
:math:`\mathcal{N}(\hat{\boldsymbol{\mu}}, \hat{\boldsymbol{\Sigma}}^{-1})` where the parameter
:math:`\hat{\boldsymbol{\mu}}` and :math:`\hat{\boldsymbol{\Sigma}}^{-1}` are
:ref:`unbiased estimations <unbias estimation>` of mean vector and precision matrix using training data.
For new observation :math:`\boldsymbol{x}^\prime`, define its T\ :sup:`2` statistic as:

.. math::
   :label: T2 statistic

   T^2 = \frac{N-M}{(N+1)M} (\boldsymbol{x}^\prime - \hat{\boldsymbol{\mu}})^T \hat{\boldsymbol{\Sigma}}^{-1}
   (\boldsymbol{x}^\prime - \hat{\boldsymbol{\mu}}) \sim F(M, N-M)

Where :math:`N` is the number of observations, and :math:`M` is the dimensionality.

.. note::

   .. _`unbias estimation`:

   Bias is a concept in parameter estimation in statistics. An essential hypothesis is that we always get samples
   rather than population as our dataset, however we generally want to make some conclusions on population via
   these samples. An identical statistic may differ on population and samples. It called bias in terminology.
   The unbiased estimation is designed in consideration of those impacts in order to reduce the bias of samples
   from population. (e.g. for :math:`n` observations, if they are of population, the denominator of its standard
   deviation is :math:`n`, while if they are of samples from certain population, :math:`n-1`)

_`Naive bayes`
~~~~~~~~~~~~~~

text here

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Apr 2, 2024