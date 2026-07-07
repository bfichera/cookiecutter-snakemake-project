from pathlib import Path
from subprocess import run

project_name = '{{ cookiecutter.project_name }}'
venv_dest_path = Path(project_name) / 'workflow' / 'envs' / 'venv'
run(['/usr/bin/env', 'python', '-m', 'venv', str(venv_dest_path)])
packages = '{{ cookiecutter.install_packages }}'.split()
if packages:
    run([str(venv_dest_path / 'bin' / 'python'), '-m', 'pip', 'install'] +
        packages)
