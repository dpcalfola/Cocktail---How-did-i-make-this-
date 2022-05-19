FROM python:3.10.4

WORKDIR /home/

RUN git clone https://github.com/dpcalfola/cocktail_how_did_i_make_this.git

COPY secret_env.py /home/cococktail_how_did_i_make_this/config/env/secret_env.py

WORKDIR /home/cocktail_how_did_i_make_this/

RUN pip install -r requirements.txt

EXPOSE 48009

CMD ["python", "manage.py", "runserver", "0.0.0.0:48009"]