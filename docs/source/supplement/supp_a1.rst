_`High dimensional data`
========================

_`Design matrix`
----------------

.. index:: design matrix

The :numref:`Table %s <design_mat1>` is a common data organized form with data points (or observations) arranged
along rows, and dimensions (or features) of each data point arranged along columns, to describe high dimensional
data in statistics :ref:`[Box1973, <[Box1973]>` :ref:`Timm2007] <[Timm2007]>`. Here shows an instance:

.. table:: table of design matrix (:math:`n \times m`)
   :name: design_mat1
   :align: center

   =============== =============== =============== =============== =============== ===============
   :math:`-`       :math:`d_{1}`   :math:`d_{1}`   ...             :math:`d_{m-1}` :math:`d_{m}`
   =============== =============== =============== =============== =============== ===============
   :math:`x_{1}`   0.99            0.95            ...             96.41           4182.37
   :math:`x_{2}`   0.99            0.95            ...             3170.75         8285.88
   ...             ...             ...             ...             ...             ...
   :math:`x_{n-1}` 0.95            0.96            ...             100.41          4239.75
   :math:`x_{n}`   0.99            0.95            ...             3223.52         8349.49
   =============== =============== =============== =============== =============== ===============

However, not all dimensions response observations equal-sensitively. If visualize that matrix as
:numref:`Figure %s <design_mat2>`, it not hard to tell the red-dashed dimensions are of more sensitivity, responded to
data points, than that of green ones. In some specific disciplines, dimensions were considered on basis of groups
of the same sort (e.g. spatial omics for tumor researches :ref:`[Wu2022] <[Wu2022]>`)

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/d33dafaf-b571-4348-95ff-f412ad26b517
   :name: design_mat2
   :width: 250
   :align: center

   heatmap for design matrix

_`Distance matrix`
------------------

.. index:: distance matrix

The distance matrix is generally defined as a square-like matrix, which consists of pairwise distance among all
observations :ref:`[Weyenberg2015] <[Weyenberg2015]>`. It informs the spatial relations among the high dimensional
points, or how they distributed, to some extent.

For a specific design matrix :math:`\boldsymbol{A} \in \boldsymbol{R}^{n \times m}`, its corresponding distance
matrix :math:`\boldsymbol{M}_{i, j} \in \boldsymbol{R}^{n \times n}` can be calculated through
:math:`d(\boldsymbol{A}_{i,:}, \boldsymbol{A}_{j,:})`, where the :math:`\boldsymbol{A}_{k,:}` denotes all elements
within the *k*-th observation in matrix :math:`\boldsymbol{A}`, :math:`d` refers the measure for distance (e.g.
Euclidean, Frobenius).

Using Euclidean norm of two vectors as their distance, the distance matrix for previous design matrix
:math:`\boldsymbol{A}` would be like:

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/fccf13da-fd2a-401c-a6f5-5623afceebe8
   :name: distance_mat1
   :width: 300
   :align: center

   distance matrix for :ref:`design matrix A <design_mat2>`

.. note::

   Note that distance matrix reveals symmetry in lot of cases, due to that most distance measures satisfied the
   commutative law (:math:`d(\boldsymbol{a}, \boldsymbol{b}) = d(\boldsymbol{b}, \boldsymbol{a})`).

Generally, the distance matrix can afford an intuitive visualization, for how dense of the information in some
specific dimensions. Moreover, it is a foundation of comprehensive analytics, as well as quantitative measure,
applied in lots of fields. The following result compares the identical data in three different dimension groups:

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/9eb61579-4096-4244-a4c8-8890dcf4ae63
   :name: design_distance
   :width: 700
   :align: center

   comparison for design matrix and distance matrix among varying dimension groups

Significantly, the more the dimension group response to data points, the more details presented in design matrix
(i.e. more informative in those groups).

.. note::

   Design matrix is determined by the arrangement of data points. Therefore if there's necessary to evaluate
   dimension(s), or combination of dimensions through design matrix, some order-free statistics (e.g.
   :math:`\mathrm{r}(\boldsymbol{A})`, :math:`\mathrm{Tr}(\boldsymbol{A})`) will be effective. Furthermore,
   some permutation-included method can also alleviate the error induced from one specific order.

_`Pattern in high dimensional data`
-----------------------------------

The concept, pattern, can be summarized as the most efficient expression for certain dataset. People want this
:ref:`minimal representation of information <How we define features>`, in order to obtain the regularity possibly
exists underlying the data.

As example showed in :numref:`Figure %s <distance_mat1>`, the distance matrix calculated from the subset design
matrix using high informative dimensions exclusively, is expected as almost identical as the one that calculated
from the original design matrix. Removing low expressive dimensions will not change the distribution of datapoints,
that's the reason of dimension reduction techniques are generally applied on data pre processing.

Despite the variation of datapoints, we use the term *informative* is somehow not exact, as it cannot exclude the
possibility of exist of coupled dimensions (imagine two highly correlated dimensions). In that case, decomposition
algorithms can further factorize dataset, after which possible pattern of data can be readily determined.

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/e70a47c6-03af-4107-846a-2bbe514510c0
   :name: decomposition for pattern
   :width: 650
   :align: center

   linear decomposition to determine pattern

Using demonstration in :numref:`Figure %s <decomposition for pattern>` as example, removing low informative content
(or content that might interfere) is somewhat like segmenting, and signal decomposition and synthesis is of the
similarity as extracting pattern: for species recognition, using 20 groups of singular values and their vector pairs
is sufficient, instead of the image itself.

This illustration takes linear decomposition as example is not to make explanation for the algorithm self, is to
express the idea that the informative thing of data is commonly underlying other spaces (just like k-space in
:ref:`MR <MR>` image, the frequency domain in speech recognition, linear sub spaces in natural image). There is
neither elixir for all diseases in this world, nor generic solution for all questions. A valid algorithm targeted
as solution for certain scientific problem, should include the specific framework designed to process and interpret
this key information according to the discipline characteristics, instead of introducing and integrating set of
gorgeous things unreasonably.

_`Correlation on high dimensional data`
---------------------------------------

Different from pattern extraction which characterize the data self via the optimal number of informative dimensions,
the correlation on multiple high dimensional datasets will calculate for their respective optimal number of dimension
in condition of their mutual characterizations.

Multi graph correlation (MGC) suggested by Vogelstein et.al. is a statistically powerful methodology for high
dimensional data, as well as benchmark to determine its intrinsic scales :ref:`[Vogelstein2019] <[Vogelstein2019]>`.
It can be applied in quantifying correlations, relationships, optimal scales, dense of information and etc.,
of high dimensional data with different attributes or modalities.

_`Multi Graph Correlation`
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. index:: single: multi graph correlation
           single: MGC

The detailed implementation and benchmark test of MGC has also been reported (:ref:`[Pandas2019] <[Pandas2019]>`).
Algorithm of MGC can be illustrated as :numref:`Figure %s <MGC_algorithm>`:

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/b56724b7-912d-4cb0-8d9c-f078c71a435c
   :name: MGC_algorithm
   :width: 400
   :align: center

   algorithm for multi graph correlation (MGC)

Data in two different group of dimensions were denoted as two design matrices :math:`\boldsymbol{D}_{des1}^{n \times m}`
and :math:`\boldsymbol{D}_{des2}^{n \times m}`. Their corresponding distance matrices were
:math:`\boldsymbol{D}_{dis1}^{n \times n}` and :math:`\boldsymbol{D}_{dis2}^{n \times n}`. To determine the optimal
scale, a 3rd dimension expanded bool tensor was generated from each distance matrix, as the mask to denote whether
the :math:`i`-th data point is of the :math:`s`-nearest neighbors of :math:`j`-th data point or not, when scale
:math:`s` ranges from 1 to :math:`n` (:math:`i, j, s \in \{1, 2, \dots, n\}`), as denoted by :math:`\textbf{G}` and
:math:`\textbf{H}` in the illustration. Hadamard product between mask slices and the corresponding distance matrix
was broadcast along the scale axis (e.g.
:math:`\textbf{G}_{:, :, s_i}' = \textbf{G}_{:, :, s_i} \circ \boldsymbol{D}_{dis1}^{n \times n}`, where
:math:`s_i \in \{1, 2, \dots, n\}`). Then two numeric tensors :math:`\textbf{G}'` and :math:`\textbf{H}'` were
generated. The scale map :math:`\boldsymbol{S}` was calculated based on that numeric tensors through
:math:`\boldsymbol{S}_{i, j} = D(\textbf{G}'_{:, :, i}, \textbf{G}'_{:, :, j})`, where :math:`D` is a distance
measure for two different matrices
(e.g. :math:`D(\boldsymbol{A}, \boldsymbol{B}) = \Vert \boldsymbol{A}-\boldsymbol{B} \Vert_2`).
After repeating previous steps in certain permutations derived from the original dataset, the statistics, p-value,
as well as the optimal scales were determined.

.. note::

   The notation :math:`:` in the subscript of :math:`\textbf{G}_{:, :, s_i}` refers all elements in that dimension
   (i.e. :math:`\textbf{G}_{:, i, j}` is a certain vector, :math:`\textbf{G}_{:, :, j}` is a certain matrix). Refer
   :ref:`nomenclature <Math symbols>` for more details about vector, matrix, and tensor.

_`Applied analysis of MGC`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assume the design matrices of the data in two different modalities were denoted as :math:`\boldsymbol{X}` and
:math:`\boldsymbol{Y}`. The null hypothesis and alternative in MGC were:

.. math::

   H_0:&\ \boldsymbol{X} \text{ and } \boldsymbol{Y} \text{ are independent.} \\
   H_1:&\ \boldsymbol{X} \text{ and } \boldsymbol{Y} \text{ are not independent.}

From which the conventional uni-variate statistics and corresponding methodologies are still applied in MGC.
However, more than had the conventional statistical test, MGC consists of luxuriant details about independence
between two set to be compared, inside the scale map in the test result:

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/ebbf5fba-132e-48d4-a674-5567f08c373b
   :name: MGC_pattern
   :width: 700
   :align: center

   scale maps of varying dependence in MGC benchmark test :ref:`[Vogelstein2019] <[Vogelstein2019]>`

There are the identical data set measured from different modalities (from 1 to 5). MGC is utilized to evaluate
relations between different modalities, as showed in :numref:`Figure %s <MGC_applied>`. In subplot (a), modality 1
contains absolutely identical information as that of modality 2 due to the maximum correlation statistic (1.000) and
low p-value (0.001); For case (b), the relatively high correlation indicates the massively overlapped information
between modality 1 and 3. Nevertheless, in that circumstance, the optimal scales would be helpful for the trade off
for the final modality selection, if only one modality was required; Result in (c) is the opposite of that of (a)
where information barely overlaps among those two modalities, it means that juxtaposition for those two modalities is
expected to be profitable; The last case (d) shows the those two modalities are entirely of the same, however this
conclusion is not supported by statistical significance, additional data would be beneficial to further analysis.

.. figure:: https://github.com/users/CubicZebra/projects/6/assets/34041412/34d6f1d7-46d8-4f75-b68a-d43dfa905972
   :name: MGC_applied
   :width: 500
   :align: center

   case analysis for different MGC results

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: May 8, 2023