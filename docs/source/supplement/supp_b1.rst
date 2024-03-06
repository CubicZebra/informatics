_`Feature capturing`
====================

_`How we define features`
-------------------------

In many field, people process and analysis data, not only for summary, but for the possible fact underneath the
data self. Different disciplines have their own context or terminology. In machine learning, we call it *pattern*;
in statistics, we call it *probability distribution*; in physics or other related researches, we call it *model*.
However, when it comes to this concept, they consistently desires there's the thing: the minimal representation
of information.

Use the image recognition task for example, values of grey level varies pixel to pixel, but people can still
distinguish the objective from background, can tell whether the object is a person, or the other creatures.
Thus, even though pixel varies, the form of their combinations, or the location where they changed, is regular
to some extent.

Concisely, the really informative thing is not pixels themselves, but how they distributed, where they changed.
If the thing is capable enough to automatically finish a certain task, it can be considered as the `features`,
bonding with this task.

_`Spatial filtering`
--------------------

Spatial filtering is the techniques to emphasis the local features. It is applied globally, but can augment
local contrast where obvious changes occurs. This tech has been widely used in edge detection, object recognition.

The :numref:`Figure %s <kernel framework>` shows the principle of spatial filtering applied in 2 dimensional
image. kernel moves globally on image, and values of output image are replaced pixel by pixel based on pre-defined
computing method.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/kernel_for_tensor.jpg
   :name: kernel framework
   :width: 450
   :align: center

   data transition via kernel

The most used computing methods, are illustrated in :numref:`Figure %s <kernel calculation methods>`.
:math:`\boldsymbol{K}` refers kernel, and the values from :math:`r` to :math:`z` are the weights in
:math:`\boldsymbol{K}`. :math:`\boldsymbol{F}` refers the figure, and the values from :math:`a` to :math:`i`
are the numeric on :math:`\boldsymbol{F}`, overlapped where the kernel :math:`\boldsymbol{K}` is currently located.
:math:`\boldsymbol{I}` is the numeric to replace after filtering. The difference between correlation and
convolution, is the order of weight. Additionally, there also some generic filter using certain statistic
on the localized values (e.g. rank filter).

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/numerical_computing_through_kernel.jpg
   :name: kernel calculation methods
   :width: 450
   :align: center

   correlation, convolution, and generic mapping using kernel

Technically, it is not enough to understand how values will be calculated, but where the replacement will take place.
There's a concept of *anchor* in kernel, as shown in :numref:`Figure %s <anchor in kernel>`. The grey pixel is the
anchor location of kernel where the pixel will be replaced. By default, an anchor should be the center of a kernel
(otherwise the output image will be biased), however, it is weired to limit all dimensions of kernel as odd numbers.
The basic idea in **scipy** is showed in :numref:`Figure %s <anchor in kernel>` which is also applied in informatics,
for even number, the anchor in that dimension will be located one pixel next to the center.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/anchor_in_kernel.jpg
   :name: anchor in kernel
   :width: 450
   :align: center

   positions of anchor in kernels

In addition, when kernel moves on edges or corners of the image, the real numeric in original image will be
insufficient for calculation. In this condition it requires padding some pseudo-data in outer scope.
:numref:`Figure %s <edge padding methods>` shows five padding methods. Keep in mind that this factor only makes
difference on the corner- or edge-like regions.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/padding_methods.jpg
   :name: edge padding methods
   :width: 550
   :align: center

   padding methods for numerical computing in edges

Back to the kernel itself. Different kernels are designed for different purposes. For example, gaussian
kernel is a center-emphasising localized averaging, can be used for smoothing or de-noising. laplacian of
gaussian kernel using contrary signs between center and the area enveloped, to measure the local contrast.
The gaussian kernel and laplacian of gaussian kernel in 2 dimension are illustrated in
:numref:`Figure %s <gaussian kernel>` and :numref:`Figure %s <LoG kernel>`.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/gaussian_kernel.jpg
   :name: gaussian kernel
   :width: 270
   :align: center

   gaussian kernel

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/laplacian_of_gaussian_kernel.jpg
   :name: LoG kernel
   :width: 270
   :align: center

   laplacian of gaussian kernel


The effect of denoising, or object edge and profile detection, through gaussian and some gaussian-related kernels
filtering will be like:

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/spatial_filtering_examples.jpg
   :name: spatial filtering applied on image processing
   :width: 650
   :align: center

   spatial filtering applied on image processing

.. note::

   Most kernels are central symmetric, in which condition the correlation and convolution will be substantially
   equivalent.

Some kernels are designed to augment features along some certain orientations, due to their aeolotropy. For example,
the real part of 2-dimensional gabor kernel with radian of :math:`\theta = 0.5\pi` will be like the surface in
:numref:`Figure %s <gabor kernel>`

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/gabor_kernel.jpg
   :name: gabor kernel
   :width: 270
   :align: center

   gabor kernel

Specifying the desired direction of :ref:`spatial sine harmonic function <spatial sine function>`, the texture of
object aligned with, will be augmented. This tech is generally thought to be in accordance with the principle of
primary visual cortex. It can be applied on feature engineering for data augmentation for multipurpose, if the
directional information of the data is though to be of importance in analysis. For easy of understanding, here shows
the real and imaginary parts of the case (a) in :numref:`Figure %s <spatial filtering applied on image processing>`
convolved using gabor filtering, with directions of :math:`(1, 0)` and :math:`(0, 1)`, respectively:

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/gabor_filtering_examples.jpg
   :name: gabor filtering applied on image processing
   :width: 650
   :align: center

   gabor filtering applied on image processing

.. note::

   .. _`spatial sine function`:

   Gabor kernel is defined as a gaussian envelope, multiplied with a sine harmonic function. However, when dealing
   with data in different dimensions, its form might be different since in different coordinate systems (e.g. cartesian
   or polar in dimension 2, or spherical frame in dimension 3).

   For most libraries, they has presumed the dimensions of data to be processed therefore it is difficult to use a
   consistent method to obtain the Gabor kernel. Based on definition, the multivariate gaussian is handy to be
   obtained, so the keypoint is the generalization for sine function into n-dimension.

   Consider the degeneracy of degree fo freedom (:ref:`DoF <DoF>`) occurs (see topic :ref:`degeneracy <degeneracy>`),
   for sine function, in 1D line (DoF=1), value varies in each point (DoF=0); in 2D plane (DoF=2), value varies in
   each line (DoF=1); for 3D volume (DoF=3), value varies in each plane (DoF=2). Generally, for n-dimension case, if
   a 1-dimension degenerated hyperplane is defined, the sine function will be described as simple as that in
   1-dimension. Here, we use normal to define those hyperplanes, through which the spatial sine function can be
   implemented in different dimensions with the identical interface:

   .. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/spatial_sine.jpg
      :name: real part of spatial sine in different dimensions
      :width: 600
      :align: center

      real part of spatial sine in different dimensions

   Then multiply them into the corresponding multivariate gaussian, the gabor kernel will be obtained as:

   .. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/spatial_gabor.jpg
      :name: real part of gabor kernel in different dimensions
      :width: 600
      :align: center

      real part of gabor kernel in different dimensions

_`Keypoint detection`
---------------------

Text here...

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/gaussian_curvature.jpg
   :name: effect of gaussian curvature via hessian filter
   :width: 600
   :align: center

   effect of gaussian curvature via hessian filter

Text here...

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/keypoint_detector.jpg
   :name: keypoint determination through curvature
   :width: 600
   :align: center

   keypoint determination through curvature

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Jun 28, 2023
