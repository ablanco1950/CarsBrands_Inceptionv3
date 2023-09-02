# CarsBrands_Inceptionv3
Project that detects the brand of a car, between 1 and 49 brands ( the 49 brands of Stanford car file), that appears in a photograph with a success rate of more than 70% (using a test file that has not been involved in the training as a valid or training file) and can be implemented on a personal computer.

All used packages, if any are missing, can be installed with a simple pip after de error of missing.

For this, the Stanford car file downloaded from https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download has been used.

When you download and unzip the download file you will see that it contains the directories
archive\cars_train\cars_train with 8144 numbered images. This folder should be copied to the c: directory so that it is accessible by other projects apart from CarsBrand_Inceptionv3 and also change the name of the archive folder to archiveKaggle so that there is a folder with C:\\archiveKaggle\\cars_train\ \cars_train

Download all the files that accompany the CarsBrand_Inceptionv3 project in a single folder.

The director file is cardatasettrain.csv downloaded from:
https://github.com/BotechEngineering/StanfordCarsDatasetCSV/tree/main

Inception_v3 has been chosen as a model due to its speed, since the whole project has been executed on a home laptop (no GPU).

For the training, images 1 to 7000 will be considered as train, from 7000 to 8000 as valid and from 8000 to 8144 as an independent test of the training process.

You have to create the folder structure that Inception_v3 requires: a directory with 3 folders: train, valid and test. From train and valid hang as many folders as car brands are considered named with the code assigned to each brand. This structure is created by running the program in the download folder of the project:

CreateDirTrainTestCarBrands_1_49.py

Next, the structure created in the previous step is filled in by executing:

FillDirKaggleCarsByBrand_1_49.py

As part of the downloaded Stanford file is supposed to be located in C:\\archiveKaggle\\cars_train\\cars_train, if not, modify the FillDirKaggleCarsByBrand_1_49.py line 52 so that it points to where the Stanford file is located.

Run the train:

lrTrainCarsBrandInception_v3CALLBACK_1_49.py
which comes ready for 100 epoch, designed so that it can run in a reasonable time on a laptop.

As 100 epoch are not enough to achieve acceptable val_acc values. The program:

lrTrainCarsBrandInception_v3CALLBACK_1_49CONTINUE.py

allows you to continue the epoch, taking advantage of the results of previous steps, simply by modifying the initial number of the epoch and the end ( instructions number 51 and 52) and using the model obtained in the preceding step: lrModelCarsBrands_Inception_v3_1_49.h5 . All of this, as indicated, to allow the training to be executed on a personal computer, dividing  epochs into 10 executions.

In the 800-900 epoch range, acceptable results are obtained.

The results of the test are evaluated by executing

lrGuessCarsBrandsKaggle_Inception_v3_1_49.py

The results of the training are shown in the attached file lr val_acc 49 epoch 800-900.txt and the results of the test with images from 8000.jpg to 8146.jpg, which have not been used as train or valid, in the file ResultsTestCarBrands.txt which is also attached


lrModelCarsBrands_Inception_v3_1_49.h5 is taken as the resulting file with the weigths, it could be changed by lrbest_brand_1_49.h5 , keep the one that gave better results. This .h5 files are very large (1.9Gb) so they could not be uploaded to Github

As an output, a file is also obtained: BrandsResults.txt with the list of images whose car brands have been correct and the wrong ones with the brands that have been predicted to them.

References:

https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download

https://github.com/BotechEngineering/StanfordCarsDatasetCSV/blob/main/cardatasettest.csv

https://medium.com/analytics-vidhya/top-4-pre-trained-models-for-image-classification-with-python-code-a3cb5846248b

https://github.com/afaq-ahmad/Car-Models-and-Make-Classification-Standford_Car_dataset-mobilenetv2-imagenet-93-percent-accuracy/blob/master/Car_classification.ipynb


