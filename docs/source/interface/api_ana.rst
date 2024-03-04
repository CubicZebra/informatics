_`Modules for analysis`
=======================

_`Module hypotest`
------------------

Description
~~~~~~~~~~~

Hypothesis test module in dataflow. Location in ``info.toolbox.libs.hypotest``. For convenience in practice,
importing from main entry via ``from info.me import hypotest`` is also supported.

The prefix ``hypoi`` denotes the test required independent data populations, based on which the sizes of all
population are unnecessary to be identical. ``hypoj`` for joint pairs generally required the sizes of two
samples are of the same. ``hypos`` is simulation methods using random sampling.

Docstrings
~~~~~~~~~~

.. autodata:: info.docfunc.hypoi_f
   :no-value:

.. autodata:: info.docfunc.hypoi_t
   :no-value:

.. autodata:: info.docfunc.hypoi_sw
   :no-value:

.. autodata:: info.docfunc.hypoi_normality
   :no-value:

.. autodata:: info.docfunc.hypoi_ks
   :no-value:

.. autodata:: info.docfunc.hypoi_cvm
   :no-value:

.. autodata:: info.docfunc.hypoi_ag
   :no-value:

.. autodata:: info.docfunc.hypoi_thsd
   :no-value:

.. autodata:: info.docfunc.hypoi_kw
   :no-value:

.. autodata:: info.docfunc.hypoi_mood
   :no-value:

.. autodata:: info.docfunc.hypoi_bartlett
   :no-value:

.. autodata:: info.docfunc.hypoi_levene
   :no-value:

.. autodata:: info.docfunc.hypoi_fk
   :no-value:

.. autodata:: info.docfunc.hypoi_ad
   :no-value:

.. autodata:: info.docfunc.hypoi_rank
   :no-value:

.. autodata:: info.docfunc.hypoi_es
   :no-value:

.. autodata:: info.docfunc.hypoi_u
   :no-value:

.. autodata:: info.docfunc.hypoi_bm
   :no-value:

.. autodata:: info.docfunc.hypoi_ab
   :no-value:

.. autodata:: info.docfunc.hypoi_skew
   :no-value:

.. autodata:: info.docfunc.hypoi_kurtosis
   :no-value:

.. autodata:: info.docfunc.hypoi_jb
   :no-value:

.. autodata:: info.docfunc.hypoi_pd
   :no-value:

.. autodata:: info.docfunc.hypoi_chi2
   :no-value:

.. autodata:: info.docfunc.hypoj_pearson
   :no-value:

.. autodata:: info.docfunc.hypoj_spearman
   :no-value:

.. autodata:: info.docfunc.hypoj_kendall
   :no-value:

.. autodata:: info.docfunc.hypoj_t
   :no-value:

.. autodata:: info.docfunc.hypoj_rank
   :no-value:

.. autodata:: info.docfunc.hypoj_friedman
   :no-value:

.. autodata:: info.docfunc.hypoj_mgc
   :no-value:

.. autodata:: info.docfunc.hypos_mc
   :no-value:

.. autodata:: info.docfunc.hypos_permu
   :no-value:

_`Module feature`
-----------------

Description
~~~~~~~~~~~

Radiomics feature extraction and analysis module in dataflow. Location in ``info.toolbox.omics.radi.feature``.
For convenience in practice, importing directly from main entry through ``info.me``.

Docstrings
~~~~~~~~~~

.. autodata:: info.docfunc.radiomics_features
   :no-value:

.. autodata:: info.docfunc.priori_scoring
   :no-value:

.. sectionauthor:: |author|, |create| Jun 30, 2023
