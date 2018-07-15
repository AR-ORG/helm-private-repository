FROM python:3.6.6-alpine3.7

LABEL maintainer="aliasmee"

ENV HELM_VERSION="v2.8.2"
ENV HELM_REPO_PORT="80"
ENV HELM_REPO_URL="http://example.com"

RUN mkdir /wwwdata /helm_repo_data \
   && wget -q http://storage.googleapis.com/kubernetes-helm/helm-${HELM_VERSION}-linux-amd64.tar.gz -O - | tar -xzO linux-amd64/helm > /usr/local/bin/helm \
   && chmod +x /usr/local/bin/helm

WORKDIR /helm_repo_data

COPY . /helm_repo_data

EXPOSE ${HELM_REPO_PORT}/tcp

# abspath: ref:https://stackoverflow.com/questions/7783308/os-path-dirname-file-returns-empty 
RUN python /helm_repo_data/scan_package.py

# helm serve --repo-path ./wwwdata
# CMD [ "helm", "serve", "--address", "0.0.0.0:8000", "--repo-path", "/wwwdata"]

CMD [ "python", "http_server.py"]
