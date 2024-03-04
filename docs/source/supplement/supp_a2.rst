_`About matrix`
===============

In :ref:`previous section <High dimensional data>` we discuss about how dataset organized in form of matrix.
Thus, knowledge about matrix, will contribute for correctly building downstream analysis flow.

For a design matrix :math:`\boldsymbol{M} \in \mathbb{R}^{n \times m}` where :math:`n` and :math:`m`
refer the numbers of observations (samples) and data dimensions, respectively, most statistical methods are of
basis on certain hypothesis, in which condition that requires the design matrix to satisfy certain properties
(usually related to :math:`n` and :math:`m`). Therefore, the estimation for some problems such like how large of
the data scale should be prepared for an experiment, or the rational number of dimension for modeling the data,
can be deducted through matrix properties, on the basis of scientific rigor, instead of empiricism.

_`Rank and trace`
-----------------

Rank of matrix corresponds to the maximal dimension of a *no-degeneration* (see :ref:`degeneration <degeneracy>`)
linear system. In most cases, :math:`m \neq n`, therefore the rank of :math:`\boldsymbol{M}` will be like
:math:`\mathrm{r}(\boldsymbol{M}) = \min{(m, n)}`. Using linear model as example, when :math:`m` is much greater
than :math:`n`, the upper bound of matrix rank, that means most dimensions in that design matrix are redundant to be
removed through dimension reduction component. In reverse, in case of :math:`m \lt n`, the number of observations is
sufficient for building linear (or generalized linear) model.

.. note::

   linear model here can be conventional linear function like square error
   :math:`f(\boldsymbol{M}) = (\boldsymbol{M} - \overline{\boldsymbol{M}})(\boldsymbol{M} -
   \overline{\boldsymbol{M}})^T`, or other derived methods :math:`f(\boldsymbol{M}, \dots)` such like Pearson
   correlation coefficient (PCC), Pearson product moment correlation coefficient (PPMCC), or other formats with
   different location and rescale items (detailed definition see :ref:`SPSS tutorial <[SPSS2014]>`).

Further visualization for meaning of rank...

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: May 11, 2023