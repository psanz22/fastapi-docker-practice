.PHONY: install dev build start clean

build:
	docker build --no-cache -t guess_number .

up:
	docker run -d --name guess_number_container -p 8000:80 -v $$PWD:/guess_number guess_number


logs:
	docker logs guess_number_container

list:
	docker ps -a

clean:
	docker rm -f guess_number_container

