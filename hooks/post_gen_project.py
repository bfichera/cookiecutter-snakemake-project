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
elif remote_choice == 'carbon':
    run([
        'mv',
        str(Path('workflow') / 'Snakefile-remote-carbon'),
        str(snakefile_path)
    ])
run(['rm', str(Path('workflow') / 'Snakefile-*')])
