start: build	
	@docker run \
	--publish 8501:8501 \
	--name=marcocarmonadev-frontend \
	--env-file=.envs/production.env \
	--network=marcocarmonadev-backend-default \
	--rm \
	marcocarmonadev-frontend

build:
	@docker build \
	--tag marcocarmonadev-frontend \
	.