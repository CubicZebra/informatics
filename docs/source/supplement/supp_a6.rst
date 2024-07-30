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

In the context of classical statistics, it customarily utilize the maximum likelihood estimation (MLE) to solve the
parameter(s) of interested distribution. For an observed data set :math:`\mathcal{D}`, assume there is a statistical
model and its corresponding parameter :math:`\theta`. The MLE approach actually calculate
the :math:`\arg\max_{\theta} p(\mathcal{D} | \theta)`. In this situation, parameter :math:`\theta` is nothing else but
a numerical solution.

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
that could be simplified as a certain constant during calculation. Therefore it generally using
:math:`p(\theta | \mathcal{D}) \propto p(\mathcal{D} | \theta) p(\theta)` for further calculations.
And also, during calculation it concerns more about the parameter related term. If a
:ref:`kernel <Kernel and scale>` unveiled during simplification, the corresponding distribution can be established
rationally.

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
of :math:`\{0, 1\}` instead. The posterior of categorical distribution is consequently still dirichlet distribution
with parameter in accordance with :eq:`parameter of multinomial posterior` as well. However for its posteriori
predictive, consider the :math:`0! = 1! = 1`, the :math:`p(\boldsymbol{m}^*)` is actually:

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

text here...

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Jul 28, 2024