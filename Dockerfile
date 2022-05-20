FROM python:3.10.4

MAINTAINER FolaFlor


RUN apt-get update -y

RUN apt-get upgrade -y

RUN apt-get install git -y

RUN apt-get install iputils-ping -y

RUN apt-get install net-tools


WORKDIR /home/

RUN git clone https://github.com/dpcalfola/cocktail_how_did_i_make_this.git

COPY secret_env.py /home/cococktail_how_did_i_make_this/config/env/secret_env.py

WORKDIR /home/cocktail_how_did_i_make_this/

RUN pip install -r requirements.txt

COPY node_modules /node_modules

EXPOSE 48019

CMD ["python", "manage.py", "runserver", "0.0.0.0:48019"]