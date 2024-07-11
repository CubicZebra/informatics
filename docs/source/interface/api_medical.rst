_`Option digitmed`
==================

.. currentmodule:: info.docfunc

Description
-----------

Medical image related tools (data mainly in :ref:`DICOM <DICOM>` or :ref:`NIfTI <NIfTI>` protocol). For DICOM,
Operations include regrouping and re-sorting slices, read meta information, link to other type of DICOM files
and etc. In addition, measurement for images as feature extraction is also supported. For NIfTI image, the
relation between pixel and voxel space requires computation. Dependencies of `SimpltITK <http://simpleitk.org>`_
and `pydicom <https://github.com/pydicom/pydicom>`_ are required.

Namespace of this module is mainly in ``info.toolbox.digitmed.rebuild``. For convenience in practice, use main
entry of ``info.med``. As for the image reconstruction related functions, import the ``rebuild`` module from
``info.med``.

.. autosummary::
   :nosignatures:

   DcmSetConstructor
   DcmSeries
   dcm_hierarchical_parser
   dcm_attr_loader
   dcm_constructor
   dcm_regroup
   NIfTI
   nii_constructor

While for other functional units, directly import from ``info.med``.

.. autosummary::
   :nosignatures:

   radiomics_features
   vascular_invasion

Docstrings
----------

.. autoclass:: DcmSetConstructor

.. autoclass:: DcmSeries

.. autodata:: dcm_hierarchical_parser
   :no-value:

.. autodata:: dcm_attr_loader
   :no-value:

.. autodata:: dcm_constructor
   :no-value:

.. autodata:: dcm_regroup
   :no-value:

.. autoclass:: NIfTI

.. autodata:: nii_constructor
   :no-value:

.. autodata:: radiomics_features
   :no-value:

.. autodata:: vascular_invasion
   :no-value:

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Jun 29, 2023
