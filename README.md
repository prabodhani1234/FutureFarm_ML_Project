# FUTUREFARM

A simple ML and DL-based website that suggests suitable crops based on soil chemical factors and environmental factors and suggests suitable crops and their growing season using a soil image.

![home](https://github.com/prabodhani1234/FutureFarm_ML_Project/blob/master/images/home.png)

## Datasets
- [Crop dataset ](https://drive.google.com/file/d/1pDQM-Y4y37DVZjFowy-7GhWFX-0SB9b_/view?usp=sharing)
- [Soil_dataset](https://drive.google.com/drive/folders/1qjkug3Wj6idSXwpK96pIi_pD90cg_5kE?usp=sharing)

## Notebooks
- [Crop Suggestion](https://github.com/prabodhani1234/soil_classification_and_crop_suggestion/tree/master/Jupyter%20Notebook)
- [Soil_Classification](https://github.com/prabodhani1234/soil_classification_and_crop_suggestion/tree/master/Jupyter%20Notebook)

## How To Run Local Demo
- First make sure you have [python](https://www.python.org/downloads/), [git](https://git-scm.com/download), [Anaconda](https://www.anaconda.com/) or [miniconda](https://docs.conda.io/en/latest/miniconda.html) installed on your computer.
- Clone the complete project with `https://github.com/prabodhani1234/FutureFarm_ML_Project.git` or you can just download the code and unzip it.
  ```
  ❯ git clone https://github.com/prabodhani1234/FutureFarm_ML_Project.git 
  ```
- Once the project is cloned, open the anaconda prompt in the directory where the project was cloned and paste the following block
  ```
  conda create -n futerfarm python
  conda activate futurefarm
  pip install -r requirements.txt
  ```
- And finally, run the project with
  ```
  python app.py
  ```
- Open the localhost url provided after running `app.py` and now you can use the project locally in your web browser.

## How to use this system
- Soil Classification and crop suggestion using Soil images system ==> Click the "Choose File" Button and select the soil image. After click the "Predict" Button.

  OUTPUT - soil type of input soil image, crops that can be grown on it, the season for growing it.

![soil_clssification](https://github.com/prabodhani1234/FutureFarm_ML_Project/blob/master/images/soil_clssification.png)

<details>
  <summary>Supported Soil Types
</summary>

- Red Soil
- Black Soil
- Clay Soil
- Sandy Soil
- Alluvial Soil
</details>

- Crop suggestion using soil factors and environmental factors system ==> Enter the relevant data such as Soil(N,P,K), Ph value, humidity, temperature and rainfall
Note: When you enter the Province name, make sure to enter district names. Because, if the user does not enter the temperature and humidity, then system automatically calculates it using weather API.

![crop_suggestion](https://github.com/prabodhani1234/FutureFarm_ML_Project/blob/master/images/crop_suggestion.png)

<details>
  <summary>Supported crops
</summary>

- Bean
- Carrots
- Chilli
- Cowpea
- Ground Nut
- Onion
- Potato
- Pumpkin
- banana
- cashew nuts
- coconut
- coffee
- grapes
- maize
- mango
- mungbean
- orange
- papaya
- pigeonpeas
- pomegranate
- rice
- watermelon
</details>


## Contact

#### If you have any doubt [email](prabodhaniherath2@gmail.com) me or hit me up on [LinkedIn](https://www.linkedin.com/in/prabodhani-herath-aa644224a/)




