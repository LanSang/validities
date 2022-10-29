
.PHONY: conda
conda:
	conda env update --file config/causaldsr.yml --prune -n causaldsr