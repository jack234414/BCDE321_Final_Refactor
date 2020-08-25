import esprima
import json
import visitor
from graphviz import Digraph, Source
import astpretty
import pygraphviz as pgv
import os
import subprocess
import pydot
import pyparsing
import json


class Converter(esprima.NodeVisitor):
    def __init__(self):
        # Initialize property
        self._operator = []
        self._obj_type = []
        self._prop_name = []
        self._right_ele = []
        self._class_names = []
        self._class_methods = []
        self._attributes = []
        self._dict_of_everything = {}
        self._index = 0

    def extract_data(self, con_class):
        filecontents = ""
        with open("JStest1.js", 'r') as f:
            for line in f:
                filecontents += line
        return esprima.parseScript(filecontents, delegate=con_class)

    def visit_ClassDeclaration(self, node):
        self._class_names.append(node.id.name)
        self.generic_visit(node)

    def is_constructor(self, node):
        result = False
        if node.key.name == 'constructor':
            result = True
        return result

    def visit_MethodDefinition(self, node):
        if self.is_constructor(node):
            self._class_methods = []
            self._attributes = []
            self._index += 1
            body = node.value.body.body
            self.set_class_attributes(body)
            # print("-------------")
            # print(self._prop_name)
            # print(self._operator)
            # print(self._right_ele)
            # print("-------------")
        self._class_methods.append(node.key.name)
        class_values = {
            'classname': self._class_names[self._index - 1],
            'classmethod': self._class_methods,
            'attributes': self._attributes
        }
        class_num = "class" + str(self._index)
        self._dict_of_everything[class_num] = class_values

    def set_class_attributes(self, body):
        for key in body:
            expr = key.expression
            result = 'this.'
            # self._attributes.append(expr.left.property.name)
            if expr.left != None:
                result += expr.left.property.name
            # self._attributes.append(expr.operator)
            result += expr.operator
            if expr.right.type == 'ArrayExpression':
                # self._attributes.append(expr.right.elements)
                result += str(expr.right.elements)
            elif expr.right.type == 'Literal':
                # self._attributes.append(expr.right.raw)
                result += expr.right.raw
            else:
                # self._attributes.append(expr.right.name)
                result += expr.right.name
            self._attributes.append(result)

    def convert_to_dot(self):
        dot = Digraph(comment='UML Diagram')
        for key in self._dict_of_everything:
            class_info = self._dict_of_everything.get(key)
            classname = class_info.get('classname')
            methods = class_info.get('classmethod')
            attributes = class_info.get('attributes')
            dot.node(classname, '{{{classname}|{attributes}|{methods}}}'.format(
                classname=classname,
                attributes='\l'.join(attributes),
                methods='()\l'.join(methods) + '()'), shape='record',)
        print(dot.source)

        print("=" * 100)
        print(self._dict_of_everything)
        s = Source(dot.source, filename="test.gv", format="png")
        s.view()


