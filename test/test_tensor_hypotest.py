from info.me import archive, unarchive, Unit, F, TrialDict, io
from info.me import tensorn as tsn
from info.me import tensorb as tsb
from info.me import autotesting as tst
from info.me import hypotest as ht
from info.ins import datasets
from scipy.stats import norm
import sys
import numpy


file = 'exports/tensor_hypotest.pyp'
numpy.random.seed(3)
tested = True
segs = [_ for _ in tsb.connected_domain(data=datasets.segs())]
_repeat_2d = (lambda x, r: numpy.array([x for _ in range(r)]))
_3d_seg = numpy.zeros((19, 23, 21))
_3d_seg[2:5, 4:7, 10: 13] = 1
_3d_seg[9:14, 15:20, 15:19] = 1
meta_flow = (tst.functest >> Unit(mappings=[archive])).shadow(to_file=file, scope_in_builtin=False)
p1 = meta_flow.shadow(branch_comment='1D_CPU:')
p2 = meta_flow.shadow(branch_comment='2D_CPU:')
p3 = meta_flow.shadow(branch_comment='3D_CPU:')


ts1d = TrialDict({'data': [numpy.random.random(20)*3, numpy.random.random(70)*100]})
ts2d = TrialDict({'data': [datasets.cat()[50:100, 40:96], datasets.accent()[40:96, 50:115]]})
ts3d = TrialDict({'data': [numpy.random.random((16, 18, 17)), numpy.random.random((13, 30, 23))*3]})
sg1d = TrialDict({'data': [numpy.array([0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]).astype(bool)]})
sg2d = TrialDict({'data': [datasets.segs().astype(bool)]})
sg3d = TrialDict({'data': [_3d_seg.astype(bool)]})
uni = TrialDict({'data': [{f"group{_+1}": numpy.random.random(30) * (_*5) + (_*10) for _ in range(3)},
                          {f"group{_+1}": numpy.random.random((10, 3)) * (_*5) + (_*10) for _ in range(3)},
                          {f"group{_+1}": numpy.random.random((5, 2, 3)) * (_*5) + (_*10) for _ in range(3)}]})
neq = TrialDict({'data': [{f"group{_+1}": numpy.random.random(30+_) * (_*5) + (_*10) for _ in range(3)},
                          {f"group{_+1}": numpy.random.random((10+_, 3)) * (_*5) + (_*10) for _ in range(3)},
                          {f"group{_+1}": numpy.random.random((5+_, 2, 3)) * (_*5) + (_*10) for _ in range(3)}]})
path = TrialDict({'data': ['.', '..']})
iter_obj = TrialDict({'data': [['Apple', 'Microsoft', 'Oracle', 'AutoDesk', 'Adobe'],
                               ['audit', 'learning', 'mathematics', 'amazing', 'proper', 'critical']]})
dict_obj = TrialDict({'data': [{"argv": sys.argv, "path": sys.path},
                               {"m0": dir(segs), "m1": dir(meta_flow), "m2": dir(ts1d)}]})
iter_ft = iter_obj.trial(filter_pattern=[r'.*', r'^[aA]{1}'], apply_map=[None, (lambda x: len(x))])
iter_grp = iter_obj.trial(regroup_labels=[[r'^[aA]{1}', r'[mM]{1}'], [r'\b[a-zA-Z]{8}\b', r'\b[aA]{1}']])
dict_ft = dict_obj.trial(match_pattern=[r'_+', r'\b_{2}'], using_map=[None, len])


tsn_1d2d3d = F(lambda x, y=None: [[eval(f"p{_}(data=tsn.{x.__name__}, params_pool=ts{_}d)") if y is None
                                   else eval(f"p{_}(data=tsn.{x.__name__}, params_pool=ts{_}d.trial(**{y}{_}d))")
                                   for _ in '123'], 0][-1])
tsb_1d2d3d = F(lambda x, y=None: [[eval(f"p{_}(data=tsb.{x.__name__}, params_pool=sg{_}d)") if y is None
                                   else eval(f"p{_}(data=tsb.{x.__name__}, params_pool=sg{_}d.trial(**{y}{_}d))")
                                   for _ in '123'], 0][-1])

moment_arg1d = dict(moment_order=[1, 2], moment_axis=[0, (0, )], moment_rescale=[True, False])
moment_arg2d = dict(moment_order=[1, 2], moment_axis=[0, 1, (0, ), (0, 1)], moment_rescale=[True, False])
moment_arg3d = dict(moment_order=[1, 2], moment_axis=[0, 2, (0, 1), (0, 1, 2)], moment_rescale=[True, False])

clip_arg1d = clip_arg2d = clip_arg3d = dict(clip=[(0, 2)])

crop_arg1d = dict(crop_range=[[(0.1,), (0.9,)], [(1,), (20, )]])
crop_arg2d = dict(crop_range=[[(0.1, 0.2), (0.8, 0.9)], [(1, 2), (20, 30)]])
crop_arg3d = dict(crop_range=[[(0.1, 0.2, 0.14), (0.9, 0.8, 0.83)], [(1, 3, 2), (20, 30, 25)]])

interp_meth = ['linear', 'nearest', 'nearest-up', 'zero', 'slinear', 'quadratic', 'cubic', 'previous', 'next']
resize_arg1d = dict(new_size=[(50, ), (30, )], decomp_method=['cp', 'tucker', 'tt', 'tr'], interp_method=interp_meth)
resize_arg2d = dict(new_size=[(66, 88), (1000, 2000)], decomp_method=['cp', 'tucker', 'tt', 'tr'],
                    interp_method=interp_meth)
resize_arg3d = dict(new_size=[(50, 30, 20), (13, 17, 19)], decomp_method=['cp', 'tucker', 'tt', 'tr'],
                    interp_method=interp_meth)

_kernel_arg = TrialDict(k_mode=['reflect', 'constant', 'nearest', 'mirror', 'wrap'], k_cval=[0.0, 1.3])
shape_arg1d = _kernel_arg.trial(k_shape=[(3,), (5,)], k_origin=[0, [1], (-1,)])
shape_arg2d = _kernel_arg.trial(k_shape=[(3, 3), (5, 6)], k_origin=[1, [1, 0], (-1, 0)])
shape_arg3d = _kernel_arg.trial(k_shape=[(3, 3, 4), (5, 4, 6)], k_origin=[0, [-1, 1, 0], (0, 1, -1)])

rank_arg1d = shape_arg1d.trial(k_rank=[-1, 0.3])
rank_arg2d = shape_arg2d.trial(k_rank=[-1, 0.3])
rank_arg3d = shape_arg3d.trial(k_rank=[-1, 0.3])

gs_arg1d = shape_arg1d.trial(k_mu=[numpy.array([1])], k_sigma=[numpy.array([[1]])])
gs_arg2d = shape_arg2d.trial(k_mu=[numpy.array([0, 1])], k_sigma=[numpy.eye(2), numpy.array([[1, 0.3], [0.3, 1.4]])])
gs_arg3d = shape_arg3d.trial(k_mu=[numpy.array([0, 1, 0.3])],
                             k_sigma=[numpy.eye(3), numpy.array([[1, 0.3, 0.1], [0.3, 1.3, 0.2], [0.1, 0.2, 1]])])

gb_arg1d = shape_arg1d.trial(k_rescale=[1.2, 0.5], k_orientation=[[1]], k_wavelength=[2, 3.1], k_phase=[0, 1.2])
gb_arg2d = shape_arg2d.trial(k_rescale=[1.2, 0.5], k_orientation=[[1, -1], [0, 1]], k_wavelength=[2, 3.1],
                             k_phase=[0, 1.2])
gb_arg3d = shape_arg3d.trial(k_rescale=[1.2, 0.5], k_orientation=[[1, 1, 2], [0, 1.2, -1.5]], k_wavelength=[2, 3.1],
                             k_phase=[0, 1.2])

bf_arg1d = shape_arg1d.trial(sigma_d=[numpy.eye(1), numpy.array([[1.3]])], sigma_r=[1, 1.4])
bf_arg2d = shape_arg2d.trial(sigma_d=[numpy.eye(2), numpy.array([[2.3, 0.5], [0.5, 3]])], sigma_r=[1, 1.4])
bf_arg3d = shape_arg3d.trial(sigma_d=[numpy.eye(3), numpy.array([[1, 0.3, 0.1], [0.3, 1.3, 0.2], [0.1, 0.2, 1]])],
                             sigma_r=[1, 1.4])

pwd_arg1d = shape_arg1d.trial(prewitt_limen=[0.9, 0.8])
pwd_arg2d = shape_arg2d.trial(prewitt_limen=[0.9, 0.8])
pwd_arg3d = shape_arg3d.trial(prewitt_limen=[0.9, 0.8])

sharp_arg1d = shape_arg1d.trial(sharp_alpha=[0.9, 1.8])
sharp_arg2d = shape_arg2d.trial(sharp_alpha=[0.9, 1.8])
sharp_arg3d = shape_arg3d.trial(sharp_alpha=[0.9, 1.8])

sbd_arg1d = shape_arg1d.trial(sobel_limen=[0.9, 0.8])
sbd_arg2d = shape_arg2d.trial(sobel_limen=[0.9, 0.8])
sbd_arg3d = shape_arg3d.trial(sobel_limen=[0.9, 0.8])

cnd_arg1d = shape_arg1d.trial(canny_limen=[0.9, 0.8])
cnd_arg2d = shape_arg2d.trial(canny_limen=[0.9, 0.8])
cnd_arg3d = shape_arg3d.trial(canny_limen=[0.9, 0.8])

log_arg1d = shape_arg1d.trial(log_limen=[0.9, 0.8])
log_arg2d = shape_arg2d.trial(log_limen=[0.9, 0.8])
log_arg3d = shape_arg3d.trial(log_limen=[0.9, 0.8])

dog_f_arg1d = shape_arg1d.trial(sigma_ratio=[1.6, 1.8])
dog_f_arg2d = shape_arg2d.trial(sigma_ratio=[1.6, 1.8])
dog_f_arg3d = shape_arg3d.trial(sigma_ratio=[1.6, 1.8])

dog_d_arg1d = dog_f_arg1d.trial(dog_limen=[0.9, 0.8])
dog_d_arg2d = dog_f_arg2d.trial(dog_limen=[0.9, 0.8])
dog_d_arg3d = dog_f_arg3d.trial(dog_limen=[0.9, 0.8])

dog_s_arg1d = dog_f_arg1d.trial(sharp_alpha=[0.9, 1.8])
dog_s_arg2d = dog_f_arg2d.trial(sharp_alpha=[0.9, 1.8])
dog_s_arg3d = dog_f_arg3d.trial(sharp_alpha=[0.9, 1.8])

h_arg1d = sharp_arg1d.trial(in_spacing=[1, (0.9,)])
h_arg2d = sharp_arg2d.trial(in_spacing=[1, (1.1, 0.9)])
h_arg3d = sharp_arg3d.trial(in_spacing=[1, (0.9, 0.95, 1.1)])

hs_arg1d = h_arg1d.trial(hessian_limen=[0.9, 0.8])
hs_arg2d = h_arg2d.trial(hessian_limen=[0.9, 0.8])
hs_arg3d = h_arg3d.trial(hessian_limen=[0.9, 0.8])

us_arg1d = h_arg1d.trial(clip_window=['binomial', 'continuous'])
us_arg2d = h_arg2d.trial(clip_window=['binomial', 'continuous'])
us_arg3d = h_arg3d.trial(clip_window=['binomial', 'continuous'])

hr_arg1d = us_arg1d.trial(trace_coef=[0.05, 0.06])
hr_arg2d = us_arg2d.trial(trace_coef=[0.05, 0.06])
hr_arg3d = us_arg3d.trial(trace_coef=[0.05, 0.06])

sg_arg1d = shape_arg1d.trial(segment_threshold=[0.7, 1])
sg_arg2d = shape_arg2d.trial(segment_threshold=[0.7, 1])
sg_arg3d = shape_arg3d.trial(segment_threshold=[0.7, 1])

fst_arg1d = shape_arg1d.trial(fast_reject_thresholds=[(0.4, 0.6), (0.1, 0.9)])
fst_arg2d = shape_arg2d.trial(fast_reject_thresholds=[(0.4, 0.6), (0.1, 0.9)])
fst_arg3d = shape_arg3d.trial(fast_reject_thresholds=[(0.4, 0.6), (0.1, 0.9)])

sg_sp_arg1d = sg1d.trial(in_spacing=[None, (1,), (1.2,)])
sg_sp_arg2d = sg2d.trial(in_spacing=[None, (1, 1.2)])
sg_sp_arg3d = sg3d.trial(in_spacing=[None, (1, 1.2, 0.9)])

pb_arg1d = sg_sp_arg1d.trial(prob_nums=[4, 5], prob_radius=[1, 2])
pb_arg2d = sg_sp_arg2d.trial(prob_nums=[4, 5], prob_radius=[1, 2])
pb_arg3d = sg_sp_arg3d.trial(prob_nums=[4, 5], prob_radius=[1, 2])

cd_arg1d = sg1d.trial(detector=[None, numpy.array([1, 0, 1])])
cd_arg2d = sg2d.trial(detector=[None, numpy.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])])
cd_arg3d = sg3d.trial(detector=[None, numpy.ones((3, 3, 3))])

sg_resize_arg1d = sg1d.trial(new_size=[(50, ), (30, )], interp_method=interp_meth)
sg_resize_arg2d = sg2d.trial(new_size=[(660, 720), (1200, 1000)], interp_method=interp_meth)
sg_resize_arg3d = sg3d.trial(new_size=[(50, 30, 20), (13, 17, 19)], interp_method=interp_meth)

ed_arg1d = sg_sp_arg1d.trial(norm=[1.2, (1.1,)])
ed_arg2d = sg_sp_arg2d.trial(norm=[1.1, (1, 0.5)])
ed_arg3d = sg_sp_arg3d.trial(norm=[1.2, (1, 0.5, 0.6)])

op_arg1d = sg1d.trial(data=[numpy.random.randint(0, 2, 20).astype(bool)],
                      instances=[numpy.random.randint(0, 2, 20).astype(bool),
                                 [numpy.random.randint(0, 2, 20).astype(bool) for _ in range(5)]])
op_arg2d = sg2d.trial(data=[numpy.random.randint(0, 2, (20, 10)).astype(bool)],
                      instances=[numpy.random.randint(0, 2, (20, 10)).astype(bool),
                                 [numpy.random.randint(0, 2, (20, 10)).astype(bool) for _ in range(5)]])
op_arg3d = sg3d.trial(data=[numpy.random.randint(0, 2, (20, 10, 15)).astype(bool)],
                      instances=[numpy.random.randint(0, 2, (20, 10, 15)).astype(bool),
                                 [numpy.random.randint(0, 2, (20, 10, 15)).astype(bool) for _ in range(5)]])

npo, at, meth = ['propagate', 'raise', 'omit'], ['two-sided', 'less', 'greater'], ['auto', 'exact']
neq_t = neq.trial(equal_var=[True, False], trim=[0.0], permutations=[None, 1, 2], random_state=[None, 3, 6],
                  nan_policy=npo, alternative=at)
neq_ks = neq.trial(dist=[norm(loc=0, scale=1), [norm(loc=0.1, scale=0.9), norm(loc=0.2, scale=1.3)]],
                   alternative=at, method=meth+['asymp'], n_samples=[20, 30, 40])
neq_cvm = neq.trial(dist=[norm(loc=0, scale=1), [norm(loc=0.1, scale=0.9), norm(loc=0.2, scale=1.3)]],
                    method=meth+['asymp'])
neq_mood = neq.trial(ties=['below', 'above', 'ignore'], correction=[True, False], power_lambda=[0.5, 1.0],
                     nan_policy=npo, alternative=at)
neq_lev = neq.trial(center=['mean', 'median', 'trimmed'], proportiontocut=[0.05, 0.1])
neq_pd = neq.trial(f_exp=[None], ddf=[1, 3], pd_lambda=[1, 1.3, 2.8])
neq_chi2 = neq.trial(f_exp=[None], ddf=[1, 3])

uni_kendall = uni.trial(nan_policy=npo, alternative=at, method=meth+['asymptotic'], kendall_tau=['b', 'c', 'w'],
                        rank=[True, False], weigher=[None], additive=[True, False])
uni_t = uni.trial(nan_policy=npo, alternative=at)
uni_rank = uni.trial(correction=[True, False], zero_method=['wilcox', 'pratt', 'zsplit'], alternative=at,
                     method=meth+['approx'])
uni_mgc = uni.trial(data=[{f"group{_+1}": numpy.random.random(30) for _ in range(3)},
                          {f"group{_+1}": numpy.random.random((10, 3)) for _ in range(3)}],
                    distance_criteria=[(lambda x, y: numpy.linalg.norm(x-y, ord=2, axis=0)),
                                       (lambda x, y: numpy.mean(x)-numpy.mean(y))],
                    n_resamples=[1000, 1500], random_state=[None, 1, 3])

neq_mc = neq.trial(dist=[norm(loc=0, scale=1), norm(loc=0.1, scale=0.9)],
                   n_resamples=[9999, 5000], batch=[None, 500, 1000],
                   agg_statistics=[{'mean': (lambda x: numpy.mean(x))},
                                   {'std': (lambda x: numpy.std(x)), 'var': (lambda x: numpy.var(x))}],
                   alternative=at)
uni_permu = uni.trial(dist=[norm(loc=0, scale=1), norm(loc=0.1, scale=0.9)],
                      n_resamples=[9999, 5000], batch=[None, 500, 1000],
                      permu_type=['independent', 'samples', 'pairings'], binding_groups=[2, 3],
                      agg_statistics=[{'std_of_mean': lambda *x: numpy.std([numpy.mean(_) for _ in x])}],
                      alternative=at, random_state=[None, 3])

search = path.trial(search_condition=[(lambda x: x[-3:] == 'pyp'), (lambda x: x[-2:] == 'py')])


if not tested:
    tsn_1d2d3d(tsn.standardization)
    tsn_1d2d3d(tsn.normalization)
    tsn_1d2d3d(tsn.clipper, 'clip_arg')
    tsn_1d2d3d(tsn.cropper, 'crop_arg')
    tsn_1d2d3d(tsn.resize, 'resize_arg')
    tsn_1d2d3d(tsn.averaging_filter, 'shape_arg')
    tsn_1d2d3d(tsn.rank_filter, 'rank_arg')
    tsn_1d2d3d(tsn.minimum_filter, 'shape_arg')
    tsn_1d2d3d(tsn.maximum_filter, 'shape_arg')
    tsn_1d2d3d(tsn.mean_filter, 'shape_arg')
    tsn_1d2d3d(tsn.median_filter, 'shape_arg')
    tsn_1d2d3d(tsn.gaussian_filter, 'gs_arg')
    tsn_1d2d3d(tsn.gabor_filter, 'gb_arg')
    tsn_1d2d3d(tsn.bilateral_filter, 'bf_arg')
    tsn_1d2d3d(tsn.prewitt_filter, 'shape_arg')
    tsn_1d2d3d(tsn.prewitt_detector, 'pwd_arg')
    tsn_1d2d3d(tsn.prewitt_sharpen, 'sharp_arg')
    tsn_1d2d3d(tsn.sobel_filter, 'shape_arg')
    tsn_1d2d3d(tsn.sobel_detector, 'sbd_arg')
    tsn_1d2d3d(tsn.sobel_sharpen, 'sharp_arg')
    tsn_1d2d3d(tsn.canny_filter, 'shape_arg')
    tsn_1d2d3d(tsn.canny_detector, 'cnd_arg')
    tsn_1d2d3d(tsn.canny_sharpen, 'sharp_arg')
    tsn_1d2d3d(tsn.laplacian_of_gaussian_filter, 'shape_arg')
    tsn_1d2d3d(tsn.laplacian_of_gaussian_detector, 'log_arg')
    tsn_1d2d3d(tsn.laplacian_of_gaussian_sharpen, 'sharp_arg')
    tsn_1d2d3d(tsn.difference_of_gaussian_filter, 'dog_f_arg')
    tsn_1d2d3d(tsn.difference_of_gaussian_detector, 'dog_d_arg')
    tsn_1d2d3d(tsn.difference_of_gaussian_sharpen, 'dog_s_arg')
    tsn_1d2d3d(tsn.hessian_determinant_response, 'h_arg')
    tsn_1d2d3d(tsn.hessian_curvature_response, 'h_arg')
    tsn_1d2d3d(tsn.hessian_curvature_detector, 'hs_arg')
    tsn_1d2d3d(tsn.moravec_response, 'h_arg')
    tsn_1d2d3d(tsn.harris_response, 'hr_arg')
    tsn_1d2d3d(tsn.usan_response, 'us_arg')
    tsn_1d2d3d(tsn.segment_response, 'sg_arg')
    tsn_1d2d3d(tsn.fast_response, 'fst_arg')

    tsb_1d2d3d(tsb.prober, 'pb_arg')
    tsb_1d2d3d(tsb.connected_domain, 'cd_arg')
    tsb_1d2d3d(tsb.seg_resize, 'sg_resize_arg')
    tsb_1d2d3d(tsb.erosion, 'ed_arg')
    tsb_1d2d3d(tsb.dilation, 'ed_arg')
    tsb_1d2d3d(tsb.intersection, 'op_arg')
    tsb_1d2d3d(tsb.union, 'op_arg')
    tsb_1d2d3d(tsb.difference, 'op_arg')

    meta_flow(data=ht.hypoi_f, params_pool=neq)
    meta_flow(data=ht.hypoi_t, params_pool=neq_t)
    meta_flow(data=ht.hypoi_sw, params_pool=neq)
    meta_flow(data=ht.hypoi_normality, params_pool=neq.trial(nan_policy=npo))
    meta_flow(data=ht.hypoi_ks, params_pool=neq_ks)
    meta_flow(data=ht.hypoi_cvm, params_pool=neq_cvm)
    meta_flow(data=ht.hypoi_ag, params_pool=neq.trial(nan_policy=npo))
    meta_flow(data=ht.hypoi_thsd, params_pool=neq)
    meta_flow(data=ht.hypoi_kw, params_pool=neq.trial(nan_policy=npo))
    meta_flow(data=ht.hypoi_mood, params_pool=neq_mood)
    meta_flow(data=ht.hypoi_bartlett, params_pool=neq)
    meta_flow(data=ht.hypoi_levene, params_pool=neq_lev)
    meta_flow(data=ht.hypoi_fk, params_pool=neq_lev)
    meta_flow(data=ht.hypoi_ad, params_pool=neq.trial(midrank=[True, False]))
    meta_flow(data=ht.hypoi_rank, params_pool=neq.trial(alternative=at))
    meta_flow(data=ht.hypoi_es, params_pool=neq.trial(es_t=[(0.4, 0.8), (0.3, 0.72)]))
    meta_flow(data=ht.hypoi_u, params_pool=neq.trial(method=meth, alternative=at, u_continuity=[True, False]))
    meta_flow(data=ht.hypoi_bm, params_pool=neq.trial(method=meth, alternative=at, bm_dis=['t', 'normal']))
    meta_flow(data=ht.hypoi_ab, params_pool=neq.trial(alternative=at))
    meta_flow(data=ht.hypoi_skew, params_pool=neq.trial(nan_policy=npo, alternative=at))
    meta_flow(data=ht.hypoi_kurtosis, params_pool=neq.trial(nan_policy=npo, alternative=at))
    meta_flow(data=ht.hypoi_jb, params_pool=neq)
    meta_flow(data=ht.hypoi_pd, params_pool=neq_pd)
    meta_flow(data=ht.hypoi_chi2, params_pool=neq_chi2)

    meta_flow(data=ht.hypoj_pearson, params_pool=uni.trial(alternative=at))
    meta_flow(data=ht.hypoj_spearman, params_pool=uni.trial(nan_policy=npo, alternative=at))
    meta_flow(data=ht.hypoj_kendall, params_pool=uni_kendall)
    meta_flow(data=ht.hypoj_t, params_pool=uni_t)
    meta_flow(data=ht.hypoj_rank, params_pool=uni_rank)
    meta_flow(data=ht.hypoj_friedman, params_pool=uni)
    meta_flow(data=ht.hypoj_mgc, params_pool=uni_mgc)

    meta_flow(data=ht.hypos_mc, params_pool=neq_mc)
    meta_flow(data=ht.hypos_permu, params_pool=uni_permu)

    meta_flow(data=io.leaf_folders, params_pool=path)
    meta_flow(data=io.search_from_root, params_pool=search)
    meta_flow(data=io.generic_filter, params_pool=iter_ft)
    meta_flow(data=io.files_regroup, params_pool=iter_grp)
    meta_flow(data=io.dict_filter, params_pool=dict_ft)
else:
    ...


res = unarchive(data=file)
for k, v in res.items():
    if not all(ref := tst.diagnosing_tests(data=v)):
        tst.diagnosing_tests(data=v, **{'~verbosity': True})
        print(f' exceptive case(s) collection in {k} '.join(['-'*60 for _ in range(2)]))


if __name__ == '__main__':
    pass
