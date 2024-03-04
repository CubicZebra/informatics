#!/bin/bash
root='/home/chen/Projects/info'
envs='39 310 311'
dist_dir="${root}/dist"
doc_dir="${root}/docs"
cwd="$(pwd .)"


function single_compiler() {
    conda activate "py${1}"
    echo "Compiling in environment:"
    python --version
    if pip list | grep info; then pip uninstall info --yes; fi
    python -m build -w -Cbuild_ext
    cd "${dist_dir}" || exit
    whl=$(find . -maxdepth 1 | grep linux_x86_64.whl | grep "cp${1}")
    if (($(echo "${whl}" | wc -l) == 1)); then pip install "${whl}"; fi
    cd "${doc_dir}" || exit
    make clean && make html
    cd "${2}" || exit
    python -m build -w -Cbuild_ext
    pip uninstall info --yes
    conda deactivate
}

function batch_compiler() {
    source /home/chen/anaconda3/etc/profile.d/conda.sh
    for var in "$@"; do single_compiler "${var}" "${root}"; done
    cd "${cwd}" || exit
}

# shellcheck disable=SC2046
batch_compiler $( if (( "$#" == 0 )); then echo "${envs}"; else echo "$@"; fi)