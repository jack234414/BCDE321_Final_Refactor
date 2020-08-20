import esprima


class Converter(esprima.NodeVisitor):
    def __init__(self):
        # Initialize property
        self._operator = []
        self._obj_type = []
        self._prop_name = []
        self._right_ele = []

    def extract_data(self, con_class):
        filecontents = ""
        with open("JStest1.js", 'r') as f:
            for line in f:
                filecontents += line
        return esprima.parseScript(filecontents, delegate=con_class)

    def visit_ClassDeclaration(self, node):
        class_names = []
        if node.type == 'ClassDeclaration':
            class_names.append(node.id.name)
        print(class_names)
        self.generic_visit(node)

    def is_constructor(self, node):
        result = False
        if node.key.name == 'constructor':
            result = True
        return result

    def visit_MethodDefinition(self, node):
        if self.is_constructor(node):
            body = node.value.body.body
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

            print("-------------")
            print(self._prop_name)
            print(self._operator)
            print(self._right_ele)
            print("-------------")

        print(node.key.name)
