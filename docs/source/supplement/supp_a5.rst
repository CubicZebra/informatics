_`Monte Carlo method`
=====================

Monte Carlo is a powerful technique used to understand and analyze complex systems by generating synthetic data that
mimic real-world processes. It can be used to solve any problem having a probabilistic interpretation. By creating
virtual experiments that are difficult or even impossible to study through traditional methods on computer, it provides
approximate solutions to problems that are too intractable to be analyzed mathematically, enables many scientific
and technological breakthroughs in fields such like physics, engineering, finance.

The Monte Carlo is often associated with Markov Chain due to its inherent stochastic nature, which typically manifests
as a stochastic process.  Contrary to simultaneous generation, the pseudo data points are determined individually in
a sequential manner.  Beginning with an initial point, subsequent cases are sampled from the conditional probability.
This process is iteratively repeated, thereby establishing a connection with the concept of random walk.

A Monte Carlo Markov Chain can be recognized with the property that from any initial start point, it will converge
towards an identical stationary distribution if the period for generation is long enough
(:ref:`Metropolis1953 <[Metropolis1953]>`, :ref:`Hastings1970 <[Hastings1970]>`, :ref:`Robert1999 <[Robert1999]>`).

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Feb 27, 2024