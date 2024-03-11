#!/bin/bash
# author: Chen Zhang
# usage:
#     * compiling for python 3.9 | 3.10 | 3.11 with documents embedded
#       shell> bash posix.sh
#     * compiling for python 3.10 | 3.11 without documents embedded
#       shell> bash posix.sh '310 311' false
envs="39 310 311"
add_doc=$([ "$#" == 0 ] && echo "true" || echo "${2}")
root="$(pwd .)"
dist_dir="${root}/dist"
doc_dir="${root}/docs"
# shellcheck disable=SC2050
# shellcheck disable=SC1014
target=$([ uname != 'Linux' ] && echo "linux_x86_64.whl" || echo "macos_10_9_x86_64.whl")


function single_compiler() {
    conda activate "py${1}"
    echo "Compiling in environment:"
    python --version
    if pip list | grep informatics; then pip uninstall informatics --yes; fi

    if ! (${2}); then cd "${doc_dir}" || exit; make clean; cd "${root}" || exit; fi

    python -m build -w -Cbuild_ext

    if ($2)
    then
    	cd "${dist_dir}" || exit
    	whl=$(find . -maxdepth 1 | grep "$target" | grep "cp${1}")
    	if (($(echo "${whl}" | wc -l) == 1)); then pip install "${whl}"; fi
    	cd "${doc_dir}" || exit
    	make clean && make html
    	cd "${root}" || exit
    	python -m build -w -Cbuild_ext
    	pip uninstall informatics --yes
    fi
    conda deactivate
}

function batch_compiler() {
    source /home/chen/anaconda3/etc/profile.d/conda.sh
    single_compiler "${1}" "${2}"
    cd "${root}" || exit
}

environments=$([ "$#" == 0 ] && echo "$envs" || echo "${1}")
IFS=' '
read -ra arr <<< "$environments"
for var in "${arr[@]}";
do
    batch_compiler "$var" "$add_doc" "${3}"
done
