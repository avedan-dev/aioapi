all:
	@echo "make postgres	- Start postgres container"

postgres:
	docker stop analyzer-postgres || true
	docker run --rm --detach --name=analyzer-postgres \
		--env POSTGRES_USER=user \
		--env POSTGRES_PASSWORD=hackme \
		--env POSTGRES_DB=analyzer \
		--publish 5432:5432 postgres