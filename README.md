# CarsBrands_Inceptionv3
Project that detects the brand of a car, between 1 and 20 brands, that appears in a photograph with a success rate of more than 70%

For this, the Stanford car file downloaded from https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download has been used.

When you download and unzip the download file you will see that it contains the directories
archive\cars_train\cars_train with 8144 numbered images. This folder should be copied to the c: directory so that it is accessible by other projects apart from CarsBrand_Inceptionv3 and also change the name of the archive folder to archiveKaggle so that there is a folder with C:\\archiveKaggle\\cars_train\ \cars_train

Download all the files that accompany the CarsBrand_Inceptionv3 project in a single folder.

The director file is cardatasettrain.csv downloaded from:
https://github.com/BotechEngineering/StanfordCarsDatasetCSV/tree/main

Inception_v3 has been chosen as a model due to its speed, since the whole project has been executed on a home laptop (No GPU).

For the training, images 1 to 7000 will be considered as train, from 7000 to 8000 as valid and from 8000 to 8144 as an independent test of the training process.

You have to create the folder structure that Inception_v3 requires: a directory with 3 folders: train, valid and test. From train and valid hang as many folders as car brands are considered named with the code assigned to each brand. This structure is created by running the program in the download folder of the project:

CreateDirTrainTestCarBrands_1_20.py

Next, the structure created in the previous step is filled in by executing:

FillDirKaggleCarsByBrand_1_20.py

which part of the downloaded Stanford file is supposed to be located in C:\\archiveKaggle\\cars_train\\cars_train, if not, modify the FillDirKaggleCarsByBrand_1_20.py line 52 so that it points to where the Stanford file is located.

run the train:

TrainCarsBrandInception_v3CALLBACK_1_20.py
which comes ready for 100 epoch, designed so that it can run in a reasonable time on a laptop.

The results of the test are evaluated by executing

GuessCarsBrandsKaggle_Inception_v3_1_20.py

you get a hit rate


1/1 [===============================] - 0s 86ms/step
HIT 08140.jpg is assigned brand 11Chrysler

1/1 [===============================] - 0s 127ms/step
ERROR 08143.jpg is assigned brand 17FisKer
   True brand is 18Ford

1/1 [===============================] - 0s 124ms/step
HIT 08144.jpg is assigned brand 4Audi


Total hits = 67
Total failures = 25
Accuracy = 72.82608695652173%

An attempt can be made to improve the results by continuing the training process, building on the results of the previous training by running the program.

TrainCarsBrandInception_v3CALLBACK_1_20CONTINUE.py

It is observed that it continues in epoch 100 until it reaches 200. Then try again

GuessCarsBrandsKaggle_Inception_v3_1_20.py

ModelCarsBrands_Inception_v3_1_20.h5 is taken as the resulting file with the weigth, it could be changed by best_brand_1_20.h5 , keep the one that gave better results.

As an output, a file is also obtained: BrandsResults.txt with the list of images whose car brands have been correct and the wrong ones with the brands that have been predicted to them.

References:

https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download

https://github.com/BotechEngineering/StanfordCarsDatasetCSV/blob/main/cardatasettest.csv

https://medium.com/analytics-vidhya/top-4-pre-trained-models-for-image-classification-with-python-code-a3cb5846248b

