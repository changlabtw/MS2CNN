# Under construction, we will update it soon.

## MS2CNN
Predicting MS/MS spectrum based on protein sequence by Deep Convolutional Neural Networks

Prerequisites
--------------
MS2CNN compilation requires the following tools installed on your system ``Python``, ``Keras==2.0.4`` and ``Tensorflow==1.1.0``.

Compile/Installation 
--------------------

Download the git repository on your computer with the following command: 

    git clone git@github.com:jmchanglab/MS2CNN.git MS2CNN
    
Make sure you have installed the required dependencies listed above. 
When done, move in the project root folder named ``MS2CNN`` and enter the 
following commands:     
    
    $ cd src
    $ make

Usage 
--------------------
We only provide length 15 to 19 in peptide charge 2.

	python predict.py -l 19  


Input
--------------------
format

Output
--------------------
format

Reference
--------------------
[Lin YM, Chen CT, Chang JM. MS2CNN: predicting MS/MS spectrum based on protein sequence using deep convolutional neural networks. BMC Genomics. 2019;20(Suppl 9):906.](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6297-6)
