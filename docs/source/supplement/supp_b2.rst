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

To concrete this abstract concept, imagine two thought experiments: training classifiers for distinguishing images of
cat and dog, and for distinguishing images of cat and no cat. For the former, obviously you know what those two
species look like, but for the later, can you image a precise definition for the class *no cat*? A dog can be no cat,
however a book, a pen, a cup can also be called *no cat*. Either cat or dog, is narrow concept with explicit
definition, abstraction for these narrow concepts is also the suggested scope for practice of current :ref:`AI <AI>`
approaches. But for *no cat*, it is a comparatively broader concept more than a clear definition.

Thus, for summary using the following :numref:`Figure %s <classification and anomaly>`, the most difference between
binary classification and anomaly determination, is that for binary classification, it actually calculates the most
possible margin between two clusters, however for anomaly determination, it only hypotheses the existence of one
cluster, then using certain approaches to determine the boundary of this cluster.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/classification_and_anomaly_diff.jpg
   :name: classification and anomaly
   :width: 600
   :align: center

   difference between binary classification and anomaly determination

Make confusion on those two types of tasks seems ridiculous, but this mistake takes place over and over on many
junior data analysts. They uses classification algorithm frames to train models expected to make distinguishing
on *stable* and *unstable* signals, on *healthy* and *unhealthy* cases, or such like. They integrated expertise,
struggled in dealing with data cleaning and labeling, trained and validated the models. Nevertheless, once
observations, with new patterns in comparison to the ones embedded in their training data, appear, the performance
of the models decline, hence new model is in urgent. All things happen just like in an infinite loop.

Therefore, the correct understanding and definition of the problem is a prerequisite and crucial step in
problem-solving. If our analytical data tends to establish one side pattern, various methods of anomaly detection
will excel in such tasks.

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

   T^2 = \frac{N-M}{(N+1)M} (\boldsymbol{x}^\prime - \hat{\boldsymbol{\mu}})^\top \hat{\boldsymbol{\Sigma}}^{-1}
   (\boldsymbol{x}^\prime - \hat{\boldsymbol{\mu}}) \sim F(M, N-M)

.. note::

   .. _`unbias estimation`:

   Bias is a concept in parameter estimation in statistics. An essential hypothesis is that we always get samples
   rather than population as our dataset, however we generally want to make some conclusions on population via
   these samples. An identical statistic may differ on population and samples. It called bias in terminology.
   The unbiased estimation is designed in consideration of those impacts in order to reduce the bias of samples
   from population. (e.g. for :math:`n` observations, if they are of population, the denominator of its standard
   deviation is :math:`n`, while if they are of samples from certain population, this value will be :math:`n-1`)

Where :math:`N` is the number of observations, and :math:`M` is the dimensionality. Now consider the condition
:math:`N \geq M` which can be easily achieved through data preparation or dimension reduction, the full rank
property of :math:`\boldsymbol{\Sigma}` can be established. Thus, the item of :math:`(\boldsymbol{x}^\prime -
\hat{\boldsymbol{\mu}})^\top \hat{\boldsymbol{\Sigma}}^{-1} (\boldsymbol{x}^\prime - \hat{\boldsymbol{\mu}})` in
:eq:`T2 statistic` is actually the sum of squares with :math:`M` degree of freedom.

For new variable :math:`z` as function of :math:`z = f(\boldsymbol{x}) \in \mathbb{R}^1`, the Jacobian transformation
is generally used for calculation for its probability mass or density. In this case, the :math:`M`-variate version
of probability density function can be noted as:

.. math::
   :label: Jacobian of probability density function

   q(z) = \int_{-\infty}^{\infty} d\boldsymbol{x} \delta (z-f(x^{(1)}, \dots, x^{(M)})) p(x_1, \dots, x_M)

Where :math:`\delta` is Dirac's delta function. Now we assume there is :math:`M` samples independently derived from
:math:`\mathcal{N}(0, \sigma^2)` noted as :math:`x_1, \dots, x_M`, and a coefficient :math:`c > 0`, the probability
density function of variable :math:`u = c(x_1^2 + x_2^2 + \cdots + x_M^2)` is:

.. math::
   :label: probability density function of u

   q(u) = \int_{-\infty}^{\infty} dx_1 \cdots dx_M \delta (u - c(x_1^2 + \cdots + x_M^2)) \prod_{n=1}^M
   \mathcal{N} (x_n | 0, \sigma^2)

It can utilize the :math:`M`-dimensional spherical coordinates to make simplification for
:eq:`probability density function of u`, the infinitesimal of :math:`dx_1 \cdots dx_M` can be equivalently replaced
by the :math:`dr \cdot r^{M-1}dS_M` (:math:`dr` and :math:`r^{M-1}dS_M` are infinitesimals of thickness, and surface
area in :math:`M`-dimensional sphere respectively). Let :math:`v = cr^2 = c \sum_{i=1}^{M} x_i^2`, :math:`dr` will
be :math:`d(v/c)^{1/2} = (1/2c) \cdot (v/c)^(1/2) dv`, the :eq:`probability density function of u` will be:

.. math::
   :label: integral transformation of u

   q(u) = \int_{0}^{\infty} \frac{dv}{2c} (\frac{v}{c})^{(M/2)-1} \delta (u-v) \frac{1}{(2 \pi
   \sigma^2)^{M/2}} \exp(-\frac{v}{2c\sigma^2}) \int dS_M

For the last item :math:`\int dS_M`, it is the surface area of :math:`M`-dimensional sphere with :math:`r = 1`.
Consider the property of :ref:`high dimensional sphere <high dimensional sphere>`.
:math:`\int S_M` is actually :math:`(2\pi^{M/2})/\Gamma(M/2)`. Because for :math:`\delta` impulse,
:math:`\int dx \delta (x - b) f(x) = \int dx \delta (b - x) = f(b)`, the :eq:`integral transformation of u` can be
finally simplified as :eq:`final simplification of u`:

.. note::

   .. _`high dimensional sphere`:

   For a :math:`K`-dimensional sphere with radius of :math:`R`, its volume is:

   .. math::
      :label: volume of K dimensional sphere

      V_K = \frac{\pi^{\frac{K}{2}}}{\Gamma(\frac{K}{2}+1)} R^K

   Its surface area will be one dimension degenerated as the form of:

   .. math::
      :label: surface of K dimensional sphere

      S_{K-1} = \frac{2 \pi^{\frac{K}{2}}}{\Gamma(\frac{K}{2})} R^{K-1}

.. math::
   :label: final simplification of u

   q(u) &= \int_0^{\infty} dv \delta (u-v) \frac{1}{2c} (\frac{v}{c})^{\frac{M}{2}-1} (2 \pi \sigma^2)^{-\frac{M}{2}}
   \exp (-\frac{v}{2 c \sigma^2}) \frac{2 \pi^{\frac{M}{2}}}{\Gamma(M/2)} \\
   &= \int_0^{\infty} dv \delta (u-v) \frac{1}{2 c \sigma^2 \Gamma(M/2)} (\frac{v}{2 c \sigma^2})^{\frac{M}{2}-1}
   \exp (-\frac{v}{2 c \sigma^2}) \\
   &= \frac{1}{2 c \sigma^2 \Gamma(M/2)} (\frac{u}{2 c \sigma^2})^{\frac{M}{2}-1} \exp (-\frac{u}{2 c \sigma^2})
   \sim \chi^2 (u | M, c \sigma^2)

Here deduced the most important property: the probability density of sum of squares, is come from a certain
:math:`\chi^2` distribution with :math:`M` degrees of freedom, and :math:`c \sigma^2` as scale. For the item
:math:`(\boldsymbol{x}^\prime - \hat{\boldsymbol{\mu}})^\top \hat{\boldsymbol{\Sigma}}^{-1} (\boldsymbol{x}^\prime -
\hat{\boldsymbol{\mu}})`, it uses unbias estimation as standardization while no spatial rescaling for
:math:`\boldsymbol{x}^\prime`, thus :math:`c = \sigma^2 = 1`. Therefore, the final anomaly threshold is determined
through the maximum likelihood estimation of :math:`\chi^2 (x | M, 1)`.

_`Empirical distribution and neighbors`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In spite of concision and lightweight, Hotelling T\ :sup:`2` sometime shows insufficient accuracy due to its
strong assumption on statistical distribution. Once the collected data is not as sufficient to satisfy the
underlying conditions like :math:`F` or :math:`\chi^2` distributions, this method hits possible the ceiling.

Here introduce a :ref:`non-parametric <Parametric and non-parametric>` concept of empirical distribution which
is defined as:

.. math::
   :label: empirical distribution

   p_{\mathrm{emp}} (\boldsymbol{x} | \boldsymbol{x}^{(1)}, \dots, \boldsymbol{x}^{(N)}) = \frac{1}{N} \sum_{n=1}^N
   \delta (\boldsymbol{x} - \boldsymbol{x}^{(n)})

It is a probability density function because for any :math:`\boldsymbol{x} \in \mathbb{R}^M`, its
:math:`p_{\mathrm{emp}}` value in :eq:`empirical distribution` is equal or greater than 1, while
:math:`\int p_{\mathrm{emp}} d\boldsymbol{x} = 1`. For any point :math:`\boldsymbol{x}^\prime \in \mathbb{R}^M`, define
its neighbor a :math:`M`-dimensional sphere with radius :math:`\epsilon`, according to :eq:`volume of K dimensional sphere` its volume will be
:math:`V_M (\boldsymbol{x}^\prime, \epsilon) = (\epsilon^M \pi^{M/2}) / \Gamma(M/2 + 1) = C \cdot \epsilon^M`, where
:math:`C` is an :math:`\epsilon` independent constant.

Therefore in empirical distribution, the probability of that :math:`\boldsymbol{x}^\prime` will be
:math:`p (\boldsymbol{x}^\prime) = k/(N \cdot V_M (\boldsymbol{x}^\prime, \epsilon))`, :math:`k` is the number of
existing data from :math:`x_1` to :math:`x_N` inside the :math:`V_M (\boldsymbol{x}^\prime, \epsilon))` sphere.
The anomaly statistic of :math:`\boldsymbol{x}^\prime` is:

.. math::
   :label: anomaly statistic on empirical distribution

   a(\boldsymbol{x}^\prime) = - \ln p (\boldsymbol{x}^\prime) = - \ln k + M \ln \epsilon + C^\prime

Where :math:`C^\prime` is a constant which independent with :math:`k`, and :math:`\epsilon`. The lower the
:math:`k` in condition of fixed :math:`\epsilon`, or the greater the :math:`\epsilon` in condition of fixed
:math:`k`, the less probability of :math:`\boldsymbol{x}^\prime` as anomalous instance. It is not difficult to
imagine, if we modeled a certain dataset :math:`D = \{\boldsymbol{x}_1, \dots, \boldsymbol{x}_N\}` with almost
normal observations, for given radius :math:`\epsilon`, the more similar data points distributed inside the
:math:`V_M` of a new observation, the higher tendency of no anomaly; while for given :math:`k`, if a new observation
will require greater radius :math:`\epsilon`, it means the higher bias this new observation distributed from
the original :math:`D`, so it is safe to say it, anomaly like.

We can also back the topic to binary classification. If we use :math:`y=0` and :math:`y=1` to label the classes of
normal and anomaly, respectively, the anomaly statistic can be noted as:

.. math::
   :label: anomaly statistic of binary classification

   a (\boldsymbol{x}^\prime) = \ln \frac{p(\boldsymbol{x}^\prime | y=1, D)}{p(\boldsymbol{x}^\prime | y=0, D)}

Consider the bayes formula:

.. math::
   :label: bayes formula in anomaly statistic

   p(\boldsymbol{x}^\prime|y=i, D) = \frac{p(y=i |\boldsymbol{x}^\prime, D) p(\boldsymbol{x}^\prime, D)}{p(y=i, D)}
   = \frac{N^i (\boldsymbol{x}^\prime)}{k} \cdot \frac{1}{\pi^i} \cdot p(\boldsymbol{x}^\prime, D)

The :math:`N^i (\boldsymbol{x}^\prime) / k` corresponds to :math:`p (y=i | \boldsymbol{x}^\prime, D)` that for
:math:`k` neighbors of :math:`\boldsymbol{x}^\prime`, the number of data points in :math:`D` with label of
:math:`y=i`; While the :math:`\pi^i` corresponds to the fraction of :math:`y=i` among total data points. Thus, the
:eq:`anomaly statistic of binary classification` can be further simplified into:

.. math::
   :label: simplification of anomaly statistic of binary classification

   a (\boldsymbol{x}^\prime) = \ln \frac{\pi^0 N^1 (\boldsymbol{x}^\prime)}{\pi^1 N^0 (\boldsymbol{x}^\prime)}

For method using neighbor data points, it requires computing and sort the distance. The distance measure of
neighbor related method is pre-determined. Customarily, people use Euclidean distance in original space
(e.g. for :math:`\boldsymbol{a}` and :math:`\boldsymbol{b}`,
:math:`d^2 (\boldsymbol{a}, \boldsymbol{b}) = (\boldsymbol{a}-\boldsymbol{b})^\top(\boldsymbol{a}-\boldsymbol{b})`).
Or for some algorithm frames, the order of norm has also been designed as an optional callback for distance
measurement. Whatever norm order was defined, the calculation of distance takes places in original Cartesian
coordinate system.

Based on the former discussion, it is cleared how neighbors distributed makes difference on the accuracy of neighbor
related method. Therefore, the performance ceil for this algorithm, depends seldom on norm order, it indeed relies
on whether we can obtain a space, that data points with same labels can as clustered as possible, while ones with
different labels can be separated. From :ref:`previous section <About matrix>` we know the matrix, or transformation
means certain operation(s) on the original (Cartesian) space. Here we introduce the
:ref:`Riemannian metric <Riemannian metric>`, to fulfill that spatial transformation we desired.

.. note::

   .. _`Homeomorphism`:

   .. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/homeomorphism_donut_mug.gif
      :name: homeomorphism joke animation
      :width: 200
      :align: center

      coffee mug as a homeomorphic object of donut :ref:`[Hubbard2012] <[Hubbard2012]>`

   When it comes to the concept *homeomorphism* in topology, a very famous example is the joke about donut and
   coffee mug :ref:`[Hubbard2012] <[Hubbard2012]>`. As it is still little difficult to imagine, it is preferential
   to use *decompression toy* as analogous example: now there is an ideal elastic decompression toy, you can press,
   tense, twist, squeeze it into whatever shape you like. For this toy, although it can possess different shapes
   under varying effects of deformation, these shapes are of *homeomorphic*. While the operations of deformation,
   are conceptually in consistence with the transformation on the original space.

   .. _`Riemannian metric`:

   .. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/deformation_riemannian.jpg
      :name: deformation in riemannian
      :width: 350
      :align: center

      illustration for deformation in Riemannian geometry

   The concept of homeomorphism is of essence to understand Riemannian metric. As illustration in
   :numref:`Figure %s <deformation in riemannian>`, transformation on Riemannian geometry allows local deformation
   anywhere. Imagine all of the data points located on surface of a certain Riemannian geometry (ideal elasticity),
   it can get any desired new distribution of these data points, by introducing a combination of certain
   local deformation operations.

The measure of distance varies from different algorithms. Euclidean defined as :math:`d^2 (\boldsymbol{a},
\boldsymbol{b}) = (\boldsymbol{a} - \boldsymbol{b})^\top\boldsymbol{I}(\boldsymbol{a} - \boldsymbol{b})` can be deem
as the computation in original Cartesian space, while the anomaly statistic mentioned in :ref:`Hotelling T-squared
<Hotelling T-squared>` is equivalent of using a rescaled Cartesian space via :math:`\hat{\boldsymbol{\Sigma}}^{-1}`.
More generally, it can define a Riemannian space :math:`\boldsymbol{R}` that the corresponding distance measure is
:math:`d^2_{\boldsymbol{R}} (\boldsymbol{a}, \boldsymbol{b}) = (\boldsymbol{a} - \boldsymbol{b})^\top
\boldsymbol{R} (\boldsymbol{a} - \boldsymbol{b})`. How to determine an optimal Riemannian
metric :math:`\boldsymbol{R}` so that data points with identical labels can be clustered, while different clusters
can be as separated as possible (like the illustration in :numref:`Figure %s <deformation in riemannian>`), is the
scope of a sub field in machine learning, called *metric learning*.

For more generic solution, we can discuss this problem in frame of multi classification so that it is rational to
assume a prior weights for all categories, and the prior weight for peers of :math:`y = y^{(n)}` is :math:`w_{(n)}`.
Focus on a certain :math:`\boldsymbol{x}^{(n)}` in :eq:`empirical distribution` with label :math:`y = y^{(n)}`,
define the set :math:`N^{(n)}` the points with identical label as :math:`\boldsymbol{x}^{(n)}`, among :math:`k`-nearest
neighbors of :math:`\boldsymbol{x}^{(n)}`, the mathematical expression for concept *data points with identical
labels can be clustered*, can be represented as:

.. math::
   :label: Riemannian item 1

   \psi_1^{(n)} (\boldsymbol{R}) = \sum_{i \in N^{(n)}} d_{\boldsymbol{R}}^2 (\boldsymbol{x}^{(n)},
   \boldsymbol{x}^{(i)})

While for the concept *different clusters can be as separated as possible*:

.. math::
   :label: Riemannian item 2

   \psi_2^{(n)} (\boldsymbol{R}) = \sum_{j \in N^{(n)}} \sum_{l=1}^N I_{y^{(l)} \neq y^{(n)}}(y^{(l)}) \left[ 1 +
   d^2_{\boldsymbol{R}} (\boldsymbol{x}^{(n)}, \boldsymbol{x}^{(j)}) -  d^2_{\boldsymbol{R}} (\boldsymbol{x}^{(n)},
   \boldsymbol{x}^{(l)}) \right]_{+}

The item :math:`\boldsymbol{x}^{(j)}` and :math:`\boldsymbol{x}^{(l)}` in :eq:`Riemannian item 2` are the data
points, with and without identical label as :math:`\boldsymbol{x}^{(n)}` respectively. Assume the set of labels
:math:`C = {1, \dots, s}` represents for :math:`s` different classes, the optimization target of Riemannian
:math:`\boldsymbol{R}` is:

.. math::
   :label: Riemannian optimization

   \Psi (\boldsymbol{R}) = \frac{1}{N} \sum_{c=1}^s \sum_{n=1}^N \left[ w_c \cdot \psi_1^{(n)} (\boldsymbol{R}) +
   \sum_{m \in \{c\}^C} w_m \cdot \psi_2^{(n)} (\boldsymbol{R}) \right] \quad \mathrm{s.t.} \> \boldsymbol{R} \succeq 0

The constraint :math:`\boldsymbol{R} \succeq 0` is for semi-positive definite matrix. Therefore set the eigen
value(s) as 0, if negative value dimension(s) were calculated during learning steps. :math:`\{c\}^C` is the
complementary set of :math:`c` in :math:`C`. Metric learning updates the :math:`\boldsymbol{R}` using subgradient
via the item :math:`\partial \Psi (\boldsymbol{R}) / \partial \boldsymbol{R}` until convergence. Using decomposition
on the updated Riemannian metric :math:`\boldsymbol{R}^* = \boldsymbol{L}^\top \boldsymbol{L}`, the distance measure in
Riemannian space is therefore :math:`(\boldsymbol{a} - \boldsymbol{b})^\top \boldsymbol{R}^* (\boldsymbol{a} -
\boldsymbol{b}) = [\boldsymbol{L}(\boldsymbol{a} - \boldsymbol{b})]^\top [\boldsymbol{L}(\boldsymbol{a} -
\boldsymbol{b})]`. Thus, the relationship between original space and the final Riemannian space is nothing other
than the transformation :math:`\boldsymbol{L}`.

_`Bayesian and mixture Gaussian`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

text here

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Apr 2, 2024