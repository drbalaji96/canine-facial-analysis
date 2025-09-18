---
license: other
---

# Canine Facial Morphology Dataset

This dataset is an augmented version of the original **Stanford Dogs Dataset**. It contains the original 20,580 images across 120 breeds, with new metadata fields added to quantify facial features relevant to veterinary pain assessment.

## Project Description

The goal of this project was to analyze canine facial structures to determine how breed-specific morphology might interfere with the ability to read a dog's facial expressions for clinical purposes (e.g., pain assessment).

An AI pipeline using MediaPipe's facial landmark detection was created to analyze each image and generate three novel scores:

* **`brachy_score`**: A measure of how flat-faced (brachycephalic) a dog is.
* **`hair_score`**: An estimation of how much hair is occluding the eye regions.
* **`wrinkle_score`**: An estimation of the density of skin folds on the muzzle.

These scores were then normalized and combined into a final **`difficulty_score`**, which serves as a proxy for how difficult it is to visually assess that dog's facial expressions.

## Dataset Details
* **Total Images:** 20,580
* **Number of Breeds:** 120
* **Added Features:** `brachy_score`, `hair_score`, `wrinkle_score`, `difficulty_score`

## Original Dataset Citation & License

This work would not be possible without the original dataset provided by Stanford University.

* **Original Source:** [Stanford Dogs Dataset](http://vision.stanford.edu/aditya86/ImageNetDogs/)
* **Original Paper:** Khosla, A., Jaiswal, N., Matuszek, T., & Zadeh, A. (2011). *Novel dataset for fine-grained image categorization*.
* **License:** The original dataset was made available for **non-commercial research purposes only**. This augmented dataset is therefore also intended for non-commercial use. Users of this data are expected to adhere to the original terms of use.
