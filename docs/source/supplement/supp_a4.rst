_`Mathematical statistics`
==========================

_`Probability distribution`
---------------------------

At-least required concepts for properly using statistical analysis.

_`Parameters`
~~~~~~~~~~~~~

.. index:: single: distribution parameter
           single: parameter estimation

Most of probabilities, discrete or continuous ones, can be uniquely described using several numbers. Those
numbers are commonly expressed by Greek letter. These numbers are called parameters of distribution. For examples,
uni-variate gaussian is expressed as :math:`\mathcal{N}(\mu, \sigma)`, beta distribution is expressed as
:math:`\mathrm{Beta}(\alpha, \beta)`.

Generally, those numbers are unknown variate. Customarily it uses hat :math:`\hat{a}` as example, to describe a
certain calculation rule to obtained approximated result for the parameter :math:`a` from some data points (samples).
Or in terminology, *parameter estimation*. As example, we assume some data sampled from a certain uni-variate
gaussian :math:`\mathcal{N}(\mu, \sigma)`, the parameter :math:`\mu` is actually unknown, however, we can estimate via
:math:`\hat{\mu} = (\sum_{i=1}^n x_i)/n`.

_`Kernel and scale`
~~~~~~~~~~~~~~~~~~~

.. index:: single: probability mass function
           single: probability density function
           single: distribution kernel
           single: distribution scale

For functions which can analytically express distributions, we call them *probability mass function* (in discrete
case) or *probability density function* (in continuous case). Those functions can be factorized as several multiplied
items. The minimal item which contains variable and all of required parameters of distributions, we call it *kernel*.
The *scale* refers the parameters in no-kernel items. For instance, the probability density function of uni-variate
gaussian is:

.. math::
   :label: pdf of uni-variate gaussian

   f(x|\mu,\sigma) = \frac{1}{\sqrt{2\pi}\sigma} \exp{[-\frac{(x-\mu)^2}{\sigma^2}]}

The kernel item :math:`k = \exp{[-(x-\mu)^2/\sigma^2]}` contains :math:`x`, :math:`\mu` and :math:`\sigma`. And
for item :math:`s = \frac{1}{\sqrt{2\pi}\sigma}`, it only contains parameter :math:`\sigma`, therefore :math:`\sigma`
is also called the scale of uni-variate gaussian.

Additionally, it is unnecessary for :math:`k = k(x)` to guarantee its sum or integral as 1. But for :math:`s \cdot k`,
:math:`\sum_{i} s \cdot k \cdot x_i = 1` or :math:`\int_{x} s \cdot k dx = 1` should be ensured.

_`Parametric and non-parametric`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In statistics, there is a system with strong assumption relying on probability distribution, called *parametric*
methods in terminology. We *believe* the data sourced from a uni-variate gaussian :math:`\mathcal{N}(\mu, \sigma)`,
therefore we use :math:`\hat{\mu} = \mathbb{E}[X]` and :math:`\hat{\sigma^2} = \mathbb{E}[X^2] - (\mathbb{E}[X])^2`
to make estimation. It works well unless the priori belief is actually guaranteed.

*Non-parametric*, correspondingly, is the method to focus the rank of values, rather than the values themselves.
Considering sets with two treatments :math:`A = \{1, 2, 3, 4, 5\}` and :math:`B = \{1, 2, 3, 4, 5000\}`,
with parametric methods it can simplistically report some misleading information such as the treatment :math:`B` can
significantly improve something, or whatever, due to its mean value is totally different. However, if we use median,
the non-parametric version for mean, it will result in a opposite conclusion.

.. epigraph::

   Data does not lie. People do.

   -- Lee Baker, *Truth, Lies & Statistics: How to Lie with Statistics*

_`Marginal probability`
~~~~~~~~~~~~~~~~~~~~~~~

.. index:: single: marginal probability
           single: degeneracy

For a certain :math:`n`-variate distribution :math:`f(X_1, X_2, \dots, X_n)`, if it denotes the set
:math:`U = \{1, 2, \dots, n\}`, and assume there is a positive integer :math:`m` which satisfies
:math:`0 < m < n`, the marginal probability density of :math:`f(X_1, X_2, \dots, X_n)` can be denoted as
:math:`f(X_{s_1}, X_{s_2}, \dots, X_{s_m})`, where the set :math:`A = \{s_1, s_{2}, \dots, s_{m}\}`
is subset of :math:`U` (:math:`A \subset U`).

Formally, for complement :math:`A^C = \{k_1, k_2, \dots, k_{n-m}\}`, the calculation for
:math:`f(X_{s_1}, X_{s_2}, \dots, X_{s_m})` is:

.. math::
   :label: marginal probability density

   f({X}_{s_1}, {X}_{s_2}, \dots, {X}_{s_m}) &= \int_{{X}_{k_1}} \int_{{X}_{k_2}} \cdots \int_{{X}_{{k}_{n-m}}}
   \mathrm{}f(X_1, X_2, \dots, X_n) d{X}_{k_1} dt{X}_{k_2} \cdots d{X}_{{k}_{n-m}} \\
   \mathrm{}&= {E}_{{X}_{k_1}, {X}_{k_2}, \cdots, {X}_{{k}_{n-m}}} [f(X_1, X_2, \dots, X_n)]

Apparently, the marginal probability :math:`f(X_{s_1}, X_{s_2}, \dots, X_{s_m})` is in a :math:`m`-dimensional
subspace. Particularly, if :math:`n - m = 1`, this marginal probability density is 1 dimensionally
:ref:`degenerated <degeneracy>` from the original :math:`n`-space.

.. note::

   .. _`degeneracy`:

   Degeneracy describe a class of object changes its nature in the condition of some constraints. For example,
   for an ellipse :math:`g(a, b)`, if :math:`a = b`, it degenerates into a circle; if
   :math:`a \cdot b = 0,\ a+b \neq 0`, it degenerates into a line segment; if :math:`a \cdot b = 0,\ a+b = 0`,
   it degenerates into a point.

   Degeneracy also occurs in probability distribution. One-point distribution can be degenerated from an uni-variate
   Gaussian :math:`g(x|\mu, s)` when :math:`s = 0`; beta distribution can be degenerated from a Dirichlet distribution
   :math:`\mathrm{Dir}(\alpha_1, \dots, \alpha_m)` if :math:`m = 2`. However, for multivariate Gaussian, either its
   marginal or its conditional distribution will always be multivariate Gaussian, despite degeneracy occurred in
   dimensions.

_`Hypothesis testing`
---------------------

.. index:: hypothesis testing

Statistical hypothesis testing is developed and enriched by Karl Pearson, William Sealy Gosset, Ronald Fisher,
Jerzy Neyman, and Egon Pearson :ref:`[Fisher1955, <[Fisher1955]>` :ref:`Neyman1933, <[Neyman1933]>`
:ref:`Goodman1999, <[Goodman1999]>` :ref:`Heyde2001] <[Heyde2001]>`. It is the method to decide whether
the collected data can sufficiently support a certain statistical hypothesis.

For all hypothesis testing, there must be an assumption called *null hypothesis* :math:`H_0`, and its complement
:math:`H_1 = H_0^C` is *alternative hypothesis* where :math:`C` refers the full probability space (:math:`p(C) = 1`).
Most types of test will export the statistic, commonly scalar indicator devised for describing some property,
and :math:`p`-value, how likely we obtain the collected data in one study if our :math:`H_0` is of the truth.

Because the :math:`p`-value refers probability, its value will range from 0 to 1. Practically, the less the
:math:`p`-value, the more tendency to reject the null hypothesis :math:`H_0`, based on our tested data.

There are two types as for :math:`H_0`: similarity hypothesis called `two-tailed`, and un-similarity hypothesis
called `single-tailed`. For example, :math:`\mu_1` and :math:`\mu_2` are mean values for two populations :math:`X_1`
and :math:`X_2`, the hypothesis :math:`\mu_1 = \mu_2` is two-tailed; but for :math:`\mu_1 > \mu_2` or
:math:`\mu_1 < \mu_2`, they are single-tailed. Notes two key facts: 1) this concept only exist in cases for two
group comparison; 2) difference of alternative generally changes the final :math:`p`-value, but not for the
statistic.

_`one-way ANOVA test`
~~~~~~~~~~~~~~~~~~~~~

.. index:: one-way ANOVA test

One-way ANOVA is designed to compare whether two or more sample's means are significantly different using :math:`F`
distribution :ref:`[Lowry2014, <[Lowry2014]>` :ref:`Heiman2001] <[Heiman2001]>`. For one-way ANOVA:

.. container:: one-way ANOVA test

   :math:`H_0`:
      Samples of all groups are drawn from the populations with the same mean

   :math:`H_1`:
      Samples of all groups are not drawn from the populations with the same mean

   Statistic:

      .. math::
         :label: statistic_f

         s = \frac{{MS}_{B}}{{MS}_{W}} \sim F

Where :math:`MS_{B}` and :math:`MS_{W}` are the mean squares between and within groups respectively. This statistic
:math:`s` follows a certain :math:`F` distribution.

More specifically, :math:`MS_{B} = S_{B}/f_{B}`, where :math:`S_{B}` is the sum of squared difference, and the
:math:`f_{B}` is the degrees of freedom, for between groups. All about :math:`MS_{W}` is as similar as those of
:math:`MS_{B}` but for within groups.

_`Student's T test`
~~~~~~~~~~~~~~~~~~~

.. index:: Student's T test

Student's T test is designed to evaluate whether the population mean of one group is equal, greater, or less than
a specific value (`one-sample` in statistical terminology), or that mean of another group (i.e. `two-sample` in
statistics). It gets its name from the paper publication from William Sealy Gosset with his pseudonym `Student`
:ref:`[Lehmann1992] <[Lehmann1992]>`. For the two-tailed independent T test:

.. container:: Student's T test

   :math:`H_0`:
      For population mean values :math:`\mu_1` and :math:`\mu_2` in two groups, :math:`\mu_1 = \mu_2`

   :math:`H_1`:
      :math:`\mu_1 \neq \mu_2`

   statistic:

      .. math::
         :label: statistic_t1

         s = \frac{\mu_1 - \mu_2}{{s}_{\Delta}}

      :math:`s_{\Delta}` differs when data possess in different variance level in two groups. Assume :math:`n_1`
      and :math:`n_2` are number of samples, and :math:`s_1` and :math:`s_2` are unbiased estimators of standard
      variance, for the 1st and 2nd group respectively. For similar variances:

      .. math::
         :label: statistic_t2

         {s}_{\Delta} = \sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}} \cdot \sqrt{\frac{1}{n_1}+\frac{1}{n_2}}

      For two groups with variances in great difference, the :ref:`Welch's T test <[Welch1947]>` will be executed
      for adaption. In this condition:

      .. math::
         :label: statistic_t3

         {s}_{\Delta} = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}

      Specifically, if :math:`n_1 = n_2 = n`, those :math:`s_{\Delta}` will simultaneously converge into the form of
      :math:`\sqrt{s_1^2 + s_2^2}/\sqrt{n}`. Assume :math:`s^{\prime} = \sqrt{s_1^2 + s_2^2}`, it can be
      found that :math:`s_1` and :math:`s_2` are defined in two orthogonal axes. That's the reason why it is called
      `independent` T test. Additionally, for no independent (related) case, :math:`s_1` and :math:`s_2` are defined
      within the same axis, the calculation for :math:`s^{\prime}` will be :math:`\mid s_1 - s_2 \mid`, therefore
      the statistic in this circumstance is:

      .. math::
         :label: statistic_t4

         s = \frac{\mu_1 - \mu_2}{\mid s_1 - s_2\mid/\sqrt{n}}

_`Shapiro-Wilk test`
~~~~~~~~~~~~~~~~~~~~

.. index:: Shapiro-Wilk test

Shapiro-Wilk test is proposed by Shapiro and Wilk :ref:`[Shapiro1965] <[Shapiro1965]>` for determining the normality
of data where:

.. container:: Shapiro-Wilk test

   :math:`H_0`:
      The data was drawn from a normal distribution

   :math:`H_1`:
      The data was not drawn from a normal distribution

   Statistic:

      .. math::
         :label: statistic_sw

         s = \frac{(\sum_{i=1}^n a_i {x}_{(i)})^2}{\sum_{i=1}^n (x_i - \bar{x})^2}

      Where :math:`a_i` is :math:`i`-th element in coefficient vector :math:`\boldsymbol{a}`, as defined in
      :ref:`[Davis1977] <[Davis1977]>`.

      Note that no analytical formula for its distribution, then the corresponding :math:`p`-value is obtain via
      Monte Carlo (:ref:`MC <MC>`) simulation.

_`Omnibus Normality test`
~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Omnibus Normality test

Omnibus test for normality is proposed main by D’Agostino :ref:`[Agostino1971, <[Agostino1971]>`
:ref:`Agostino1973] <[Agostino1973]>`, for determining the departure of sample distribution from uni-variate
gaussian:

.. container:: Omnibus Normality test

   :math:`H_0`:
      The data was drawn from a normal distribution

   :math:`H_1`:
      The data was not drawn from a normal distribution

   statistic:

      .. math::
         :label: statistic_normality

         s = s_s^2 + s_k^2

      Where the :math:`s_s` and :math:`s_k` are statistics returned from :ref:`skew test <Skew test>`  and
      :ref:`kurtosis test <Kurtosis test>`.

_`Kolmogorov-Smirnov test`
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Kolmogorov-Smirnov test

The Kolmogorov-Smirnov test is a non-parametric method to quantify the distance from one empirical distribution
function to a cumulative distribution function (one-sample), or to another empirical distribution function
(two-sample). It is generally be used to test the goodness of fit. As for two-tailed Kolmogorov-Smirnov test:

.. container:: Kolmogorov-Smirnov test

   :math:`H_0`:
      For cumulative distribution function :math:`F(x)` and :math:`F^\prime(x)`, :math:`F(x) = F^\prime(x)`

   :math:`H_1`:
      :math:`F(x) \neq F^\prime(x)`

   statistic:

      .. math::
         :label: statistic_ks1

         s = \mathrm{sup}_x \mid F(x) - F^\prime(x) \mid

      Where:

      .. math::
         :label: statistic_ks2

         F(x) = F_n(x) = \frac{1}{n} \sum_{i=1}^{n} {I}_{(-\inf, x]}(X)

      In one-sample test, :math:`F^\prime(x)` is denoted with another pre-defined distribution; In two-sample test,
      :math:`F^\prime(x) = F_m(x)` which is of the similarity as :math:`F_n(x)` but from another dataset

_`Cramér-von Mises test`
~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Cramér-von Mises test

The Cramér-von Mises test is proposed by :ref:`Harald Cramér <[Cramér1928]>` and
:ref:`Richard Edler von Mises <[Von1928]>` as a criterion to measure the distance from one empirical distribution
function to a cumulative distribution function (one-sample), or to another empirical distribution function
(two-sample).

.. container:: Cramér-von Mises test

   :math:`H_0`:
      For empirical distribution and cumulative distribution function :math:`F_{n}(x)` and :math:`F^\prime(x)`,
      :math:`F_{n}(x) = F^\prime(x)`

   :math:`H_1`:
      :math:`F_{n}(x) \neq F^\prime(x)`

   statistic:

      .. math::
         :label: statistic_cvm1

         s = \frac{1}{12n} + \sum_{i=1}^{n} [\frac{2i-1}{2n} - F^\prime(x_i)]^2

      Specially, if the :math:`F^\prime(x)` sources from another empirical distribution :math:`F_{m}(y)`, it will
      be two-sample test with the following statistic:

      .. math::
         :label: statistic_cvm2

         s = \frac{n\sum_{i=1}^{n}({r}_{x_i, a}-i)^2+m\sum_{j=1}^{m}({r}_{y_j, a}-j)^2 }{mn(m+n)}-\frac{4mn-1}{6(m+n)}

      Where :math:`r_{v, a}` are rank of :math:`v` in series :math:`a = \{x_1, x_2, \dots, x_n, y_1, y_2, \dots, y_m\}`

_`Alexander Govern test`
~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Alexander Govern test

An alternative testing for :ref:`one-way ANOVA test <one-way ANOVA test>` proposed by
:ref:`Alexander <[Alexander1994]>` for dealing with multi grouped data with heterogeneity on variance.
Similar as one-way ANOVA:

.. container:: Alexander Govern test

   :math:`H_0`:
      Samples of all groups are drawn from the populations with the same mean

   :math:`H_1`:
      Samples of all groups are not drawn from the populations with the same mean

   Statistic:

      .. math::
         :label: statistic_ag

         s = \sum_{j=1}^{J} Z_j^2

      Where :math:`J` is the number of groups, :math:`Z_j` is the standard normal deviate for each group.
      For more details, see description summarized by :ref:`Ochuko <[Ochuko2015]>`.

_`Tukey's range test`
~~~~~~~~~~~~~~~~~~~~~

.. index:: Tukey's range test

Tukey's honestly significant difference (HSD) test, a comprehensive test proposed by John Tukey
:ref:`[Tukey1949] <[Tukey1949]>` compares all possible pairs of means.

.. container:: Tukey's range test

   :math:`H_0`:
      Samples of all groups are drawn from the populations with the same mean

   :math:`H_1`:
      Samples of all groups are not drawn from the populations with the same mean

   Statistic:

      .. math::
         :label: statistic_thsd

         {s}_{i, j} = \frac{\mu_{i} -\mu_{j}}{SE} \sim Q

      Where :math:`\mu_{i}` and :math:`\mu_{j}` are means of group :math:`i` and :math:`j`; :math:`SE` is the
      standard error of the sum of means. :math:`Q` is a certain studentized range distribution.

_`Kruskal-Wallis H-test`
~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Kruskal-Wallis H-test

A non-parametric method proposed by William Kruskal and W. Allen Wallis :ref:`[Kruskal1952] <[Kruskal1952]>` to
measure whether samples originate from the identical distribution. It can be seen as the non-parametric alternative
for :ref:`one-way ANOVA test <one-way ANOVA test>`.

.. container:: Kruskal-Wallis H-test

   :math:`H_0`:
      Samples of all groups are drawn from the populations with the same median

   :math:`H_1`:
      Samples of all groups are not drawn from the populations with the same median

   Statistic:

      .. math::
         :label: statistic_kw

         s = (N-1)\frac{\sum_{i=1}^{g} n_i (\bar{r}_{i\cdot}-\bar{r})^2}{\sum_{i=1}^g \sum_{j=1}^{n_i}
         ({r}_{ij} - \bar{r})^2}

      Where :math:`N` is the number of all observations; :math:`n_i` is the number of observation in :math:`i`-th
      group; :math:`g` is the number of groups; :math:`r_{i, j}` is the global rank of :math:`j`-th observation
      in :math:`i`-th group, while :math:`\bar{r}_{i\cdot}` is calculated from :math:`(\sum_{j=1}^{n_i} r_{ij})/n_i`,
      and :math:`\bar{r}` is calculated from :math:`0.5\cdot(N+1)`.

_`Mood's test`
~~~~~~~~~~~~~~

.. index:: single: Mood's median test
           single: Mood's scale test

Mood's test can measure median and scale on multi-grouped data. Mood's median test is a non-parametric alternative
to :ref:`one-way ANOVA test <one-way ANOVA test>`, and also a special case of
:ref:`Pearson’s Chi-Squared Test <Chi-Squared Test>`.

.. container:: Mood's median test

   :math:`H_0`:
      Samples of all groups are drawn from the populations with the same median

   :math:`H_1`:
      Samples of all groups are not drawn from the populations with the same median

   statistic:

      .. math::
         :label: statistic_mood

         s = \sum_{i=1}^{g} \sum_{j=0}^{1} \frac{({A}_{i,j}-{B}_{i,j})^2}{{B}_{i,j}}

      Assume the grand median is :math:`\bar{m}`. :math:`A_{i,0}` is the counts of observations less than or equal
      as :math:`\bar{m}` in :math:`i`-th group, :math:`A_{i,1}` is that greater than :math:`\bar{m}`. :math:`B_{i, j}`
      is defined as :math:`(\sum_{i=1}^{g} A_{i,j} \cdot \sum_{j=0}^{1} A_{i,j})/\sum_{i=1}^{g} \sum_{j=0}^{1} A_{i,j}`.

Scale is parameter to describe the range of distribution (See :ref:`scale <Kernel and scale>`). For pair-wised
Mood's scale test, the underlying model is assumption that two samples are drawn from distributions :math:`f(x-l)`
and :math:`f((x-l)/m)/m` respectively, :math:`l` is for location and :math:`m` is for scale. Null hypothesis in
these case is :math:`m = 1`.

_`Bartlett's test`
~~~~~~~~~~~~~~~~~~

.. index:: Bartlett's test

The statistical approach proposed by :ref:`Maurice Stevenson Bartlett <[Bartlett1937]>` for testing homoscedasticity
on samples drawn from populations with equal variances.

.. container:: Bartlett's test

   :math:`H_0`:
      Samples of all groups are of the same variance

   :math:`H_1`:
      Samples of all groups are not of the same variance

   statistic:

      .. math::
         :label: statistic_barlett

         s = \frac{(N-g)\mathrm{ln}S_p^2 - \sum_{i=1}^g (n_i - 1)\mathrm{ln}S_i^2}{1 + \frac{1}{3(g-1)}
         [\sum_{i=1}^g (\frac{1}{n_i-1} - \frac{1}{N-g})]} \sim \chi^2

      Where :math:`n_i` is the number of observations in :math:`i`-th group among :math:`g` groups; :math:`S_i^2`
      is variance of group :math:`i`; :math:`N=\sum_{i=1}^g n_i`; and
      :math:`S_p^2 = (N-g)^{-1} \sum_{i=1}^g (n_i-1)S_i^2`. This statistic obeys a :math:`\chi^2` distribution
      with degree of freedom of :math:`g-1`.

_`Levene test`
~~~~~~~~~~~~~~

.. index:: Levene test

The statistical approach proposed by :ref:`Levene <[Levene1960]>` for testing homoscedasticity on samples drawn
from populations with equal variances. An alternative for :ref:`Bartlett's test <Bartlett's test>` due to its robust
performance.

.. container:: Levene test

   :math:`H_0`:
      Samples of all groups are of the same variance

   :math:`H_1`:
      Samples of all groups are not of the same variance

   statistic:

      .. math::
         :label: statistic_levene

         s = \frac{N-g}{g-1}\cdot\frac{\sum_{i=1}^g n_i ({z}_{i,\cdot}-{z}_{\cdot,\cdot})^2}{\sum_{i=1}^g
         \sum_{j=1}^{n_i} ({z}_{i,j}-{z}_{i,\cdot})^2}

      Where :math:`z_{i,j}` is the absolute distance to the mean (trimmed or not), or median of all observations
      of :math:`i`-th group, from :math:`j`-th case. :math:`n_i` is the number of all observations of the :math:`i`-th
      group, among :math:`g` groups. Group mean :math:`z_{i,\cdot}` is defined as
      :math:`n_i^{-1} \sum_{j=1}^{n_i} z_{i,j}`. Grand mean :math:`z_{\cdot, \cdot}` is defined as
      :math:`(\sum_{i=1}^g n_i)^{-1} \cdot \sum_{i=1}^{g} \sum_{j=1}^{n_i} z_{i,j}`.

_`Fligner-Killeen test`
~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Fligner-Killeen test

Non-parametric alternative of :ref:`Bartlett's test <Bartlett's test>` for testing homoscedasticity on samples.
Perform well when observations distributed non-normally, or outliers existed.

.. container:: Fligner-Killeen test

   :math:`H_0`:
      Samples of all groups are of the same variance

   :math:`H_1`:
      Samples of all groups are not of the same variance

   statistic:

      .. math::
         :label: statistic_fk

         s = \frac{\sum_{i=1}^g n_i (\bar{z}_i - \bar{z})^2}{s^2}

      Where :math:`\bar{z}_i` is the mean of :math:`z` scores of :math:`i`-th group among :math:`g` groups.
      :math:`\bar{z}` and :math:`s^2` are grand mean and variance of all :math:`z` scores. :math:`n_i` is the
      number of observations for :math:`i`-th group.

_`Anderson-Darling test`
~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Anderson-Darling test

Statistical approach proposed by Theodore Wilbur Anderson and Donald A. Darling :ref:`[Anderson1952] <[Anderson1952]>`,
to determine whether a given set of observations is drawn from a given probability distribution. For *K* samples
Anderson-Darling test, it can measure whether several group of observations are sourced from a single distribution.
For *K* samples samples Anderson-Darling test:

.. container:: Anderson-Darling test

   :math:`H_0`:
      Samples of all groups are drawn from the same population

   :math:`H_1`:
      Samples of all groups are not drawn from the same population

   statistic:

      .. math::
         :label: statistic_ad

         s = \frac{1}{N} \sum_{i=1}^{g} \frac{1}{n_i} \sum_{j=1}^{N-1} \frac{(N\cdot{M}_{i,j}-j \cdot n_i)^2}{j(N-j)}

      Where :math:`n_i` is the number of all observations of the :math:`i`-th group, among :math:`g` groups. :math:`N`
      is the total number of observations (:math:`N = \sum_{i=1}^g n_i`). :math:`M_{i,j}` is the number of observations
      in :math:`i`-th group that less than or equal as :math:`r_j`, the pooled rank of :math:`x_j` in
      :math:`\{x_1, x_2, \dots, x_N\}` in ascending order.

_`Wilcoxon rank test`
~~~~~~~~~~~~~~~~~~~~~

.. index:: Wilcoxon rank test

Frank Wilcoxon firstly proposed in 1945 :ref:`[Wilcoxon1992] <[Wilcoxon1992]>` to use rank instead of the values
themselves to run variance analysis. It concludes unpaired and paired methods. Unpaired one is known as rank sum
test, while paired one is known as single rank test. For rank sum test:

.. container:: Wilcoxon rank test

   :math:`H_0`:
      Samples of two groups are drawn from the same distribution

   :math:`H_1`:
      Samples of two groups are not drawn from the same distribution

   statistic:

      .. math::
         :label: statistic_rank1

         s = \sum_{j=1}^{n_1} {r}_{1, j}

      Where :math:`n_1` is the number of observations in first group, :math:`r_{1, j}` refers the rank of all 1st
      group observations in pooled set of two groups.

      Additionally, for single rank version, the statistic will be like:

      .. math::
         :label: statistic_rank2

         s = \sum_{i=1}^{n} \mathrm{sgn}(x_i - y_i) r_i

      Where :math:`r_i` is the rank of :math:`i`-th item in the set of
      :math:`\{|x_1 - y_1|, |x_2 - y_2|, \dots, |x_n - y_n|\}`.

_`Epps-Singleton test`
~~~~~~~~~~~~~~~~~~~~~~

.. index:: Epps-Singleton test

The method suggested by Epps and Singleton :ref:`[Epps1986] <[Epps1986]>` to use characteristic function :math:`g`
instead of observed distribution :math:`F` for test. This method weakens the assumptions for specifying type
continuity of probability distributions, and applied whether continuity or not of the underlying distributions.

.. container:: Epps-Singleton test

   :math:`H_0`:
      Samples of two groups are of the same underlying distribution; :math:`g_1 = g_2`

   :math:`H_1`:
      Samples of two groups are not of the same underlying distribution; :math:`g_1 \neq g_2`

   statistic:

      .. math::
         :label: statistic_es

         s  = \sqrt{n_1+n_2} \cdot (g_1-g_2) \sim \mathcal{N}(\boldsymbol{0}, \boldsymbol{\Omega})

      Where :math:`n_1` and :math:`n_2` are numbers of observations of two groups. :math:`g` is the characteristic
      function defined as Fourier transform of observed distribution :math:`F`
      (:math:`g_i = \int_{-\inf}^{\inf} e^{itx} dF_{n_i}(x) = n_i^{-1} \sum_{j=1}^{n_i} e^{itX_{ij}}`). The item
      :math:`g(X_{ij}) = e^{itX_{ij}}` is expressed via Euler number as 4-dimensional vector. This statistic will
      asymptotically approximates to a multivariate gaussian :math:`\mathcal{N}(\boldsymbol{0}, \boldsymbol{\Omega})`.
      For :math:`\boldsymbol{\Omega}`, it can be estimated as
      :math:`\hat{\boldsymbol{\Omega}}=\sum_{i=1}^{2}[(n_{i}-1)(\sum_{i=1}^{2}n_i)/n_{i}^2]\mathrm{cov}\{g(X_{ij})\}`.

_`Mann–Whitney U test`
~~~~~~~~~~~~~~~~~~~~~~

.. index:: Mann–Whitney U test

None parametric method proposed by Mann Henry B. and Whitney Donald R. :ref:`[Mann1947] <[Mann1947]>` to measure
the distance of two :ref:`I.I.D. <I.I.D.>` samples drawn from two populations.

.. container:: Mann–Whitney U test

   :math:`H_0`:
      Samples of two groups are drawn from the same distribution

   :math:`H_1`:
      Samples of two groups are not drawn from the same distribution

   statistic:

      .. math::
         :label: statistic_u

         s  = \sum_{i=1}^{n} \sum_{j=1}^{m} S(x_i, y_j)

      Where :math:`n` and :math:`m` are numbers of observations of two groups. :math:`S(x_i, y_j)` is 1 if
      :math:`x_i > y_j`; 0.5 if :math:`x_i = y_j`; and 0 if :math:`x_i < y_j`.

_`Brunner-Munzel test`
~~~~~~~~~~~~~~~~~~~~~~

.. index:: Brunner-Munzel test

Test with equal or even greater power than that of :ref:`Mann–Whitney U test <Mann–Whitney U test>` proposed
by Brunner and Munzel :ref:`[Brunner2000, <[Brunner2000]>` :ref:`Karch2021] <[Karch2021]>`.

.. container:: Brunner-Munzel test

   :math:`H_0`:
      for observations from two populations :math:`X` and :math:`Y`, :math:`P(X > Y) = P(X < Y)`

   :math:`H_1`:
      :math:`P(X > Y) \neq P(X < Y)`

   statistic:

      .. math::
         :label: statistic_bm

         s  = \frac{U}{n_1 \cdot n_2}

      Where :math:`U` is the statistic of :ref:`U test <Mann–Whitney U test>`, :math:`n_1` and
      :math:`n_2` are number of observations for two groups.

_`Ansari-Bradley test`
~~~~~~~~~~~~~~~~~~~~~~

.. index:: Ansari-Bradley test

Also know as dispersion test firstly proposed by Ansari and Bradley :ref:`[Ansari1960] <[Ansari1960]>` to measure
the scales difference between two groups of samples.

.. container:: Ansari-Bradley test

   :math:`H_0`:
      for two populations with scales :math:`\sigma_x` and :math:`\sigma_y`, :math:`\sigma_x = \sigma_y`

   :math:`H_1`:
      :math:`\sigma_x \neq \sigma_y`

   statistic:

      .. math::
         :label: statistic_ab

         s  = \sum_{i=1}^{n_x} {r}_{x_i}

      Where :math:`n_x` is the number of observations for :math:`x`, :math:`r_{x_i}` is the rank assigned to
      :math:`x_i` in pooled set of :math:`x` and :math:`y`.

_`Skew test`
~~~~~~~~~~~~

.. index:: Skew test

Test to quantify how extent the skewness of data distribution departed from a standard uni-variate gaussian suggested
by :ref:`Agostino et. al. <[Agostino1990]>`:

.. container:: Skew test

   :math:`H_0`:
      skewness of data is of the same as that of standard uni-variate gaussian

   :math:`H_1`:
      skewness of data is not of the same as that of standard uni-variate gaussian

   statistic:

      .. math::
         :label: statistic_skew1

         s  = \delta + \log{[\frac{y}{\alpha} + \sqrt{(\frac{y}{\alpha})^2 + 1}]}

      Where :math:`n` is the number of samples, for :math:`\delta`, :math:`y` and :math:`\alpha`:

      .. math::
         :label: statistic_skew2

         \delta = \frac{1}{\sqrt{0.5 \cdot \log{W_2}}}

      .. math::
         :label: statistic_skew3

         y = \frac{b_2}{\sqrt{\frac{6(n-2)}{(n+1)(n+3)}}}

      .. math::
         :label: statistic_skew4

         \alpha = \sqrt{\frac{2}{W_2 -1}}

      And for :math:`W_2` and :math:`b_2` (skewness know as :math:`z^3`):

      .. math::
         :label: statistic_skew5

         W_2 &= -1 + \sqrt{2(\beta_2 - 1)} \\
         \mathrm{for}\ \beta_2 &= \frac{3(n^2+27n-70)(n+1)(n+3)}{(n-2)(n+5)(n+7)(n+9)}

      .. math::
         :label: statistic_skew6

         b_2 = \frac{\sum_{i=1}^{n} z_i^3}{n}

_`Kurtosis test`
~~~~~~~~~~~~~~~~

.. index:: Kurtosis test

Test to quantify how extent the kurtosis of data distribution departed from a standard uni-variate gaussian suggested
by :ref:`Anscombe et. al. <[Anscombe1983]>`:

.. container:: Kurtosis test

   :math:`H_0`:
      kurtosis of data is of the same as that of standard uni-variate gaussian

   :math:`H_1`:
      kurtosis of data is not of the same as that of standard uni-variate gaussian

   statistic:

      .. math::
         :label: statistic_kurtosis1

         s  = (T_1 - T_2) \cdot \sqrt{\frac{9A}{2}}

      Where for :math:`T_1`, :math:`T_2` and :math:`A`:

      .. math::
         :label: statistic_kurtosis2

         T_1 = 1 - \frac{2}{9A}

      .. math::
         :label: statistic_kurtosis3

         T_2 = \mathrm{sgn}(D) \cdot [\frac{(1-\frac{2}{A})}{\mid D \mid}]^{\frac{1}{3}}

      .. math::
         :label: statistic_kurtosis4

         A = 6 + \frac{8}{\surd b_1} (\frac{2}{\surd b_1} + \sqrt{1 + \frac{4}{{\surd b_1}^2}})

      and :math:`n` is the number of samples, for :math:`D`, :math:`\surd b_1`, and the intermediate variable
      :math:`x`:

      .. math::
         :label: statistic_kurtosis5

         D = 1 + x \cdot \sqrt{\frac{2}{A-4}}

      .. math::
         :label: statistic_kurtosis6

         \surd b_1 = \frac{6(n^2-5n+2)}{(n+7)(n+9)} \cdot \sqrt{\frac{n(n-2)(n-3)}{6(n+3)(n+5)}}

      .. math::
         :label: statistic_kurtosis7

         x = \frac{b_2 - E}{\sqrt{V}}

      Where :math:`b_2` is the kurtosis of the :math:`z` scores; :math:`E = 3(n-1)/(n+1)`; and
      :math:`V = [24n(n-2)(n-3)]/[(n+1)^2(n+5)(n+5)]`.

_`Jarque-Bera test`
~~~~~~~~~~~~~~~~~~~

.. index:: Jarque-Bera test

Statistical approach proposed by Carlos Jarque and  Anil K. Bera :ref:`[Jarque1980] <[Jarque1980]>` to test the
goodness of fit of samples to standard uni-variate gaussian. Work well only large number of observations.

.. container:: Jarque-Bera test

   :math:`H_0`:
      sample has the skewness and kurtosis matching the standard uni-variate gaussian

   :math:`H_1`:
      sample has the skewness and kurtosis not matching the standard uni-variate gaussian

   statistic:

      .. math::
         :label: statistic_jb

         s  = \frac{n}{6} [S^2 + \frac{1}{4} (K-3)^2]

      Where the :math:`S` is the skewness (:math:`b_2` in :eq:`statistic_skew3`), :math:`K` is the kurtosis of
      samples (:math:`b_2` in :eq:`statistic_kurtosis7`).

_`Cressie-Read power divergence test`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Cressie-Read power divergence test

Test proposed by Read and Cressie :ref:`[Read1988] <[Read1988]>` to determine whether the samples match the
given categorical frequencies.

.. container:: Cressie-Read power divergence test

   :math:`H_0`:
      observations match the given categorical frequencies

   :math:`H_1`:
      observations not match the given categorical frequencies

   statistic:

      .. math::
         :label: statistic_pd

         s  = \frac{2}{\lambda (\lambda + 1)} \sum_{i=1}^k o_i [(\frac{o_i}{e_i})^\lambda - 1]

      Where :math:`\lambda` is an user-predefined real-value parameter. :math:`k` is the parameter of an :math:`k`
      categorical distribution. :math:`o_i` and :math:`e_i` are observed frequency and expected frequency for the
      :math:`k`-th category, respectively.

_`Chi-Squared test`
~~~~~~~~~~~~~~~~~~~

.. index:: Chi-Squared test

Pearson's chi-squared test :ref:`[Pearson1900] <[Pearson1900]>` to determine whether the samples match the
given categorical frequencies. If priori frequencies not given, the expected frequencies are calculated
from the data.

.. container:: Chi-Squared test

   :math:`H_0`:
      observations match the expected categorical frequencies

   :math:`H_1`:
      observations not match the expected categorical frequencies

   statistic:

      .. math::
         :label: statistic_chi2_1

         s  = \sum_{i=1}^{n} \sum_{j=1}^{m} \frac{({o}_{i,j}-{e}_{i,j})^2}{{e}_{i,j}} \sim \chi^2

      Assume there are :math:`n` options of variable 1 coupled with :math:`m` options of variable 2. :math:`o_{i,j}`
      is the observed frequency of :math:`i`-th option in variable 1 and :math:`j`-th option in variable 2.
      :math:`e_{i,j}` is calculated from:

      .. math::
         :label: statistic_chi2_2

         {e}_{i,j} = \frac{\sum_{i=1}^{n} {o}_{i,j} \cdot \sum_{j=1}^{m} {o}_{i,j}}{\sum_{i=1}^{n}
         \sum_{j=1}^{m} {o}_{i,j}}

      This statistic obeys a :math:`\chi^2` distribution with degree of freedom :math:`(n-1)\cdot(m-1)`.

_`Pearson correlation coefficient`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Pearson correlation coefficient

Correlation coefficient (:abbr:`PCC (Pearson Correlation Coefficient)`, or
:abbr:`PPMCC (Pearson Product-Moment Correlation Coefficient)`) is the statistical approach to measure
the relation between two factors in observed samples.

.. container:: Pearson correlation coefficient

   :math:`H_0`:
      two factors of observed samples are uncorrelated

   :math:`H_1`:
      two factors of observed samples are not uncorrelated

   statistic:

      .. math::
         :label: statistic_pearson

         s  = \frac{\mathrm{cov} (X, Y)}{ \rho_X \rho_Y} = \frac{\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]}{\rho_X \rho_Y}

      Notes that :math:`\rho_X` and :math:`\rho_Y` are standard deviation for two factors :math:`X` and :math:`Y`;
      :math:`\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]` can be calculated as :math:`\mathbb{E}[XY]-\mathbb{E}[X]\mathbb{E}[Y]`.

_`Spearman correlation coefficient`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Spearman correlation coefficient

Non-parametric version of :ref:`Pearson correlation coefficient <Pearson correlation coefficient>` using ranks of
values instead of values themselves when computing coefficient.

.. container:: Spearman correlation coefficient

   :math:`H_0`:
      factors of observed samples are uncorrelated

   :math:`H_1`:
      factors of observed samples are not uncorrelated

   statistic:

      .. math::
         :label: statistic_spearman

         s  = \frac{\mathrm{cov} (R(X), R(Y))}{ \rho_{R(X)} \rho_{R(Y)}} = \frac{\mathbb{E}[(R(X)-\mu_{R(X)})
         (R(Y)-\mu_{R(Y)})]}{\rho_{R(X)} \rho_{R(Y)}}

      :math:`R(X)` and :math:`R(Y)` are the rank of :math:`X` and :math:`Y` series, respectively.

_`Kendall's tau correlation coefficient`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Kendall's tau correlation coefficient

The statistic :math:`\tau` measure the fraction of difference from concordant to discordant pairs, over all number
of pairs. For any concordant pairs :math:`(x_i, y_i)` and :math:`(x_j, y_j)` when :math:`i < j`,
:math:`\mathrm{sgn} (x_i - x_j) \mathrm{sgn} (y_i - y_j) > 0`. This method is developed by Kendall in 1938
:ref:`[Kendall1938] <[Kendall1938]>`.

.. container:: Kendall's tau correlation coefficient

   :math:`H_0`:
      factors of observed samples are uncorrelated

   :math:`H_1`:
      factors of observed samples are not uncorrelated

   statistic:

      .. math::
         :label: statistic_kendall

         s  = \frac{1}{n(n-1)} \sum_{i < j} \mathrm{sgn} (x_i - x_j) \mathrm{sgn} (y_i - y_j)

_`Friedman test`
~~~~~~~~~~~~~~~~

.. index:: Friedman test

The test to measure whether repeated samples of the same individuals have the same distribution. This method
is firstly proposed by Milton Friedman :ref:`[Friedman1937] <[Friedman1937]>`.

.. container:: Friedman test

   :math:`H_0`:
      repeated samples have the same distribution

   :math:`H_1`:
      repeated samples not have the same distribution

   statistic:

      .. math::
         :label: statistic_friedman

         s  = \frac{12n}{g(g+1)} \sum_{j=1}^{g} (\bar{r}_{\cdot j} - \frac{g+1}{2})^2 \sim \chi_{g-1}^2

      Assume the data is organized in :math:`\boldsymbol{X} \in \mathbb{R}^{n \times g}` where :math:`n` is the
      number of observations while :math:`g` is the number of factors. There is also a rank matrix
      :math:`\boldsymbol{R} \in \mathbb{Z}^{+\ n \times g}` where :math:`r_{i j}` is the rank of :math:`x_{i j}`
      in :math:`x_{i \cdot} = \{x_{i 1}, x_{i 2}, \dots, x_{i g}\}`. :math:`\bar{r}_{\cdot j}` is defined
      as :math:`n^{-1}\sum_{i=1}^{n} r_{i j}`. This statistic obeys a :math:`\chi^2` distribution with :math:`g-1`
      degree of freedom.

_`Multiscale Graph Correlation test`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Multiscale Graph Correlation test

The method proposed by :ref:`Vogelstein et.al. <[Vogelstein2019]>` to quantify the correlation between two
high-dimensional observations. Refer the section :ref:`Multi Graph Correlation <Multi Graph Correlation>` for
algorithm details.

.. container:: Multiscale Graph Correlation test

   :math:`H_0`:
      two high-dimensional data :math:`\boldsymbol{X}` and :math:`\boldsymbol{Y}` are independent

   :math:`H_1`:
      two high-dimensional data :math:`\boldsymbol{X}` and :math:`\boldsymbol{Y}` are not independent

   statistic:

      .. math::
         :label: statistic_mgc

         s  = f(M_X, M_Y)

      Where :math:`M_X` and :math:`M_Y` are distance matrices for :math:`X` and :math:`Y` respectively.

_`Monte Carlo hypothesis test`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: Monte Carlo hypothesis test

Test data whether significantly varies from the from specified distributions, via comparing to a pseudo data set
generated for simulation.

.. container:: Monte Carlo hypothesis test

   :math:`H_0`:
      test data are randomly sampled from specified distribution

   :math:`H_1`:
      test data are not randomly sampled from specified distribution

   statistic:

      .. math::
         :label: statistic_mc

         s  = f({s}_{agg}(X), {s}_{agg}({X}_{d}^\prime))

      Where the aggregation function :math:`s_{agg}` is predefined as statistic by user. :math:`X^\prime` is the
      randomly sampling data generated from user defined distribution :math:`d`.

_`Permutation test`
~~~~~~~~~~~~~~~~~~~

.. index:: Permutation test

statistical simulation to test whether two groups of data have the same underlying distribution.

.. container:: Permutation test

   :math:`H_0`:
      test :math:`n\ (n \geq 2)` groups of data are randomly sampled from the same distribution

   :math:`H_1`:
      test :math:`n\ (n \geq 2)` groups of data are not  randomly sampled from the same distribution

   statistic:

      .. math::
         :label: statistic_permu

         s  = f({s}_{agg}(X_1), {s}_{agg}(X_2), \dots, {s}_{agg}(X_n))

      Where the aggregation function :math:`s_{agg}` is predefined by user.

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: May 26, 2023