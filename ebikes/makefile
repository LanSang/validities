.PHONY: upworkpreprocessor
.PHONY: upworkpostprocessor


prelims:
	gunzip -c ebikes.RC_2022-10.gz| shuf | head -500 | jq .permalink | sed "s/^/https:\/\/www.reddit.com/g" > sample.csv


upworkpreprocessor:
	gunzip -c ebikes.RC_2022-10.gz| shuf | head -10 | jq .permalink | sed "s/^/https:\/\/www.reddit.com/g" | tr -d '"' > sample.txt
	python make_file_for_upwork.py


upworkpostprocessor:
	python upwork_post_processor.py