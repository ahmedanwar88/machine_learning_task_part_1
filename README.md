# machine_learning_task_part_1
This repository includes part 1 solution of the Machine Learning task.

## Steps

1. Data cleaning and preparation
2. Named entities extraction using statistical and transformer based models
3. Evaluation of the models by comparing the extracted named entities to the ground truth labels

## Approach

## Results

1. Stanford Named Entity Recognition Statistical Model

Entity | Precision | Recall | F1-score
 ------------ | ------------- | ------------ | ------------- 
Persons | 0.964 | 0.839 | 0.897 
Locations | 0.972 | 0.898 | 0.934
Organizations | 0.944 | 0.792 | 0.861

2. Transformer Based Model using Spacy

Entity | Precision | Recall | F1-score
 ------------ | ------------- | ------------ | ------------- 
Persons | 0.984 | 0.849 | 0.912 
Locations | 0.828 | 0.868 | 0.848
Organizations | 0.684 | 0.763 | 0.722