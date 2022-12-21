
.PHONY: test
test:
	cd gp && conda run -n causaldsr --no-capture-output pytest test --disable-warnings && cd ..

.PHONY: conda
conda:
	conda env update --file config/causaldsr.yml --prune -n causaldsr