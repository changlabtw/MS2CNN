# MS2CNN
Predicting MS/MS spectrum based on protein sequence using Deep Convolutional Neural Networks
**(Under construction, we will update it soon)**.

Prerequisites
--------------
MS2CNN compilation requires the following tools installed on your system:
* ``Python``
* ``Keras v2.0.4``
* ``Tensorflow v1.1.0``.

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
We provide prediction models for length 15 to 19 in peptide charge 2 or 3.

```bash
python predict.py -l length -c charge
	length: 15~19
	chareg: 2|3
```
	
An example commend for peptide charge 2 with lentgh 19
```bash
python predict.py -l 19 -c 2
```

Input
--------------------
format

Output
--------------------
format

Reference
--------------------
Lin YM, Chen CT, Chang JM. [MS2CNN: predicting MS/MS spectrum based on protein sequence using deep convolutional neural networks](https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-019-6297-6). BMC Genomics. 2019;20(Suppl 9):906.
