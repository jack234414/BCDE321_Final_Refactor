import esprima


class Converter(esprima.NodeVisitor):
    def extract_data(self, con_class):
        filecontents = ""
        with open("JStest1.js", 'r') as f:
            for line in f:
                filecontents += line
        return esprima.parseScript(filecontents, delegate=con_class)

    def visit_Program(self, node):
        pass
        # for key in node:
        #     if node.hasatt(key):
        #         child = node[key]
        #         if type(child) == 'object' and child is not None:
        #             if isinstance(child, list):
        #                 for node in child:
        #                     self.visit_Program(node)
        #             else:
        #                 self.visit_Program(child)
        # self.generic_visit(node)

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
            self.visit_BlockStatement(node)
        print(node.key.name)


    def visit_BlockStatement(self, node):
        body = node.value.body.body
        for key in body:
            expr = key.expression

            operator = expr.operator
            obj_type = expr.left.object.type
            prop_name = expr.left.property.name
            right_ele = expr.right.elements

            print("----------------------------------")
            print(obj_type)
            print(prop_name)
            print(operator)
            print(right_ele)
            print("----------------------------------")

    def visit_ExpressionStatement(self, node):
        pass