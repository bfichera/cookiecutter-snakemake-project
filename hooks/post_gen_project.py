from pathlib import Path
from subprocess import run

run(['uv', 'python', 'pin', '{{ cookiecutter.python_version }}'], check=True)
packages = '{{ cookiecutter.install_packages }}'.split()
if packages:
    run(['uv', 'add'] + packages, check=True)
else:
    run(['uv', 'sync'], check=True)

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
            run(['rm', '-r', str(path)])
elif remote_choice == 'carbon':
    run([
        'mv',
        str(Path('workflow') / 'Snakefile-remote-carbon'),
        str(snakefile_path)
    ])
    for path in Path('profiles').glob('*'):
        if path.name not in ['carbon', 'local']:
            run(['rm', '-r', str(path)])
for path in Path('workflow').glob('Snakefile-*'):
    run(['rm', str(path)])
