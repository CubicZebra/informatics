_`Pipelining the data process`
==============================

As the preferred language for artificial intelligence, Python is featured as its rich ecosystem, as well as the
convenience for fast implementation and developing. Data processing involving in different technical approaches
requires systematical integration. Thus, the unified data controlling among those utilities contributes to accelerate
verifying prototypes, optimize algorithm performance, as well as lower maintenance cost.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/python_ecosystem.jpg
   :name: python ecosystem
   :width: 650
   :align: center

   ecosystem of Python

Data processing is akin to an assembly line, where an increase in the number of steps results in a exponential
growth of factors that can impact the final result. While manually configuring all possible options for trial may
seem feasible, it often leads to a chaotic outcome. Following examples demonstrate how to establish pipelines for
automating complex tasks.

_`Normalized scientific computing`
----------------------------------

Scientific computing flow implemented through dataflow functions is of high completeness. And their units are readily
to be flexibly reused when create new processing flow. :numref:`flexibility and reusability of unit` is a snippet
in implementation for exporting :numref:`Figure %s <pathological image statistics>`.

.. code-block:: python
   :caption: flexibility and reusability of unit
   :name: flexibility and reusability of unit

   u1, u2, u3, u4, u5, v1, v2 = [Unit(mappings=[_]) for _ in [load, binarize, identification_cells, colorize,
                                                              tsb.connected_domain, imshow, hist]]
   to_fig1 = u1 >> v1
   to_fig2 = u1 >> u2 >> v1
   to_fig3 = Unit(mappings=[F(lambda **kw: [res := (u1 | (u1 >> u2 >> u3 >> u4))(**kw),
                                            np.dstack([res[1], np.linalg.norm(res[0], ord=2, axis=2)])][-1])]) >> v1
   to_fig4 = Unit(mappings=[F(lambda **kw: np.array([_.sum() for _ in (u1 >> u2 >> u3 >> u5)(**kw)]))]) >> v2

:code:`to_fig3` corresponds to the case (c). Obtain this figure must overlap the random colored cell nucleus masks,
superpositioned with grey scale image, then pass on an image viewer unit. It is the reason unit :code:`u1` is arranged
paralleled with a sequential processing line :code:`u1 >> u2 >> u3 >> u4`.

To export the (c) case in :numref:`Figure %s <pathological image statistics>`, call :code:`to_fig3(data=file)`. If a
researcher desires other parameters, call :code:`to_fig3(data=file, **user_defined_config)`. Or in more complicated
situation, if the researcher want to compare outcomes from an identical pipe in different parameters, those derived
pipes can also be readily obtained by: :code:`p = to_fig3.shadow(**config1) | to_fig3.shadow(**config2)`.

_`Automation experiment`
------------------------

There are also meta tools, for automation computing. The following example concerned the difference between global
prewitt and canny filters on a natural image:

.. code-block:: python
   :caption: auto experiment pipeline
   :name: auto experiment pipeline

   from info.me import datasets, Unit, F
   from info.me import tensorn as tsn
   from info.me import visualization as vis
   import numpy as np
   img = datasets.cat()

   config = vis.FigConfigs.Histogram.update(width=1.2, name=['prewitt', 'canny'])
   evaluate = F(lambda **kw: [res := kw.get('data'), print(np.std(res[0]-res[1])),
                              vis.Canvas.play(data=np.array([res[0].ravel(), res[1].ravel()]),
                                                             fig_type='histogram', cvs_legend=True,
                                                             fig_configs=config), res][-1])
   u1, u2, u3, u4, u5, v1 = [Unit(mappings=[_]) for _ in [tsn.cropper, tsn.gaussian_filter, tsn.resize, tsn.prewitt_filter,
                                                          tsn.canny_filter, evaluate]]
   p = u1 >> u2 >> u3 >> (u4 | u5) >> v1
   p.required_args  # {'data', 'new_size', 'k_shape', 'crop_range'}

It includes data processing functions dealing with cropping, de-noising, and resampling, followed by another
paralleled unit of filters. The user-customized process is implemented via lambda calculus: print out the standard
deviation of difference between two paralleled output, display their pixel distribution difference, then return
those two filtered figures.

As most functions in tensor namespace, including the :code:`F` lambda, have been already registered as dataflow
version, the :code:`p` can automatically analyze what keyword arguments are the required at least. Making a
parameter pool based on the required arguments. The following code can auto trigger the experiments then dump
each running case.

.. code-block:: python
   :caption: run auto experiment
   :name: run auto experiment

   to_test = {
       'data': [img],
       'crop_range': [[(0.2, 0.2), (0.8, 0.8)], [(0.3, 0.3), (0.7, 0.7)]],
       'k_shape': [(3, 3), (6, 6), (9, 9)],
       'new_size': [(400, 400), (600, 600)]
   }

   from info.me import autotesting as tst
   res = tst.experiments(data=p, params_pool=to_test, to_file='./experiment_results')

Prompt will info the current condition and calculated standard deviation, running time, and the final result case
by case; then the histogram figure will be popped up like :numref:`Figure %s <experiment flow histogram>`.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/experiment_flow_demo.jpg
   :name: experiment flow histogram
   :width: 450
   :align: center

   histogram for pixels distribution after prewitt and canny filters

All experiment results will be collected into a persistence file titled `experiment_results. pyp` inplace.

_`Automation testing`
---------------------

Different from automation experiment which can export the computed results, the automation testing only records
the exit code. If the pipeline exits with raised exception, related information will also be noted. Similar as
:code:`experiments` in :numref:`run auto experiment`, this meta implementation :code:`funtest` is in the same
namespace. It can test for dataflow functions, unit and pipelines defined via this framework.

.. figure:: https://cdn.jsdelivr.net/gh/CubicZebra/PicHost@master/misc/auto_test.jpg
   :name: automation testing result
   :width: 500
   :align: center

   automation testing result for resize function

:numref:`Figure %s <automation testing result>` is the test result for :code:`resize` function. Class type remains
in *result* column. The cost time, arguments for each test item are also be recorded.

----

:Authors: Chen Zhang
:Version: 0.0.4
:|create|: Feb 7, 2024