from pathlib import Path
from subprocess import run

venv_dest_path = Path('workflow') / 'envs' / 'venv'
run(['/usr/bin/env', 'python', '-m', 'venv', str(venv_dest_path)])
packages = '{{ cookiecutter.install_packages }}'.split()
if packages:
    run([str(venv_dest_path / 'bin' / 'python'), '-m', 'pip', 'install'] +
        packages)

remote_choice = '{{ cookiecutter.remote_profile }}'
snakefile_path = Path('workflow') / 'Snakefile'
if remote_choice == 'none':
    run([
        'mv',
        str(Path('workflow') / 'Snakefile-local'),
        str(snakefile_path),
    ])
    for path in Path('profiles').glob('*'):
        if path.name != 'local':
            run(['rm', str(path)])
elif remote_choice == 'carbon':
    run([
        'mv',
        str(Path('workflow') / 'Snakefile-remote-carbon'),
        str(snakefile_path)
    ])
    for path in Path('profiles').glob('*'):
        if path.name not in ['carbon', 'local']:
            run(['rm', str(path)])
for path in Path('workflow').glob('Snakefile-*'):
    run(['rm', str(path)])
