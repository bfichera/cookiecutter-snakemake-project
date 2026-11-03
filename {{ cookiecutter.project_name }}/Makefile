main:
	uv run snakemake --profile profiles/{{ cookiecutter.__remote_profile_name }} --rerun-incomplete

check:
	uv run snakemake --profile profiles/{{ cookiecutter.__remote_profile_name }} --rerun-incomplete -n

sync:
	uv sync

clean:
	rm -rf .snakemake/
