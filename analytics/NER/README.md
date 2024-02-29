# Named Entity Recognition

## Implementation

**Named entity recognition** (**NER**) or **entity extraction** is an information extraction task that seeks to identify and classify named entities referenced in unstructured text into predefined categories, such as people names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. ([Wikipedia](https://en.wikipedia.org/wiki/Named-entity_recognition)).

The aim of the following work is to find popular entities during the period of the Greek crisis.

For finding entities in speeches the spaCy library has been used, which supports NER in Greek using a pre-trained model.

<https://spacy.io/models/el>.

<https://github.com/eellak/gsoc2018-spacy>

The library is unable to discover entities in stemmed words, therefore the original dataset has been used.

The **crisis_generator.py** script creates a subset of the original dataset by keeping the speeches spoken from September 2, 2009 to August 20, 2018 and stores it back in memory in a crisis.csv file.

The **NER.py** script reads the subset generated primarily and for each speech performs named-entity recognition by generating pairs (word, entity type) if the word is identified as an entity. The results are stored in an entities_crisis.csv file which contains the entity pairs of each speech as well as the ID of the original speech (foreign key).

The **ner_aggregator.py** script reads the primarily created entity file and aggregates the entities based on their type. For each entity it finds its occurrence number. At the end for each entity type the top-k entities based on the number of occurrences are stored in a frequent_{k}.txt file

The types of entities supported by the Greek language and the above analysis are the following:

<https://stackoverflow.com/questions/76206507/spacy-where-are-terminologies-defined>

The results can be viewed manually from the previously mentioned files and also through the search engine web app.

## Results

The discovery of important entities begins on 2 September 2009 when, under the weight of the economic crisis, Prime Minister Karamanlis announces early elections for 4 October 2009, which are won by PASOK. The investigation ends on 20 August 2018, when the third memorandum expires and Greece leaves the memorandum supervision and enters the "post-memorandum supervision".

The results consist of trivial results that offer no further information but interesting results that can be logically evaluated if we look at the history of the Greek crisis.

### Person
For the PERSON entities: the speeches contain several persons who were prominent in those periods such as Kyriakos Mitsotakis, Alexis Tsipras, Evangelos Venizelos, George Papandreou, Andreas Loverdos, Adonis Georgiades, Panos Kammenos, etc. Of course, there are also foreign faces such as Merkel, Schäuble, Erdogan, Juncker or even Hitler. The results seem logical as all of the above persons have played a leading role either in the country's domestic or foreign affairs.

### GPE
For the GPE entities: the first entities on the list are obviously Greece and Europe. Neighbouring countries such as Turkey, Cyprus, Bulgaria, Albania or Skopje, but also European countries such as Germany, the USA, France, Italy or Russia. Of course there are the big cities of Greece such as Athens or Thessaloniki but also smaller cities such as Lamia, Patras. There are also references to all the major prefectures and our seas such as the Aegean Sea.

### ORG
For ORG entities: first on the list are of course the major parties that have been in the forefront of the country for years such as PASOK, SYRIZA, KKE and New Democracy (not taken into account as ORG but as GPE). Many appearances are made by entities referring to state institutions such as NSPA, PPC, EOPYY, ERT, IKA, ELGA, ASEP, OAED. But also to various global ones such as NATO, Eurogroup, IMF _(due to memoranda)_, UN or SIEMENS _(remember the scandal that had arisen at the time)_.

### EVENT
For EVENT entities: in general, fewer entities of this type appear. The World War, the summit, **Twitter,** and the World Bank are prominent.

### PRODUCT
For PRODUCT entities: again, fewer entities of this type appear. GOLDMAN SACKS/SACHS _(scandal under Prime Minister K. Simitis where the famous "currency swap" was agreed with Goldman Sachs)_ and Lehman Brothers _(bankruptcy in 2008, financial freeze)_.