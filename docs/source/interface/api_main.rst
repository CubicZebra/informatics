_`API documentations`
=====================

.. currentmodule:: info.docfunc

_`API reference`
----------------

_`Dataflow gallery`
~~~~~~~~~~~~~~~~~~~

Utility set of dataflow framework for agile development. Functions cover attribute registering, document attaching,
runtime type checking, unit testing, workflow design, building and wrapping.

.. autosummary::
   :nosignatures:

   T
   F
   FuncTools
   Unit
   TrialDict
   ExeDict
   SingleMap
   traversal_on_params
   experiments
   functest

And also some meta implementation frameworks for data loading, processing, visualization, analyzing, and exporting,
as well as some code block wrapper for easy develop.

.. autosummary::
   :nosignatures:

   operations
   printing_u
   saving_u
   visual_u
   generic_printer
   generic_logger
   exception_logger
   assert_info_raiser
   default_param
   diagnosing_tests
   drop_down
   distance_matrix
   window_to_clipper

_`Input and output`
~~~~~~~~~~~~~~~~~~~

Utilities for file or folder selection, filter, regrouping, or mapping. Can be derived as attribute or data loader
function as required.

.. autosummary::
   :nosignatures:

   leaf_folders
   search_from_root
   generic_filter
   files_regroup
   dict_filter
   archive
   unarchive

_`DICOM construction`
~~~~~~~~~~~~~~~~~~~~~

:ref:`DICOM <DICOM>` related tools. Operations include regrouping and re-sorting slices, read meta information,
link to other type of DICOM files and etc.

.. autosummary::
   :nosignatures:

   DcmSetConstructor
   DcmSeries
   dcm_hierarchical_parser
   dcm_attr_loader
   dcm_constructor
   dcm_regroup

_`Data processing`
~~~~~~~~~~~~~~~~~~

Utilities for data processing. Data can be vector, series (1-dimensional tensor), matrix (2-dimensional tensor),
conventional medical image (3-dimensional tensor), or tensors in higher dimensions.

Numeric tensor is generally used as container for raw data. For dealing with numeric tensor:

.. autosummary::
   :nosignatures:

   standardization
   normalization
   clipper
   cropper
   resize
   averaging_filter
   rank_filter
   minimum_filter
   maximum_filter
   mean_filter
   median_filter
   gaussian_filter
   gabor_filter
   bilateral_filter
   prewitt_filter
   prewitt_detector
   prewitt_sharpen
   sobel_filter
   sobel_detector
   sobel_sharpen
   canny_filter
   canny_detector
   canny_sharpen
   laplacian_of_gaussian_filter
   laplacian_of_gaussian_detector
   laplacian_of_gaussian_sharpen
   difference_of_gaussian_filter
   difference_of_gaussian_detector
   difference_of_gaussian_sharpen
   hessian_determinant_response
   hessian_curvature_response
   hessian_curvature_detector
   moravec_response
   harris_response
   usan_response
   segment_response
   fast_response

Boolean tensor is generally used for segmentation, assisted for some specific tasks such as emphasizing some certain
area of raw data. For dealing with boolean tensor:

.. autosummary::
   :nosignatures:

   prober
   connected_domain
   seg_resize
   erosion
   dilation
   intersection
   union
   difference
   watershed

_`Kernel related utilities`
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Kernel generator using for multipurpose such as de-noising, filtering, local feature capturing, and etc. Advanced
constructor tool applied for highly customized numerical computing. Or kernel related utilities.

.. autosummary::
   :nosignatures:

   KernelGen
   averaging_kernel
   gaussian_kernel
   laplacian_of_gaussian_kernel
   gabor_kernel

_`Visualization utilities`
~~~~~~~~~~~~~~~~~~~~~~~~~~

Applications that enable visualize data anywhere in any stages through minimal calling. Helpful for data diagnosis,
position and orientation checking (specifically for medical images), making analysis and summary, as well as result
export.

.. autosummary::
   :nosignatures:

   GrpSettings
   FigConfigs
   Canvas
   ImageViewer

_`Quantify analysis`
~~~~~~~~~~~~~~~~~~~~

Quantitative statistics on multi grouped data. Building proper hypothesis test and quantitative analysis requires
some basic knowledge on :ref:`mathematical statistics <Mathematical statistics>`.

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

And also for radiomics feature extraction, as well as auto factor analysis. Refer
:ref:`supplementary <Factor analysis>` for the scientific background.

.. autosummary::
   :nosignatures:

   radiomics_features
   priori_scoring

_`Documentation collection`
---------------------------

.. toctree::
   api_frame
   api_io
   api_dicom
   api_tensor
   api_kernel
   api_visual
   api_ana
   :maxdepth: 1

.. sectionauthor:: |author|, |create| Jun 15, 2023
