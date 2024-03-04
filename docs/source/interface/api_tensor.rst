_`Module tensor`
================

Description
-----------

Data processing module in dataflow. Location in ``info.toolbox.libs.tensor``. For convenience in practice,
importing from main entry via ``from info.me import tensorn`` for processing numeric tensor, or
``from info.me import tensorb`` for dealing with the boolean one.

Computing in this module support :ref:`GPU <GPU>` accelerating. Reset the configuration to activate it:

.. code-block:: python
   :caption: activate gpu accelerating for computing
   :name: activate gpu accelerating for computing

   from info.me import tensorn as tsn
   tsn.config.reset(device='gpu')

Docstrings
----------

_`Numeric tensor`
~~~~~~~~~~~~~~~~~

.. autodata:: info.docfunc.standardization
   :no-value:

.. autodata:: info.docfunc.normalization
   :no-value:

.. autodata:: info.docfunc.clipper
   :no-value:

.. autodata:: info.docfunc.cropper
   :no-value:

.. autodata:: info.docfunc.resize
   :no-value:

.. autodata:: info.docfunc.averaging_filter
   :no-value:

.. autodata:: info.docfunc.rank_filter
   :no-value:

.. autodata:: info.docfunc.minimum_filter
   :no-value:

.. autodata:: info.docfunc.maximum_filter
   :no-value:

.. autodata:: info.docfunc.mean_filter
   :no-value:

.. autodata:: info.docfunc.median_filter
   :no-value:

.. autodata:: info.docfunc.gaussian_filter
   :no-value:

.. autodata:: info.docfunc.gabor_filter
   :no-value:

.. autodata:: info.docfunc.bilateral_filter
   :no-value:

.. autodata:: info.docfunc.prewitt_filter
   :no-value:

.. autodata:: info.docfunc.prewitt_detector
   :no-value:

.. autodata:: info.docfunc.prewitt_sharpen
   :no-value:

.. autodata:: info.docfunc.sobel_filter
   :no-value:

.. autodata:: info.docfunc.sobel_detector
   :no-value:

.. autodata:: info.docfunc.sobel_sharpen
   :no-value:

.. autodata:: info.docfunc.canny_filter
   :no-value:

.. autodata:: info.docfunc.canny_detector
   :no-value:

.. autodata:: info.docfunc.canny_sharpen
   :no-value:

.. autodata:: info.docfunc.laplacian_of_gaussian_filter
   :no-value:

.. autodata:: info.docfunc.laplacian_of_gaussian_detector
   :no-value:

.. autodata:: info.docfunc.laplacian_of_gaussian_sharpen
   :no-value:

.. autodata:: info.docfunc.difference_of_gaussian_filter
   :no-value:

.. autodata:: info.docfunc.difference_of_gaussian_detector
   :no-value:

.. autodata:: info.docfunc.difference_of_gaussian_sharpen
   :no-value:

.. autodata:: info.docfunc.hessian_determinant_response
   :no-value:

.. autodata:: info.docfunc.hessian_curvature_response
   :no-value:

.. autodata:: info.docfunc.hessian_curvature_detector
   :no-value:

.. autodata:: info.docfunc.moravec_response
   :no-value:

.. autodata:: info.docfunc.harris_response
   :no-value:

.. autodata:: info.docfunc.usan_response
   :no-value:

.. autodata:: info.docfunc.segment_response
   :no-value:

.. autodata:: info.docfunc.fast_response
   :no-value:

_`Boolean tensor`
~~~~~~~~~~~~~~~~~

.. autodata:: info.docfunc.prober
   :no-value:

.. autodata:: info.docfunc.connected_domain
   :no-value:

.. autodata:: info.docfunc.seg_resize
   :no-value:

.. autodata:: info.docfunc.erosion
   :no-value:

.. autodata:: info.docfunc.dilation
   :no-value:

.. autodata:: info.docfunc.intersection
   :no-value:

.. autodata:: info.docfunc.union
   :no-value:

.. autodata:: info.docfunc.difference
   :no-value:

.. autodata:: info.docfunc.watershed
   :no-value:

.. sectionauthor:: |author|, |create| Jun 27, 2023
