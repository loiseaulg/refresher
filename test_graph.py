from graph import *

def test_initial_graph():
    assert Graph().graph == {}

def test_simple_graph():
    g1 = Graph()
    g2 = Graph()
    g1.addNode("A")
    g2.addNode("A")
    assert g1.graph == g2.graph 

def test_simple_graph2():
    g1 = Graph()
    g2 = Graph()
    g1.addNode("A")
    g1.addNode('B')
    g2.addNode("B")
    assert g1.graph != g2.graph

def test_simple_graph3():
    g1 = Graph()
    g2 = Graph()
    g1.addNode("A")
    g2.addNode("C")
    assert g1.graph != g2.graph 