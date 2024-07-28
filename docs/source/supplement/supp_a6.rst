_`Bayesian statistics`
======================

Bayesian statistics represents a powerful paradigm that offers a probabilistic framework for updating beliefs and
making inferences in the face of uncertainty. Rooted in the foundational works of Thomas Bayes and later refined
by prominent statisticians, it incorporates prior knowledge or beliefs, along with observed data, to form posterior
distributions, thereby enabling more informed decision-making.

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

_`Discrete distributions`
-------------------------

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

----

:Authors: Chen Zhang
:Version: 0.0.5
:|create|: Jul 28, 2024