# CarsBrands_Inceptionv3
Project that detects the brand of a car, between 1 and 49 brands ( the 49 brands of Stanford car file), that appears in a photograph with a success rate of more than 70% (using a test file that has not been involved in the training as a valid or training file, "unseen data") and can be implemented on a personal computer.

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

In the 800-900 epoch range, acceptable results are obtained:



(alfonso1) c:\CarsBrands_Inceptionv3>python lrTrainCarsBrandInception_v3CALLBACK_1_49CONTINUE.py
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\numpy\_distributor_init.py:30: UserWarning: loaded more than 1 DLL from .libs:
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\numpy\.libs\libopenblas.FB5AE2TYXYH2IJRDKGDGQ3XBKLKTF43H.gfortran-win_amd64.dll
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\numpy\.libs\libopenblas64__v0.3.21-gcc_10_3_0.dll
  warnings.warn("loaded more than 1 DLL from .libs:"
Found 6999 images belonging to 49 classes.
Found 1000 images belonging to 49 classes.
Epoch 801/900
10/10 [==============================] - ETA: 0s - loss: 0.2229 - acc: 0.9550
Epoch 801: val_acc improved from -inf to 0.69200, saving model to lrbest_brand_1_49.h5
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\keras\src\engine\training.py:3000: UserWarning: You are saving your model as an HDF5 file via `model.save()`. This file format is considered legacy. We recommend using instead the native Keras format, e.g. `model.save('my_model.keras')`.
  saving_api.save_model(
10/10 [==============================] - 88s 9s/step - loss: 0.2229 - acc: 0.9550 - val_loss: 2.3578 - val_acc: 0.6920
Epoch 802/900
10/10 [==============================] - ETA: 0s - loss: 0.1245 - acc: 0.9700
Epoch 802: val_acc improved from 0.69200 to 0.69400, saving model to lrbest_brand_1_49.h5
10/10 [==============================] - 84s 9s/step - loss: 0.1245 - acc: 0.9700 - val_loss: 2.4685 - val_acc: 0.6940
Epoch 803/900
10/10 [==============================] - ETA: 0s - loss: 0.0476 - acc: 0.9900
Epoch 803: val_acc did not improve from 0.69400
10/10 [==============================] - 88s 9s/step - loss: 0.0476 - acc: 0.9900 - val_loss: 2.3922 - val_acc: 0.6810
Epoch 804/900
10/10 [==============================] - ETA: 0s - loss: 0.0702 - acc: 0.9850
Epoch 804: val_acc did not improve from 0.69400
10/10 [==============================] - 87s 9s/step - loss: 0.0702 - acc: 0.9850 - val_loss: 2.3497 - val_acc: 0.6740
Epoch 805/900
10/10 [==============================] - ETA: 0s - loss: 0.2336 - acc: 0.9700
Epoch 805: val_acc improved from 0.69400 to 0.70400, saving model to lrbest_brand_1_49.h5
10/10 [==============================] - 105s 11s/step - loss: 0.2336 - acc: 0.9700 - val_loss: 1.9800 - val_acc: 0.7040
Epoch 806/900
10/10 [==============================] - ETA: 0s - loss: 0.1636 - acc: 0.9700
Epoch 806: val_acc did not improve from 0.70400
10/10 [==============================] - 94s 10s/step - loss: 0.1636 - acc: 0.9700 - val_loss: 2.7439 - val_acc: 0.6740
Epoch 807/900
10/10 [==============================] - ETA: 0s - loss: 0.1219 - acc: 0.9750
Epoch 807: val_acc did not improve from 0.70400
10/10 [==============================] - 94s 10s/step - loss: 0.1219 - acc: 0.9750 - val_loss: 2.2127 - val_acc: 0.6900
Epoch 808/900
10/10 [==============================] - ETA: 0s - loss: 0.1719 - acc: 0.9600
Epoch 808: val_acc did not improve from 0.70400
10/10 [==============================] - 95s 10s/step - loss: 0.1719 - acc: 0.9600 - val_loss: 2.5141 - val_acc: 0.7000
Epoch 809/900
10/10 [==============================] - ETA: 0s - loss: 0.2235 - acc: 0.9650
Epoch 809: val_acc did not improve from 0.70400
10/10 [==============================] - 87s 9s/step - loss: 0.2235 - acc: 0.9650 - val_loss: 2.7069 - val_acc: 0.6940
Epoch 810/900
10/10 [==============================] - ETA: 0s - loss: 0.0951 - acc: 0.9800
Epoch 810: val_acc did not improve from 0.70400
10/10 [==============================] - 88s 9s/step - loss: 0.0951 - acc: 0.9800 - val_loss: 2.5354 - val_acc: 0.6950
Epoch 811/900
10/10 [==============================] - ETA: 0s - loss: 0.0987 - acc: 0.9800
Epoch 811: val_acc did not improve from 0.70400
10/10 [==============================] - 94s 10s/step - loss: 0.0987 - acc: 0.9800 - val_loss: 2.8535 - val_acc: 0.6960
Epoch 812/900
10/10 [==============================] - ETA: 0s - loss: 0.1883 - acc: 0.9500
Epoch 812: val_acc did not improve from 0.70400
10/10 [==============================] - 97s 10s/step - loss: 0.1883 - acc: 0.9500 - val_loss: 3.0876 - val_acc: 0.6770
Epoch 813/900
10/10 [==============================] - ETA: 0s - loss: 0.1975 - acc: 0.9400
Epoch 813: val_acc did not improve from 0.70400
10/10 [==============================] - 94s 10s/step - loss: 0.1975 - acc: 0.9400 - val_loss: 3.1766 - val_acc: 0.6680
Epoch 814/900
10/10 [==============================] - ETA: 0s - loss: 0.0646 - acc: 0.9800
Epoch 814: val_acc did not improve from 0.70400
10/10 [==============================] - 95s 10s/step - loss: 0.0646 - acc: 0.9800 - val_loss: 2.6720 - val_acc: 0.6880
Epoch 815/900
10/10 [==============================] - ETA: 0s - loss: 0.0804 - acc: 0.9700
Epoch 815: val_acc improved from 0.70400 to 0.71500, saving model to lrbest_brand_1_49.h5
10/10 [==============================] - 107s 11s/step - loss: 0.0804 - acc: 0.9700 - val_loss: 2.3677 - val_acc: 0.7150
Epoch 816/900
10/10 [==============================] - ETA: 0s - loss: 0.0564 - acc: 0.9800
Epoch 816: val_acc improved from 0.71500 to 0.72000, saving model to lrbest_brand_1_49.h5
10/10 [==============================] - 342s 37s/step - loss: 0.0564 - acc: 0.9800 - val_loss: 2.2460 - val_acc: 0.7200
Epoch 817/900
10/10 [==============================] - ETA: 0s - loss: 0.1518 - acc: 0.9650
Epoch 817: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.1518 - acc: 0.9650 - val_loss: 2.4790 - val_acc: 0.7020
Epoch 818/900
10/10 [==============================] - ETA: 0s - loss: 0.1615 - acc: 0.9650
Epoch 818: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.1615 - acc: 0.9650 - val_loss: 2.3520 - val_acc: 0.6960
Epoch 819/900
10/10 [==============================] - ETA: 0s - loss: 0.0599 - acc: 0.9750
Epoch 819: val_acc did not improve from 0.72000
10/10 [==============================] - 92s 10s/step - loss: 0.0599 - acc: 0.9750 - val_loss: 2.3032 - val_acc: 0.7030
Epoch 820/900
10/10 [==============================] - ETA: 0s - loss: 0.1345 - acc: 0.9600
Epoch 820: val_acc did not improve from 0.72000
10/10 [==============================] - 90s 9s/step - loss: 0.1345 - acc: 0.9600 - val_loss: 2.0507 - val_acc: 0.6930
Epoch 821/900
10/10 [==============================] - ETA: 0s - loss: 0.0613 - acc: 0.9850
Epoch 821: val_acc did not improve from 0.72000
10/10 [==============================] - 92s 10s/step - loss: 0.0613 - acc: 0.9850 - val_loss: 1.9277 - val_acc: 0.6900
Epoch 822/900
10/10 [==============================] - ETA: 0s - loss: 0.0587 - acc: 0.9800
Epoch 822: val_acc did not improve from 0.72000
10/10 [==============================] - 96s 10s/step - loss: 0.0587 - acc: 0.9800 - val_loss: 1.9737 - val_acc: 0.6850
Epoch 823/900
10/10 [==============================] - ETA: 0s - loss: 0.1214 - acc: 0.9700
Epoch 823: val_acc did not improve from 0.72000
10/10 [==============================] - 96s 10s/step - loss: 0.1214 - acc: 0.9700 - val_loss: 3.0378 - val_acc: 0.6740
Epoch 824/900
10/10 [==============================] - ETA: 0s - loss: 0.2767 - acc: 0.9550
Epoch 824: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.2767 - acc: 0.9550 - val_loss: 3.3765 - val_acc: 0.6550
Epoch 825/900
10/10 [==============================] - ETA: 0s - loss: 0.1463 - acc: 0.9550
Epoch 825: val_acc did not improve from 0.72000
10/10 [==============================] - 99s 10s/step - loss: 0.1463 - acc: 0.9550 - val_loss: 3.8881 - val_acc: 0.6440
Epoch 826/900
10/10 [==============================] - ETA: 0s - loss: 0.1572 - acc: 0.9600
Epoch 826: val_acc did not improve from 0.72000
10/10 [==============================] - 101s 11s/step - loss: 0.1572 - acc: 0.9600 - val_loss: 3.0920 - val_acc: 0.6590
Epoch 827/900
10/10 [==============================] - ETA: 0s - loss: 0.1743 - acc: 0.9650
Epoch 827: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.1743 - acc: 0.9650 - val_loss: 2.6041 - val_acc: 0.6520
Epoch 828/900
10/10 [==============================] - ETA: 0s - loss: 0.3121 - acc: 0.9500
Epoch 828: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.3121 - acc: 0.9500 - val_loss: 3.2781 - val_acc: 0.6440
Epoch 829/900
10/10 [==============================] - ETA: 0s - loss: 0.2336 - acc: 0.9500
Epoch 829: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.2336 - acc: 0.9500 - val_loss: 2.4599 - val_acc: 0.6560
Epoch 830/900
10/10 [==============================] - ETA: 0s - loss: 0.1323 - acc: 0.9750
Epoch 830: val_acc did not improve from 0.72000
10/10 [==============================] - 96s 10s/step - loss: 0.1323 - acc: 0.9750 - val_loss: 2.1611 - val_acc: 0.6710
Epoch 831/900
10/10 [==============================] - ETA: 0s - loss: 0.0590 - acc: 0.9850
Epoch 831: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.0590 - acc: 0.9850 - val_loss: 1.8724 - val_acc: 0.6910
Epoch 832/900
10/10 [==============================] - ETA: 0s - loss: 0.2082 - acc: 0.9700
Epoch 832: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.2082 - acc: 0.9700 - val_loss: 2.0091 - val_acc: 0.7050
Epoch 833/900
10/10 [==============================] - ETA: 0s - loss: 0.1277 - acc: 0.9600
Epoch 833: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.1277 - acc: 0.9600 - val_loss: 1.9180 - val_acc: 0.7050
Epoch 834/900
10/10 [==============================] - ETA: 0s - loss: 0.0836 - acc: 0.9800
Epoch 834: val_acc did not improve from 0.72000
10/10 [==============================] - 89s 9s/step - loss: 0.0836 - acc: 0.9800 - val_loss: 2.1199 - val_acc: 0.6970
Epoch 835/900
10/10 [==============================] - ETA: 0s - loss: 0.1282 - acc: 0.9600
Epoch 835: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.1282 - acc: 0.9600 - val_loss: 2.4351 - val_acc: 0.6940
Epoch 836/900
10/10 [==============================] - ETA: 0s - loss: 0.0480 - acc: 0.9850
Epoch 836: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.0480 - acc: 0.9850 - val_loss: 2.1244 - val_acc: 0.7070
Epoch 837/900
10/10 [==============================] - ETA: 0s - loss: 0.0844 - acc: 0.9700
Epoch 837: val_acc did not improve from 0.72000
10/10 [==============================] - 98s 10s/step - loss: 0.0844 - acc: 0.9700 - val_loss: 1.8097 - val_acc: 0.7100
Epoch 838/900
10/10 [==============================] - ETA: 0s - loss: 0.0982 - acc: 0.9800
Epoch 838: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.0982 - acc: 0.9800 - val_loss: 1.8226 - val_acc: 0.7000
Epoch 839/900
10/10 [==============================] - ETA: 0s - loss: 0.1452 - acc: 0.9800
Epoch 839: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.1452 - acc: 0.9800 - val_loss: 1.9787 - val_acc: 0.7190
Epoch 840/900
10/10 [==============================] - ETA: 0s - loss: 0.1633 - acc: 0.9550
Epoch 840: val_acc did not improve from 0.72000
10/10 [==============================] - 94s 10s/step - loss: 0.1633 - acc: 0.9550 - val_loss: 2.0270 - val_acc: 0.7130
Epoch 841/900
10/10 [==============================] - ETA: 0s - loss: 0.0418 - acc: 0.9800
Epoch 841: val_acc did not improve from 0.72000
10/10 [==============================] - 98s 10s/step - loss: 0.0418 - acc: 0.9800 - val_loss: 1.9262 - val_acc: 0.7140
Epoch 842/900
10/10 [==============================] - ETA: 0s - loss: 0.1474 - acc: 0.9700
Epoch 842: val_acc did not improve from 0.72000
10/10 [==============================] - 96s 10s/step - loss: 0.1474 - acc: 0.9700 - val_loss: 2.3462 - val_acc: 0.6950
Epoch 843/900
10/10 [==============================] - ETA: 0s - loss: 0.0638 - acc: 0.9850
Epoch 843: val_acc did not improve from 0.72000
10/10 [==============================] - 97s 10s/step - loss: 0.0638 - acc: 0.9850 - val_loss: 2.1442 - val_acc: 0.7110
Epoch 844/900
10/10 [==============================] - ETA: 0s - loss: 0.0756 - acc: 0.9850
Epoch 844: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.0756 - acc: 0.9850 - val_loss: 1.9374 - val_acc: 0.7150
Epoch 845/900
10/10 [==============================] - ETA: 0s - loss: 0.1753 - acc: 0.9698
Epoch 845: val_acc did not improve from 0.72000
10/10 [==============================] - 92s 10s/step - loss: 0.1753 - acc: 0.9698 - val_loss: 2.0223 - val_acc: 0.6790
Epoch 846/900
10/10 [==============================] - ETA: 0s - loss: 0.2685 - acc: 0.9500
Epoch 846: val_acc did not improve from 0.72000
10/10 [==============================] - 93s 10s/step - loss: 0.2685 - acc: 0.9500 - val_loss: 2.3212 - val_acc: 0.6670
Epoch 847/900
10/10 [==============================] - ETA: 0s - loss: 0.1120 - acc: 0.9650
Epoch 847: val_acc did not improve from 0.72000
10/10 [==============================] - 95s 10s/step - loss: 0.1120 - acc: 0.9650 - val_loss: 1.9444 - val_acc: 0.6860
Epoch 848/900
10/10 [==============================] - ETA: 0s - loss: 0.1561 - acc: 0.9700
Epoch 848: val_acc did not improve from 0.72000
10/10 [==============================] - 447s 49s/step - loss: 0.1561 - acc: 0.9700 - val_loss: 1.7083 - val_acc: 0.7020
Epoch 849/900
10/10 [==============================] - ETA: 0s - loss: 0.2394 - acc: 0.9550
Epoch 849: val_acc did not improve from 0.72000
10/10 [==============================] - 89s 9s/step - loss: 0.2394 - acc: 0.9550 - val_loss: 1.9904 - val_acc: 0.7030
Epoch 850/900
10/10 [==============================] - ETA: 0s - loss: 0.0947 - acc: 0.9850
Epoch 850: val_acc did not improve from 0.72000
10/10 [==============================] - 84s 9s/step - loss: 0.0947 - acc: 0.9850 - val_loss: 2.0480 - val_acc: 0.7180
Epoch 851/900
10/10 [==============================] - ETA: 0s - loss: 0.0923 - acc: 0.9800
Epoch 851: val_acc improved from 0.72000 to 0.74200, saving model to lrbest_brand_1_49.h5
10/10 [==============================] - 94s 10s/step - loss: 0.0923 - acc: 0.9800 - val_loss: 1.6226 - val_acc: 0.7420
Epoch 852/900
10/10 [==============================] - ETA: 0s - loss: 0.0949 - acc: 0.9650
Epoch 852: val_acc improved from 0.74200 to 0.74500, saving model to lrbest_brand_1_49.h5
10/10 [==============================] - 1315s 146s/step - loss: 0.0949 - acc: 0.9650 - val_loss: 1.7047 - val_acc: 0.7450
Epoch 853/900
10/10 [==============================] - ETA: 0s - loss: 0.0693 - acc: 0.9800
Epoch 853: val_acc did not improve from 0.74500
10/10 [==============================] - 86s 9s/step - loss: 0.0693 - acc: 0.9800 - val_loss: 1.7053 - val_acc: 0.7400
Epoch 854/900
10/10 [==============================] - ETA: 0s - loss: 0.0299 - acc: 0.9950
Epoch 854: val_acc did not improve from 0.74500
10/10 [==============================] - 89s 9s/step - loss: 0.0299 - acc: 0.9950 - val_loss: 1.6219 - val_acc: 0.7370
Epoch 855/900
10/10 [==============================] - ETA: 0s - loss: 0.1456 - acc: 0.9650
Epoch 855: val_acc did not improve from 0.74500
10/10 [==============================] - 87s 9s/step - loss: 0.1456 - acc: 0.9650 - val_loss: 1.9800 - val_acc: 0.6990
Epoch 856/900
10/10 [==============================] - ETA: 0s - loss: 0.1535 - acc: 0.9650
Epoch 856: val_acc did not improve from 0.74500
10/10 [==============================] - 84s 9s/step - loss: 0.1535 - acc: 0.9650 - val_loss: 1.8653 - val_acc: 0.7240
Epoch 857/900
10/10 [==============================] - ETA: 0s - loss: 0.0659 - acc: 0.9800
Epoch 857: val_acc did not improve from 0.74500
10/10 [==============================] - 84s 9s/step - loss: 0.0659 - acc: 0.9800 - val_loss: 1.8506 - val_acc: 0.7080
Epoch 858/900
10/10 [==============================] - ETA: 0s - loss: 0.0214 - acc: 0.9900
Epoch 858: val_acc did not improve from 0.74500
10/10 [==============================] - 90s 9s/step - loss: 0.0214 - acc: 0.9900 - val_loss: 1.8732 - val_acc: 0.7010
Epoch 859/900
10/10 [==============================] - ETA: 0s - loss: 0.1051 - acc: 0.9800
Epoch 859: val_acc did not improve from 0.74500
10/10 [==============================] - 87s 9s/step - loss: 0.1051 - acc: 0.9800 - val_loss: 2.5801 - val_acc: 0.6890
Epoch 860/900
10/10 [==============================] - ETA: 0s - loss: 0.3583 - acc: 0.9450
Epoch 860: val_acc did not improve from 0.74500
10/10 [==============================] - 88s 9s/step - loss: 0.3583 - acc: 0.9450 - val_loss: 2.6811 - val_acc: 0.6810
Epoch 861/900
10/10 [==============================] - ETA: 0s - loss: 0.1467 - acc: 0.9650
Epoch 861: val_acc did not improve from 0.74500
10/10 [==============================] - 88s 9s/step - loss: 0.1467 - acc: 0.9650 - val_loss: 2.7021 - val_acc: 0.6970
Epoch 862/900
10/10 [==============================] - ETA: 0s - loss: 0.2163 - acc: 0.9800
Epoch 862: val_acc did not improve from 0.74500
10/10 [==============================] - 91s 10s/step - loss: 0.2163 - acc: 0.9800 - val_loss: 3.9987 - val_acc: 0.6430
Epoch 863/900
10/10 [==============================] - ETA: 0s - loss: 0.0971 - acc: 0.9700
Epoch 863: val_acc did not improve from 0.74500
10/10 [==============================] - 93s 10s/step - loss: 0.0971 - acc: 0.9700 - val_loss: 3.8097 - val_acc: 0.6620
Epoch 864/900
10/10 [==============================] - ETA: 0s - loss: 0.0749 - acc: 0.9800
Epoch 864: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.0749 - acc: 0.9800 - val_loss: 2.5030 - val_acc: 0.7100
Epoch 865/900
10/10 [==============================] - ETA: 0s - loss: 0.1277 - acc: 0.9800
Epoch 865: val_acc did not improve from 0.74500
10/10 [==============================] - 152s 16s/step - loss: 0.1277 - acc: 0.9800 - val_loss: 2.5285 - val_acc: 0.7090
Epoch 866/900
10/10 [==============================] - ETA: 0s - loss: 0.1387 - acc: 0.9800
Epoch 866: val_acc did not improve from 0.74500
10/10 [==============================] - 99s 10s/step - loss: 0.1387 - acc: 0.9800 - val_loss: 2.5771 - val_acc: 0.6990
Epoch 867/900
10/10 [==============================] - ETA: 0s - loss: 0.1701 - acc: 0.9650
Epoch 867: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.1701 - acc: 0.9650 - val_loss: 2.5573 - val_acc: 0.6920
Epoch 868/900
10/10 [==============================] - ETA: 0s - loss: 0.1223 - acc: 0.9700
Epoch 868: val_acc did not improve from 0.74500
10/10 [==============================] - 98s 10s/step - loss: 0.1223 - acc: 0.9700 - val_loss: 2.2864 - val_acc: 0.7060
Epoch 869/900
10/10 [==============================] - ETA: 0s - loss: 0.1436 - acc: 0.9548
Epoch 869: val_acc did not improve from 0.74500
10/10 [==============================] - 94s 10s/step - loss: 0.1436 - acc: 0.9548 - val_loss: 2.0477 - val_acc: 0.7110
Epoch 870/900
10/10 [==============================] - ETA: 0s - loss: 0.0806 - acc: 0.9750
Epoch 870: val_acc did not improve from 0.74500
10/10 [==============================] - 96s 10s/step - loss: 0.0806 - acc: 0.9750 - val_loss: 2.2687 - val_acc: 0.7020
Epoch 871/900
10/10 [==============================] - ETA: 0s - loss: 0.0722 - acc: 0.9800
Epoch 871: val_acc did not improve from 0.74500
10/10 [==============================] - 101s 11s/step - loss: 0.0722 - acc: 0.9800 - val_loss: 1.8828 - val_acc: 0.7240
Epoch 872/900
10/10 [==============================] - ETA: 0s - loss: 0.1015 - acc: 0.9800
Epoch 872: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.1015 - acc: 0.9800 - val_loss: 1.9429 - val_acc: 0.7020
Epoch 873/900
10/10 [==============================] - ETA: 0s - loss: 0.2502 - acc: 0.9550
Epoch 873: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.2502 - acc: 0.9550 - val_loss: 2.0423 - val_acc: 0.7100
Epoch 874/900
10/10 [==============================] - ETA: 0s - loss: 0.0880 - acc: 0.9750
Epoch 874: val_acc did not improve from 0.74500
10/10 [==============================] - 94s 10s/step - loss: 0.0880 - acc: 0.9750 - val_loss: 1.7831 - val_acc: 0.7280
Epoch 875/900
10/10 [==============================] - ETA: 0s - loss: 0.0605 - acc: 0.9800
Epoch 875: val_acc did not improve from 0.74500
10/10 [==============================] - 92s 10s/step - loss: 0.0605 - acc: 0.9800 - val_loss: 1.6783 - val_acc: 0.7390
Epoch 876/900
10/10 [==============================] - ETA: 0s - loss: 0.1119 - acc: 0.9750
Epoch 876: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.1119 - acc: 0.9750 - val_loss: 1.7231 - val_acc: 0.7320
Epoch 877/900
10/10 [==============================] - ETA: 0s - loss: 0.0136 - acc: 0.9950
Epoch 877: val_acc did not improve from 0.74500
10/10 [==============================] - 96s 10s/step - loss: 0.0136 - acc: 0.9950 - val_loss: 1.7213 - val_acc: 0.7350
Epoch 878/900
10/10 [==============================] - ETA: 0s - loss: 0.0442 - acc: 0.9900
Epoch 878: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.0442 - acc: 0.9900 - val_loss: 1.9065 - val_acc: 0.7250
Epoch 879/900
10/10 [==============================] - ETA: 0s - loss: 0.0399 - acc: 0.9900
Epoch 879: val_acc did not improve from 0.74500
10/10 [==============================] - 82s 9s/step - loss: 0.0399 - acc: 0.9900 - val_loss: 1.7287 - val_acc: 0.7260
Epoch 880/900
10/10 [==============================] - ETA: 0s - loss: 0.0788 - acc: 0.9800
Epoch 880: val_acc did not improve from 0.74500
10/10 [==============================] - 82s 9s/step - loss: 0.0788 - acc: 0.9800 - val_loss: 2.3758 - val_acc: 0.6870
Epoch 881/900
10/10 [==============================] - ETA: 0s - loss: 0.1772 - acc: 0.9750
Epoch 881: val_acc did not improve from 0.74500
10/10 [==============================] - 82s 9s/step - loss: 0.1772 - acc: 0.9750 - val_loss: 2.4928 - val_acc: 0.7120
Epoch 882/900
10/10 [==============================] - ETA: 0s - loss: 0.0949 - acc: 0.9800
Epoch 882: val_acc did not improve from 0.74500
10/10 [==============================] - 786s 87s/step - loss: 0.0949 - acc: 0.9800 - val_loss: 2.3051 - val_acc: 0.7000
Epoch 883/900
10/10 [==============================] - ETA: 0s - loss: 0.1100 - acc: 0.9650
Epoch 883: val_acc did not improve from 0.74500
10/10 [==============================] - 78s 8s/step - loss: 0.1100 - acc: 0.9650 - val_loss: 2.1888 - val_acc: 0.7130
Epoch 884/900
10/10 [==============================] - ETA: 0s - loss: 0.2453 - acc: 0.9799
Epoch 884: val_acc did not improve from 0.74500
10/10 [==============================] - 75s 8s/step - loss: 0.2453 - acc: 0.9799 - val_loss: 2.0951 - val_acc: 0.7140
Epoch 885/900
10/10 [==============================] - ETA: 0s - loss: 0.2945 - acc: 0.9750
Epoch 885: val_acc did not improve from 0.74500
10/10 [==============================] - 75s 8s/step - loss: 0.2945 - acc: 0.9750 - val_loss: 2.3629 - val_acc: 0.7040
Epoch 886/900
10/10 [==============================] - ETA: 0s - loss: 0.0467 - acc: 0.9850
Epoch 886: val_acc did not improve from 0.74500
10/10 [==============================] - 76s 8s/step - loss: 0.0467 - acc: 0.9850 - val_loss: 2.2268 - val_acc: 0.7140
Epoch 887/900
10/10 [==============================] - ETA: 0s - loss: 0.1784 - acc: 0.9700
Epoch 887: val_acc did not improve from 0.74500
10/10 [==============================] - 78s 8s/step - loss: 0.1784 - acc: 0.9700 - val_loss: 2.0799 - val_acc: 0.7020
Epoch 888/900
10/10 [==============================] - ETA: 0s - loss: 0.0759 - acc: 0.9700
Epoch 888: val_acc did not improve from 0.74500
10/10 [==============================] - 177s 19s/step - loss: 0.0759 - acc: 0.9700 - val_loss: 1.9450 - val_acc: 0.7200
Epoch 889/900
10/10 [==============================] - ETA: 0s - loss: 0.1360 - acc: 0.9700
Epoch 889: val_acc did not improve from 0.74500
10/10 [==============================] - 90s 10s/step - loss: 0.1360 - acc: 0.9700 - val_loss: 1.8495 - val_acc: 0.7150
Epoch 890/900
10/10 [==============================] - ETA: 0s - loss: 0.0953 - acc: 0.9698
Epoch 890: val_acc did not improve from 0.74500
10/10 [==============================] - 87s 9s/step - loss: 0.0953 - acc: 0.9698 - val_loss: 2.0171 - val_acc: 0.7190
Epoch 891/900
10/10 [==============================] - ETA: 0s - loss: 0.1972 - acc: 0.9600
Epoch 891: val_acc did not improve from 0.74500
10/10 [==============================] - 80s 8s/step - loss: 0.1972 - acc: 0.9600 - val_loss: 2.0584 - val_acc: 0.7050
Epoch 892/900
10/10 [==============================] - ETA: 0s - loss: 0.1276 - acc: 0.9700
Epoch 892: val_acc did not improve from 0.74500
10/10 [==============================] - 81s 9s/step - loss: 0.1276 - acc: 0.9700 - val_loss: 1.8146 - val_acc: 0.7380
Epoch 893/900
10/10 [==============================] - ETA: 0s - loss: 0.1233 - acc: 0.9750
Epoch 893: val_acc did not improve from 0.74500
10/10 [==============================] - 83s 9s/step - loss: 0.1233 - acc: 0.9750 - val_loss: 2.2162 - val_acc: 0.7200
Epoch 894/900
10/10 [==============================] - ETA: 0s - loss: 0.0526 - acc: 0.9750
Epoch 894: val_acc did not improve from 0.74500
10/10 [==============================] - 764s 84s/step - loss: 0.0526 - acc: 0.9750 - val_loss: 2.1579 - val_acc: 0.7220
Epoch 895/900
10/10 [==============================] - ETA: 0s - loss: 0.0781 - acc: 0.9700
Epoch 895: val_acc did not improve from 0.74500
10/10 [==============================] - 91s 10s/step - loss: 0.0781 - acc: 0.9700 - val_loss: 2.1839 - val_acc: 0.7280
Epoch 896/900
10/10 [==============================] - ETA: 0s - loss: 0.1541 - acc: 0.9800
Epoch 896: val_acc did not improve from 0.74500
10/10 [==============================] - 95s 10s/step - loss: 0.1541 - acc: 0.9800 - val_loss: 2.2485 - val_acc: 0.7140
Epoch 897/900
10/10 [==============================] - ETA: 0s - loss: 0.1317 - acc: 0.9650
Epoch 897: val_acc did not improve from 0.74500
10/10 [==============================] - 92s 10s/step - loss: 0.1317 - acc: 0.9650 - val_loss: 2.2170 - val_acc: 0.7170
Epoch 898/900
10/10 [==============================] - ETA: 0s - loss: 0.1174 - acc: 0.9600
Epoch 898: val_acc did not improve from 0.74500
10/10 [==============================] - 94s 10s/step - loss: 0.1174 - acc: 0.9600 - val_loss: 2.5838 - val_acc: 0.6920
Epoch 899/900
10/10 [==============================] - ETA: 0s - loss: 0.0316 - acc: 0.9900
Epoch 899: val_acc did not improve from 0.74500
10/10 [==============================] - 87s 9s/step - loss: 0.0316 - acc: 0.9900 - val_loss: 2.1390 - val_acc: 0.7080
Epoch 900/900
10/10 [==============================] - ETA: 0s - loss: 0.1985 - acc: 0.9750
Epoch 900: val_acc did not improve from 0.74500
10/10 [==============================] - 89s 9s/step - loss: 0.1985 - acc: 0.9750 - val_loss: 2.0407 - val_acc: 0.7180

(alfonso1) c:\CarsBrands_Inceptionv3>



The results of the test are evaluated by executing
==================================================



lrGuessCarsBrandsKaggle_Inception_v3_1_49.py




(alfonso1) c:\CarsBrands_Inceptionv3>python lrGuessCarsBrandsKaggle_Inception_v3_1_49.py
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\numpy\_distributor_init.py:30: UserWarning: loaded more than 1 DLL from .libs:
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\numpy\.libs\libopenblas.FB5AE2TYXYH2IJRDKGDGQ3XBKLKTF43H.gfortran-win_amd64.dll
C:\Users\Alfonso Blanco\.conda\envs\alfonso1\lib\site-packages\numpy\.libs\libopenblas64__v0.3.21-gcc_10_3_0.dll
  warnings.warn("loaded more than 1 DLL from .libs:"
2023-09-02 21:17:52.567384: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 838860800 exceeds 10% of free system memory.
2023-09-02 21:17:53.250702: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 838860800 exceeds 10% of free system memory.
2023-09-02 21:17:53.326413: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 838860800 exceeds 10% of free system memory.
2023-09-02 21:17:55.562550: W tensorflow/tsl/framework/cpu_allocator_impl.cc:83] Allocation of 838860800 exceeds 10% of free system memory.
1/1 [==============================] - 1s 1s/step
HIT 07999.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 95ms/step
HIT 08000.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 79ms/step
HIT 08001.jpg is assigned brand 27Jeep

1/1 [==============================] - 0s 94ms/step
ERROR 08002.jpg is assigned brand 20Geo
  True brand is 35Mercedes-Benz

1/1 [==============================] - 0s 94ms/step
HIT 08003.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 94ms/step
HIT 08004.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 94ms/step
ERROR 08005.jpg is assigned brand 23Hyundai
  True brand is 2Acura

1/1 [==============================] - 0s 94ms/step
HIT 08006.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 94ms/step
ERROR 08007.jpg is assigned brand 10Chevrolet
  True brand is 5BMW

1/1 [==============================] - 0s 80ms/step
HIT 08008.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 94ms/step
HIT 08009.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 94ms/step
HIT 08010.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 94ms/step
ERROR 08011.jpg is assigned brand 21HUMMER
  True brand is 1AM

1/1 [==============================] - 0s 94ms/step
HIT 08012.jpg is assigned brand 28Lamborghini

1/1 [==============================] - 0s 94ms/step
ERROR 08013.jpg is assigned brand 37Nissan
  True brand is 19GMC

1/1 [==============================] - 0s 79ms/step
HIT 08014.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 94ms/step
ERROR 08015.jpg is assigned brand 35Mercedes-Benz
  True brand is 6Bentley

1/1 [==============================] - 0s 95ms/step
HIT 08016.jpg is assigned brand 2Acura

1/1 [==============================] - 0s 94ms/step
HIT 08017.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 98ms/step
ERROR 08018.jpg is assigned brand 10Chevrolet
  True brand is 2Acura

1/1 [==============================] - 0s 79ms/step
HIT 08019.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 90ms/step
HIT 08020.jpg is assigned brand 13Dodge

1/1 [==============================] - 0s 94ms/step
HIT 08021.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 94ms/step
HIT 08022.jpg is assigned brand 28Lamborghini

1/1 [==============================] - 0s 110ms/step
HIT 08023.jpg is assigned brand 24Infiniti

1/1 [==============================] - 0s 95ms/step
ERROR 08024.jpg is assigned brand 35Mercedes-Benz
  True brand is 33Mazda

1/1 [==============================] - 0s 79ms/step
HIT 08025.jpg is assigned brand 19GMC

1/1 [==============================] - 0s 94ms/step
HIT 08026.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 94ms/step
HIT 08027.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 79ms/step
HIT 08028.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 79ms/step
HIT 08029.jpg is assigned brand 18Ford

1/1 [==============================] - 0s 78ms/step
ERROR 08030.jpg is assigned brand 2Acura
  True brand is 15FIAT

1/1 [==============================] - 0s 78ms/step
HIT 08031.jpg is assigned brand 1AM

1/1 [==============================] - 0s 80ms/step
HIT 08032.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 94ms/step
HIT 08033.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 94ms/step
HIT 08034.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 78ms/step
HIT 08035.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 78ms/step
ERROR 08036.jpg is assigned brand 23Hyundai
  True brand is 46Toyota

1/1 [==============================] - 0s 94ms/step
ERROR 08037.jpg is assigned brand 18Ford
  True brand is 10Chevrolet

1/1 [==============================] - 0s 94ms/step
HIT 08038.jpg is assigned brand 11Chrysler

1/1 [==============================] - 0s 94ms/step
HIT 08039.jpg is assigned brand 27Jeep

1/1 [==============================] - 0s 95ms/step
ERROR 08040.jpg is assigned brand 2Acura
  True brand is 10Chevrolet

1/1 [==============================] - 0s 94ms/step
HIT 08041.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 94ms/step
HIT 08042.jpg is assigned brand 8Buick

1/1 [==============================] - 0s 94ms/step
HIT 08043.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 94ms/step
ERROR 08044.jpg is assigned brand 16Ferrari
  True brand is 3Astom Martin

1/1 [==============================] - 0s 110ms/step
HIT 08045.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 95ms/step
ERROR 08046.jpg is assigned brand 2Acura
  True brand is 46Toyota

1/1 [==============================] - 0s 78ms/step
HIT 08047.jpg is assigned brand 11Chrysler

1/1 [==============================] - 0s 80ms/step
ERROR 08048.jpg is assigned brand 10Chevrolet
  True brand is 5BMW

1/1 [==============================] - 0s 78ms/step
ERROR 08049.jpg is assigned brand 46Toyota
  True brand is 10Chevrolet

1/1 [==============================] - 0s 95ms/step
ERROR 08050.jpg is assigned brand 22Honda
  True brand is 13Dodge

1/1 [==============================] - 0s 96ms/step
ERROR 08051.jpg is assigned brand 5BMW
  True brand is 3Astom Martin

1/1 [==============================] - 0s 78ms/step
HIT 08052.jpg is assigned brand 29Land Rover

1/1 [==============================] - 0s 94ms/step
HIT 08053.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 95ms/step
ERROR 08054.jpg is assigned brand 45Tesla
  True brand is 18Ford

1/1 [==============================] - 0s 110ms/step
ERROR 08055.jpg is assigned brand 2Acura
  True brand is 4Audi

1/1 [==============================] - 0s 96ms/step
ERROR 08056.jpg is assigned brand 10Chevrolet
  True brand is 19GMC

1/1 [==============================] - 0s 79ms/step
HIT 08057.jpg is assigned brand 25Isuzu

1/1 [==============================] - 0s 96ms/step
HIT 08058.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 94ms/step
HIT 08059.jpg is assigned brand 19GMC

1/1 [==============================] - 0s 84ms/step
ERROR 08060.jpg is assigned brand 11Chrysler
  True brand is 27Jeep

1/1 [==============================] - 0s 94ms/step
HIT 08061.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 94ms/step
HIT 08062.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 95ms/step
ERROR 08063.jpg is assigned brand 27Jeep
  True brand is 19GMC

1/1 [==============================] - 0s 97ms/step
HIT 08064.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 94ms/step
HIT 08065.jpg is assigned brand 27Jeep

1/1 [==============================] - 0s 94ms/step
ERROR 08066.jpg is assigned brand 5BMW
  True brand is 18Ford

1/1 [==============================] - 0s 94ms/step
ERROR 08067.jpg is assigned brand 32Maybach
  True brand is 28Lamborghini

1/1 [==============================] - 0s 109ms/step
HIT 08068.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 110ms/step
HIT 08069.jpg is assigned brand 29Land Rover

1/1 [==============================] - 0s 110ms/step
HIT 08070.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 111ms/step
ERROR 08071.jpg is assigned brand 23Hyundai
  True brand is 48Volvo

1/1 [==============================] - 0s 110ms/step
HIT 08072.jpg is assigned brand 22Honda

1/1 [==============================] - 0s 94ms/step
HIT 08073.jpg is assigned brand 6Bentley

1/1 [==============================] - 0s 110ms/step
ERROR 08074.jpg is assigned brand 2Acura
  True brand is 10Chevrolet

1/1 [==============================] - 0s 95ms/step
HIT 08075.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 110ms/step
ERROR 08076.jpg is assigned brand 2Acura
  True brand is 17FisKer

1/1 [==============================] - 0s 110ms/step
HIT 08077.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 95ms/step
HIT 08078.jpg is assigned brand 44Suzuki

1/1 [==============================] - 0s 95ms/step
HIT 08079.jpg is assigned brand 18Ford

1/1 [==============================] - 0s 94ms/step
HIT 08080.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 110ms/step
HIT 08081.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 94ms/step
HIT 08082.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 95ms/step
HIT 08083.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 95ms/step
HIT 08084.jpg is assigned brand 23Hyundai

1/1 [==============================] - 0s 95ms/step
HIT 08085.jpg is assigned brand 3Astom Martin

1/1 [==============================] - 0s 109ms/step
HIT 08086.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 109ms/step
ERROR 08087.jpg is assigned brand 10Chevrolet
  True brand is 20Geo

1/1 [==============================] - 0s 94ms/step
HIT 08088.jpg is assigned brand 47Volkswagen

1/1 [==============================] - 0s 110ms/step
HIT 08089.jpg is assigned brand 22Honda

1/1 [==============================] - 0s 94ms/step
HIT 08090.jpg is assigned brand 13Dodge

1/1 [==============================] - 0s 94ms/step
HIT 08091.jpg is assigned brand 13Dodge

1/1 [==============================] - 0s 96ms/step
HIT 08092.jpg is assigned brand 13Dodge

1/1 [==============================] - 0s 94ms/step
HIT 08093.jpg is assigned brand 16Ferrari

1/1 [==============================] - 0s 125ms/step
HIT 08094.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 128ms/step
ERROR 08095.jpg is assigned brand 10Chevrolet
  True brand is 7Bugatti

1/1 [==============================] - 0s 127ms/step
HIT 08096.jpg is assigned brand 3Astom Martin

1/1 [==============================] - 0s 142ms/step
HIT 08097.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 143ms/step
HIT 08098.jpg is assigned brand 44Suzuki

1/1 [==============================] - 0s 142ms/step
ERROR 08099.jpg is assigned brand 19GMC
  True brand is 18Ford

1/1 [==============================] - 0s 141ms/step
HIT 08100.jpg is assigned brand 11Chrysler

1/1 [==============================] - 0s 126ms/step
HIT 08101.jpg is assigned brand 37Nissan

1/1 [==============================] - 0s 127ms/step
ERROR 08102.jpg is assigned brand 23Hyundai
  True brand is 35Mercedes-Benz

1/1 [==============================] - 0s 143ms/step
HIT 08103.jpg is assigned brand 46Toyota

1/1 [==============================] - 0s 142ms/step
HIT 08104.jpg is assigned brand 46Toyota

1/1 [==============================] - 0s 157ms/step
ERROR 08105.jpg is assigned brand 47Volkswagen
  True brand is 13Dodge

1/1 [==============================] - 0s 141ms/step
HIT 08106.jpg is assigned brand 28Lamborghini

1/1 [==============================] - 0s 141ms/step
HIT 08107.jpg is assigned brand 11Chrysler

1/1 [==============================] - 0s 144ms/step
HIT 08108.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 140ms/step
ERROR 08109.jpg is assigned brand 11Chrysler
  True brand is 29Land Rover

1/1 [==============================] - 0s 141ms/step
HIT 08110.jpg is assigned brand 46Toyota

1/1 [==============================] - 0s 127ms/step
HIT 08111.jpg is assigned brand 37Nissan

1/1 [==============================] - 0s 126ms/step
HIT 08112.jpg is assigned brand 13Dodge

1/1 [==============================] - 0s 117ms/step
HIT 08113.jpg is assigned brand 18Ford

1/1 [==============================] - 0s 110ms/step
ERROR 08114.jpg is assigned brand 13Dodge
  True brand is 35Mercedes-Benz

1/1 [==============================] - 0s 110ms/step
ERROR 08115.jpg is assigned brand 35Mercedes-Benz
  True brand is 34McLaren

1/1 [==============================] - 0s 109ms/step
HIT 08116.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 94ms/step
HIT 08117.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 109ms/step
HIT 08118.jpg is assigned brand 5BMW

1/1 [==============================] - 0s 111ms/step
HIT 08119.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 94ms/step
HIT 08120.jpg is assigned brand 22Honda

1/1 [==============================] - 0s 98ms/step
ERROR 08121.jpg is assigned brand 6Bentley
  True brand is 28Lamborghini

1/1 [==============================] - 0s 110ms/step
HIT 08122.jpg is assigned brand 9Cadillac

1/1 [==============================] - 0s 110ms/step
HIT 08123.jpg is assigned brand 42Scion

1/1 [==============================] - 0s 94ms/step
HIT 08124.jpg is assigned brand 6Bentley

1/1 [==============================] - 0s 111ms/step
HIT 08125.jpg is assigned brand 10Chevrolet

1/1 [==============================] - 0s 95ms/step
ERROR 08126.jpg is assigned brand 23Hyundai
  True brand is 18Ford

1/1 [==============================] - 0s 94ms/step
HIT 08127.jpg is assigned brand 2Acura

1/1 [==============================] - 0s 94ms/step
HIT 08128.jpg is assigned brand 18Ford

1/1 [==============================] - 0s 94ms/step
ERROR 08129.jpg is assigned brand 14Eagle
  True brand is 7Bugatti

1/1 [==============================] - 0s 94ms/step
HIT 08130.jpg is assigned brand 7Bugatti

1/1 [==============================] - 0s 94ms/step
HIT 08131.jpg is assigned brand 19GMC

1/1 [==============================] - 0s 110ms/step
HIT 08132.jpg is assigned brand 28Lamborghini

1/1 [==============================] - 0s 110ms/step
HIT 08133.jpg is assigned brand 2Acura

1/1 [==============================] - 0s 111ms/step
HIT 08134.jpg is assigned brand 21HUMMER

1/1 [==============================] - 0s 94ms/step
HIT 08135.jpg is assigned brand 13Dodge

1/1 [==============================] - 0s 110ms/step
HIT 08136.jpg is assigned brand 46Toyota

1/1 [==============================] - 0s 110ms/step
HIT 08137.jpg is assigned brand 4Audi

1/1 [==============================] - 0s 109ms/step
HIT 08138.jpg is assigned brand 44Suzuki

1/1 [==============================] - 0s 109ms/step
ERROR 08139.jpg is assigned brand 2Acura
  True brand is 46Toyota

1/1 [==============================] - 0s 111ms/step
ERROR 08140.jpg is assigned brand 10Chevrolet
  True brand is 11Chrysler

1/1 [==============================] - 0s 110ms/step
HIT 08141.jpg is assigned brand 49smart

1/1 [==============================] - 0s 94ms/step
HIT 08142.jpg is assigned brand 35Mercedes-Benz

1/1 [==============================] - 0s 109ms/step
ERROR 08143.jpg is assigned brand 10Chevrolet
  True brand is 18Ford

1/1 [==============================] - 0s 94ms/step
HIT 08144.jpg is assigned brand 4Audi


Total hits = 104
Total failures = 42
Accuracy = 71.23287671232876%

(alfonso1) c:\CarsBrands_Inceptionv3>

Shows the results of the test with images from 8000.jpg to 8144.jpg, which have not been used as train or valid.









The results of the training are also shown in the attached file lr val_acc 49 epoch 800-900.txt and the results of the test with images from 8000.jpg to 8144.jpg, which have not been used as train or valid, in the file ResultsTestCarBrands.txt which is also attached



lrModelCarsBrands_Inception_v3_1_49.h5 is taken as the resulting file with the weigths, it could be changed by lrbest_brand_1_49.h5 created using the keras.callbacks.ModelCheckpoint (attention mechanism) , keep the one that gave better results. This .h5 files are very large (1.9Gb) so they could not be uploaded to Github

As an output, a file is also obtained: BrandsResults.txt with the list of images whose car brands have been correct and the wrong ones with the brands that have been predicted to them and error probabilities.


References:

https://www.kaggle.com/datasets/jessicali9530/stanford-cars-dataset/code?resource=download

https://github.com/BotechEngineering/StanfordCarsDatasetCSV/blob/main/cardatasettest.csv

https://medium.com/analytics-vidhya/top-4-pre-trained-models-for-image-classification-with-python-code-a3cb5846248b

https://github.com/afaq-ahmad/Car-Models-and-Make-Classification-Standford_Car_dataset-mobilenetv2-imagenet-93-percent-accuracy/blob/master/Car_classification.ipynb


