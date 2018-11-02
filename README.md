# Zeinab-China-Research

## Setup Environment ##

In order to execute the notebooks on your host you can use Spyder (ready to use development environment with all libraries required to do data analytics).

### Installing Docker ###
 
Download & install Docker from: https://www.docker.com/get-started

### Running the Docker Image ###

To run the Docker image, first download the script spyder_desktop.py
and save it to the working directory where you will store your codes and data. You can download the script using command line: On Windows, start Windows PowerShell, use the cd command to change to the working directory where you will store your codes and data, and then run the following command:
curl https://raw.githubusercontent.com/compdatasci/spyder-desktop/master/spyder_desktop.py -outfile spyder_desktop.py

On Linux or Mac, start a terminal, use the cd command to change to the working directory, and then run the following command:
curl -s -O https://raw.githubusercontent.com/compdatasci/spyder-desktop/master/spyder_desktop.py

After downloading the script, you can start the Docker image using the command:
python spyder_desktop.py -p

For more details about the Spyder installation you can see the following video where Spyder is installed:
https://app.box.com/s/of4zr9v933ihd56mpk359uq8livhaht2

Official documentation:
https://hub.docker.com/r/compdatasci/spyder-desktop/

## SinaWeibo API exploration ##

The next notebook shows the SinaWeibo API exploration in order to extract publib weibos. It makes use of Google Colab to connect with US IP address and also to take advantage of cloud services.

https://colab.research.google.com/drive/1hLKUSrtCGHQ7gcjUxYdEf5Ut19zYXvrP


In addition, daily is being downloaded public SinaWeibo data. The Notebook along with daily datasets are available from: https://colab.research.google.com/drive/1dHLeYQa86u3KksiHucwPhtlXvLTRnvMW
