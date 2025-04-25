dp-dev:
	poetry run ipython -i padrao_freguesia.py

dp:
	poetry run python padrao_freguesia.py
	git add READme.md
	git commit -m "Atualizando README"
	git push -u origin main