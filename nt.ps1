param([Array]$envs=('39', '310', '311'), [String]$root='C:\Users\Chen\Projects\Python\informatics')
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
    python -m build -w -Cbuild_ext
    Set-Location $dist_dir
    $whl1 = Get-ChildItem -Name | Where-Object {$_ -Match 'win_amd64.whl$'} | Where-Object {$_ -Match 'cp'+$env}
    if ($whl1) {pip install $whl1}
    Set-Location $doc_dir
    (make clean)-and(make html)
    Set-Location $root
    python -m build -w -Cbuild_ext
    pip uninstall informatics --yes
    conda deactivate
}

function batch_compiler([Array]$arr) {
    activate_conda_hook
    foreach ($env in $arr) {single_compiler $env}
}

batch_compiler $envs
