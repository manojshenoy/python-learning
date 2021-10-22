FROM python:3.8-slim
RUN useradd --create-home --shell /bin/bash app_user
WORKDIR /home/app_user/
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
USER app_user
COPY . .
USER root
RUN cp -a /home/app_user/calc.py /usr/bin/calc
RUN chmod a+x /home/app_user/calc.py
USER app_user
CMD ["bash"]
