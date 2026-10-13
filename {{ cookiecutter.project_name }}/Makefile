main:
	snakemake --profile profiles/{{ cookiecutter.__remote_profile_name }} --rerun-incomplete

check:
	snakemake --profile profiles/{{ cookiecutter.__remote_profile_name }} --rerun-incomplete -n

clean:
	rm -rf .snakemake/
