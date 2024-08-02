_`Bayesian statistics`
======================

Bayesian statistics represents a powerful paradigm that offers a probabilistic framework for updating beliefs and
making inferences in the face of uncertainty. Rooted in the foundational works of :ref:`Thomas Bayes <[Bayes1958]>`
and later refined by prominent statisticians, it incorporates prior knowledge or beliefs, along with observed data,
to form posterior distributions, thereby enabling more informed decision-making.

This methodology finds extensive applications across diverse domains, where dealing with incomplete or uncertain
information is inherent. In the realm of science, Bayesian statistics has revolutionized fields such as genetics,
where it aids in identifying causal variants by integrating prior biological knowledge with sequencing data. In
finance, it is employed for portfolio optimization, risk assessment, and asset pricing, accounting for investors'
subjective beliefs and market dynamics.

Moreover, Bayesian approaches are indispensable in machine learning, particularly for tasks involving classification,
regression, and clustering, where they facilitate the integration of prior assumptions into the learning process,
often leading to improved model interpretability and performance. Within the field of epidemiology, Bayesian methods
are employed to estimate disease prevalence, transmission rates, and the effectiveness of interventions, taking into
account the inherent uncertainties surrounding disease spread.

The language of Bayesian statistics is formal and rigorous, relying on mathematical notation to describe probability
distributions and update rules. Its appeal lies in its ability to provide a coherent and principled framework for
integrating diverse sources of information, making it an invaluable tool for researchers and practitioners alike who
seek to navigate the complexities of decision-making under uncertainty.

_`The basic theories`
---------------------

In the context of classical statistics, the classical model of probability customarily utilize the maximum likelihood
estimation (MLE) to solve the interested distribution. For an observed data set :math:`\mathcal{D}`,
assume there is a statistical model and its corresponding parameter :math:`\theta`. The MLE approach actually
calculate the :math:`\arg\max_{\theta} p(\mathcal{D} | \theta)`. In this manner, parameter :math:`\theta` is
nothing else but a numerical solution.

While in the Bayesian context, if it identically assumes a statistical model with parameter :math:`\theta`, as well
as an observed data :math:`\mathcal{D}`, according to the Bayesian theorem:

.. math::
   :label: Bayesian theorem

   p(\theta | \mathcal{D}) = \frac{p(\mathcal{D} | \theta) p(\theta)}{p(\mathcal{D})}

In this circumstance, parameter :math:`\theta` is a sort of probabilistic distribution instead. In the
:eq:`Bayesian theorem`, the term :math:`p(\mathcal{D} | \theta)` is precisely the likelihood function in MLE
approach. The distribution :math:`p(\theta)` is called the Bayesian prior while the :math:`p(\theta | \mathcal{D})`
is termed as Bayesian posterior.

For convenience, the denominator of :eq:`Bayesian theorem` is a parameter :math:`\theta` independent distribution
that is reducible as a certain constant during calculation. Therefore it generally employs
:math:`p(\theta | \mathcal{D}) \propto p(\mathcal{D} | \theta) p(\theta)` for further calculations.
And also, during reduction it concerns more about the parameter related term. If a
:ref:`kernel <Kernel and scale>` like term unveiled during simplification, the corresponding distribution can be
established rationally.

Generally, the :math:`p(\theta)` and :math:`p(\theta | \mathcal{D})` are of the identical family of
probabilistic distribution, therefore the Bayesian prior and posterior are relative concepts. A updated Bayesian
model with calculated posterior, can be treated as prior for following learning tasks as well, through which manner
the Bayesian model can possess the property of self adaption to variation data.

Another important concept in Bayesian context, is that the prediction is also probabilistic distribution instead
of concrete numerics. As illustrated in the :numref:`Figure %s <bayes predictive graph>`, the observed data
:math:`\mathcal{D}` and the variable :math:`x^*` are both in dependence with the parameter :math:`\theta`.

.. figure:: https://github.com/user-attachments/assets/f71b4ea2-7d11-44ed-a540-c724ed1d943e
   :name: bayes predictive graph
   :width: 150
   :align: center

   graphical model of Bayesian predictive distribution

Based on the graphical model in :numref:`Figure %s <bayes predictive graph>`, the joint probability of
:math:`\theta`, :math:`x^*` and :math:`\mathcal{D}` is
:math:`p(\theta, x^*, \mathcal{D}) = p(x^* | \theta) p(\mathcal{D} | \theta) p(\theta)`. Consider the
:eq:`Bayesian theorem`, the posterior joint probability :math:`p(x^*, \theta | \mathcal{D})` will be:

.. math::
   :label: Bayesian posterior joint

   p(x^*, \theta | \mathcal{D}) &= \frac{p(x^* | \theta) p(\mathcal{D} | \theta) p(\theta)}{p(\mathcal{D})} \\
   &= p(x^* | \theta) p(\theta | \mathcal{D})

For prediction, it can be formulated via the marginalization on the parameter :math:`\theta` through
:math:`p(x^*) = \int p(x^* | \theta) p(\theta) d\theta`. As the conjugate property of :math:`p(\theta)` and
:math:`p(\theta | \mathcal{D})`, if it substitutes the :math:`p(\theta)` by :math:`p(\theta | \mathcal{D})`, the
Bayesian posterior predictive distribution can be obtained:

.. math::
   :label: Bayesian posterior predictive

   p(x^*) = \int p(x^*, \theta | \mathcal{D}) d\theta = \int p(x^* | \theta) p(\theta | \mathcal{D}) d\theta

_`Discrete distribution family`
-------------------------------

For a comprehensive understanding on the relationship among majority of common discrete distributions,
:numref:`Table %s <discrete distribution relations>` lists the typical sort of distributions in accordance with
the trial times :math:`n`, as well as the number of categories :math:`K`.

.. table:: relationship of discrete distributions
   :name: discrete distribution relations
   :align: center

   ====================================== ============= =============
   trials :math:`n`, categories :math:`K` :math:`K = 2` :math:`K > 2`
   ====================================== ============= =============
   :math:`n = 1`                          bernoulli     categorical
   :math:`n > 1`                          binomial      multinomial
   ====================================== ============= =============

For general, the format of multinomial distribution with :math:`n` trials and :math:`K` can be preferentially
investigated, due to it actually the super set of the three other ones. When :math:`K = 2`, it collapses to
categorical distribution; when :math:`n = 1`, it collapses to the binomial one. While for simultaneously
:math:`K = 2` and :math:`n = 1`, the bernoulli distribution.

In addition, such mathematical degeneration similarly exists in their conjugate prior distributions. For
categorical or multinomial distributions, the dirichlet distribution is always considered as the prior.
When the number of categories is 2, it uses beta distribution instead. However, beta distribution is merely
a specific kind of dirichlet distribution with only 2 parameters.

_`Multinomial distribution`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Without loss of generality, following interpretation and deduction will be conducted within the context of
multinomial distribution.

.. math::
   :label: multinomial bayes posterior 1

   p(\boldsymbol{\pi} | \boldsymbol{m}, M) &\propto p(\boldsymbol{m} | \boldsymbol{\pi}, M) p(\boldsymbol{\pi}) \\
   &= \{ \prod_{n=1}^{N} \mathrm{Mult}(\boldsymbol{m}_n | \boldsymbol{\pi}) \} \mathrm{Dir}(\boldsymbol{\pi} |
   \boldsymbol{\alpha})

Convert the calculation to logarithm space, and combine the :math:`\boldsymbol{\pi}` independent factors into
constant, the :eq:`multinomial bayes posterior 1` can be further simplified as:

.. math::
   :label: multinomial bayes posterior 2

   \ln p(\boldsymbol{\pi} | \boldsymbol{m}, M) &= \sum_{n=1}^N \ln \mathrm{Mult}(\boldsymbol{m}_n | \boldsymbol{\pi},
   M) + \ln \mathrm{Dir}(\boldsymbol{\pi} | \boldsymbol{\alpha}) + C_1 \\
   &= \sum_{n=1}^N \sum_{k=1}^{K} {m}_{n, k} \ln \pi_k + \sum_{k=1}^K (\alpha_k - 1) \ln \pi_k + C_2 \\
   &= \sum_{k=1}^K (\sum_{n=1}^N {m}_{n, k} + \alpha_k - 1) \cdot \ln \pi_k + C_3

Due to :math:`p(\boldsymbol{\pi} | \boldsymbol{m}, M)` is a probability distribution, an extra term that can
counteract the effect of :math:`C_3` then satisfy the normalization condition should be added unconstrainedly
when convert the :eq:`multinomial bayes posterior 2` into standard format. Here is unnecessary to make further
discussion. The final expression of :eq:`multinomial bayes posterior 2` showed that the Bayesian posterior of
:math:`p(\boldsymbol{\pi} | \boldsymbol{m}, M)` is exactly the kernel of a dirichlet distribution
:math:`\mathrm{Dir}(\boldsymbol{\pi} | \hat{\boldsymbol{\alpha}})`, with
:math:`\hat{\boldsymbol{\alpha}}` which satisfies:

.. math::
   :label: parameter of multinomial posterior

   \hat{\alpha}_k = \sum_{n=1}^N {m}_{n, k} + \alpha_k

As for the posterior predictive distribution of multinomial, apply the :eq:`Bayesian posterior predictive`,
the :math:`\boldsymbol{\pi}` marginalized distribution will be like:

.. math::
   :label: multinomial bayes predictive

   p(\boldsymbol{m}^* | M) &= \int p(\boldsymbol{m}^* | \boldsymbol{\pi}, M) p(\boldsymbol{\pi}) d\boldsymbol{\pi} \\
   &= \int \mathrm{Mult}(\boldsymbol{m}^* | \boldsymbol{\pi}, M) \mathrm{Dir}(\boldsymbol{\pi}|\boldsymbol{\alpha})
   d\boldsymbol{\pi} \\
   &= \int M! \prod_{k=1}^K \frac{\pi_k^{m^*_k}}{m^*_k !} \frac{\Gamma(\sum_{k=1}^K \alpha_k)}{\prod_{k=1}^K
   \Gamma(\alpha_k)} \prod_{k=1}^K \pi_k^{\alpha_k - 1} d\boldsymbol{\pi} \\
   &= \frac{M!}{\prod_{k=1}^K m^*_k !} \cdot \frac{\Gamma(\sum_{k=1}^K \alpha_k)}{\prod_{k=1}^K \Gamma(\alpha_k)}
   \int \prod_{k=1}^K \pi_k^{m^*_k + \alpha_k - 1} d\boldsymbol{\pi} \\
   &= \frac{M!}{\prod_{k=1}^K m^*_k !} \cdot \frac{\Gamma(\sum_{k=1}^K \alpha_k) \prod_{k=1}^K \Gamma(m^*_k +
   \alpha_k)}{\prod_{k=1}^K \Gamma(\alpha_k) \Gamma(\sum_{k=1}^K (m^*_k + \alpha_k))} \cdot \int
   \frac{\Gamma(\sum_{k=1}^K (m^*_k + \alpha_k))}{\prod_{k=1}^K \Gamma(m^*_k + \alpha_k)} \prod_{k=1}^K
   \pi_k^{m^*_k + \alpha_k - 1} d\boldsymbol{\pi} \\
   &= \frac{M!}{\prod_{k=1}^K m^*_k !} \cdot \frac{\Gamma(\sum_{k=1}^K \alpha_k) \prod_{k=1}^K \Gamma(m^*_k +
   \alpha_k)}{\prod_{k=1}^K \Gamma(\alpha_k) \Gamma(\sum_{k=1}^K (m^*_k + \alpha_k))} \cdot \int \mathrm{Dir}
   (\boldsymbol{\pi} | \boldsymbol{\alpha} + \boldsymbol{m}^*) d\boldsymbol{\pi} \\
   &\propto \prod_{k=1}^K \frac{\Gamma(m^*_k + \alpha_k)}{m^*_k ! \cdot \Gamma(\alpha_k)}

The last step can be established because :math:`\sum_{k=1}^K m^*_k = M`. From :eq:`multinomial bayes predictive`
it can finally deduce that it is the kernel of a dirichlet-multinomial distribution with parameter
:math:`M` and :math:`\boldsymbol{\alpha}` (see :ref:`[Glüsenkamp] <[Glüsenkamp]>`). Consider the conjugate property
of dirichlet prior as for multinomial distribution, replace the
:math:`\mathrm{Dir}(\boldsymbol{\pi} | \boldsymbol{\alpha})` by
:math:`\mathrm{Dir}(\boldsymbol{\pi} | \hat{\boldsymbol{\alpha}})` then the Bayesian posterior of multinomial
can be obtained.

Here it have to consider two sorts of special cases. The first one is :math:`M = 1`. Under that constraint,
the main likelihood function will become categorical distribution according to
:numref:`Table %s <discrete distribution relations>`. Its Bayesian posterior still keep the form of
:eq:`multinomial bayes posterior 2` but all of the variables (:math:`m_{n, k}` and :math:`m^*_k`) take the domain
of :math:`\{0, 1\}` instead of :math:`\{0, 1, \dots, M\}`. The posterior of categorical distribution is consequently
still dirichlet distribution with parameter in accordance with :eq:`parameter of multinomial posterior` as well.
However for its posteriori predictive, consider the :math:`0! = 1! = 1`, the :math:`p(\boldsymbol{m}^*)` is actually:

.. math::
   :label: categorical bayes predictive 1

   p (\boldsymbol{m}^*) = \frac{\Gamma(\sum_{k=1}^K \alpha_k) \prod_{k=1}^K \Gamma(m^*_k +
   \alpha_k)}{\prod_{k=1}^K \Gamma(\alpha_k) \Gamma(\sum_{k=1}^K (m^*_k + \alpha_k))}

Consider the probability of :math:`p(m^*_{k^\prime} = 1)`, because the :math:`\sum_{k=1}^K m^*_k = 1` and the
property :math:`\Gamma(x + 1) = x \Gamma(x)` of gamma function, the :eq:`categorical bayes predictive 1` can be
further simplified as:

.. math::
   :label: categorical bayes predictive 2

   p (m^*_{k^\prime} = 1) &= \frac{\Gamma(\sum_{k=1}^K \alpha_k) \Gamma(1 + \alpha_{k^\prime})
   \prod_{k^c \neq k^\prime} \Gamma(\alpha_{k^c})}{\prod_{k=1}^K \Gamma(\alpha_k) \Gamma(\sum_{k=1}^K \alpha_k
   + 1)} \\
   &= \frac{\Gamma(\sum_{k=1}^K \alpha_k) \cdot \alpha_{k^\prime} \cdot \Gamma(\alpha^{k^\prime})}{(\sum_{k=1}^K
   \alpha_k) \cdot \Gamma(\sum_{k=1}^K \alpha_k) \cdot \Gamma(\alpha_{k^\prime})} \\
   & = \frac{\alpha_{k^\prime}}{\sum_{k=1}^K \alpha_k}

Therefore the Bayesian posterior predictive of categorical distribution is another categorical one noted as
:math:`\mathrm{Cat}(\boldsymbol{m}^* | \{\frac{\alpha_k}{\sum_{i=1}^K \alpha_i}\}_{k=1}^K)`.

The second special case is for the binomial distribution with constraint :math:`K = 2`. In that condition, the
:eq:`multinomial bayes posterior 2` has only two parameters :math:`\alpha_1` and :math:`\alpha_2`, the dirichlet
prior will collapse to the beta distribution :math:`\mathrm{Beta}(x | \alpha_1, \alpha_2)` as well. Its predictive
also convert correspondingly like:

.. math::
   :label: binomial bayes predictive

   p (m^*_1 | M) &\propto \frac{\Gamma(m^*_1 + \alpha_1)}{m^*_1 ! \Gamma(\alpha_1)} \cdot \frac{\Gamma(M - m^*_1 +
   \alpha_2)}{(M - m^*_1)! \Gamma(\alpha_2)} \\
   &\propto \frac{M!}{m^*_1 ! (M - m^*_1) !} \cdot \frac{\Gamma(m^*_1 + \alpha_1) \Gamma(M - m^*_1 + \alpha_2)}{
   \Gamma(M + \alpha_1 + \alpha_2)} \cdot \frac{\Gamma(\alpha_1 + \alpha_2)}{\Gamma(\alpha_1) \Gamma(\alpha_2)}

Which is exactly the kernel of a certain beta binomial distribution.

If simultaneously consider the :math:`M = 1` and :math:`K = 2`. It can be conducted for the bernoulli likelihood,
its Bayesian posterior is beta distribution, while its predictive is another bernoulli.

For conclusion, the common likelihood functions with discrete distribution family can be summarized in the
:numref:`Table %s <summary of discrete family>`:

.. table:: Bayesian statistics of discrete distributions
   :name: summary of discrete family
   :align: center

   =========== ======================== ========= ========= =====================
   likelihood  parameter                condition conjugate predictive
   =========== ======================== ========= ========= =====================
   bernoulli   :math:`p`                :math:`-` beta      bernoulli
   binomial    :math:`p`                :math:`M` beta      beta binomial
   categorical :math:`\boldsymbol{\pi}` :math:`-` dirichlet categorical
   multinomial :math:`\boldsymbol{\pi}` :math:`M` dirichlet dirichlet multinomial
   =========== ======================== ========= ========= =====================

_`Poisson distribution`
~~~~~~~~~~~~~~~~~~~~~~~

Poisson distribution is a discrete probability distribution that models the probability of a given number of
events occurring in a fixed interval of time or space, given that these events occur with a known average rate
and independently of each other.   It is commonly used in various fields such as statistics, probability theory,
and even in some applications of artificial intelligence.

As for the poisson likelihood function, its conjugate prior and posterior are of gamma distributions. Let
:math:`p(x | \lambda) = \mathrm{Poi}(x | \lambda)`, :math:`p(x) = \mathrm{Gam}(\lambda | a, b)`, and :math:`N`
non-negative observations :math:`\textbf{X} = \{x_1, \dots, x_N \}`, its Bayesian posterior will be like:

.. math::
   :label: poisson bayes posterior

   p(\lambda | \textbf{X}) &\propto p(\textbf{X} | \lambda) p(\lambda) \\
   &= \{ \prod_{n=1}^N \mathrm{Poi}(x_n | \lambda) \} \mathrm{Gam}(\lambda | a, b)

For convenience, conduct the reduction in logarithmic space:

.. math::
   :label: log poisson bayes posterior

   \ln p(\lambda | \textbf{X}) &= \sum_{n=1}^N \ln \mathrm{Poi}(x_n | \lambda) + \ln \mathrm{Gam}(\lambda | a, b)
   + C_1 \\
   &= \sum_{n=1}^N \{ x_n \ln \lambda - \ln x_n ! - \lambda \} + (a-1) \ln \lambda - b \ln \lambda + \ln \left(
   \frac{b^a}{\Gamma(a)} \right) + C_1 \\
   &= (\sum_{n=1}^N x_n + a - 1) \ln \lambda - (N + b) \lambda + C_2

The final step of :eq:`log poisson bayes posterior` is established because that for :math:`p(\lambda | \textbf{X})`,
the variable :math:`\lambda` involved terms are just :math:`\lambda` and :math:`\ln \lambda`. Other :math:`\lambda`
independent factors are all included into the constant :math:`C_2`. The posterior of :eq:`log poisson bayes posterior`
obviously reveals the kernel of a gamma :math:`\mathrm{Gam}(\lambda | \hat{a}, \hat{b})`, with parameters
:math:`\hat{a}` and :math:`\hat{b}` that satisfies:

.. math::
   :label: poisson posterior parameters

   \hat{a} &= \sum_{n=1}^N x_n + a \\
   \hat{b} &= N + b

And for the predictive:

.. math::
   :label: poisson bayes predictive

   p(x^*) &= \int p(x^* | \lambda) p(\lambda) d\lambda \\
   &= \int \frac{\lambda^{x^*}}{x^* !} e^{-\lambda} \frac{b^a}{\Gamma(a)} \lambda^{a-1} e^{-b\lambda} d\lambda \\
   &= \frac{b^a}{x^* ! \Gamma(a)} \cdot \frac{\Gamma(x^* + a)}{(x^* + a)^{(1 + b)}} \int  \frac{(x^* + a)^{(1 + b)}
   }{\Gamma(x^* + a)} \lambda^{x^* + a - 1} e^{-(1+b)\lambda} d\lambda \\
   &= \frac{b^a}{x^* ! \Gamma(a)} \cdot \frac{\Gamma(x^* + a)}{(x^* + a)^{(1 + b)}} \int \mathrm{Gam}(\lambda |
   x^* + a, 1 + b) d\lambda \\
   &= \frac{b^a}{x^* ! \Gamma(a)} \cdot \frac{\Gamma(x^* + a)}{(x^* + a)^{(1 + b)}} \\
   &= \frac{\Gamma(x^* + a)}{x^* ! \Gamma(a)} \cdot (\frac{1}{b+1})^{x^*} (1-\frac{1}{b+1})^a

Thus, the predictive of poisson distribution is a negative binomial distribution with parameter :math:`a` and
:math:`(1+b)^{-1}`. As for its Bayesian posterior predictive, replace the :math:`a` and :math:`b` by :math:`\hat{a}`
and :math:`\hat{b}` as showed in :eq:`poisson posterior parameters`.

_`Continuous distribution family`
---------------------------------

Gauss, also called normal distribution, is a conventional but widely used continuous distribution. In statistics and
probability theory, beyond its fundamental role in describing natural phenomena and modeling error distributions, the
normal distribution has evolved to serve as a cornerstone in statistical inference.   In hypothesis testing, for
instance, the null hypothesis is often assumed to follow a normal distribution under certain conditions, allowing
researchers to determine the statistical significance of their findings. This framework has facilitated
groundbreaking discoveries in numerous scientific disciplines, where the precision and reliability of conclusions
are paramount.

As for Gauss likelihood function, it is acceptable for 3 different types of conjugate priors. Similarly without loss
of generality, all following reduction will be conducted in the context of multivariate Gauss. The properties of
univariate one will be further investigated through distribution degeneration. For convenience, here introduces
precision matrix :math:`\boldsymbol{\Lambda}` which is the inverse of covariance matrix :math:`\boldsymbol{\Sigma}`
of Gauss (:math:`\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}, \boldsymbol{\Sigma})` is equivalent to
:math:`\mathcal{N}(\boldsymbol{x}|\boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1})`).

- **Gauss prior**

For the likelihood :math:`\mathcal{N}(\boldsymbol{x} | \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1})`, the prior of
another Gauss :math:`\mathcal{N}(\boldsymbol{\mu} | \boldsymbol{m}, \boldsymbol{\Lambda}_{\boldsymbol{\mu}}^{-1})`
is the framework to infer the unknown mean :math:`\boldsymbol{\mu}`. In that case, the precision
:math:`\boldsymbol{\Lambda}` is the given condition during whole calculation.

Therefore for :math:`N` observations :math:`\boldsymbol{X} = \{\boldsymbol{x}_1, \dots, \boldsymbol{x}_N\}`, its
Bayesian posterior will be:

.. math::
   :label: Gauss bayes posterior in prior 1

   p(\boldsymbol{\mu} | \boldsymbol{X}) &\propto p(\boldsymbol{X} | \boldsymbol{\mu}) p(\boldsymbol{\mu}) \\
   &= \left\{ \prod_{n=1}^N \mathcal{N}(\boldsymbol{x}_n | \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1}) \right\}
   \mathcal{N}(\boldsymbol{\mu} | \boldsymbol{m}, \boldsymbol{\Lambda}_{\boldsymbol{\mu}}^{-1})

Conduct further calculation in logarithmic space:

.. math::
   :label: log Gauss bayes posterior in prior 1

   \ln p(\boldsymbol{\mu} | \boldsymbol{X}) &=  \sum_{n=1}^N \ln \mathcal{N}(\boldsymbol{x}_n | \boldsymbol{\mu},
   \boldsymbol{\Lambda}^{-1}) + \ln \mathcal{N}(\boldsymbol{\mu} | \boldsymbol{m},
   \boldsymbol{\Lambda}_{\boldsymbol{\mu}}^{-1}) + C_1 \\
   &= -\frac{1}{2} \left\{ \sum_{n=1}^N (\boldsymbol{x}_n - \boldsymbol{\mu})^\top \boldsymbol{\Lambda}
   (\boldsymbol{x}_n - \boldsymbol{\mu})  + (\boldsymbol{\mu} - \boldsymbol{m})^\top
   \boldsymbol{\Lambda}_{\boldsymbol{\mu}} (\boldsymbol{\mu} - \boldsymbol{m}) \right\} + C_2 \\
   &= -\frac{1}{2} \left\{ \boldsymbol{\mu}^\top (N\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_{\boldsymbol{\mu}})
   \boldsymbol{\mu} - 2\boldsymbol{\mu}^\top (\boldsymbol{\Lambda} \sum_{n=1}^N \boldsymbol{x}_n +
   \boldsymbol{\Lambda}_{\boldsymbol{\mu}} \boldsymbol{m}) \right\} + C_3 \\
   &= -\frac{1}{2} \left\{ \boldsymbol{\mu}^\top \hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}} \boldsymbol{\mu} -
   2 \boldsymbol{\mu}^\top \hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}} \hat{\boldsymbol{m}} \right\} + C_3 \\
   &= -\frac{1}{2} \left\{ (\boldsymbol{\mu}-\hat{\boldsymbol{m}})^\top \hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}}
   (\boldsymbol{\mu} - \hat{\boldsymbol{m}}) \right\} + C_4

Thus, the Bayesian posterior of Gauss used Gauss prior is also another Gauss distribution
:math:`\mathcal{N}(\boldsymbol{\mu} | \hat{\boldsymbol{m}}, \hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}}^{-1})` with
parameters of :math:`\hat{\boldsymbol{m}}` and :math:`\hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}}` where:

.. math::
   :label: solution of Gauss posterior in prior 1

   \hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}} &= N\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_{\boldsymbol{\mu}} \\
   \hat{\boldsymbol{m}} &= \hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}}^{-1} (\boldsymbol{\Lambda} \sum_{n=1}^N
   \boldsymbol{x}_n + \boldsymbol{\Lambda}_{\boldsymbol{\mu}} \boldsymbol{m})

Because :math:`p(\boldsymbol{x}^*|\boldsymbol{\mu}) \propto p(\boldsymbol{\mu}|\boldsymbol{x}^*) p(\boldsymbol{x}^*)`,
the predictive under Gauss prior can be calculated via:

.. math::
   :label: predictive in Gauss prior 1

   \ln p(\boldsymbol{x}^*) = \ln p(\boldsymbol{x}^* | \boldsymbol{\mu}) - \ln p(\boldsymbol{\mu}|\boldsymbol{x}^*) + C

Where the :math:`p(\boldsymbol{\mu}|\boldsymbol{x}^*)` can be defined as taking one :math:`\boldsymbol{x}^*` sample.
Thus, from :eq:`solution of Gauss posterior in prior 1`, the :math:`p(\boldsymbol{x}^*|\boldsymbol{\mu})` will be:

.. math::
   :label: predictive in Gauss prior 2

   p(\boldsymbol{x}^*|\boldsymbol{\mu}) &= \mathcal{N} (\boldsymbol{\mu} | (\boldsymbol{\Lambda} +
   \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1} (\boldsymbol{\Lambda x}^* + \boldsymbol{\Lambda_{\mu} m}),
   (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1}) \\
   &= \mathcal{N} (\boldsymbol{\mu} | \boldsymbol{m}(\boldsymbol{x}^*), (\boldsymbol{\Lambda} +
   \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1})

In this circumstance, consider the :math:`\boldsymbol{\Lambda}` and :math:`\boldsymbol{\Lambda_{\mu}}` are both
symmetric matrices, the :eq:`predictive in Gauss prior 1` can be simplified by the following steps:

.. math::
   :label: predictive in Gauss prior 3

   \ln p(\boldsymbol{x}^*) =& -\frac{1}{2} (\boldsymbol{x}^* - \boldsymbol{\mu})^\top \boldsymbol{\Lambda}
   (\boldsymbol{x}^* - \boldsymbol{\mu}) + \frac{1}{2} \left\{ \left[\boldsymbol{\mu} -\boldsymbol{m}(\boldsymbol{x}^*)
   \right]^\top (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu}) \left[ \boldsymbol{\mu} -
   \boldsymbol{m}(\boldsymbol{x}^*) \right] \right\} + C_1 \\
   \propto& -\frac{1}{2} \left[ \boldsymbol{x}^{*\top} \boldsymbol{\Lambda} \boldsymbol{x}^* - 2 \boldsymbol{x}^{*\top}
   \boldsymbol{\Lambda} \boldsymbol{\mu} + C_2 \right] + \frac{1}{2} \left[ \boldsymbol{m}(\boldsymbol{x}^*)^\top
   (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu}) \boldsymbol{m}(\boldsymbol{x}^*) -
   2 \boldsymbol{\mu}^\top (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu})
   \boldsymbol{m}(\boldsymbol{x}^*) + C_3 \right] \\
   \propto& -\frac{1}{2} \left[ \boldsymbol{x}^{*\top} \boldsymbol{\Lambda} \boldsymbol{x}^* - 2 \boldsymbol{x}^{*\top}
   \boldsymbol{\Lambda} \boldsymbol{\mu} \right] + \frac{1}{2} \left\{ (\boldsymbol{\Lambda x}^* +
   \boldsymbol{\Lambda_{\mu} m})^\top \left[ (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1}
   \right]^\top (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu}) (\boldsymbol{\Lambda} +
   \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1} (\boldsymbol{\Lambda x}^* + \boldsymbol{\Lambda_{\mu} m}) \right\} \\
   &- \left[ \boldsymbol{\mu}^\top (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu}) (\boldsymbol{\Lambda}
   + \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1} (\boldsymbol{\Lambda x}^* + \boldsymbol{\Lambda_{\mu} m})
   + C_3 \right] \\
   =& -\frac{1}{2} \left[ \boldsymbol{x}^{*\top} \boldsymbol{\Lambda} \boldsymbol{x}^* - 2 \boldsymbol{x}^{*\top}
   \boldsymbol{\Lambda} \boldsymbol{\mu} \right] + \frac{1}{2} \left[ \boldsymbol{x}^* \boldsymbol{\Lambda}
   (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1} \boldsymbol{\Lambda x}^* + 2
   \boldsymbol{x}^{*\top} \boldsymbol{\Lambda} (\boldsymbol{\Lambda} + \boldsymbol{\Lambda}_\boldsymbol{\mu})^{-1}
   \boldsymbol{\Lambda_{\mu} m} - 2 \boldsymbol{x}^{*\top} \boldsymbol{\Lambda \mu} + C_4 \right] \\
   =& -\frac{1}{2} \left\{ \boldsymbol{x}^{*\top} \left[ \boldsymbol{\Lambda} - \boldsymbol{\Lambda}
   (\boldsymbol{\Lambda} + \boldsymbol{\Lambda_\mu})^{-1} \boldsymbol{\Lambda} \right] \boldsymbol{x}^* -
   2 \boldsymbol{x}^{*\top} \boldsymbol{\Lambda} (\boldsymbol{\Lambda} + \boldsymbol{\Lambda_\mu})^{-1}
   \boldsymbol{\Lambda_\mu m}  \right\} + C_5

Therefore, its Bayesian predictive is still a sort of Gauss distribution
:math:`\mathcal{N}(\boldsymbol{x}^* | \boldsymbol{\mu}^*, \boldsymbol{\Lambda}^{* -1})` that:

.. math::
   :label: solution of Gauss predictive in prior 1

   \boldsymbol{\Lambda}^* &= \boldsymbol{\Lambda} - \boldsymbol{\Lambda} (\boldsymbol{\Lambda} +
   \boldsymbol{\Lambda_\mu})^{-1} \boldsymbol{\Lambda} \\
   &= \boldsymbol{\Lambda} - \boldsymbol{\Lambda I} (\boldsymbol{\Lambda} +
   \boldsymbol{\Lambda_\mu})^{-1} \boldsymbol{I \Lambda} \\
   &= (\boldsymbol{\Lambda}^{-1} + \boldsymbol{I \Lambda_{\mu}}^{-1} \boldsymbol{I})^{-1} \\
   &= (\boldsymbol{\Lambda}^{-1} + \boldsymbol{\Lambda_{\mu}}^{-1})^{-1} \\
   \boldsymbol{\mu}^* &= \boldsymbol{\Lambda}^{* -1} \boldsymbol{\Lambda} (\boldsymbol{\Lambda} +
   \boldsymbol{\Lambda_\mu})^{-1} \boldsymbol{\Lambda_\mu m} \\
   &= \boldsymbol{\Lambda}^{* -1} \boldsymbol{\Lambda} [\boldsymbol{\Lambda}^{-1} - \boldsymbol{\Lambda}^{-1}
   \boldsymbol{\Lambda}^* \boldsymbol{\Lambda}^{-1}] \boldsymbol{\Lambda_{\mu} m} \\
   &= (\boldsymbol{\Lambda}^{* -1} \boldsymbol{\Lambda_{\mu}} - \boldsymbol{\Lambda}^{-1}
   \boldsymbol{\Lambda_{\mu}}) \boldsymbol{m} \\
   & = (\boldsymbol{\Lambda}^{-1} + \boldsymbol{\Lambda_{\mu}}^{-1} - \boldsymbol{\Lambda}^{-1})
   \boldsymbol{\Lambda_{\mu} m} = \boldsymbol{m}

The reduction of :eq:`solution of Gauss predictive in prior 1` can be established by Sherman–Morrison–Woodbury
formula (see :ref:`[Higham2002] <[Higham2002]>`). As for Bayesian posterior predictive, replace all the
:math:`\boldsymbol{m}` and :math:`\boldsymbol{\Lambda_{\mu}}` by :math:`\hat{\boldsymbol{m}}` and
:math:`\hat{\boldsymbol{\Lambda}}_{\boldsymbol{\mu}}` as noted in :eq:`solution of Gauss posterior in prior 1`.

If it confines all :math:`\boldsymbol{\mu}` related variables :math:`\in \mathbb{R}^1`, and all
:math:`\boldsymbol{\Lambda}` ones are :math:`\in \mathbb{R}^{1 \times 1}` (e.g. :math:`\lambda = \sigma^2`), all
above conclusions can be applied in univariate Gauss.

- **Wishart prior**

For the likelihood :math:`\mathcal{N}(\boldsymbol{x} | \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1})`, the prior of
a Wishart distribution :math:`\mathcal{W}(\boldsymbol{\Lambda} | \mu, \boldsymbol{W})`
is the framework to infer the unknown precision :math:`\boldsymbol{\Lambda}`. Conditions of
:math:`\boldsymbol{W} \in \mathbb{R}^{D \times D}` and :math:`\nu > D - 1` are established. In that case, the mean
vector :math:`\boldsymbol{\mu}` is the given condition during whole calculation.

Therefore for :math:`N` observations :math:`\boldsymbol{X} = \{\boldsymbol{x}_1, \dots, \boldsymbol{x}_N\}`, its
Bayesian posterior will be:

.. math::
   :label: Gauss bayes posterior in prior 2

   \ln p(\boldsymbol{\Lambda} | \boldsymbol{X}) &\propto \ln \left\{ \left[ \prod_{n=1}^N \mathcal{N}(\boldsymbol{x}_n
   | \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1}) \right] \mathcal{W}(\boldsymbol{\Lambda} | \nu, \boldsymbol{W})
   \right\} + C_1 \\
   &= \sum_{n=1}^N \ln \mathcal{N} (\boldsymbol{x}_n | \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1}) + \ln \mathcal{W}
   (\boldsymbol{\Lambda} | \nu, \boldsymbol{W}) + C_1 \\
   &= \frac{N + \nu - D - 1}{2} \ln | \boldsymbol{\Lambda} | - \frac{1}{2} \mathrm{Tr} \left\{ [\sum_{n=1}^N
   (\boldsymbol{x}_n - \boldsymbol{\mu})(\boldsymbol{x}_n - \boldsymbol{\mu})^\top + \boldsymbol{W}^{-1}]
   \boldsymbol{\Lambda} \right\} + C_2

The last step of :eq:`Gauss bayes posterior in prior 2` is established because that for scalar
:math:`\boldsymbol{x}^\top \boldsymbol{\Lambda x} = \mathrm{Tr}(\boldsymbol{x}^\top \boldsymbol{\Lambda x})` and
:math:`\mathrm{Tr}(\boldsymbol{ABC}) = \mathrm{Tr}(\boldsymbol{BCA}) = \mathrm{Tr}(\boldsymbol{CAB})`. Consequently,
the Bayesian posterior in condition of Wishart prior is also another Wishart distribution
:math:`\mathcal{W}(\boldsymbol{\Lambda} | \hat{\nu}, \hat{\boldsymbol{W}})` that:

.. math::
   :label: solution of Gauss posterior in prior 2

   \hat{\nu} &= N + \nu \\
   \hat{\boldsymbol{W}}^{-1} &= \sum_{n=1}^N (\boldsymbol{x}_n - \boldsymbol{\mu})(\boldsymbol{x}_n -
   \boldsymbol{\mu})^\top + \boldsymbol{W}^{-1}

Because :math:`p(\boldsymbol{x}^*|\boldsymbol{\Lambda})\propto p(\boldsymbol{\Lambda}|\boldsymbol{x}^*)
p(\boldsymbol{x}^*)`, the predictive under Wishart prior can be calculated via:

.. math::
   :label: predictive in Wishart prior 1

   \ln p(\boldsymbol{x}^*) = \ln p(\boldsymbol{x}^* | \boldsymbol{\Lambda}) - \ln p(\boldsymbol{\Lambda} |
   \boldsymbol{x}^*) + C

Takes one :math:`\boldsymbol{x}^*` sample to explicitly express the :math:`p(\boldsymbol{\Lambda}|\boldsymbol{x}^*)`,
from the :eq:`solution of Gauss posterior in prior 2`, the following relationship can be ascertained:

.. math::
   :label: predictive in Wishart prior 2

   p(\boldsymbol{\Lambda} | \boldsymbol{x}^*) = \mathcal{W} (\boldsymbol{\Lambda} | 1 + \nu, [(\boldsymbol{x}^* -
   \boldsymbol{\mu})(\boldsymbol{x}^* - \boldsymbol{\mu})^\top + \boldsymbol{W}^{-1}]^{-1})

In this circumstance, the :eq:`predictive in Wishart prior 1` can be simplified by the following steps:

.. math::
   :label: predictive in Wishart prior 3

   \ln p(\boldsymbol{x}^*) =& -\frac{1}{2} (\boldsymbol{x}^* - \boldsymbol{\mu})^\top \boldsymbol{\Lambda}
   (\boldsymbol{x}^* - \boldsymbol{\mu}) + \frac{1}{2}\mathrm{Tr} \left\{ \left[ (\boldsymbol{x}^* -
   \boldsymbol{\mu})(\boldsymbol{x}^* - \boldsymbol{\mu})^\top + \boldsymbol{W}^{-1} \right]\boldsymbol{\Lambda}
   \right\} \\
   &+ \frac{\nu+1}{2} \ln | [(\boldsymbol{x}^* - \boldsymbol{\mu})(\boldsymbol{x}^* - \boldsymbol{\mu})^\top +
   \boldsymbol{W}^{-1}]^{-1} | + C_1 \\
   =& -\frac{\nu+1}{2} \ln | (\boldsymbol{x}^* - \boldsymbol{\mu})(\boldsymbol{x}^* - \boldsymbol{\mu})^\top +
   \boldsymbol{W}^{-1} | + C_2 \\
   =& -\frac{\nu+1}{2} \ln | \boldsymbol{I} + \boldsymbol{W} (\boldsymbol{x}^* - \boldsymbol{\mu})(\boldsymbol{x}^* -
   \boldsymbol{\mu})^\top | + C_3 \\
   =& -\frac{\nu+1}{2} \ln \left[1 + (\boldsymbol{x}^* - \boldsymbol{\mu})^\top \boldsymbol{W} (\boldsymbol{x}^* -
   \boldsymbol{\mu}) \right] + C_3

The reduction process in :eq:`predictive in Wishart prior 3` has employed the relation
:math:`| \boldsymbol{I} + \boldsymbol{ab}^\top | = | 1 + \boldsymbol{b}^\top \boldsymbol{a} |`. From final
expression of :eq:`predictive in Wishart prior 3`, it reveals the kernel of multivariate student-t distribution
:math:`\mathrm{Stu}(\boldsymbol{x} | \boldsymbol{\mu}_s, \boldsymbol{\Lambda}_s, \nu_s)` where:

.. math::
   :label: solution of Gauss predictive in prior 2

   \boldsymbol{\mu}_s &= \boldsymbol{\mu} \\
   \nu_s &= \nu + 1 - D \\
   \boldsymbol{\Lambda}_s &= \nu_s \boldsymbol{W}

For Bayesian posterior predictive in the condition of Wishart prior, replace all the :math:`\nu` and
:math:`\boldsymbol{W}` with :math:`\hat{\nu}` and :math:`\hat{\boldsymbol{W}}` respectively, as noted
in :eq:`solution of Gauss posterior in prior 2`.

If it confines all dimension related variables into the domain :math:`\mathbb{R}^1`, the Wishart distribution
will collapse to :math:`\mathcal{W}(\Lambda | \nu, W)` so that:

.. math::
   :label: degeneration of Wishart

   \ln \mathcal{W}(\Lambda | \nu, W) &\propto \frac{\nu - 2}{2} \ln \Lambda - \frac{\Lambda}{2W} + C_1 \\
   &= (\frac{\nu}{2} - 1) \ln \Lambda - \frac{1}{2W} \Lambda + C_1 \sim \ln \mathrm{Gam} (\Lambda | \frac{\nu}{2},
   \frac{1}{2W})

The multivariate student-t distribution will collapse to univariate one as well.

- **Gauss-Wishart prior**

For the likelihood :math:`\mathcal{N}(\boldsymbol{x} | \boldsymbol{\mu}, \boldsymbol{\Lambda}^{-1})`, if
mean :math:`\boldsymbol{\mu}` and precision :math:`\boldsymbol{\Lambda}` are both unknown, it employs the
Gaussian-Wishart distribution as conjugate prior to infer those two parameters. A Gaussian-Wishart distribution
:math:`\mathcal{NW}(\boldsymbol{\mu}, \boldsymbol{\Lambda} | \boldsymbol{m}, \beta, \nu, \boldsymbol{W})` can be
seen as the coupling of Wishart and Gauss distribution:

.. math::
   :label: Gaussian-Wishart distribution

   p(\boldsymbol{\mu}, \boldsymbol{\Lambda}) &= \mathcal{NW}(\boldsymbol{\mu}, \boldsymbol{\Lambda} | \boldsymbol{m},
   \beta, \nu, \boldsymbol{W}) \\
   &= \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Lambda} | \boldsymbol{m}, (\beta \boldsymbol{\Lambda})^{-1})
   \mathcal{W}(\boldsymbol{\Lambda} | \nu, \boldsymbol{W})

In reduction, firstly uses the
:math:`\mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Lambda} | \boldsymbol{m}, (\beta \boldsymbol{\Lambda})^{-1})` only
to infer the posterior :math:`\hat{\boldsymbol{m}}` and :math:`\hat{\beta}`. Takes the precision
:math:`\boldsymbol{\Lambda}` as a given condition in this step, according to
:eq:`solution of Gauss posterior in prior 1`, the posterior will be like:

.. math::
   :label: Gauss bayes posterior in prior 3

   p(\boldsymbol{\mu} | \boldsymbol{\Lambda}, \boldsymbol{X}) = \mathcal{N} (\boldsymbol{\mu} | \hat{\boldsymbol{m}},
   (\hat{\beta} \boldsymbol{\Lambda})^{-1})

Where:

.. math::
   :label: solution of Gauss posterior in prior 3

   \hat{\beta} \boldsymbol{\Lambda} &= N \boldsymbol{\Lambda} + \beta \boldsymbol{\Lambda} \\
   \hat{\beta} &= N + \beta \\
   \hat{\boldsymbol{m}} &= (\hat{\beta} \boldsymbol{\Lambda})^{-1} (\boldsymbol{\Lambda} \sum_{n=1}^N
   \boldsymbol{x}_n + \beta \boldsymbol{\Lambda m}) \\
   &= \frac{1}{N+\beta} (\sum_{n=1}^N \boldsymbol{x}_n + \beta \boldsymbol{m})

Because the Bayesian formula:

.. math::
   :label: Gauss bayes posterior in prior 3 distribution relation

   \because&\ p(\boldsymbol{\mu} | \boldsymbol{\Lambda}, \boldsymbol{X}) p(\boldsymbol{\Lambda} | \boldsymbol{X})
   = \frac{p(\boldsymbol{X} | \boldsymbol{\mu}, \boldsymbol{\Lambda})p(\boldsymbol{\mu},
   \boldsymbol{\Lambda})}{p(\boldsymbol{X})} \\
   \therefore&\ \ln p(\boldsymbol{\Lambda} | \boldsymbol{X}) = \ln p(\boldsymbol{X} | \boldsymbol{\mu},
   \boldsymbol{\Lambda}) + \ln p(\boldsymbol{\mu}, \boldsymbol{\Lambda}) - \ln p(\boldsymbol{\mu} |
   \boldsymbol{\Lambda}, \boldsymbol{X}) + C

Put :eq:`Gaussian-Wishart distribution` and :eq:`Gauss bayes posterior in prior 3` into the
:eq:`Gauss bayes posterior in prior 3 distribution relation`, reduce the :math:`\boldsymbol{\Lambda}` related terms:

.. math::
   :label: Gauss bayes posterior in prior 3 reduction 1

   \ln p(\boldsymbol{\Lambda} | \boldsymbol{X}) =& \ln \mathcal{N} (\boldsymbol{X} | \boldsymbol{\mu},
   \boldsymbol{\Lambda}^{-1}) + \ln \mathcal{N} (\boldsymbol{\mu} | \boldsymbol{m}, (\beta \boldsymbol{\Lambda})^{-1})
   + \ln \mathcal{W} (\boldsymbol{\Lambda} | \nu, \boldsymbol{W}) - \ln \mathcal{N} (\boldsymbol{\mu} |
   \hat{\boldsymbol{m}}, (\hat{\beta} \boldsymbol{\Lambda})^{-1}) + C_1 \\
   =& \frac{1}{2} \sum_{n=1}^N [ \ln | \boldsymbol{\Lambda} | - (\boldsymbol{x}_n - \boldsymbol{\mu})^\top
   \boldsymbol{\Lambda} (\boldsymbol{x}_n - \boldsymbol{\mu}) ] + \frac{1}{2} [ \ln | \beta \boldsymbol{\Lambda} | -
   \beta (\boldsymbol{\mu} - \boldsymbol{m})^\top \boldsymbol{\Lambda} (\boldsymbol{\mu} - \boldsymbol{m}) ] \\
   &+ \frac{\nu + D - 1}{2} \ln | \boldsymbol{\Lambda} | - \frac{1}{2} \mathrm{Tr}(\boldsymbol{W}^{-1}
   \boldsymbol{\Lambda}) - \frac{1}{2} [ \ln | \hat{\beta} \boldsymbol{\Lambda} | - \hat{\beta} (\boldsymbol{\mu} -
   \hat{\boldsymbol{m}})^\top \boldsymbol{\Lambda} (\boldsymbol{\mu} - \hat{\boldsymbol{m}}) ] + C_2 \\
   =& \frac{1}{2} [ \hat{\beta} (\boldsymbol{\mu} - \hat{\boldsymbol{m}})^\top \boldsymbol{\Lambda}
   (\boldsymbol{\mu} - \hat{\boldsymbol{m}}) - \sum_{n=1}^N (\boldsymbol{x}_n - \boldsymbol{\mu})^\top
   \boldsymbol{\Lambda} (\boldsymbol{x}_n - \boldsymbol{\mu}) - \beta (\boldsymbol{\mu} - \boldsymbol{m})^\top
   \boldsymbol{\Lambda} (\boldsymbol{\mu} - \boldsymbol{m}) - \mathrm{Tr}(\boldsymbol{W}^{-1}\boldsymbol{\Lambda}) ] \\
   &+ \frac{N+\nu-D-1}{2} \ln | \boldsymbol{\Lambda} | + C_3

Substitute part of variables in the :eq:`Gauss bayes posterior in prior 3 reduction 1` with
:eq:`solution of Gauss posterior in prior 3`, the first term in :eq:`Gauss bayes posterior in prior 3 reduction 1`
will be like:

.. math::
   :label: Gauss bayes posterior in prior 3 reduction 2

   \frac{1}{2}[\cdot] =& \frac{1}{2} [(N+\beta) \boldsymbol{\mu}^\top \boldsymbol{\Lambda \mu} -
   2 \boldsymbol{\mu}^\top \boldsymbol{\Lambda} (\sum_{n=1}^N \boldsymbol{x}_n + \beta \boldsymbol{m}) + \hat{\beta}
   \hat{\boldsymbol{m}}^\top \boldsymbol{\Lambda} \hat{\boldsymbol{m}} - \sum_{n=1}^N \boldsymbol{x}_n^\top
   \boldsymbol{\Lambda} \boldsymbol{x}_n + 2\boldsymbol{\mu}^\top \boldsymbol{\Lambda} \sum_{n=1}^N \boldsymbol{x}_n \\
   &- N \boldsymbol{\mu}^\top \boldsymbol{\Lambda} \boldsymbol{\mu} - \beta \boldsymbol{\mu}^\top \boldsymbol{\Lambda}
   \boldsymbol{\mu} + 2\beta \boldsymbol{\mu}^\top \boldsymbol{\Lambda} \boldsymbol{m} - \beta \boldsymbol{m}^\top
   \boldsymbol{\Lambda} \boldsymbol{m} - \mathrm{Tr}(\boldsymbol{W}^{-1}\boldsymbol{\Lambda})] \\
   =& \frac{1}{2} [\hat{\beta} \hat{\boldsymbol{m}}^\top \boldsymbol{\Lambda} \hat{\boldsymbol{m}} - \sum_{n=1}^N
   \boldsymbol{x}_n^\top \boldsymbol{\Lambda} \boldsymbol{x}_n - \beta \boldsymbol{m}^\top \boldsymbol{\Lambda m}
   - \mathrm{Tr}(\boldsymbol{W}^{-1}\boldsymbol{\Lambda}) ] \\
   =& \frac{1}{2} [\mathrm{Tr}(\hat{\beta} \hat{\boldsymbol{m}} \hat{\boldsymbol{m}}^\top \boldsymbol{\Lambda}) -
   \mathrm{Tr}(\sum_{n=1}^N \boldsymbol{x}_n \boldsymbol{x}_n^\top \boldsymbol{\Lambda} ) - \mathrm{Tr} (
   \beta \boldsymbol{m} \boldsymbol{m}^\top \boldsymbol{\Lambda}) - \mathrm{Tr}(\boldsymbol{W}^{-1}
   \boldsymbol{\Lambda})] \\
   =& -\frac{1}{2} \mathrm{Tr}[(\sum_{n=1}^N \boldsymbol{x}_n \boldsymbol{x}_n^\top + \beta \boldsymbol{m}
   \boldsymbol{m}^\top - \hat{\beta} \hat{\boldsymbol{m}} \hat{\boldsymbol{m}}^\top + \boldsymbol{W}^{-1})
   \boldsymbol{\Lambda}]

Therefore the final expression of :eq:`Gauss bayes posterior in prior 3 reduction 1` can be further simplified
as:

.. math::
   :label: Gauss bayes posterior in prior 3 reduction 3

   \ln p(\boldsymbol{\Lambda} | \boldsymbol{X}) = \frac{N+\nu-D-1}{2} \ln | \boldsymbol{\Lambda} | -\frac{1}{2}
   \mathrm{Tr}[(\sum_{n=1}^N \boldsymbol{x}_n \boldsymbol{x}_n^\top + \beta \boldsymbol{m} \boldsymbol{m}^\top
   - \hat{\beta} \hat{\boldsymbol{m}} \hat{\boldsymbol{m}}^\top + \boldsymbol{W}^{-1})
   \boldsymbol{\Lambda}] + C

Obviously for the Wishart part of conjugate, the :eq:`Gauss bayes posterior in prior 3 reduction 3` shows the
kernel of another Wishart :math:`\mathcal{W} (\boldsymbol{\Lambda} | \hat{\mu}, \hat{\boldsymbol{W}})` where:

.. math::
   :label: solution of Gauss posterior in prior 3 extra

   \hat{\nu} &= N + \nu \\
   \hat{\boldsymbol{W}}^{-1} &= \sum_{n=1}^N \boldsymbol{x}_n \boldsymbol{x}_n^\top + \beta \boldsymbol{m}
   \boldsymbol{m}^\top - \hat{\beta} \hat{\boldsymbol{m}} \hat{\boldsymbol{m}}^\top + \boldsymbol{W}^{-1}

The solutions in :eq:`solution of Gauss posterior in prior 3` and :eq:`solution of Gauss posterior in prior 3 extra`
simultaneously constitute the Bayesian posterior :math:`\mathcal{NW}(\boldsymbol{\mu}, \boldsymbol{\Lambda} |
\hat{\boldsymbol{m}}, \hat{\beta}, \hat{\nu}, \hat{\boldsymbol{W}})`, in the condition of using Gauss-Wishart
prior.

For the Bayesian posterior predictive under the Gauss-Wishart distribution, use one single point
:math:`\boldsymbol{x}^*` likely to express the marginalized :math:`p(\boldsymbol{x}^*)`, merge all
:math:`\boldsymbol{x}^*` involved terms so that:

.. math::
   :label: predictive in Gauss-Wishart prior 1

   \ln p(\boldsymbol{x}^*) =& \ln p(\boldsymbol{x}^* | \boldsymbol{\mu}, \boldsymbol{\Lambda}) - \ln
   p(\boldsymbol{\mu}, \boldsymbol{\Lambda} | \boldsymbol{x}^*) + C_1 \\
   =& \ln \mathcal{N}(\boldsymbol{x}^* | \boldsymbol{\mu}, \boldsymbol{\Lambda}) - \ln \mathcal{N}(\boldsymbol{\mu} |
   \boldsymbol{m}(\boldsymbol{x}^*), ((1+\beta)\boldsymbol{\Lambda})^{-1}) - \ln \mathcal{W} (\boldsymbol{\Lambda} |
   1+\nu, \boldsymbol{W}(\boldsymbol{x}^*)) + C_1 \\
   =& -\frac{1}{2} [(\boldsymbol{x}^* - \boldsymbol{\mu})^\top \boldsymbol{\Lambda} (\boldsymbol{x}^* -
   \boldsymbol{\mu})] + \frac{1}{2} \left\{ [\boldsymbol{\mu} - \boldsymbol{m}(\boldsymbol{x}^*)]^\top [(1+\beta)
   \boldsymbol{\Lambda} ] [\boldsymbol{\mu} - \boldsymbol{m}(\boldsymbol{x}^*)] \right\} + \frac{1}{2} \mathrm{Tr}[
   \boldsymbol{W}^{-1}(\boldsymbol{x}^*) \boldsymbol{\Lambda} ] \\
   &+  \frac{\nu+1}{2} \ln | \boldsymbol{W}(\boldsymbol{x}^*) | + C_2

On basis of :eq:`solution of Gauss posterior in prior 3` and :eq:`solution of Gauss posterior in prior 3 extra`,
replace :math:`\boldsymbol{m}(\boldsymbol{x}^*)` and :math:`\boldsymbol{W}^{-1}(\boldsymbol{x}^*)` by:

.. math::
   :label: predictive in Gauss-Wishart prior 2

   \boldsymbol{m}(\boldsymbol{x}^*) &= \frac{\boldsymbol{x}^* + \beta \boldsymbol{m}}{1 + \beta} \\
   \boldsymbol{W}^{-1}(\boldsymbol{x}^*) &= \boldsymbol{x}^* \boldsymbol{x}^{*\top} + \beta \boldsymbol{m}
   \boldsymbol{m}^\top - \frac{1}{1+\beta} (\boldsymbol{x}^* + \beta \boldsymbol{m})(\boldsymbol{x}^* + \beta
   \boldsymbol{m})^\top + \boldsymbol{W}^{-1} \\
   &= \frac{\beta}{1+\beta} \boldsymbol{x}^* \boldsymbol{x}^{*\top} + \frac{\beta(1+\beta) - \beta^2}{1+\beta}
   \boldsymbol{m} \boldsymbol{m}^\top - \frac{\boldsymbol{x}^* \boldsymbol{x}^{*\top} + 2\beta
   \boldsymbol{x}^* \boldsymbol{m}^\top+\beta^2 \boldsymbol{m}\boldsymbol{m}^\top }{1+\beta} + \boldsymbol{W}^{-1} \\
   &= \frac{\beta (\boldsymbol{x}^* \boldsymbol{x}^{*\top}  + \boldsymbol{m} \boldsymbol{m}^\top - 2 \beta
   \boldsymbol{x}^* \boldsymbol{m}^\top )}{1+\beta} + \boldsymbol{W}^{-1} \\
   &= \frac{\beta}{1+\beta} (\boldsymbol{x}^* - \boldsymbol{m})(\boldsymbol{x}^* - \boldsymbol{m})^\top +
   \boldsymbol{W}^{-1}

Under which condition, the :eq:`predictive in Gauss-Wishart prior 1` can be further simplified as:

.. math::
   :label: predictive in Gauss-Wishart prior 3

   \ln p(\boldsymbol{x}^*) =& - \frac{1}{2} [ \boldsymbol{x}^{*\top} \boldsymbol{\Lambda x}^* - 2
   \boldsymbol{x}^{*\top} \boldsymbol{\Lambda \mu}  - \frac{\boldsymbol{x}^* \boldsymbol{\Lambda x}^* }{1+\beta}
   + 2 \boldsymbol{x}^{*\top} \boldsymbol{\Lambda} (\boldsymbol{\mu} - \frac{\beta}{1+\beta} \boldsymbol{m}) -
   \frac{\beta}{1+\beta} \boldsymbol{x}^{*\top} \boldsymbol{\Lambda x}^* \\
   &+ \frac{\beta}{1+\beta} \cdot 2 \boldsymbol{x}^{*\top} \boldsymbol{\Lambda m} + \mathrm{Tr} (\boldsymbol{W}^{-1}
   \boldsymbol{\Lambda} ) ] + \frac{\nu+1}{2} \ln | \boldsymbol{W} (\boldsymbol{x}^*) | + C_3 \\
   =& -\frac{\nu+1}{2} \ln | \boldsymbol{W}^{-1} (\boldsymbol{x}^*) | + C_3 \\
   =& -\frac{\nu+1}{2} \ln | \frac{\beta}{1+\beta} (\boldsymbol{x}^* - \boldsymbol{m}) (\boldsymbol{x}^* -
   \boldsymbol{m})^\top + \boldsymbol{W}^{-1} | + C_3 \\
   =& -\frac{\nu+1}{2} \ln | \boldsymbol{I} + \frac{\beta}{1+\beta} [\boldsymbol{W}(\boldsymbol{x}^* -
   \boldsymbol{m})] (\boldsymbol{x}^* - \boldsymbol{m})^\top | + C_4 \\
   =& -\frac{\nu+1}{2} \ln \left[ 1 + \frac{\beta}{1+\beta} (\boldsymbol{x}^* - \boldsymbol{m})^\top \boldsymbol{W}
   (\boldsymbol{x}^* - \boldsymbol{m}) \right] + C_4

Be similar to :eq:`predictive in Wishart prior 3`, the final expression of :eq:`predictive in Gauss-Wishart prior 3`
shows the kernel of a multivariate student-t
:math:`\mathrm{Stu}(\boldsymbol{x} | \boldsymbol{\mu}_s, \boldsymbol{\Lambda}_s, \nu_s)` with the parameters that:

.. math::
   :label: solution of Gauss predictive in prior 3

   \boldsymbol{\mu}_s &= \boldsymbol{\mu} \\
   \nu_s &= \nu + 1 - D \\
   \boldsymbol{\Lambda}_s &= \frac{\nu_s \beta}{1+\beta} \boldsymbol{W}

As for its Bayesian posterior predictive, replace all the :math:`\boldsymbol{m}`, :math:`\beta`, :math:`\nu`, and
:math:`\boldsymbol{W}` by :math:`\hat{\boldsymbol{m}}`, :math:`\hat{\beta}`, :math:`\hat{\mu}` and
:math:`\hat{\boldsymbol{W}}` as determined by :eq:`solution of Gauss posterior in prior 3` and
:eq:`solution of Gauss posterior in prior 3 extra` respectively.

In the condition if univariate Gauss likelihood, the conjugate distribution will collapse from Gauss-Wishart to
Gauss-Gamma, while its predictive distribution will correspondingly become the univariate student-t as well.

For summary, the common continuous Gauss likelihood functions can be referred using the following
:numref:`Table %s <summary of gauss family>`:

.. table:: Bayesian statistics of Gauss distributions
   :name: summary of gauss family
   :align: center

   ================== ============================================== ============================ ================== ======================
   likelihood         parameter                                      condition                    conjugate          predictive
   ================== ============================================== ============================ ================== ======================
   univariate gauss   :math:`\mu`                                    :math:`\lambda`              univariate gauss   univariate gauss
   univariate gauss   :math:`\lambda`                                :math:`\mu`                  gamma              univariate student-t
   univariate gauss   :math:`\mu, \lambda`                           :math:`-`                    gauss-gamma        univariate student-t
   multivariate gauss :math:`\boldsymbol{\mu}`                       :math:`\boldsymbol{\Lambda}` multivariate gauss multivariate gauss
   multivariate gauss :math:`\boldsymbol{\Lambda}`                   :math:`\boldsymbol{\mu}`     wishart            multivariate student-t
   multivariate gauss :math:`\boldsymbol{\mu}, \boldsymbol{\Lambda}` :math:`-`                    gauss-wishart      multivariate student-t
   ================== ============================================== ============================ ================== ======================

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Jul 28, 2024