FROM python:3.10
SHELL ["/bin/bash", "-c"]
EXPOSE 5000
RUN ["git", "clone", "https://github.com/annihilator2751/appium_parallel.git"]
WORKDIR appium_parallel/
RUN ["python", "-m", "venv", "venv"]
RUN source venv/bin/activate && pip install -r requirements.txt && pip install -e .
CMD source venv/bin/activate && python core/server/
