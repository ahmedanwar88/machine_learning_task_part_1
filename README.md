# machine_learning_task_part_1
This repository includes part 1 solution of the Machine Learning task.

## Steps

1. Data cleaning and preparation
2. Named entities extraction using statistical and transformer based models
3. Evaluation of the models by comparing the extracted named entities to the ground truth labels

## Approach

1. Data cleaning and preparation
    - I used BeautifulSoup to clean the data from all tags and get raw text.
    - Extracted the paragraphs from the cleaned text and extracted the sentences from each paragraph, resulting in 2578 sentences.
    - Extracted the labels (named entities) from the HTML file using BeautifulSoup and added them to a dictionary with keys corresponding to the entities (Locations, Persons and Organizations) and the values of each key are the words present in the HTML file.

2. Named entities extraction using statistical and transformer based models
    - I used Stanford Named Entity Recognition model as a statistical model which uses a Conditional Random Field (CRF) model.
    - In addition to Stanford NER model, I used also the NER model present in NLTK, as well as that present in Spacy. It has been observed that Stanford NER model shows the best results for a statistical model.
    - I used a transformer based NER model from Spacy library, and compared its results to the Stanford NER model.

3. Evaluation
    - I used precision, recall and F1-score to evaluate the predictions of the two models against the ground truth for each entity.
    - I calculated precision for each named entity (Location, Person and Organization) as: How many predicted entities by the model correctly appear in the ground truth for that named entity, and divided that number by the total number of predicted entities by the models.
    - I calculated recall for each named entity (Location, Person and Organization) as: From the ground truth entities, how many entities correctly appear in the model prediction, and divided that number by the total number of ground truth entities.
    - I calculated F1-score as the harmonic mean of precision and recall, in order to get a number representing the balance between them.

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

## Comparison

- Transformer based model shows better *Persons* F1-score result (0.912) compared to Stanford NER statistical model (0.897).

- Stanford NER statistical model shows better *Locations* F1-score result (0.934) compared to Transformer based model (0.848).

- Stanford NER statistical model shows better *Organizations* F1-score result (0.861) compared to Transformer based model (0.722).

- The transformer based solution processed the data much faster than the Stanford NER solution. The transformer based solution takes 0.16s on average to process 1 sentence on the CPU. The Stanford NER solution takes 3s on average to process 1 sentence on the CPU.

- If runtime is an important metric based on the application, I think that the transformer based solution is better as its runtime is low and its results are good.

- If runtime is not so much important based on the application, I think that the Stanford NER solution is better as its results are very good in all named entities (Persons, Locations and Organizations).

## Problems and Improvements
- I faced a problem in aligning each word in the data and its named entity to the predicted words and named entities.
- The approach that I took is to extract all the named entities from the data (ground truth) and get the predictions of the models. Then, I evaluated the models by the correctly predicted named entities that appeared in the ground truth and calculated precision, recall and F1-score as described before.
- Better alignment between the data ground truth and model predictions can give more accurate results.