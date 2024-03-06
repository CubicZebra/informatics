_`Modules for analysis`
=======================

.. currentmodule:: info.docfunc

_`Module hypotest`
------------------

Description
~~~~~~~~~~~

Quantitative statistics on multi grouped data. Building proper hypothesis test and quantitative analysis requires
some basic knowledge on :ref:`mathematical statistics <Mathematical statistics>`.

Hypothesis test module in informatics is mainly in the namespace of ``info.toolbox.libs.hypotest``. For convenience
the import from mian entry (like ``from info.me import hypotest``) is also supported.

The prefix ``hypoi`` denotes the test required independent data populations, based on which the sizes of all
population are unnecessary to be identical. ``hypoj`` for joint pairs generally required the sizes of two
samples are of the same, intrinsically paired. ``hypos`` is simulation methods using random sampling.

.. autosummary::
   :nosignatures:

   hypoi_f
   hypoi_t
   hypoi_sw
   hypoi_normality
   hypoi_ks
   hypoi_cvm
   hypoi_ag
   hypoi_thsd
   hypoi_kw
   hypoi_mood
   hypoi_bartlett
   hypoi_levene
   hypoi_fk
   hypoi_ad
   hypoi_rank
   hypoi_es
   hypoi_u
   hypoi_bm
   hypoi_ab
   hypoi_skew
   hypoi_kurtosis
   hypoi_jb
   hypoi_pd
   hypoi_chi2
   hypoj_pearson
   hypoj_spearman
   hypoj_kendall
   hypoj_t
   hypoj_rank
   hypoj_friedman
   hypoj_mgc
   hypos_mc
   hypos_permu

Docstrings
~~~~~~~~~~

.. autodata:: hypoi_f
   :no-value:

.. autodata:: hypoi_t
   :no-value:

.. autodata:: hypoi_sw
   :no-value:

.. autodata:: hypoi_normality
   :no-value:

.. autodata:: hypoi_ks
   :no-value:

.. autodata:: hypoi_cvm
   :no-value:

.. autodata:: hypoi_ag
   :no-value:

.. autodata:: hypoi_thsd
   :no-value:

.. autodata:: hypoi_kw
   :no-value:

.. autodata:: hypoi_mood
   :no-value:

.. autodata:: hypoi_bartlett
   :no-value:

.. autodata:: hypoi_levene
   :no-value:

.. autodata:: hypoi_fk
   :no-value:

.. autodata:: hypoi_ad
   :no-value:

.. autodata:: hypoi_rank
   :no-value:

.. autodata:: hypoi_es
   :no-value:

.. autodata:: hypoi_u
   :no-value:

.. autodata:: hypoi_bm
   :no-value:

.. autodata:: hypoi_ab
   :no-value:

.. autodata:: hypoi_skew
   :no-value:

.. autodata:: hypoi_kurtosis
   :no-value:

.. autodata:: hypoi_jb
   :no-value:

.. autodata:: hypoi_pd
   :no-value:

.. autodata:: hypoi_chi2
   :no-value:

.. autodata:: hypoj_pearson
   :no-value:

.. autodata:: hypoj_spearman
   :no-value:

.. autodata:: hypoj_kendall
   :no-value:

.. autodata:: hypoj_t
   :no-value:

.. autodata:: hypoj_rank
   :no-value:

.. autodata:: hypoj_friedman
   :no-value:

.. autodata:: hypoj_mgc
   :no-value:

.. autodata:: hypos_mc
   :no-value:

.. autodata:: hypos_permu
   :no-value:

_`Module factors`
-----------------

Description
~~~~~~~~~~~

The module factors will support for scientific experiment design, data exploration, and etc. It is a powerful tool
for data exploration, allowing researchers to extract meaningful patterns and relationships from complex datasets.
Refer :ref:`supplementary <Factor analysis>` for its scientific background.

Similarly, the import through entry through ``info.me`` is available.

.. autosummary::
   :nosignatures:

   priori_scoring

Docstrings
~~~~~~~~~~

.. autodata:: priori_scoring
   :no-value:

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Jun 30, 2023
