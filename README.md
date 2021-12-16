# reading-list-backend

The frontend code have written in React, find out [here](https://github.com/faayam/reading-list-frontend.git)

### App running instructions:

```console
$ sudo apt update
$ sudo apt install docker.io
$ git clone https://github.com/faayam/reading-list-backend.git
$ cd reading-list-backend
$ sudo docker build . -t backend
$ sudo docker run -p 5000:5000 -d -e POSTGRES_HOST=0.0.0.0 backend
```
