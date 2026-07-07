from pathlib import Path
from subprocess import run

venv_dest_path = Path('workflow') / 'envs' / 'venv'
run(['/usr/bin/env', 'python', '-m', 'venv', str(venv_dest_path)])
packages = '{{ cookiecutter.install_packages }}'.split()
if packages:
    run([str(venv_dest_path / 'bin' / 'python'), '-m', 'pip', 'install'] +
        packages)
