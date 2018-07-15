#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path


p = Path(".")
chart_dirs = list(p.glob('**/Chart.yaml'))
dep_chart_dirs = list(p.glob('**/requirements.yaml'))
helm_package_path = []
helm_package_dep_path = []
web_data_dir = '/wwwdata'
repo_url = os.environ['HELM_REPO_URL'] + ':' + (os.environ['HELM_REPO_PORT'])

# 解决google连不上，导致 helm init失败
stable_repo_url = 'https://helm-chart-repo.pek3a.qingstor.com/kubernetes-charts/'

# Package charts
def helm_package(pack_source='.', pack_target=web_data_dir):
    # subprocess.check_output(['helm', 'package', pack_source, '-d', pack_target])
    result = subprocess.run(['helm', 'package', pack_source, '-d', pack_target, '--debug', '--save=false'],
                            stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(result)

# Generation repo index
def generate_index(index_path='.', index_url='http://chart.example.com'):
    result2 = subprocess.run(['helm', 'repo', 'index', index_path, '--url', index_url],
                             stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(result2)

# Handling chart packages with dependencies
def dep_update():
    result3 = subprocess.run(['helm', 'dependency', 'update'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    print(result3)

# Main 
def main():
    # Initialization local dir for helm
    subprocess.run(['helm', 'init', '--client-only', '--stable-repo-url', stable_repo_url], stdout=subprocess.PIPE)

    # Find all charts dir list
    for chart in chart_dirs:
        helm_package_path.append(str(chart.parent))

    # Find all charts with dependency, and remove them from the previous list, will be handled separately later
    for dep_chart in dep_chart_dirs:
        helm_package_dep_path.append(str(dep_chart.parent))
        helm_package_path.remove(str(dep_chart.parent))
    
    # Start package charts
    for package in helm_package_path:
        helm_package(package)

    generate_index(web_data_dir, repo_url)
    
    for dep_package in helm_package_dep_path:
        os.chdir(os.path.join(os.path.dirname(__file__), dep_package))
        dep_update()
        os.chdir(os.path.dirname(__file__))
        helm_package(dep_package)
    
    generate_index(web_data_dir, repo_url)


if __name__ == '__main__':
    print("Packaging your chart...")
    main()
    print("Helm charts resource now is ready!")
