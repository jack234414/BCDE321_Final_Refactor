import esprima


class Converter(esprima.NodeVisitor):
    def extract_data(self, obj):
        filecontents = ""
        with open("JStest1.js", 'r') as f:
            for line in f:
                filecontents += line
        return esprima.parseScript(filecontents, delegate=obj)

    # def visit_Program(self, node):
    #     for key in node:
    #         if node.hasatt(key):
    #             child = node[key]
    #             if type(child) == 'object' and child is not None:
    #                 if isinstance(child, list):
    #                     for node in child:
    #                         self.visit_Program(node)
    #                 else:
    #                     self.visit_Program(child)

    def visit_ClassDeclaration(self, node):
        classnames = []
        if node.type == 'ClassDeclaration':
            classnames.append(node.id.name)
        self.generic_visit(node)

        # for key in node.body:
        #     if node.hasatt(key):
        #         child = node[key]
        #         if isinstance(child, list):
        #             for node in child:
        #                 self.visit_MethodDefinition(handle_node)

    def visit_MethodDefinition(self, node):
        if node.key.name == 'constructor':
            self.visit_list(node.value.body)

    def visit_BlockStatement(self, node):
        pass

    def visit_ExpressionStatement(self, node):
        pass