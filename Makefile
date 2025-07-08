install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pip install black

format:S
	black *.py

train:
	python train.py

eval:
	echo "## Model Metrics" > report.md
	cat ./Results/metrics.txt >> report.md

	echo '\n## Confusion Matrix Plot' >> report.md
	echo '![Confusion Matrix](./Results/model_results.png)' >> report.md

	cml comment create report.md

update-branch:
	git config --global user.name $(USER_NAME)
	git config --global user.name $(USER_EMAIL)
	git commit -am "Update with new results"
	git push --force origin HEAD:update

hf-login:
    git pull origin update
    git switch update
    pip install -U "huggingface_hub[cli]"
    huggingface-cli login --token $(HF) --add-to-git-credential

push-hub:
    huggingface-cli upload Bagus21/Tugas1_kel1_MLOps_SA25 ./App --repo-type=space --commit-message="Sync App files"
    huggingface-cli upload Bagus21/Tugas1_kel1_MLOps_SA25 ./Model /Model --repo-type=space --commit-message="Sync Model"
    huggingface-cli upload Bagus21/Tugas1_kel1_MLOps_SA25 ./Results /Metrics --repo-type=space --commit-message="Sync Model"

deploy: hf-login push-hub