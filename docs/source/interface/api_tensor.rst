_`Module tensor`
================

.. currentmodule:: info.docfunc

Description
-----------

Data processing module in informatics. Utilities for data processing. Data can be vector, series (1-dimensional
tensor), matrix (2-dimensional tensor), conventional medical image (3-dimensional tensor), or tensors in higher
dimensions. Dependent on the type of data being processed, tensors are categorized into two distinct classes:
Boolean and numerical.

Namespace of this module is originally ``info.toolbox.libs.tensor``. For convenience, import from main entry via
``from info.me import tensorn`` for processing numeric tensor, or ``from info.me import tensorb`` for dealing with
the boolean one, is also available.

Computing in this module support :ref:`GPU <GPU>` accelerating. If `cupy <https://cupy.dev/>`_ is installed in the
environment, reset the configuration to activate it:

.. code-block:: python
   :caption: activate gpu accelerating for computing
   :name: activate gpu accelerating for computing

   from info.me import tensorn as tsn
   tsn.config.reset(device='gpu')

Numerical tensor is generally used as container for raw data. For dealing with numeric tensor:

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

And boolean tensor is generally used for segmentation, assisted for some specific tasks such as emphasizing some
certain area of raw data. For dealing with boolean tensor:

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

Docstrings
----------

_`Numeric tensor`
~~~~~~~~~~~~~~~~~

.. autodata:: standardization
   :no-value:

.. autodata:: normalization
   :no-value:

.. autodata:: clipper
   :no-value:

.. autodata:: cropper
   :no-value:

.. autodata:: resize
   :no-value:

.. autodata:: averaging_filter
   :no-value:

.. autodata:: rank_filter
   :no-value:

.. autodata:: minimum_filter
   :no-value:

.. autodata:: maximum_filter
   :no-value:

.. autodata:: mean_filter
   :no-value:

.. autodata:: median_filter
   :no-value:

.. autodata:: gaussian_filter
   :no-value:

.. autodata:: gabor_filter
   :no-value:

.. autodata:: bilateral_filter
   :no-value:

.. autodata:: prewitt_filter
   :no-value:

.. autodata:: prewitt_detector
   :no-value:

.. autodata:: prewitt_sharpen
   :no-value:

.. autodata:: sobel_filter
   :no-value:

.. autodata:: sobel_detector
   :no-value:

.. autodata:: sobel_sharpen
   :no-value:

.. autodata:: canny_filter
   :no-value:

.. autodata:: canny_detector
   :no-value:

.. autodata:: canny_sharpen
   :no-value:

.. autodata:: laplacian_of_gaussian_filter
   :no-value:

.. autodata:: laplacian_of_gaussian_detector
   :no-value:

.. autodata:: laplacian_of_gaussian_sharpen
   :no-value:

.. autodata:: difference_of_gaussian_filter
   :no-value:

.. autodata:: difference_of_gaussian_detector
   :no-value:

.. autodata:: difference_of_gaussian_sharpen
   :no-value:

.. autodata:: hessian_determinant_response
   :no-value:

.. autodata:: hessian_curvature_response
   :no-value:

.. autodata:: hessian_curvature_detector
   :no-value:

.. autodata:: moravec_response
   :no-value:

.. autodata:: harris_response
   :no-value:

.. autodata:: usan_response
   :no-value:

.. autodata:: segment_response
   :no-value:

.. autodata:: fast_response
   :no-value:

_`Boolean tensor`
~~~~~~~~~~~~~~~~~

.. autodata:: prober
   :no-value:

.. autodata:: connected_domain
   :no-value:

.. autodata:: seg_resize
   :no-value:

.. autodata:: erosion
   :no-value:

.. autodata:: dilation
   :no-value:

.. autodata:: intersection
   :no-value:

.. autodata:: union
   :no-value:

.. autodata:: difference
   :no-value:

.. autodata:: watershed
   :no-value:

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Jun 27, 2023
