from info.toolbox.libs import anomaly as ano
from info.me import archive, unarchive, F, Unit
from info.me import autotesting as tst
import numpy as np
import scipy.stats as st
import scipy.sparse as sp
np.random.seed(10)


file = 'exports/anomalies.pyp'
meta_flow = (tst.functest >> Unit(mappings=[archive])).shadow(to_file=file, scope_in_builtin=False)
tested = True

_p1, _p2, _p3 = [np.array([0.03, 0.06, 0.1, 0.34, 0.22, 0.11, 0.08, 0.06]),
                 np.array([0.03, 0.08, 0.06, 0.12, 0.35, 0.2, 0.11, 0.05]),
                 np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.47, 0.47])]
_arr = [np.array([st.multinomial.rvs(50, p) for _ in range(100)]) for p in [_p1, _p2, _p3]]

dense_1class = _arr[0]
dense_2class = np.vstack(_arr[:2])
label_2class = np.array([0 for _ in range(100)] + [1 for _ in range(100)])
dense_3class = np.vstack(_arr)
label_3class = np.array([0 for _ in range(100)] + [1 for _ in range(100)] + [2 for _ in range(100)])


hotelling_pipe = F(lambda **kw: [md := ano.Hotelling(**kw), md.predict(data=kw.get('prediction'))][-1])
hot_args = {'data': [dense_1class], 'significance_level': [0.05, 0.1], 'prediction': [dense_1class, dense_2class]}


if not tested:
    meta_flow(data=hotelling_pipe, params_pool=hot_args)
else:
    ...


res = unarchive(data=file)
for k, v in res.items():
    if not all(ref := tst.diagnosing_tests(data=v)):
        tst.diagnosing_tests(data=v, **{'~verbosity': True})
        print(f' exceptive case(s) collection in {k} '.join(['-'*60 for _ in range(2)]))


if __name__ == '__main__':
    pass
