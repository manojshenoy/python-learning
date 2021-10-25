FROM python:3.8-slim
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER app_user
COPY . .
USER root
RUN cp -a /home/app_user/calc.py /usr/local/bin/calc
RUN cp -a /home/app_user/decades.py /usr/local/bin/decades
RUN cp -a /home/app_user/rockgame.py /usr/local/bin/rockgame
RUN chmod a+x /usr/local/bin/calc
RUN chmod a+x /usr/local/bin/decades
RUN chmod a+x /usr/local/bin/rockgame

USER app_user
CMD ["bash"]
