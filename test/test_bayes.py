from info.toolbox.libs.anomaly.nbayes import NaiveBayes
from info.me import archive, unarchive, F, Unit
from info.me import autotesting as tst
import numpy as np
import scipy.stats as st
import scipy.sparse as sp
np.random.seed(10)


file = 'exports/bayes.pyp'
meta_flow = (tst.functest >> Unit(mappings=[archive])).shadow(to_file=file, scope_in_builtin=False)
tested = True


_as_coo_mat = (lambda x, tp='mat': [args := np.argwhere(x != 0),
                                    dt := np.array([[v1, v2, x[v1, v2]] for (v1, v2) in args]).T,
                                    sp.coo_matrix((dt[2], (dt[0], dt[1]))) if tp == 'tp' else
                                    sp.coo_array((dt[2], (dt[0], dt[1])))][-1])
_p1, _p2 = [0.03 for _ in range(15)], [0.1, 0.1, 0.15, 0.1, 0.1]
_p3, _p4 = [0 for _ in range(395)], [0.1, 0.2, 0.4, 0.2, 0.1]
pri1, pri2 = ([st.dirichlet((np.random.random(20) * 40).__abs__().astype(int)+1),
               st.dirichlet((np.random.random(20) * 40).__abs__().astype(int)+1)],
              [st.dirichlet((np.random.random(400) * 40).__abs__().astype(int)+1),
               st.dirichlet((np.random.random(400) * 40).__abs__().astype(int)+1)])
dense_cls1 = np.array([st.multinomial.rvs(70, _p1 + _p2) for _ in range(400)])
dense_cls2 = np.array([st.multinomial.rvs(70, _p2 + _p1) for _ in range(400)])
dense = np.vstack([dense_cls1, dense_cls2])
y = np.array([0 for _ in range(400)] + [1 for _ in range(400)]).astype(bool)
_sp_cls1 = np.array([st.multinomial.rvs(30, _p3 + _p4) for _ in range(400)])
_sp_cls2 = np.array([st.multinomial.rvs(30, _p4 + _p3) for _ in range(400)])
_sparse = np.vstack([_sp_cls1, _sp_cls1])
coo_mat = _as_coo_mat(_sparse)
csr_mat = coo_mat.tocsr(copy=True)  # use this during dev
csc_mat = coo_mat.tocsc(copy=True)
bsr_mat = coo_mat.tobsr(copy=True)
dia_mat = coo_mat.todia(copy=True)
lil_mat = coo_mat.tolil(copy=True)
dok_mat = coo_mat.todok(copy=True)
coo_arr = _as_coo_mat(_sparse, tp='arr')
csr_arr = coo_arr.tocsr(copy=True)
csc_arr = coo_arr.tocsc(copy=True)
bsr_arr = coo_arr.tobsr(copy=True)
dia_arr = coo_arr.todia(copy=True)
lil_arr = coo_arr.tolil(copy=True)
dok_arr = coo_arr.todok(copy=True)


naive_bayes = F(lambda **kw: NaiveBayes(**kw))
naive_bayes.__name__ = 'naive_bayes'
nb_args = {
    'data': [dense, coo_mat, coo_arr, csr_mat, csr_arr, csc_mat, csc_arr, bsr_mat, bsr_arr, dia_mat, dia_arr,
             lil_mat, lil_arr, dok_mat, dok_arr],
    'labels': [y],
    'prior': [None, pri1, pri2],
    'validation_rate': [0.1, 0.2],
    'model_lightweight': [True, False]
}


sys = __import__('sys')
_tp, _size = np.array([(type(_s), sys.getsizeof(_s)) for _s in nb_args.get('data')], dtype=object).T
_tp, _size = np.array([_.split('.')[-1].split("'")[0] for _ in _tp.astype(str)]), _size.astype(int)  # 64218 vs 48


if not tested:
    meta_flow(data=naive_bayes, params_pool=nb_args)
else:
    ...


res = unarchive(data=file)
for k, v in res.items():
    if not all(ref := tst.diagnosing_tests(data=v)):
        tst.diagnosing_tests(data=v, **{'~verbosity': True})
        print(f' exceptive case(s) collection in {k} '.join(['-'*60 for _ in range(2)]))


if __name__ == '__main__':
    pass
