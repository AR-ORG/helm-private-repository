# Helm-private-repository
Automatically scan and package your chart app in your git repository. And generate a docker image. You can deploy it as a kubernetes app and automatically update the app using the Jenkins pipeline. Provide a private helm chart repository service within the company.


## Getting Started

These instructions will cover usage information and for the docker container 

### Prerequisities


In order to run this container you'll need docker installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

### What's Helm Repository?

>A Repository is the place where charts can be collected and shared. It’s like Perl’s CPAN archive or the Fedora Package Database, but for Kubernetes packages.Helm installs charts into Kubernetes, creating a new release for each installation. And to find new charts, you can search Helm chart repositories.

### Usage

#### Running Example
```bash
docker run -it --rm -p 8088:8088 -e HELM_REPO_PORT=8088 -e HELM_REPO_URL="http://charts.example.com" image_name
```

#### Environment Variables

When you start the helm-private-repo image, you can adjust the configuration of the helm-repo instance by passing one or more environment variables on the docker run command line. 

`HELM_REPO_URL:`

This variable is mandatory and specifies the url that will be set for the helm repository.

`HELM_REPO_PORT:`

This variable is mandatory. Do note the port on which the helm repository is running needs to be the same as the port exposed outside.

## Demo

* Build the docker image and start it locally:

[![asciicast](https://asciinema.org/a/z9LiCNZj2Rldr9rTnGvAV0LXP.png)](https://asciinema.org/a/z9LiCNZj2Rldr9rTnGvAV0LXP)


* Test the helm private repository:

[![asciicast](https://asciinema.org/a/etNbjr0IyysMay4JfLptrOtjK.png)](https://asciinema.org/a/etNbjr0IyysMay4JfLptrOtjK)

`Notes: The port at which the container is running must be consistent with the port exposed.`
## Built With

* Base image python:3.6.6-alpine3.7

## Find Us

* [GitHub](https://github.com/aliasmee/helm-private-repository.git)


## Authors

* **aliasmee** - *Initial work* - [@aliasmee](https://github.com/aliasmee)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* [HELM](https://helm.sh/)
* [Helm Repository](https://docs.helm.sh/using_helm/#three-big-concepts)
