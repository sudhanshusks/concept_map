# Concept-Map-Generator
Term Project for Language Processing for E-Learning

This work was done as part of a mini project for the course on Language Processing for E-Learning under the guidance of Professor Plaban Bhowmick.

It makes use of the DBpedia Spotlight Web API to extract important concepts from a given text and then uses OpenIE to extract relations. Visualisation is done using GraphViz.

This work uses the python wrapper for Stanford OpenIE written by [philipperemy](https://github.com/philipperemy/Stanford-OpenIE-Python).

## Usage

First of all, make sure Java 1.8 is installed. Open a terminal and run this command to check:

```
java -version
```

If this is not the case and if your OS is Ubuntu, you can install it this way:

```
sudo add-apt-repository ppa:webupd8team/java
sudo apt-get update
sudo apt-get install oracle-java8-installer
```
Note: Make sure GraphViz is installed beforehand. Try to run the `dot` command to see if this is the case. If not, run `sudo apt-get install graphviz` if you're running on Ubuntu. 

How to use:
Paste your desired input text in place of 'Your Text'
```
git clone https://github.com/philipperemy/Stanford-OpenIE-Python.git
git clone https://github.com/PranavKhadpe/Concept-Map-Generator.git
cp Concept-Map-Generator/{main2.py,conceptmap.py} Stanford-OpenIE-Python
cd Stanford-OpenIE-Python
echo Your Text > test.txt
python conceptmap.py -i test.txt
python main2.py -f test.txt -g
```
Will generate a [GraphViz DOT](http://www.graphviz.org/) graph and its related PNG file in `/tmp/openie/`

## Example

Sample map generated for elementary paragraph on Photosynthesis

<div align="center">
  <img src="https://github.com/sudhanshusks/concept_map/blob/master/sample/out.png"><br><br>
</div>



