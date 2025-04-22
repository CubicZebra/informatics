# author: Chen Zhang
# usage:
#     * compiling for python 3.9 | 3.10 | 3.11 | 3.12 | 3.13 with documents embedded
#       PS> nt.ps1
#     * compiling for python 3.11 without documents embedded
#       PS> nt.ps1 '311' -add_doc $FALSE


param([Array]$envs=('39', '310', '311', '312', '313'), [String]$root=$PWD.ToString(),
      [Bool]$add_doc=$FALSE)
$dist_dir = $root+'/dist'
$doc_dir = $root+'/docs'

function activate_conda_hook() {
    C:\ProgramData\anaconda3\shell\condabin\conda-hook.ps1
    conda activate 'C:\ProgramData\anaconda3'
}

function single_compiler([String]$env) {
    $env1 = 'py'+$env
    conda activate $env1
    Write-Output 'Compiling in environment:'
    python --version
    $installed = pip list | Where-Object {$_ -Match 'informatics'}
    if ($installed) {pip uninstall informatics --yes}

    if (!$add_doc) {
        Set-Location $doc_dir
        make clean
        Set-Location $root
    }

    python -m build -w -Cbuild_ext

    if ($add_doc) {
        Set-Location $dist_dir
        $whl1 = Get-ChildItem -Name | Where-Object {$_ -Match 'win_amd64.whl$'} | Where-Object {$_ -Match 'cp'+$env}
        if ($whl1) {pip install $whl1}
        Set-Location $doc_dir
        (make clean)-and(make html)
        Set-Location $root
        python -m build -w -Cbuild_ext
        pip uninstall informatics --yes
    }

    conda deactivate
}

function batch_compiler([Array]$arr) {
    activate_conda_hook
    foreach ($env in $arr) {single_compiler $env}
}

batch_compiler $envs
