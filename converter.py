import esprima
from graphviz import Digraph


class Converter(esprima.NodeVisitor):
    def __init__(self):
        # Initialize property
        self._operator = []
        self._obj_type = []
        self._prop_name = []
        self._right_ele = []
        self._class_names = []
        self._class_methods = []
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
        print(self._class_names)
        self.generic_visit(node)

    def is_constructor(self, node):
        result = False
        if node.key.name == 'constructor':
            result = True
        return result

    def visit_MethodDefinition(self, node):
        if self.is_constructor(node):
            self._class_methods = []
            self._operator = []
            self._prop_name = []
            self._right_ele = []
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
            'operator': self._operator,
            'propname': self._prop_name,
            'identifier': self._right_ele
        }
        class_num = "class" + str(self._index)
        self._dict_of_everything[class_num] = class_values

        print(self._dict_of_everything)

    def set_class_attributes(self, body):
        for key in body:
            expr = key.expression
            self._operator.append(expr.operator)
            self._prop_name.append(expr.left.property.name)
            if expr.right.type == 'ArrayExpression':
                self._right_ele.append(expr.right.elements)
            elif expr.right.type == 'Literal':
                self._right_ele.append(expr.right.raw)
            else:
                self._right_ele.append(expr.right.name)

    def convert_to_dot(self):
        dot = Digraph(comment='UML Diagram')
        dot.node()
