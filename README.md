# RealOrAI
Developed for HackFest 2023. We made a CNN model that will predict if the given image is Real or AI-Generated.  
## Dataset 
The dataset has a total of 1,00,000 images for real and fake. We split the dataset into training, validation, and testing sets to evaluate the model's performance and prevent overfitting.. The ratio used 70:15:15. 

## Model Architecture
The CNN architecture employed in this project is designed to capture the intricate features present in images. The model consists of multiple convolutional layers followed by max-pooling layers to extract and downsample the relevant features. The final layers include fully connected layers with 'relu' activation and 'sigmoid' activation to produce the probability distribution.

## Model Training
I compiled the models using 'Binary Crossentropy' loss and 'adam' optimizer. Loss and accuracy were calculated for each epoch which is later plotted. I was able to run only 5 epochs because of hardware limitations but I believe the model will be able to get much higher accuracy if it trained a little longer.

## Accuracy
We were able to achieve accuracy up to 91%.

## Deployment
We saved the model to 'h5' file. Then in 'app.py' file, we used 'FLASK' to handle HTTP requests. We created two HTML templates, one for the input form (index.html) and another for displaying results (predictt.html).
This will allow the users to interact with the model through a user-friendly interface.
