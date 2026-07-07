from pathlib import Path
from subprocess import run

project_name = '{{ cookiecutter.project_name }}'
venv_dest_path = Path(project_name / 'workflow' / 'envs' / 'venv')
run(['/usr/bin/env', 'python', '-m', 'venv', venv_dest_path])
packages = '{{ cookiecutter.install_packages }}'
run([venv_dest_path / 'bin' / 'python', '-m', 'pip', 'install'] + packages)
